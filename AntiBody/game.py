"""
Joe O'Regan
21/09/2018
"""

import pygame
from pygame.locals import *
import sys
import os

import AntiBody.bullet as bullet
import AntiBody.background as bg, AntiBody.player as player, AntiBody.bloodcell as bloodcell, AntiBody.enemyShip as enemyship, AntiBody.spritesheet as ss, AntiBody.explosion as explosion

score = 0
time = 30
timeChange = 0

# define display surface
width, height = 1280, 720
HW, HH = width/2, height/2

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antibody - Scrolling Background")
FPS = 120

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

fontName = pygame.font.match_font("comicsansms")

# define colours
BLACK = (0,0,0,255)
BLACK_T = (0,0,0,50)
WHITE = (255,255,255,255)
GREY = (100,100,100,255)

# Sprites & Images
bgImage = pygame.image.load("Art/background.png").convert()
playerImage = pygame.image.load("Art/Player1Ship.png").convert()
laserImage = pygame.image.load("Art/LaserGreen2.png").convert()
bloodcellImage = pygame.image.load("Art/BloodCell.png").convert()
orig_image = bloodcellImage

player1 = player.Player(playerImage.get_rect().width, bgImage.get_rect().height / 2)
# bloodCell1 = bloodcell.BloodCell(500,360)

bulletList = pygame.sprite.Group()
bloodCellList = pygame.sprite.Group()
enemyList = pygame.sprite.Group()
explosionList = pygame.sprite.Group()


enemySpriteSheet = ss.SpriteSheet("Art/EnemySpriteSheet2.png", 1, 4)    # Params: filename, cols, rows
explosionSpriteSheet = ss.SpriteSheet("Art/Explosion.png", 12, 1)

CENTER_HANDLE = 4
index = 0


def drawText(surface, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text = font.render(text, True, (255, 255, 255))     # True = text anti-aliased
    textRect = text.get_rect()
    textRect.midtop = (x,y)
    surface.blit(text, textRect)                        # draw text surface at location of text rectangle


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_p:
            pause()


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # DS.fill(BLACK_T)
        drawText(DS, "Paused", 60, width/2,(height-120)/2)
        drawText(DS, "Press P to continue or Esc to quit", 24, width/2, (height-120)/2 - 60)
        pygame.display.update()
        CLOCK.tick(5)


def input():
    global nextFire
    # Keyboard input
    k = pygame.key.get_pressed()

    # player.input()
    player1.input()

    if k[K_SPACE] and pygame.time.get_ticks() > bullet.NEXT_FIRE:
        bullet1 = bullet.Bullet(player1.x, player1.y + (playerImage.get_rect().height / 2))
        bulletList.add(bullet1)
        bullet.NEXT_FIRE = pygame.time.get_ticks() + 200


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    new_image = pygame.transform.rotate(image, angle)   # Rotate the original image without modifying it.
    rect = new_image.get_rect(center=rect.center)       # Get a new rect with the center of the old rect.
    return new_image, rect


def spawnGameObjects():
    if len(bloodCellList) < 8:
        bloodCell1 = bloodcell.BloodCell()
        bloodCellList.add(bloodCell1)

    if len(enemyList) < 2:
        enemy = enemyship.EnemyShip()
        enemyList.add(enemy)


def spawnExplosion(x, y, fps):
    explosion1 = explosion.Explosion(x, y, fps)
    explosionList.add(explosion1)


def update():
    global bloodcellImage, score, time, timeChange, index

    # Scrolling Background
    rel_x = bg.x % bgImage.get_rect().width
    DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
    if rel_x < width:
        DS.blit(bgImage, (rel_x, 0))
    bg.move()

    # Move and Draw Blood Cells
    for bloodCells in bloodCellList:
        bloodCells.move()
        rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))
        bloodcellImage, rect = rotate(orig_image, rect, bloodCells.angle)
        DS.blit(bloodcellImage, rect)
        # Remove from list after they travel off screen (left)
        #if bloodCells.x < -bloodCells.width:
        #    bloodCellList.remove(bloodCells)

    # Move and Draw Enemies
    for enemies in enemyList:
        enemies.move()
       # s.draw(DS, s.animationFPS(8), HW, HH, CENTER_HANDLE)
        enemySpriteSheet.draw(DS, enemySpriteSheet.animationFPS(8), enemies.x, enemies.y, CENTER_HANDLE)
        # Remove if off screen or destroyed
        if enemies.x < -enemies.width or enemies.active == False:
            enemyList.remove(enemies)

        # Collisions
        for bullets in bulletList:
            rect = pygame.Rect(enemies.x, enemies.y, enemySpriteSheet.cellWidth, enemySpriteSheet.cellHeight)
            if bullets.collisions(rect):
                score+=20
                spawnExplosion(enemies.x,enemies.y, 10)
                enemies.active=False


    # Move and Draw Bullets
    for bullets in bulletList:
        bullets.move()
        DS.blit(laserImage, (bullets.x, bullets.y))

    # Collisions Bullets and BloodCells
    for bloodCells in bloodCellList:
        if bloodCells.x < -bloodCells.width or not bloodCells.active:
            bloodCellList.remove(bloodCells)

        for bullets in bulletList:
            if not bullets.active:
                bulletList.remove(bullets)
            rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))

            if bullets.collisions(rect):
                score += 10
                bloodCells.active=False

    # Explosion update
    for explosions in explosionList:
        explosions.move()
        # Explosion
        # explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), 96, 96, CENTER_HANDLE)
        explosionSpriteSheet.draw(DS, explosionSpriteSheet.animationFPS(10), explosions.x, explosions.y, CENTER_HANDLE)
        if not explosions.active:
            explosionList.remove(explosions)


    # Player
    player1.move()
    DS.blit(playerImage, (player1.x, player1.y))


    # Time
    if pygame.time.get_ticks() > timeChange and time > 0:
        timeChange = pygame.time.get_ticks() + 1000
        time -= 1


    # Text
    drawText(DS, "Score: " + str(score), 24, width / 2, 5)
    drawText(DS, "Level: 1", 24, 50, 5)
    drawText(DS, "Time: " + str(time), 24, width - 100, 5)
    if time == 0:
        drawText(DS, "Time Is Up", 60, width/2,(height-120)/2)

    # rect(x, y, w, h)
    pygame.draw.rect(DS, GREY, [0,600,width,120], 0)


# Game loop
while True:
    events()
    input()
    spawnGameObjects()
    update()

    pygame.display.update()
    CLOCK.tick(FPS)
    # DS.fill(BLACK)
