import pygame
from pygame.locals import *
import numpy as np
import random
from Classes.Dinosaur import Dinosaur
from Classes.Obstacle import Obstacle
from Classes.Pterodactyl import Pterodactyl

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
groundLoc = 360
gravity = 10
fps = 60
clock = pygame.time.Clock()
velocity = -400
player = Dinosaur([0,120],1/fps)
pterodactylList = []
obstacleList = [Obstacle([width,groundLoc],1/fps,'big')]
pygame.font.init()
myFont = pygame.font.SysFont("Times New Roman", 18)
duck = [20,10]
standing = [10,20]

done = False

x = 10;
y = 120;

currentTime = 0
jump = 0
    
def checkCollision(obstacleHitbox,playerHitbox):
    for i in range(len(playerHitbox)):
        corner = playerHitbox[i]
        #print(corner)
        #print(obstacleHitbox)
        if corner[0] >= obstacleHitbox[0][0] and corner[0] <= obstacleHitbox[1][0]:
            if corner[1] <= obstacleHitbox[1][1] and corner[1] >= obstacleHitbox[2][1]:
                return True
    
    return False

while not done:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                if not player.falling:
                    jump = 1
            if event.key == K_DOWN:
                player.extent = duck
        if event.type == pygame.KEYUP:
            if event.key==K_SPACE:
                jump = 0
            if event.key == K_DOWN:
                player.extent = standing
                
    player.updatePos(jump,gravity,groundLoc,screen)
    
    for i, obstacle in enumerate(obstacleList):
        obstacle.updatePos(velocity,screen) 
        collision = checkCollision(obstacle.hitbox,player.hitbox)
        if obstacle.position[0]+obstacle.extent[1] < 1:
            del obstacleList[i]
        if collision:
            print('You Died')
            done = collision
            
    for i, ptero in enumerate(pterodactylList):
        ptero.updatePos(velocity,screen) 
        collision = checkCollision(ptero.hitbox,player.hitbox)
        if ptero.position[0]+ptero.extent[1] < 1:
            del pterodactylList[i]
        if collision:
            print('You Died')
            done = collision
    
    if random.randint(1,1000) < 10 or len(obstacleList) == 0:
        obstacleList.append(Obstacle([width,groundLoc],1/fps,random.choice(['big','small'])))
        
    if random.randint(1,1000) < 10 and currentTime > 100:
        height = random.randint(0,2);
        pterodactylList.append(Pterodactyl([width,groundLoc],1/fps,height))
    
    score = myFont.render(str(currentTime),0,pygame.Color(255,255,255))
        
    screen.blit(score,(0,0))
    
    velocity = velocity - 0.1
    currentTime = currentTime+1
    clock.tick(60)
    pygame.display.flip()

# 3 - Main loop
#while 1:
    # Reset the screen each frame
