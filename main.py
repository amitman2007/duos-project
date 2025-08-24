import pygame
from consts import FPS
from duo_project.consts import BOARD_LENGTH, BOARD_WIDTH, FLAG_WIDTH,FLAG_HEIGHT,cord1,cord2
from duo_project.screen import draw_window,draw_grass
from duo_project.soldier import Soldier
from soldier import soldier_movement,SOLDIER_WIDTH,SOLDIER_HEIGHT


def main():
    pygame.display.set_caption("the flag")
    soldier1=pygame.Rect(0,0,SOLDIER_WIDTH,SOLDIER_HEIGHT)
    flag1=pygame.Rect(BOARD_WIDTH-FLAG_WIDTH,BOARD_LENGTH-FLAG_WIDTH,FLAG_WIDTH,FLAG_HEIGHT)
    grass1=pygame.Rect(cord1,cord2,60,20)
    clock=pygame.time.Clock()
    run=True
    WIN=False
    while run==True and WIN==False:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        keys_pressed=pygame.key.get_pressed()
        soldier_movement(keys_pressed,soldier1)
        draw_window(soldier1,flag1,grass1)

    pygame.quit()


main()