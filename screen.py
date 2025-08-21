import pygame
from consts import main_screen
from duo_project.consts import GRID_COLOR
from duo_project.soldier import soldier_image, Soldier


def draw_window(soldier1):
    main_screen.fill(GRID_COLOR)
    main_screen.blit(Soldier,(soldier1.x,soldier1.y))
    pygame.display.update()