import pygame
from consts import main_screen
from duo_project.consts import GRID_COLOR
from duo_project.soldier import soldier_image, Soldier


def draw_window():
    main_screen.fill(GRID_COLOR)
    main_screen.blit(Soldier,(0,0))
    pygame.display.update()