import pygame
from consts import SOLDIER_HEIGHT , SOLDIER_WIDTH,X_MOVEMENT,Y_MOVEMENT

soldier_image= pygame.image.load('soldier.png')
Soldier=pygame.transform.scale(soldier_image,(SOLDIER_WIDTH,SOLDIER_HEIGHT))


def soldier_movement(keys_pressed,soldier):
    if keys_pressed[pygame.K_LEFT]:
        soldier.x-=X_MOVEMENT
    if keys_pressed[pygame.K_LEFT]:
        soldier.x -= X_MOVEMENT
    if keys_pressed[pygame.K_LEFT]:
        soldier.x -= Y_MOVEMENT
    if keys_pressed[pygame.K_LEFT]:
        soldier.x -= Y_MOVEMENT

