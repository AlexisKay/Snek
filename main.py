import pygame
import time
import random
from pygame.constants import KEYDOWN, K_a

pygame.init()

snekColor=(9, 255, 0)
white=(255,255,255)
black=(0,0,0)
red=(227, 5, 49)
green=(0,255,0)
yellow=(225,225,102)
blue=(50,153,213)

wHeight = 800
wWidth = 600
SnakeB = 10
SnakeSpeed = 15

clock=pygame.time.Clock()
font_style = pygame.font.SysFont("helvetica", 25)
score_font = pygame.font.SysFont("helvetica",35)


dis=pygame.display.set_mode((wHeight, wWidth))
pygame.display.set_caption('Snek - AlexisKay')


def Score(score):
    value=score_font.render("Score: " +str(score), True, white)
    dis.blit(value,[wWidth/3,0])

def Snek(SnakeB, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis,snekColor,[x[0],x[1],SnakeB,SnakeB])



def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [wWidth/6, wHeight/6])

def GameLoop():
    game_over=False
    game_close=False

    
    x1=wWidth/2
    y1=wHeight/2
    x1dif=0
    y1dif=0

    snakeList=[]
    snakeLength=1

    foodx = round(random.randrange(0, wWidth - SnakeB) / 10.0) * 10.0
    foody = round(random.randrange(0, wHeight - SnakeB) / 10.0) * 10.0

    



    while not game_over:

        while game_close==True:
            dis.fill(black)
            message("You Lost - press 'Q' to quit, or 'C' to play again", red)
            Score(snakeLength-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over= True
                        game_close=False
                    if event.key == pygame.K_c:
                        GameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==KEYDOWN:
                if event.key ==  pygame.K_a:
                    x1dif=-SnakeB
                    y1dif=0
                if event.key == pygame.K_d:
                    x1dif=SnakeB
                    y1dif=0
                if event.key == pygame.K_w:
                    x1dif=0
                    y1dif=-SnakeB
                if event.key == pygame.K_s:
                    x1dif=0
                    y1dif=SnakeB
    
        if x1 >= wWidth or x1 <0 or y1 >= wHeight or y1 <0:
            game_close=True

        x1 += x1dif
        y1 += y1dif
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, SnakeB, SnakeB])
        snakeHead =[]
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]  

        for x in snakeList[:-1]:
            if x == snakeHead:
                game_close=True

        Snek(SnakeB, snakeList)
        Score(snakeLength -1) 
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, wWidth - SnakeB) / 10.0) * 10.0
            foody = round(random.randrange(0, wWidth - SnakeB) / 10.0) * 10.0
            snakeLength+=1


        clock.tick(SnakeSpeed)


    pygame.quit()
    quit()
GameLoop()