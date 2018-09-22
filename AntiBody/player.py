"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *
import AntiBody.object as object

SPEED = 5


class Player(object.Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0

    def input(self):
        # global velocityX, velocityY
        k = pygame.key.get_pressed()
        if k[K_RIGHT]:
            self.velocityX = 1
        elif k[K_LEFT]:
            self.velocityX = -1
        else:
            self.velocityX = 0

        if k[K_UP]:
            self.velocityY = -1
        elif k[K_DOWN]:
            self.velocityY = 1
        else:
            self.velocityY = 0

    def move(self):
        # global x, y, SPEED
        self.x += self.velocityX * SPEED
        self.y += self.velocityY * SPEED

        # Keep player in window boundary
        if self.y < 20:
            self.y = 20
        elif self.y > 550:
            self.y = 550

        if self.x < 0:
            self.x = 0
        elif self.x > 1180:
            self.x = 1180
