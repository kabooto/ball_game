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
    x = randint(0, 500)
    y = randint(0, 500)
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    circle(screen, rand_color, (x, y), 10)
    pygame.display.update()
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if pygame.mouse.get_pos() == (0, 0):
                break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
                pygame.quit()
