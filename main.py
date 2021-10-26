import pygame
from pygame.constants import KEYDOWN

pygame.init()

snekColor=(58,68,84)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

dis=pygame.display.set_mode((1100,1100))
pygame.display.set_caption('Snek - AlexisKay')
pygame.display.update()

game_over=False
x1=300
y1=300
x1dif=0
y1dif=0

clock=pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==KEYDOWN:
        



    pygame.draw.rect(dis,snekColor,[200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()