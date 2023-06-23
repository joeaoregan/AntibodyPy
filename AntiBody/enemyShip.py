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

import object


# class EnemyShip(pygame.sprite.Sprite):
class EnemyShip(object.Object):
    count = 0

    def __del__(self):
        # super().__del__()
        EnemyShip.count -= 1
        print("Enemy destroyed. Total Left:",EnemyShip.count)

    def __init__(self):
        super().__init__(image_src="Art/EnemySpriteSheet2.png")
        # self.width = 120
        # self.height = 50
        self.x = 1280 + random.randrange(100,1000,75)
        self.y = random.randint(40, 600-self.height)
        # self.velocityX = 0
        # self.velocityY = 0
        # self.active = True
        EnemyShip.count += 1

    def move(self):
        # global x, angle
        self.x -= 3

        if self.x < -self.width:
            self.active = False

    @staticmethod
    def increment(num):
        EnemyShip.count += num

# enemyList = pygame.sprite.Group()
# enemySpriteSheet = ss.SpriteSheet("Art/EnemySpriteSheet2.png", 1, 4)    # Params: filename, cols, rows
