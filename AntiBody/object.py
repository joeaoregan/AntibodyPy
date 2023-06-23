"""
Object Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *

WIDTH, HEIGHT = 1280, 720



class Object(pygame.sprite.Sprite):
    DS = pygame.display.set_mode((WIDTH, HEIGHT))
    width = 0
    def __init__(self, x=0, y=0, image_src="Art/Player1Ship.png", speed=5):
        super().__init__()
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.image = pygame.image.load(image_src).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = speed
        self.angle = 0
        self.active = True
        self.explosion = False
        Object.width = self.image.get_width()
        print(self.__class__.__name__, self.width, " x ", self.height)
        self.rect = self.image.get_rect()


# x, y = 0, 0
# velocityX, velocityY = 0,0

    def input(self):
        # global velocityX, velocityY
        k = pygame.key.get_pressed()
        if k[K_p]:
            self.velocityX = 0

    def move(self):
        # global x, y, SPEED
        self.x += self.velocityX * self.speed
        self.y += self.velocityY * self.speed

    def draw(self):
        Object.DS.blit(self.image, (self.x, self.y))

    def collision(self, rect):
        return False

    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))

    @staticmethod
    def get_width():
        return Object.width


