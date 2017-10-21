#coding=utf-8
import pygame
from pygame.locals import *
import sys
from random import randint
image=pygame.image.load('leaf.png')
ball=pygame.image.load('ball.png')
f=pygame.image.load('sushiplate.jpg')
pygame.init()
screen=pygame.display.set_mode((640,480),0)
clock=pygame.time.Clock()
ball_position=(120,120)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(f,(0,0))
    time_passed=clock.tick(50)
    time_passed_seconds=time_passed/1000.0
    
    p=320+time_passed_seconds*3000
    #print time_passed_seconds
    screen.blit(image,(p,240))
    
    #ball_position+=
    screen.blit(ball,ball_position)
    
    pygame.display.update()
