import pygame
from pygame.locals import *
import random


class BloodCell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 1280 + random.randrange(100,1000,75)
        self.y = random.randint(40, 600)
        self.velocityX = 0
        self.velocityY = 0
        self.angle = random.randint(0,180)
        self.width = 100
        self.height = 55
        self.active = True
        self.rotate = random.randint(0,2)
        self.rotateSpeed = random.uniform(0.5,3.0)

    def move(self):
        # global x, angle
        self.x -= 3

        if self.x < -self.width:
            self.active = False

        if self.rotate % 2 == 0:
            self.angle += self.rotateSpeed
        else:
            self.angle-=self.rotateSpeed

        self.angle %= 360
