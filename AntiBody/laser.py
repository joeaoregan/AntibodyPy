import pygame
from pygame.locals import *
import background
import AntiBody.object as object


class Laser(object.Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.width = 100
        self.height = 47
        self.active = True
        self.explosion = False

    def collisions(self, rect):
        # global explosion, active
        if self.x < rect.left + rect.width and self.x + self.width > rect.left and self.y < rect.top + rect.height and self.y + self.height > rect.top:
            self.explosion = True
            self.active = False

    def move(self):
        # global active, x
        if self.active:
            self.x += 10

            if self.x > background.width:
                self.active = False

        if not self.active:
            self.x,self.y=0,0

# x, y = 0,0
# width, height = 100, 47
# active = False
# explosion = False

# def collisions2(objectX,objectY,objectW,objectH):
#     global explosion, active
#     if x < objectX + objectW and x + width > objectX and y < objectY + objectH and y + height > objectY:
#         explosion = True
#         active = False