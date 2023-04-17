import time
from textwrap import fill

import pygame
import random
from itertools import islice
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 720))
score = 0
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
food = False
keyPressedW = False
keyPressedS = False
keyPressedA = False
keyPressedD = False
test = [keyPressedW, keyPressedS, keyPressedA, keyPressedD]
counter = 0
cords = []
cordsXY = []
clock.tick(60)

def splitingList(data_list):
    new_list = [data_list[i:i + 2] for i in range(0, len(data_list), 2)]
    return new_list

def setFalse(keys):
    keys[0] = False
    keys[1] = False
    keys[2] = False
    keys[3] = False
    return keys


def spawnObject():
    food_pos = pygame.Vector2(random.randrange(1, 1280), random.randrange(1, 720))
    return food_pos


def move():
    if test[0]:
        player_pos.y -= 8
        if player_pos.y < 5:
            test[0] = False
    if test[1]:
        player_pos.y += 8
        if player_pos.y > 715:
            test[1] = False
    if test[2]:
        player_pos.x -= 8
        if player_pos.x < 5:
            test[2] = False
    if test[3]:
        player_pos.x += 8
        if player_pos.x > 1275:
            test[3] = False


def object_Interaction():
    return int(foodCords.y) - 20 <= int(player_pos.y) <= int(foodCords.y) + 20 \
           and int(foodCords.x) - 20 <= int(player_pos.x) <= int(foodCords.x) + 20


def snake_drawing_head(player_pos, color):
    global counter
    global cords
    pygame.draw.circle(screen, color, player_pos, 20)
    cordsXY.append(player_pos.x)
    cordsXY.append(player_pos.y)
    if counter > score:
        counter = 0
        print(splitingList(cordsXY))
        cordsXY.clear()
        cords.clear()
    counter = counter + 1

def snake_drawing_tail(score, keys):
    nextXPosition = lastHeadPosition.x
    nextYPosition = lastHeadPosition.y

    for i in range(score):
        if keys[0]:
            snake_drawing_head(pygame.Vector2(nextXPosition, nextYPosition + (i + 1) * 20), "black")
        if keys[1]:
            snake_drawing_head(pygame.Vector2(nextXPosition, nextYPosition - (i + 1) * 20), "black")
        if keys[2]:
            snake_drawing_head(pygame.Vector2(nextXPosition + (i + 1) * 20, nextYPosition), "black")
        if keys[3]:
            snake_drawing_head(pygame.Vector2(nextXPosition - (i + 1) * 20, nextYPosition), "black")


def food_generatior():
    global foodCords, food
    if not food:
        foodCords = spawnObject()
        food = True


def food_drawing():
    pygame.draw.circle(screen, "black", foodCords, 20)


def growTheSnake(score):
    snake_drawing_head(player_pos, "red")
    snake_drawing_tail(score, test)


def keys_manager():
    global test

    if keys[pygame.K_w]:
        if not test[1]:
            test = setFalse(test)
            test[0] = True
    if keys[pygame.K_s]:
        if not test[0]:
            test = setFalse(test)
            test[1] = True
    if keys[pygame.K_a]:
        if not test[3]:
            test = setFalse(test)
            test[2] = True
    if keys[pygame.K_d]:
        if not test[2]:
            test = setFalse(test)
            test[3] = True
    return player_pos


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    food_generatior()

    food_drawing()

    if object_Interaction():
        food = False
        score += 1

    move()
    keys = pygame.key.get_pressed()
    lastHeadPosition = keys_manager()
    growTheSnake(score)
    myfont = pygame.font.SysFont("monospace", 15)
    label = " " + str(score) + " "
    label = myfont.render(label, 1, (0, 0, 0))
    screen.blit(label, (100, 100))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
