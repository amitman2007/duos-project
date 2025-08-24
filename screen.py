import pygame
from consts import main_screen,GRID_COLOR ,MINES_GRID_ROW, BOARD_LENGTH, BOARD_WIDTH, MINES_GRID_LINES_COLOR,MINES_GRID_COL

# from soldier import soldier_image, Soldier
#
#
# def draw_window(soldier1):
#     main_screen.fill(GRID_COLOR)
#     main_screen.blit(Soldier,(soldier1.x,soldier1.y))
#     pygame.display.update()

# def draw_grass(mine):
#     main_screen.fill(GRID_COLOR)
#     main_screen.blit(mine,(mine1))
#     pygame.display.update()


def enter (pressed):
    enter_pressed = False
    if pressed[pygame.K_KP_ENTER]:
      enter_pressed = True
    return enter_pressed

if enter () :
    pygame.init()
    size = (BOARD_WIDTH,BOARD_LENGTH)  # Width, Height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Pygame mines Window")
    screen.fill((255, 255, 255))
    cord_list = []


    x= 0
    y=25
    for i in range(MINES_GRID_ROW):
        cord_list.append((x,y))
        x = x+25
        y=y+25
    x2 = 0
    y2 = 50

    for i in range(MINES_GRID_COL):

        cord_list.append((x,y))
        x2 = x+25
        y2=y+25

    pygame.draw.lines(screen,MINES_GRID_LINES_COLOR ,  False,cord_list)
    pygame.display.update()

