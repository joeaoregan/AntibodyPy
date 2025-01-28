"""
Rotating Blood Cell

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import random
import object


# class BloodCell(pygame.sprite.Sprite):
#original_image = None


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    new_image = pygame.transform.rotate(image, angle)   # Rotate the original image without modifying it.
    rect = new_image.get_rect(center=rect.center)       # Get a new rect with the center of the old rect.
    return new_image, rect


class BloodCell(object.Object):
    def __init__(self):
        #super().__init__()
        super().__init__(image_src="Art/BloodCell.png")

        #global original_image

        self.x = 1280 + random.randrange(100,1000,75)
        self.y = random.randint(40, 600)
        self.velocityX = 0
        self.velocityY = 0
        self.angle = random.randint(0,180)
        # self.width = 100
        # self.height = 55
        self.active = True
        self.rotate = random.randint(0,2)
        self.rotateSpeed = random.uniform(0.5, 3.0)
        self.rect = None
        self.original_image = self.image

    def move(self):
        # global x, angle
        self.x -= 3

        # if self.x < -self.width:
        #    self.active = False

        if self.rotate % 2 == 0:
            self.angle += self.rotateSpeed
        else:
            self.angle -= self.rotateSpeed

        self.angle %= 360

        # if self.x < -self.width or not self.active:

        # Reset Blood Cell position
        if self.x < -self.width or not self.active:
            self.active = True
            self.x = 1280 + random.randrange(100,1000,75)
            self.y = random.randint(40, 600)

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image, rect = rotate(self.original_image, self.rect, self.angle)
        #self.x = rect.x
        #self.y = rect.y
        #self.image, rect = rotate(self.image, self.rect, self.angle)

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.image, rect = rotate(self.original_image, self.rect, self.angle)
        super().DS.blit(self.image, rect)

    def input(self):
        pass

    def collision(self, rect):
        return False

"""
    # Move and Draw Blood Cells
    for bloodCells in bloodCellList:
        bloodCells.move()
        rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))
        bloodcellImage, rect = rotate(orig_image, rect, bloodCells.angle)
        DS.blit(bloodcellImage, rect)
        ### Remove from list after they travel off screen (left)
        ### if bloodCells.x < -bloodCells.width:
        ###   bloodCellList.remove(bloodCells)
"""
