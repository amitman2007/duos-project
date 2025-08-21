import pygame
from consts import FPS
from duo_project.screen import draw_window
from duo_project.soldier import Soldier
from soldier import soldier_movement


def main():
    soldier1=pygame.rect()
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys_pressed=pygame.key.get_pressed()
        soldier_movement(keys_pressed,Soldier)
        draw_window()

    pygame.quit()


main()