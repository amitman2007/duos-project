import pygame
from consts import FPS, MINES_LENGTH
# from screen import draw_window
# from soldier import Soldier
# from soldier import soldier_movement,SOLDIER_WIDTH,SOLDIER_HEIGHT,soldier_image
from consts import MINES_HEIGHT , MINES_LENGTH
import random

# def main():
#     soldier1=pygame.Rect(0,0,SOLDIER_WIDTH,SOLDIER_HEIGHT)
#     clock=pygame.time.Clock()
#     run=True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 run=False
#
#         keys_pressed=pygame.key.get_pressed()
#         soldier_movement(keys_pressed,soldier1)
#         draw_window(soldier1)
#
#     pygame.quit()
#
#     mine = pygame.Rect(0,0,MINES_LENGTH,MINES_HEIGHT)
#
#
#
# main()

from consts import MINES_HEIGHT, MINES_LENGTH,MINES_AMOUNT ,BOARD_WIDTH,BOARD_LENGTH

def random_grass ():
    mine_image= pygame.image.load('mine.png')
    mine=pygame.transform.scale(mine_image,(MINES_LENGTH,MINES_HEIGHT))
    grass_list =[]
    for i in range (MINES_AMOUNT):
        mine_image = pygame.image.load('mine.png')
        mine = pygame.transform.scale(mine_image, (MINES_LENGTH, MINES_HEIGHT))
        RANDOM1  = random.randint(0 , BOARD_WIDTH)
        RANDOM2 = random.randint(0, BOARD_WIDTH)
        mine1 = pygame.Rect(RANDOM1,RANDOM2, MINES_LENGTH, MINES_HEIGHT)
    pygame.display.update()
    return pygame.display.update()


