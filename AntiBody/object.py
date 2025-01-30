"""
Object Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
from enum import Enum

WIDTH, HEIGHT = 1280, 720

# ExplosionAnimation = Enum('ExplosionAnimation', [('NORMAL', 1), ('BLOOD', 2)])

class Object(pygame.sprite.Sprite):
    DS = pygame.display.set_mode((WIDTH, HEIGHT))
    width = 0
    def __init__(self, x=0, y=0, image_src="Art/Player1Ship.png", speed=5, cols=1, rows=1, fps=1):
        super().__init__()
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.health = 100

        self.image = pygame.image.load(image_src).convert()
        self.cols = cols
        self.rows = rows
        self.totalCells = self.rows * self.cols
        self.width = int(self.image.get_width() / cols)
        self.height = int(self.image.get_height() / rows)
        # print(self.__class__.__name__, " width: ", self.width, " height: ", self.height)
        self.speed = speed
        self.angle = 0
        self.active = True
        self.explosion = False
        # Object.width = self.image.get_width()
        print(self.__class__.__name__, self.width, " x ", self.height)
        self.rect = self.image.get_rect()

        # Animation
        self.rate = 1000 / fps
        self.currentFrame = 0       # start animation on first frame
        self.nextFrameTime = 0      # time to change to next animation frame
        self.cells = list([(index % self.cols * self.width, index % self.rows * self.height, self.width, self.height) for index in range(self.totalCells)])


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


