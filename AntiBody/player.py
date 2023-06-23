"""
Player Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import object

SPEED = 5

WIDTH, HEIGHT = 1280, 720
#DS = pygame.display.set_mode((WIDTH, HEIGHT))
#playerImage = pygame.image.load("Art/Player1Ship.png").convert()


class Player(object.Object):
    def __init__(self, x=200, y=HEIGHT/2):
        super().__init__(x, y)
        self.score = 0
        self.nextFire = 0
        self.firing = False
        # self.x = x
        # self.y = y
        # self.velocityX = 0
        # self.velocityY = 0

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

        if k[K_SPACE] and pygame.time.get_ticks() > self.nextFire:
            # print("Fire!!!")
            # self.fire()
            self.nextFire = pygame.time.get_ticks() + 200
            return "Fire"

        return None

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

    def draw(self):
        super().draw()

    def get_width(self):
        return super().get_width()

    def fire(self):
        print("fire!!!")
        self.nextFire = pygame.time.get_ticks() + 200

    def collision(self, rect):
        # print("Player", rect)
        # return False
        if self.x < rect.left + rect.width and self.x + self.width > rect.left and self.y < rect.top + rect.height and self.y + self.height > rect.top:
            self.explosion = True
            self.active = False
            # explosionFX.play()
            print("Player - Collision", rect)
            return True
            # del self
        return False
