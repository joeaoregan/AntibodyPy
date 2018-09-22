"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *

# define display surface
width, height = 1280, 720
x = 0


def move():
    global x
    x -= 1
