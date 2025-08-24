import pygame
from consts import SOLDIER_HEIGHT , SOLDIER_WIDTH,X_MOVEMENT,Y_MOVEMENT,BOARD_LENGTH,BOARD_WIDTH,SOLDIER_LEGS,SOLDIER_BODY

soldier_image= pygame.image.load('soldier.png')
Soldier=pygame.transform.scale(soldier_image,(SOLDIER_WIDTH,SOLDIER_HEIGHT))


def soldier_movement(keys_pressed,soldier1):
    if keys_pressed[pygame.K_LEFT] and soldier1.x-X_MOVEMENT+20>0:
        soldier1.x-=X_MOVEMENT
    if keys_pressed[pygame.K_RIGHT] and soldier1.x + X_MOVEMENT< BOARD_WIDTH-20:
        soldier1.x += X_MOVEMENT
    if keys_pressed[pygame.K_UP] and soldier1.y-Y_MOVEMENT+20>0:
        soldier1.y -= Y_MOVEMENT
    if keys_pressed[pygame.K_DOWN] and soldier1.y+ Y_MOVEMENT<BOARD_LENGTH-60:
        soldier1.y += Y_MOVEMENT



def soldier_body(soldier1):
    body=pygame.Rect(soldier1.x,soldier1.y,SOLDIER_WIDTH,SOLDIER_HEIGHT-SOLDIER_LEGS)
    if body.colliderect(FLAG):
        WIN=True
    return WIN

def soldier_leg(soldier1):
    legs=pygame.Rect(soldier1.x,soldier1.y,SOLDIER_WIDTH,SOLDIER_HEIGHT-SOLDIER_BODY)
    if legs.colliderect(mines):
        run=False
    return run



