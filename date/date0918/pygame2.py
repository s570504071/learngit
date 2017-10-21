#coding=utf-8
import pygame
import sys
from pygame.locals import *
from random import randint
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
red_scale0=pygame.surface.Surface((640,100))
green_scale0=pygame.surface.Surface((640,100))
blue_scale0=pygame.surface.Surface((640,100))
rest_scale0=pygame.surface.Surface((640,180))

for x in range(640):
    c=int(x*255./640.)
    red=(c,0,0)
    green=(0,c,0)
    blue=(0,0,c)
    pygame.draw.rect(red_scale0,red,(x,00,640,100))
    pygame.draw.rect(green_scale0,green,(x,00,640,100))
    pygame.draw.rect(blue_scale0,blue,(x,00,640,100))
color=[0,0,0]
    

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.fill((0,0,0))
    screen.blit(red_scale0,(0,0))
    screen.blit(green_scale0,(0,100))
    screen.blit(blue_scale0,(0,200))
    screen.blit(rest_scale0,(0,300))
    
    x,y=pygame.mouse.get_pos()
    if y in range(0,301):
        pos=x,y
    pygame.draw.circle(screen,(125,125,125),pos,20)
    if pygame.mouse.get_pressed()[0]:
        if y in range(100):
            color[0]=int(x*255./639.)
        elif y in range(101,200):
            color[1]=int(x*255./639.)
        elif y in range(201,300):
            color[2]=int(x*255./639.)
    cl=tuple(color)
    pygame.draw.rect(rest_scale0,cl,(0,0,640,180))
    pygame.display.set_caption('color:%s'%color)
    pygame.display.update()
