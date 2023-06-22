import pygame
from pygame.locals import *
import sys
import os

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# define display surface
W, H = 576, 1024
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W,H))
pygame.display.set_caption("code.Pylet - Seamless Background Scrolling")
FPS = 120

bkgd = pygame.image.load("mountains.png").convert()
x = 0

# main loop
while True:
    events()

    rel_x = x % bkgd.get_rect().width
    DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))
    x -= 1

    #pygame.draw.line(DS, 255,0,0), (rel_x, 0)
    pygame.display.update()
    CLOCK.tick(FPS)
