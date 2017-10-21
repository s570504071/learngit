#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
SCREEN_SIZE=(640,480)
pygame.init()
background_image_filename='sushiplate.jpg'
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_image_filename).convert()
while True:
    event=pygame.event.wait()
    if event.type==QUIT:
        exit()
    if event.type==VIDEORESIZE:
        SCREEN_SIZE=event.size
        screen=pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
        pygame.display.set_caption('current size:'+str(event.size))
        
    screen_width,screen_height=SCREEN_SIZE
    '''
显示新一张的图
    for y in range(0,screen_height,background.get_height()):
        for x in range(0,screen_width,background.get_width()):
            screen.blit(background,(x,y))
            '''
    background=pygame.transform.scale(background,SCREEN_SIZE)
    for y in range(0,screen_height,background.get_height()):
        for x in range(0,screen_width,background.get_width()):
            screen.blit(background,(x,y))
    pygame.display.update()