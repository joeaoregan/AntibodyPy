"""
Animated Explosion Class

@Author: Joe O'Regan
@Date: 07/10/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import random
import object

NUM_ANIMATION_FRAMES = 12           # number of cells in the animation sprite sheet

# class Explosion(pygame.sprite.Sprite):
class Explosion(object.Object):
    def __del__(self):
        # super().__del__()
        print("Explosion destroyed")

    def __init__(self, x, y, fps):
        super().__init__(x, y, image_src="Art/Explosion.png")

        self.x = x
        self.y = y
        self.width = self.height = 96
        self.active = True

        self.rows = 1
        self.cols = 12
        self.totalCells = self.rows * self.cols        
        # self.cells = list([(index % self.cols * self.w, index % rows * h, w, h) for index in range(self.totalCells)])
        self.cells = list([(index % self.cols * self.width, index % self.rows * 96, 96, 96) for index in range(self.totalCells)])

        # Animation
        self.rate = 1000 / fps
        self.currentFrame = 0       # start animation on first frame
        self.nextFrameTime = 0      # time to change to next animation frame

    def move(self):
        global NUM_ANIMATION_FRAMES

        # Update current animation frame
        if pygame.time.get_ticks() > self.nextFrameTime:
            self.nextFrameTime = pygame.time.get_ticks() + self.rate
            self.currentFrame+=1

        # If the animation has started and current frame is the last frame, destroy the animation
        # if self.currentFrame > 0 and self.currentFrame % NUM_ANIMATION_FRAMES == 0:   # shows 1st frame again
        # if self.currentFrame > 0 and self.currentFrame % (NUM_ANIMATION_FRAMES-1) == 0:   # shows first few frames
        if self.currentFrame == (NUM_ANIMATION_FRAMES-1):
            self.active = False

    #def draw(self):
    #    # super().draw()        
    
    # def draw(self, surface, cellIndex, x, y, handle = 0):
    #    surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
    def draw(self, handle = 0):
        if (self.active):
            self.DS.blit(self.image, (self.x - (self.width/2), self.y - (self.width/2)), self.cells[self.currentFrame])

        ##### self.DS.blit(self.image, (self.x, self.y))
        # self.draw(DS, self.animationFPS)
        
# Explosion update
    # for explosions in explosionList:
        # explosions.move()
        ### Explosion
        ### explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), 96, 96, CENTER_HANDLE)
        ### explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), explosions.x, explosions.y, CENTER_HANDLE)   # same frame for all explosions
        # explosionSpriteSheet.draw(DS, explosions.currentFrame, explosions.x, explosions.y, CENTER_HANDLE)                   # each explosion has its own animation frame
        # if not explosions.active:
        #     explosionList.remove(explosions)



    # explosionList = pygame.sprite.Group()
    # explosionSpriteSheet = ss.SpriteSheet("Art/Explosion.png", 12, 1)
