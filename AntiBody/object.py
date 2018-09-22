"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *

SPEED = 5


class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0


# x, y = 0, 0
# velocityX, velocityY = 0,0

    def input(self):
        # global velocityX, velocityY
        k = pygame.key.get_pressed()
        if k[K_p]:
            self.velocityX = 0

    def move(self):
        # global x, y, SPEED
        self.x += self.velocityX * SPEED
        self.y += self.velocityY * SPEED
