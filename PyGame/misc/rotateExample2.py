import pygame as pg


class Entity(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((122, 70), pg.SRCALPHA)
        pg.draw.polygon(self.image, pg.Color('dodgerblue1'),
                        ((1, 0), (120, 35), (1, 70)))
        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self):
        self.angle += 2
        self.rotate()

    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group(Entity((320, 240)))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        all_sprites.update()
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
