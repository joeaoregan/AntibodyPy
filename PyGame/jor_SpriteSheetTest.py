"""
Python Pygame Tutorial - Sprite Sheets

Link to tutorial below

@Author: Joe O'Regan
@Date: 06/10/2018
@Links: https://www.youtube.com/watch?v=mfX3XQv9lnI
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'
__version__ = "1.02"

import pygame
from pygame.locals import *


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # exit game
            return True
    return False


# define display surface
W, H, = 1280, 720  # Window dimensions
HW, HH = W / 2, H / 2  # Sprite screen position (centered)
AREA = W * H

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 6

CENTER_HANDLE = 4

# Colours
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


class SpriteSheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename)

        self.cols = cols
        self.rows = rows
        self.totalCells = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows
        hw, hh = self.cellCenter = (w / 2, h / 2)

        self.cells = list([(index % cols * w, index % rows * h, w, h) for index in range(self.totalCells)])

        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h), ])

    def draw(self, surface, cellIndex, x, y, handle=0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])


def main():
    pygame.display.set_caption("Sprite Sheet Test")

    s = SpriteSheet("../Antibody/Art/EnemySpriteSheet2.png", 1, 4)

    index = 0

    # main loop
    done = False

    while not done:
        done = events()

        s.draw(DS, index % s.totalCells, HW, HH, CENTER_HANDLE)
        index += 1

        pygame.draw.circle(DS, WHITE, (640, 360), 2, 0)

        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)


if __name__ == '__main__':
    pygame.init()  # Initialise display
    main()
    pygame.quit()
