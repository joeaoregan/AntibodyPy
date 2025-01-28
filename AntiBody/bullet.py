"""
Bullet Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import background
import object

BLACK = (0, 0, 0)
NEXT_FIRE = 0

pygame.init()
laserFX = pygame.mixer.Sound('Audio/laser1.wav')
explosionFX = pygame.mixer.Sound('Audio/explosion.wav')


#class Bullet(pygame.sprite.Sprite):
class Bullet(object.Object):
    def __del__(self):
        # super().__del__()
        print("Bullet destroyed")

    def __init__(self, x, y):
        super().__init__(x, y, image_src="Art/LaserGreen2.png")
        laserFX.play()

    def collision(self, rect):
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

            #if self.x > background.width:
            if self.x > background.Background.get_width():
                self.active = False

        if not self.active:
            self.x,self.y=0,0

    def draw(self):
        super().draw()

# bulletList = pygame.sprite.Group()
# laserImage = pygame.image.load("Art/LaserGreen2.png").convert()
