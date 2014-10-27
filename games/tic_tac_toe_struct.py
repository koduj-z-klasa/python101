import pygame, sys, random
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((150, 150), 0, 32)
pygame.display.set_caption('TicTacToe')

#0-empty, 1-player, 2-computer
BOARD_STATE = [0,0,0,
               0,0,0,
               0,0,0]

TURN = 1
WINNER = 0      # 0-no one, 1-player, 2-computer, 3-draw
VICTORY = False

#draw the board
def draw_board():
    for i in range(0,3):
        for j in range(0,3):
            pygame.draw.rect(DISPLAYSURF, (255,255,255), Rect((j*50,i*50),(50,50)),1)


def draw_board_state():
    for i in range(0,3):
        for j in range(0,3):
            field = i*3+j
            x = j*50+25
            y = i*50+25
            
            if BOARD_STATE[field] == 1:
                pygame.draw.circle(DISPLAYSURF,(0,0,255), (x,y),10)
            elif BOARD_STATE[field] == 2:
                pygame.draw.circle(DISPLAYSURF,(255,0,0), (x,y),10)
            

def place_symbol(field, turn):
    if BOARD_STATE[field] == 0:
        if turn == 1:
            BOARD_STATE[field] = 1
            return 2
        elif turn == 2:
            BOARD_STATE[field] = 2
            return 1
        
    return turn
        

def ai_move(turn):
    field = None
    winning_combinations = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]
    blocking_combinations = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    # step 1 - check victory move
    # horizontal
    if BOARD_STATE[0:3] in winning_combinations:
        field = BOARD_STATE[0:3].index(0)
    if BOARD_STATE[3:6] in winning_combinations:
        field = BOARD_STATE[3:6].index(0)+3
    if BOARD_STATE[6:9] in winning_combinations:
        field = BOARD_STATE[6:9].index(0)+6
    # vertical
    if [BOARD_STATE[0],BOARD_STATE[3],BOARD_STATE[6]] in winning_combinations:
        if BOARD_STATE[0] == 0: field = 0
        if BOARD_STATE[3] == 0: field = 3
        if BOARD_STATE[6] == 0: field = 6
    if [BOARD_STATE[1],BOARD_STATE[4],BOARD_STATE[7]] in winning_combinations:
        if BOARD_STATE[1] == 0: field = 1
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[7] == 0: field = 7
    if [BOARD_STATE[2],BOARD_STATE[5],BOARD_STATE[8]] in winning_combinations:
        if BOARD_STATE[2] == 0: field = 2
        if BOARD_STATE[5] == 0: field = 5
        if BOARD_STATE[8] == 0: field = 8
    # cross
    if [BOARD_STATE[0],BOARD_STATE[4],BOARD_STATE[8]] in winning_combinations:
        if BOARD_STATE[0] == 0: field = 0
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[8] == 0: field = 8
    
    if [BOARD_STATE[2],BOARD_STATE[4],BOARD_STATE[6]] in winning_combinations:
        if BOARD_STATE[2] == 0: field = 2
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[6] == 0: field = 6
    
    if field:
        return place_symbol(field, turn)
    
    # step 2 - block thy enemy
    if BOARD_STATE[0:3] in blocking_combinations:
        field = BOARD_STATE[0:3].index(0)
    if BOARD_STATE[3:6] in blocking_combinations:
        field = BOARD_STATE[3:6].index(0)+3
    if BOARD_STATE[6:9] in blocking_combinations:
        field = BOARD_STATE[6:9].index(0)+6
    # vertical
    if [BOARD_STATE[0],BOARD_STATE[3],BOARD_STATE[6]] in blocking_combinations:
        if BOARD_STATE[0] == 0: field = 0
        if BOARD_STATE[3] == 0: field = 3
        if BOARD_STATE[6] == 0: field = 6
    if [BOARD_STATE[1],BOARD_STATE[4],BOARD_STATE[7]] in blocking_combinations:
        if BOARD_STATE[1] == 0: field = 1
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[7] == 0: field = 7
    if [BOARD_STATE[2],BOARD_STATE[5],BOARD_STATE[8]] in blocking_combinations:
        if BOARD_STATE[2] == 0: field = 2
        if BOARD_STATE[5] == 0: field = 5
        if BOARD_STATE[8] == 0: field = 8
    # cross
    if [BOARD_STATE[0],BOARD_STATE[4],BOARD_STATE[8]] in blocking_combinations:
        if BOARD_STATE[0] == 0: field = 0
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[8] == 0: field = 8
    
    if [BOARD_STATE[2],BOARD_STATE[4],BOARD_STATE[6]] in blocking_combinations:
        if BOARD_STATE[2] == 0: field = 2
        if BOARD_STATE[4] == 0: field = 4
        if BOARD_STATE[6] == 0: field = 6
    
    if field:
        return place_symbol(field, turn)
    
    while field == None:
        pos = random.randrange(0,9)
        if BOARD_STATE[pos] == 0:
            field = pos
            
    return place_symbol(field, turn)

def check_victory():
    #horizontal
    winner = 0
    if BOARD_STATE[0] == BOARD_STATE[1] and BOARD_STATE[0] == BOARD_STATE[2]:
        winner = BOARD_STATE[0]
    if BOARD_STATE[3] == BOARD_STATE[4] and BOARD_STATE[3] == BOARD_STATE[5]:
        winner = BOARD_STATE[3]
    if BOARD_STATE[6] == BOARD_STATE[7] and BOARD_STATE[6] == BOARD_STATE[8]:
        winner = BOARD_STATE[6]

    #vertical
    if BOARD_STATE[0] == BOARD_STATE[3] and BOARD_STATE[0] == BOARD_STATE[6]:
        winner = BOARD_STATE[0]
    if BOARD_STATE[1] == BOARD_STATE[4] and BOARD_STATE[1] == BOARD_STATE[7]:
        winner = BOARD_STATE[1]
    if BOARD_STATE[2] == BOARD_STATE[5] and BOARD_STATE[2] == BOARD_STATE[8]:
        winner = BOARD_STATE[2]
        
    #cross
    if BOARD_STATE[0] == BOARD_STATE[4] and BOARD_STATE[0] == BOARD_STATE[8]:
        winner = BOARD_STATE[0]
    if BOARD_STATE[2] == BOARD_STATE[4] and BOARD_STATE[2] == BOARD_STATE[6]:
        winner = BOARD_STATE[2]
    
    #check for draw
    if 0 not in BOARD_STATE and winner not in [1,2]:
        winner = 3
    
    return winner


def draw_winner(winner):
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    if winner == 1:
        prompt = "Player wins!"
    elif winner == 2:
        prompt = "Computer wins!"
    elif winner == 3:
        prompt = "Draw!"
    text_surf = fontObj.render(prompt, True, (20,255,20))
    text_rect = text_surf.get_rect()
    text_rect.center = (75, 75)
    DISPLAYSURF.blit(text_surf, text_rect)

# main game loop
while True:
    #handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if VICTORY == False:
            if TURN == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouseX, mouseY = event.pos
                        field = ((mouseY//50)*3)+(mouseX//50)
                        TURN = place_symbol(field, TURN)  
            elif TURN == 2:
                TURN = ai_move(TURN)
            
            WINNER = check_victory()
            if WINNER != 0:
                VICTORY = True
            
            
    DISPLAYSURF.fill((0,0,0))
    draw_board()
    draw_board_state()
    if VICTORY:
        draw_winner(WINNER)
    pygame.display.update()