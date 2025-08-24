# import conts
# #פתיחת חלון ראשי

import pygame
pygame.init()
screen = pygame.display.set_mode((1250, 750))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    from conts import GRID_COLOR
    screen.fill(GRID_COLOR)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#ניסוי

from conts import GRID_LINES_COLOR
pygame.draw.line(screen,GRID_LINES_COLOR , x , y)


#םתיחת חלון מוקשים
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1250, 750))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    from conts import MINES_GRID_COLOR
    screen.fill(MINES_GRID_COLOR)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


#מטריצת המשחק
from conts import MATRIX_ROW,MATRIX_COL , MATRIX
ind = [30,25]
for row in range(MATRIX_ROW):
    new_row =[]
    for col in range(MATRIX_COL):
        ind[row][col][0]+= 30
        ind[row][col][1]+= 25
        new_row.append(ind)
    MATRIX.append(new_row)
print(MATRIX)





