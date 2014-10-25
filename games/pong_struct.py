import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
# frames per second setting
fpsClock = pygame.time.Clock()

GAMEWINDOW_WIDTH = 800
GAMEWINDOW_HEIGHT = 400

DISPLAYSURF = pygame.display.set_mode((GAMEWINDOW_WIDTH, GAMEWINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Simple Pong')

LT_BLUE = (230, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#init paddles
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_1_POS = (350, 360)
PADDLE_2_POS = (350, 20)

AI_SPEED = 3

# SCORE COUNTERS
PLAYER_1_SCORE = '5'
PLAYER_2_SCORE = '0'

#init ball
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_X_SPEED = 6
BALL_Y_SPEED = 6

#init paddle1
paddle1_surf = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
paddle1_surf.fill(BLUE)
paddle1_rect = paddle1_surf.get_rect()
paddle1_rect.x = PADDLE_1_POS[0]
paddle1_rect.y = PADDLE_1_POS[1]

#init paddle1
paddle2_surf = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
paddle2_surf.fill(RED)
paddle2_rect = paddle2_surf.get_rect()
paddle2_rect.x = PADDLE_2_POS[0]
paddle2_rect.y = PADDLE_2_POS[1]



ball_surf = pygame.Surface([BALL_WIDTH, BALL_HEIGHT], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball_surf, GREEN, [0, 0, BALL_WIDTH, BALL_HEIGHT])
ball_rect = ball_surf.get_rect()
ball_rect.x = GAMEWINDOW_WIDTH/2
ball_rect.y = GAMEWINDOW_HEIGHT/2




fontObj = pygame.font.Font('freesansbold.ttf', 64)

def render_score_p1():
    text_surf1 = fontObj.render(PLAYER_1_SCORE, True, (0,0,0))
    text_rect1 = text_surf1.get_rect()
    text_rect1.center = (GAMEWINDOW_WIDTH/2, GAMEWINDOW_HEIGHT*0.75)
    DISPLAYSURF.blit(text_surf1, text_rect1)

def render_score_p2():
    text_surf2 = fontObj.render(PLAYER_2_SCORE, True, (0,0,0))
    text_rect2 = text_surf2.get_rect()
    text_rect2.center = (GAMEWINDOW_WIDTH/2, GAMEWINDOW_HEIGHT/4)
    DISPLAYSURF.blit(text_surf2, text_rect2)

# main game loop

start = False

while not start:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            start = True
    

while True:
    #handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.set_caption('Hello')
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            #update paddle position
            
            shift = mouseX-(PADDLE_WIDTH/2)
            #right side
            if shift > GAMEWINDOW_WIDTH-PADDLE_WIDTH:
                shift = GAMEWINDOW_WIDTH-PADDLE_WIDTH
            #left side
            if shift < 0:
                shift = 0
            paddle1_rect.x = shift
    
    #AI
    if ball_rect.centerx > paddle2_rect.centerx:
        paddle2_rect.x += AI_SPEED
    elif ball_rect.centerx < paddle2_rect.centerx:
        paddle2_rect.x -= AI_SPEED
        
    
    #move ball after events
    ball_rect.x += BALL_X_SPEED
    ball_rect.y += BALL_Y_SPEED
    
    #collision check
    
    #WALLS
    if ball_rect.right >= GAMEWINDOW_WIDTH:
        BALL_X_SPEED *= -1
    if ball_rect.left <= 0:
        BALL_X_SPEED *= -1
        
    #PADDLES
    if ball_rect.colliderect(paddle1_rect):
        BALL_Y_SPEED *= -1
        #correct clipping
        ball_rect.bottom = paddle1_rect.top
        
    if ball_rect.colliderect(paddle2_rect):
        BALL_Y_SPEED *= -1
        #correct clipping
        ball_rect.top = paddle2_rect.bottom

    if int(PLAYER_1_SCORE)%10 == 0:
        FPS = FPS * 2
        
        
    #OUT OF LEVEL
    #TOP
    if ball_rect.top <= 0:
        #reset ball position
        ball_rect.x = GAMEWINDOW_WIDTH/2
        ball_rect.y = GAMEWINDOW_HEIGHT/2
        #add point
        PLAYER_1_SCORE = str(int(PLAYER_1_SCORE)+1)
        
    if ball_rect.bottom >= GAMEWINDOW_HEIGHT:
        #reset ball position
        ball_rect.x = GAMEWINDOW_WIDTH/2
        ball_rect.y = GAMEWINDOW_HEIGHT/2
        #add point
        PLAYER_2_SCORE = str(int(PLAYER_2_SCORE)+1)
            
    
    #render elements
    DISPLAYSURF.fill(LT_BLUE)
    
    render_score_p1()
    render_score_p2()
    
    DISPLAYSURF.blit(paddle1_surf, paddle1_rect)
    DISPLAYSURF.blit(paddle2_surf, paddle2_rect)
    DISPLAYSURF.blit(ball_surf, ball_rect)
    pygame.display.update()
    fpsClock.tick(FPS)
#END
