"""
Joe O'Regan
06/10/2018

Python Pygame Tutorial - Sprite Sheets
https://www.youtube.com/watch?v=mfX3XQv9lnI
"""

import pygame
from pygame.locals import *
import random
import sys
import os


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit


# define display surface
W, H, = 1280, 720
HW, HH = W/2, H/2
AREA = W*H

# Initialise display
pygame.init()
#CLOCK = pygame.time.Clock()
#DS = pygame.display.set_mode((W, H))
#pygame.display.set_caption("Sprite Sheet Test")
#FPS = 6

# Colours
BLACK = (0, 0, 0, 255)
WHITE = (255,255,255,255)
NEXT_FRAME = 0


class SpriteSheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename)

        self.cols = cols
        self.rows = rows
        self.totalCells = cols*rows
        self.currentFrame = 0

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width/cols
        h = self.cellHeight = self.rect.height/rows
        hw, hh = self.cellCenter = (w/2,h/2)

        self.cells = list([(index % cols * w, index % rows * h, w, h) for index in range(self.totalCells)])

        self.handle = list([
            (0,0),(-hw,0), (-w,0),
             (0,-hh),(-hw,-hh),(-w,-hh),
             (0,-h),(-hw,-h),(-w,-h),])

    def animationFPS(self, perSecond):

        rate = 1000 / perSecond

        global NEXT_FRAME
        if pygame.time.get_ticks() > NEXT_FRAME:
            NEXT_FRAME = pygame.time.get_ticks() + rate
            self.currentFrame+=1

        return self.currentFrame % self.totalCells

    def draw(self, surface, cellIndex, x, y, handle = 0):
        # index % s.totalCells
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
'''
    def draw(self, surface, perSecond, x, y, handle = 0):
        global NEXT_FRAME, cellIndex
        # index % s.totalCells
        rate = 1000 / perSecond

        if pygame.time.get_ticks() > NEXT_FRAME:
            NEXT_FRAME = pygame.time.get_ticks() + rate

        cellIndex+=1
        cellIndex % s.totalCells
        
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
'''



