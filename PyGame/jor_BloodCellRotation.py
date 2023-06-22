"""
Rotating Blood Cell

@Author: Joe O'Regan
"""

__author__ = "Joe O'Regan"
__date__ = '22/06/2023'

import pygame

WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOUR = pygame.Color('gray15')
SPEED = 3
DEGREES = 2


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    new_image = pygame.transform.rotate(image, angle)  # Rotate the original image without modifying it.
    rect = new_image.get_rect(center=rect.center)  # Get a new rect with the center of the old rect.
    return new_image, rect


def main():
    pygame.display.set_caption("Blood Cell Rotation Test")
    clock = pygame.time.Clock()
    DS = pygame.display.set_mode((WIDTH, HEIGHT))

    blood_cell = pygame.image.load("../AntiBody/Art/BloodCell.png").convert()
    orig_image = blood_cell  # Keep a reference to the original to preserve the image quality.
    x = WIDTH / 2  # center sprite
    angle = 0

    done = False

    while not done:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update
        rect = blood_cell.get_rect(center=(x, HEIGHT / 2))

        if x < -(blood_cell.get_width() / 2):
            x = WIDTH + (blood_cell.get_width() / 2)
        else:
            x -= SPEED

        angle += DEGREES
        blood_cell, rect = rotate(orig_image, rect, angle)

        # Draw
        DS.fill(BACKGROUND_COLOUR)
        DS.blit(blood_cell, rect)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
