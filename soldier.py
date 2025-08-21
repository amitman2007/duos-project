import pygame
from consts import SOLDIER_HEIGHT , SOLDIER_WIDTH,X_MOVEMENT,Y_MOVEMENT

soldier_image= pygame.image.load('soldier.png')
Soldier=pygame.transform.scale(soldier_image,(SOLDIER_WIDTH,SOLDIER_HEIGHT))


def soldier_movement(keys_pressed,soldier1):
    if keys_pressed[pygame.K_LEFT]:
        soldier1.x-=X_MOVEMENT
    if keys_pressed[pygame.K_RIGHT]:
        soldier1.x += X_MOVEMENT
    if keys_pressed[pygame.K_UP]:
        soldier1.y -= Y_MOVEMENT
    if keys_pressed[pygame.K_DOWN]:
        soldier1.y += Y_MOVEMENT

