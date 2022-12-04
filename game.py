import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
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
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0] > x - 5 or mouse_pos[0] < x + 5:
                if mouse_pos[1] > y - 5 or mouse_pos[1] < y + 5:
                    finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
                pygame.quit()
