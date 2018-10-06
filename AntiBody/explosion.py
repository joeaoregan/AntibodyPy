"""
Joe O'Regan
07/10/2018
"""

import pygame
from pygame.locals import *
import random

NUM_ANIMATION_FRAMES = 12           # number of cells in the animation sprite sheet

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, fps):
        super().__init__()

        self.x = x
        self.y = y
        self.width = self.height = 96
        self.active = True

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
        if self.currentFrame > 0 and self.currentFrame % NUM_ANIMATION_FRAMES == 0:
            self.active = False
