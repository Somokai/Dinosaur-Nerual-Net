import pygame
from pygame.locals import *
import numpy as np
import random
from Classes.Dinosaur import Dinosaur

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
groundLoc = 360
gravity = 9.8
fps = 60
clock = pygame.time.Clock()
player = Dinosaur([0,120],1/fps)

done = False

x = 10;
y = 120;

currentTime = 0

jump = 0
while not done:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key==K_SPACE:
                if not player.falling:
                    jump = 1
        if event.type == pygame.KEYUP:
            if event.key==K_SPACE:
                jump = 0
                
    player.updatePos(jump,gravity,groundLoc)
    x = player.position[0];
    y = player.position[1];
    pygame.draw.polygon(screen,pygame.Color(255,255,255),[(x,y),(x+10,y),(x+10,y+20),(x,y+20)])

    currentTime = currentTime+1
    clock.tick(60)
    pygame.display.flip()

# 3 - Main loop
#while 1:
    # Reset the screen each frame
