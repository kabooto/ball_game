import pygame
from pygame.draw import *
from random import randint

pygame.init()


def new_ball():
    global x, y
    x = randint(10, 490)
    y = randint(10, 490)
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    circle(screen, rand_color, (x, y), 10)


def click():
    global event, score
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        x1, y1 = mouse_pos[0], mouse_pos[1]
        if abs(x - x1) <= 10 and abs(y - y1) <= 10:
            score += 1
            print('Your score is: ', score)


def esc_exit():
    global finished
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            finished = True
            pygame.quit()


FPS = 1
size = [500, 500]
screen = pygame.display.set_mode(size)

finished = False

pygame.display.update()
clock = pygame.time.Clock()
score = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        esc_exit()
        click()
    new_ball()
    pygame.display.update()
    screen.fill('Black')

