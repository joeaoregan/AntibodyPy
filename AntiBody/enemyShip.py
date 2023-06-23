"""
Enemy Ship Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import random



class EnemyShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 120
        self.height = 50
        self.x = 1280 + random.randrange(100,1000,75)
        self.y = random.randint(40, 600-self.height)
        self.velocityX = 0
        self.velocityY = 0
        self.active = True

    def move(self):
        # global x, angle
        self.x -= 3

        if self.x < -self.width:
            self.active = False

# enemyList = pygame.sprite.Group()
# enemySpriteSheet = ss.SpriteSheet("Art/EnemySpriteSheet2.png", 1, 4)    # Params: filename, cols, rows
