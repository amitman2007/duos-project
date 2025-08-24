import pygame
import random
from consts import main_screen
from duo_project.consts import GRID_COLOR,BOARD_LENGTH,BOARD_WIDTH
from duo_project.soldier import soldier_image, Soldier
from game_field import flag,grass




def draw_window(soldier1,flag1,grass1):
     main_screen.fill(GRID_COLOR)
     main_screen.blit(Soldier,(soldier1.x,soldier1.y))
     main_screen.blit(flag,(flag1.x,flag1.y))
     for i in range(20):
      main_screen.blit(grass,(grass1.x,grass1.y))
      cord1 = random.randint(0, BOARD_WIDTH - 20)
      cord2 = random.randint(0, BOARD_LENGTH - 20)

     pygame.display.update()

def draw_grass(number,grass1):
   for i in range(number):
       main_screen.blit(grass,(grass1.x,grass1.y))
       cord1=random.randint(0,BOARD_WIDTH-20)
       cord2=random.randint(0,BOARD_WIDTH-20)
       pygame.display.update()