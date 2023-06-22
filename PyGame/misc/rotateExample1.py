import pygame as pg


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pg.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


def main():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    gray = pg.Color('gray15')
    blue = pg.Color('dodgerblue2')

    image = pg.Surface((320, 200), pg.SRCALPHA)
    pg.draw.polygon(image, blue, ((0, 0), (320, 100), (0, 200)))
    # Keep a reference to the original to preserve the image quality.
    orig_image = image
    rect = image.get_rect(center=(320, 240))
    angle = 0

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        angle += 2
        image, rect = rotate(orig_image, rect, angle)

        screen.fill(gray)
        screen.blit(image, rect)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
