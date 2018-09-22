"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *
import AntiBody.background as background

BLACK = (0, 0, 0)
NEXT_FIRE = 0

pygame.init()
laserFX = pygame.mixer.Sound('Audio/laser1.wav')
explosionFX = pygame.mixer.Sound('Audio/explosion.wav')


class Bullet(pygame.sprite.Sprite):
    def __del__(self):
        # super().__del__()
        print("Bullet destroyed")

    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.width = 100
        self.height = 47
        self.active = True
        self.explosion = False

        self.image = pygame.Surface([4,10])
        self.image.fill(BLACK)
        laserFX.play()

    def collisions(self, rect):
        # global explosion, active
        if self.x < rect.left + rect.width and self.x + self.width > rect.left and self.y < rect.top + rect.height and self.y + self.height > rect.top:
            self.explosion = True
            self.active = False
            explosionFX.play()
            return True
            # del self
        return False

    def move(self):
        # global active, x
        if self.active:
            self.x += 10

            if self.x > background.width:
                self.active = False

        if not self.active:
            self.x,self.y=0,0
