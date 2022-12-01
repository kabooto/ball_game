import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
size = [500, 500]
screen = pygame.display.set_mode(size)

finished = False

pygame.display.update()
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
                pygame.quit()
