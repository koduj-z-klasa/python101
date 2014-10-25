import pygame, sys, random
from pygame.locals import *

pygame.init()

WIDNOW_WIDTH = 800
WINDOW_HEIGHT = 400

DISPLAYSURF = pygame.display.set_mode((WIDNOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('GameOfLife')

BOX_SIZE = 10
HOR_BOXES = WIDNOW_WIDTH/BOX_SIZE
VER_BOXES = WINDOW_HEIGHT/BOX_SIZE

DEAD_CELL = 0
LIVE_CELL = 1

GAME_BOARD = [DEAD_CELL] * HOR_BOXES
    
for i in range(HOR_BOXES):
    GAME_BOARD[i] = [DEAD_CELL] * VER_BOXES


def draw_board():
    for y in range(VER_BOXES):
        for x in range(HOR_BOXES):
            if GAME_BOARD[x][y] == LIVE_CELL:
                pygame.draw.rect(DISPLAYSURF, (255,255,255), Rect((x*BOX_SIZE,y*BOX_SIZE),(BOX_SIZE,BOX_SIZE)),1)
            
def update_life(board):
    #prepare the next generation board
    next_gen = [DEAD_CELL] * HOR_BOXES
    for i in range(HOR_BOXES):
        next_gen[i] = [DEAD_CELL] * VER_BOXES
    
    # loop over everything    
    for y in range(VER_BOXES):
        for x in range(HOR_BOXES):
            
            #count population around cell
            population = 0
            #row1
            try:
                if board[x-1][y-1] == LIVE_CELL: population += 1
            except IndexError:pass
            try:
                if board[x][y-1] == LIVE_CELL: population += 1
            except IndexError:pass
            try:
                if board[x+1][y-1] == LIVE_CELL: population += 1
            except IndexError:pass
                
            #row2
            try:
                if board[x-1][y] == LIVE_CELL: population += 1
            except IndexError:pass
            try:
                if board[x+1][y] == LIVE_CELL: population += 1
            except IndexError:pass
            
            #row3
            try:
                if board[x-1][y+1] == LIVE_CELL: population += 1
            except IndexError:pass
            try:
                if board[x][y+1] == LIVE_CELL: population += 1
            except IndexError:pass
            try:
                if board[x+1][y+1] == LIVE_CELL: population += 1
            except IndexError:pass
        
            # underpopulation or overpopulation - DEATH
            if board[x][y] == LIVE_CELL and (population < 2 or population > 3):
                next_gen[x][y] = DEAD_CELL
            # carry on with life
            elif board[x][y] == LIVE_CELL and (population == 3 or population == 2):
                next_gen[x][y] = LIVE_CELL
            # new life
            elif board[x][y] == DEAD_CELL and population == 3:
                next_gen[x][y] = LIVE_CELL
            
    #return the board with the next generation.
    return next_gen


life_running = False
button_down = False

# main game loop
while True:
    #handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN:
            life_running = True
        
        if life_running == False:
            if event.type == MOUSEBUTTONDOWN:
                button_down = True
                button_type = event.button
                
            if event.type == MOUSEBUTTONUP:
                button_down = False
                
            if button_down:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = mouse_x / BOX_SIZE
                mouse_y = mouse_y / BOX_SIZE
                # left mouse button
                if button_type == 1: GAME_BOARD[mouse_x][mouse_y] = LIVE_CELL
                # right mouse button
                if button_type == 3: GAME_BOARD[mouse_x][mouse_y] = DEAD_CELL
                
    if life_running == True:
        GAME_BOARD = update_life(GAME_BOARD)
        
    DISPLAYSURF.fill((0,0,0))
    draw_board()
    pygame.display.update()
    pygame.time.delay(100)