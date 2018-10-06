"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *
import random


class EnemyShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 1280 + random.randrange(100,1000,75)
        self.y = random.randint(40, 600)
        self.velocityX = 0
        self.velocityY = 0
        self.width = 100
        self.height = 55
        self.active = True

    def move(self):
        # global x, angle
        self.x -= 3

        if self.x < -self.width:
            self.active = False
