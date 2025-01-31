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
import math

BLACK = (0, 0, 0)
NEXT_FIRE = 0

pygame.init()
laserFX = pygame.mixer.Sound('Audio/laser1.wav')

class Bullet(object.Object):
    def __del__(self):
        # super().__del__()
        print("Bullet destroyed")

    def __init__(self, x, y, type=1):        
        super(Bullet, self).__init__(x, y, image_src="Art/LaserGreen2.png", type=type)
        self.type = type
        #if type==2:
        #    pygame.transform.rotate(self.image, 30)
        #elif type==3:
        #    pygame.transform.rotate(self.image, -30)
        laserFX.play()
        if type == 2:
            self.angle = 10
        elif type == 3:
            self.angle=-10

    def collision(self, rect):
        # global explosion, active
        if self.x < rect.left + rect.width and self.x + self.width > rect.left and self.y < rect.top + rect.height and self.y + self.height > rect.top:
            self.explosion = True
            self.active = False
            return True
            # del self
        return False

    def move(self):
        # global active, x
        if self.active:
            self.x += 10

            #if self.type == 1:

                #if self.x > background.width:
            #if self.type == 2:
                #self.y+= 7.5
           #elif self.type == 3:
                #self.y-= 7.5
            if self.angle != 0:
                self.y -= (5 * math.tan(self.angle))

            if self.x > background.Background.get_width():
                self.active = False

        if not self.active:
            self.x,self.y=0,0

    def draw(self):
        #super().draw()
        object.Object.DS.blit(pygame.transform.rotate(self.image, self.angle), (self.x, self.y))

# bulletList = pygame.sprite.Group()
# laserImage = pygame.image.load("Art/LaserGreen2.png").convert()
