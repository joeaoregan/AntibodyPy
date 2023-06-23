"""
Scrolling Background

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import object

# define display surface

WIDTH = 1280
#DS = pygame.display.set_mode((WIDTH, HEIGHT))


class Background(object.Object):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, image_src="Art/background.png")
        Background.width = self.image.get_width()

    def move(self):
        if self.x <= -self.image.get_width():
            self.x = WIDTH -1
        else:
            self.x -= 1
        # Scrolling Background
        # rel_x = bg.x % bgImage.get_rect().width
        # DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
        # if rel_x < WIDTH:
        #    DS.blit(bgImage, (rel_x, 0))
        # bg.move()

    def input(self):
        pass

    def draw(self):
        super().draw()

    def collision(self, rect):
        return False

    @staticmethod
    def get_width():
        return Background.width
