#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
my_event=pygame.event.Event(KEYDOWN,key=K_SPACE,mod=0,unicode=u'')
pygame.event.post(my_event)
for event in pygame.event.get():
    if event.type==KEYDOWN:
        if event.key==K_SPACE:
            print 'it is space'
        else:
            print 'not'
