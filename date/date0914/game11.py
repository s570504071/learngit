#coding=utf-8
import pygame
from pygame.locals import *
import sys
pygame.init()
my_font=pygame.font.SysFont('arial',16)
name_surface=my_font.render('Pygame ok!',True,(0,0,0),(255,255,255))
pygame.image.save(name_surface,'ok.png')
