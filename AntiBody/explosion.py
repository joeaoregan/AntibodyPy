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
from enum import Enum
Animation = Enum('Animation', [('NORMAL', 1), ('SPLASH', 2)])

NUM_ANIMATION_FRAMES = 12           # number of cells in the animation sprite sheet

explosionFX = pygame.mixer.Sound('Audio/explosion.wav')
splashFX = pygame.mixer.Sound('Audio/splash.wav')



# class Explosion(pygame.sprite.Sprite):
class Explosion(object.Object):
    def __del__(self):
        # super().__del__()
        print("Explosion destroyed")

    def __init__(self, x, y, fps, type=Animation['NORMAL']):
        if type==Animation['NORMAL']:
            super().__init__(x, y, image_src="Art/Explosion.png", cols=12, fps=fps)
            explosionFX.play()
        elif type==Animation['SPLASH']:
            super().__init__(x, y, image_src="Art/ExplosionBlood.png", cols=16, fps=fps)
            splashFX.play()

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

    def draw(self):
        if (self.active):
            self.DS.blit(self.image, (self.x - (self.width/2), self.y - (self.width/2)), self.cells[self.currentFrame])




    # explosionList = pygame.sprite.Group()
    # explosionSpriteSheet = ss.SpriteSheet("Art/Explosion.png", 12, 1)


'''
    # Explosion update
    for explosions in explosionList:
        explosions.move()
        ### Explosion
        ### explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), 96, 96, CENTER_HANDLE)
        ### explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), explosions.x, explosions.y, CENTER_HANDLE)   # same frame for all explosions
        explosionSpriteSheet.draw(DS, explosions.currentFrame, explosions.x, explosions.y, CENTER_HANDLE)                   # each explosion has its own animation frame
        if not explosions.active:
            explosionList.remove(explosions)
'''