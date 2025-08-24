import pygame
import random
from consts import MINES_AMOUNT,MINES_LENGTH,MINES_HEIGHT,BOARD_LENGTH,BOARD_WIDTH
from consts import FLAG_WIDTH,FLAG_HEIGHT
grass_image = pygame.image.load("grass.png")
grass = pygame.transform.scale(grass_image, (60, 60))

flag_image=pygame.image.load("flag.png")
flag=pygame.transform.scale(flag_image,(FLAG_WIDTH,FLAG_HEIGHT))





# def enter (pressed):
#     enter_pressed = False
#     if pressed[pygame.K_KP_ENTER]:
#       enter_pressed = True
#     return enter_pressed
#
# if enter () :
#     pygame.init()
#     size = (BOARD_WIDTH,BOARD_LENGTH)  # Width, Height
#     screen = pygame.display.set_mode(size)
#     pygame.display.set_caption("My Pygame mines Window")
#     screen.fill((255, 255, 255))
#     cord_list = []
#
#
#     x= 0
#     y=25
#     for i in range(MINES_GRID_ROW):
#         cord_list.append((x,y))
#         x = x+25
#         y=y+25
#     x2 = 0
#     y2 = 50
#
#     for i in range(MINES_GRID_COL):
#
#         cord_list.append((x,y))
#         x2 = x+25
#         y2=y+25
#
#     pygame.draw.lines(screen,MINES_GRID_LINES_COLOR ,  False,cord_list)
#     pygame.display.update()