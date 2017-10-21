#coding=utf-8
import pygame
from pygame.locals import *
from gameobjects.vector3 import *
A = (-6, 2, 2)
B = (7, 5, 10)
rocket_location=(-6,2,2)
plasma_speed = 100. # meters per second
AB = Vector3.from_points(A, B)
#print "Vector to droid is", AB
distance_to_target = AB.get_magnitude()
#print "Distance to droid is", distance_to_target, "meters"
plasma_heading = AB.get_normalized()
#print "Heading is", plasma_heading
pygame.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
while True:
    screen.fill((0,0,0))
    time_passed=clock.tick()
    time_passed_seconds=time_passed/1000.0
    print time_passed_seconds
    for _ in range(1000):
        rocket_location+=plasma_heading*time_passed_seconds*plasma_speed
        pygame.draw.aaline(screen,(255,255,255),(0, 2),(70, 50))
        #print rocket_location,plasma_heading,time_passed_seconds,plasma_speed
    pygame.display.update()
'''#######输出结果#########
Vector to droid is (13, 3, 8)
Distance to droid is 15.5563491861 meters
Heading is (0.835672, 0.192847, 0.514259)'''
