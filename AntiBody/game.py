"""
Enemy Ship Class

@Author: Joe O'Regan
@Date: 21/09/2018
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame
from pygame.locals import *
import sys
# import os

import bullet
import background
import player
import bloodcell
import enemyShip
# import spritesheet as ss
import explosion


FPS = 120

# define display surface
WIDTH, HEIGHT = 1280, 720
HW, HH = WIDTH/2, HEIGHT/2

game_objects = []

PAUSED = False
score = 0
time = 30
timeChange = 0

FONT = pygame.font.match_font("comicsansms")

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((WIDTH, HEIGHT))

# define colours
BLACK = (0,0,0,255)
BLACK_T = (0,0,0,50)
WHITE = (255,255,255,255)
GREY = (100,100,100,255)

CENTER_HANDLE = 4


def exit_game():
    """Exit the game"""
    pygame.quit()
    sys.exit()


def draw_text(surface, text, size, x, y):
    """Draw text at coordinates x,y"""
    font = pygame.font.Font(FONT, size)
    text = font.render(text, True, (255, 255, 255))     # True = text anti-aliased
    text_rect = text.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text, text_rect)                        # draw text surface at location of text rectangle


def events():
    """Handle game events"""
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            exit_game()

        if event.type == KEYDOWN and event.key == K_p:
            pause()


def pause():
    """Pause state"""
    global PAUSED
    PAUSED = True

    while PAUSED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    PAUSED = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()
            if event.type == QUIT:
                exit_game()

        ### DS.fill(BLACK_T)
        draw_text(DS, "Paused", 60, HW,(HEIGHT-120)/2)
        draw_text(DS, "Press P to continue or Esc to quit", 24, HW, (HEIGHT-120)/2 - 60)
        pygame.display.update()
        CLOCK.tick(5)


def handle_input():
    # global nextFire  # unused
    k = pygame.key.get_pressed()  # Keyboard input

    for obj in game_objects:
        if obj.input() == "Fire":
            # obj.fire()
            spawnBullet(obj.x, obj.y + (obj.image.get_rect().height / 2))

    # if k[K_SPACE] and pygame.time.get_ticks() > bullet.NEXT_FIRE:
    #     spawnBullet(10, 360)
    #     bullet.NEXT_FIRE = pygame.time.get_ticks() + 200

'''
    if k[K_SPACE] and pygame.time.get_ticks() > bullet.NEXT_FIRE:
        bullet1 = bullet.Bullet(player1.x, player1.y + (playerImage.get_rect().height / 2))
        bulletList.add(bullet1)
        bullet.NEXT_FIRE = pygame.time.get_ticks() + 200
'''


def spawnBullet(x, y):
    game_objects.append(bullet.Bullet(x, y))


def spawnEnemy(amount=1):
    for count in range(amount):
        if enemyShip.EnemyShip.count < 2:
            game_objects.append(enemyShip.EnemyShip())


def spawnExplosion(x, y, fps):
    # explosion1 = explosion.Explosion(x, y, fps)
    # explosionList.add(explosion1)
    game_objects.append(explosion.Explosion(x, y, fps))  # Spawn explosion


def init():
    bg1 = background.Background()
    bg2 = background.Background(x=WIDTH)
    player1 = player.Player()

    game_objects.append(bg1)
    game_objects.append(bg2)
    game_objects.append(player1)

    for i in range(8):
        game_objects.append(bloodcell.BloodCell())

    #game_objects.append(enemyShip.EnemyShip())
    #game_objects.append(enemyShip.EnemyShip())
    spawnEnemy(2)

    # for obj in game_objects:
        # print(type(obj))
        # print(obj.__class__.__name__)


def update():
    global score, time, timeChange

    pygame.display.update()
    CLOCK.tick(FPS)

    spawnEnemy()

    for obj in game_objects:
        obj.move()  # Player, etc.
        # Collisions
        for obstacle in game_objects:
            if obstacle is obj:
                # print("obj",obj.__class__.__name__,"is obstacle")
                continue

            if obstacle.__class__.__name__ in ['BloodCell', 'Enemy']:
                # print("player 1 collision check", obstacle.__class__.__name__)
                # rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.cellWidth, obstacle.cellHeight)

                if obstacle.__class__.__name__ == "BloodCell":
                    if obj.__class__.__name__ == "Player" or obj.__class__.__name__ == "Bullet":
                        # rect = obstacle.get_image().get_rect(center=(bloodCells.x, bloodCells.y))
                        if obj.collision(obstacle.get_rect()):
                            if obstacle.active:
                                score += 10
                            obstacle.active = False
                            spawnExplosion(obstacle.x,obstacle.y, 10)
                            if obj.__class__.__name__ == "Player":
                                obj.health -= 2


    # Time
    if pygame.time.get_ticks() > timeChange and time > 0:
        timeChange = pygame.time.get_ticks() + 1000
        time -= 1


def collisions():
    pass


'''
#def update():
#    global score, time, timeChange
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
   
    # Collisions Bullets and BloodCells
    for bloodCells in bloodCellList:

        for bullets in bulletList:
            if not bullets.active:
                bulletList.remove(bullets)
            rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))

            if bullets.collisions(rect):
                score += 10
                bloodCells.active=False
'''

def draw():
    """Draw the game objects"""
    # if PAUSED:
    DS.fill(BLACK)  # Clear the screen

    for obj in game_objects:
        obj.draw()  # Player, etc.

    # Text
    draw_text(DS, "Score: " + str(score), 24, HW, 5)
    draw_text(DS, "Level: 1", 24, 50, 5)
    draw_text(DS, "Time: " + str(time), 24, WIDTH - 100, 5)
    if time == 0:
        draw_text(DS, "Time Is Up", 60, HW, (HEIGHT-120)/2)
    pygame.draw.rect(DS, GREY, [0, 600, WIDTH, 120], 0)


def main():
    pygame.display.set_caption("Antibody - Scrolling Background")
    # os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

    init()

    while True:  # Game loop
        events()
        handle_input()
        update()
        draw()


if __name__ == '__main__':
    pygame.init()
    main()
    exit_game()
