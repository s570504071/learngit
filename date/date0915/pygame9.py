#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
from random import *
from math import pi
pygame.init()
background_image_filename= 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_image_filename).convert()
sprite=pygame.image.load(sprite_image_filename)
clock=pygame.time.Clock()
x=0.
speed=20.
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,200))
    time_passed=clock.tick()
    time_passed_seconds=time_passed/1000.0
    distance_moved=time_passed_seconds*speed
    x+=distance_moved
    if x>640.:
        x-=640.
    pygame.display.update()
