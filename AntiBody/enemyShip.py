"""
Enemy Ship Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import random

import object

laserEnemyFX = pygame.mixer.Sound('Audio/LaserEnemy.wav')

ATTACK_RATE = 1000
WIDTH, HEIGHT = 1280, 720

# class EnemyShip(pygame.sprite.Sprite):
class EnemyShip(object.Object):
    count = 0

    def __del__(self):
        # super().__del__()
        EnemyShip.count -= 1
        print("Enemy destroyed. Total Left:",EnemyShip.count)

    def __init__(self):
        super().__init__(image_src="Art/EnemySpriteSheet2.png", rows=4, fps=5,speed=3)
        
        self.x = int(1280 + random.randrange(100,1000,75))
        self.y = random.randint(40, 600-self.height)

        self.nextFire = 0
        
        EnemyShip.count += 1
        print("Enemy Ship Count: ", EnemyShip.count)

    def move(self):
        # global x, angle
        self.x -= self.speed
        #self.x -= 3

        if self.x < -self.width and self.active == True:
            self.active = False
            EnemyShip.count-=1
            print("Enemy Ship Out Of Range - Count: ", EnemyShip.count)


        if pygame.time.get_ticks() > self.nextFrameTime:
            self.nextFrameTime = pygame.time.get_ticks() + self.rate
            self.currentFrame+=1
            if self.currentFrame > (self.totalCells-1):
                self.currentFrame = 0

        if (self.x > 0) and (self.x + self.width < WIDTH):
            self.attack = False
            if pygame.time.get_ticks() > self.nextFire:
                self.nextFire = pygame.time.get_ticks() + ATTACK_RATE
                self.attack = True

            
    def draw(self):
        if (self.active):
            self.DS.blit(self.image, (self.x, self.y), self.cells[self.currentFrame])

    @staticmethod
    def increment(num):
        EnemyShip.count += num

# enemyList = pygame.sprite.Group()
# enemySpriteSheet = ss.SpriteSheet("Art/EnemySpriteSheet2.png", 1, 4)    # Params: filename, cols, rows
3