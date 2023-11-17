

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

# # Acquire background image
bg_surface = pygame.image.load('assets/bg-game-asset.jpg').convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.blit(bg_surface, (0,0))