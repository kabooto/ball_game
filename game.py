import pygame
from pygame.draw import *
from random import randint

pygame.init()


def new_ball():
    """
    Makes a new ball
    :return: None
    """
    global x, y  # variable for window size
    x = randint(10, 490)
    y = randint(10, 490)
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))  # Ball colors
    circle(screen, rand_color, (x, y), 10)  # Ball


def click():
    """
    processing clicking
    :return: None
    """
    global event, score  # event queue and score counter
    if event.type == pygame.MOUSEBUTTONDOWN:  # mouse bottom down process
        mouse_pos = pygame.mouse.get_pos()  # getting mouse click position
        x1, y1 = mouse_pos[0], mouse_pos[1]  # separate X, Y mouse position
        if abs(x - x1) <= 10 and abs(y - y1) <= 10:  # if mouse hit the ball
            score += 1
            print('Your score is: ', score)


def esc_exit():
    """
    exit from the game
    :return: None
    """
    global finished  # variable of working game
    if event.type == pygame.KEYDOWN:  # condition for the finish the game
        if event.key == pygame.K_ESCAPE:
            finished = True
            pygame.quit()


FPS = 1
size = [500, 500]
screen = pygame.display.set_mode(size)  # screen size

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
