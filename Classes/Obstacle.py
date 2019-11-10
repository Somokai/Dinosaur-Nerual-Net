import pygame

class Obstacle:

    # Class Attributes
    extent = [50,20]
    time = 0
    color = pygame.Color(255,255,255)

    # Constructor   
    def __init__(self,position,dt,size):
        # self.image = image
        self.position = position
        self.dt = dt
        
        if size == 'big':
            self.extent = [50,20]
        elif size == 'small':
            self.extent = [10,20]
            
        self.hitbox = [(self.position[0],self.position[1]),
                        (self.position[0]+self.extent[0],self.position[1]),
                        (self.position[0]+self.extent[0],self.position[1]-self.extent[1]),
                        (self.position[0],self.position[1]-self.extent[1])]

    def updatePos(self,velocity,win):
        
        self.position[0] = self.position[0]+velocity*self.dt
        
        self.hitbox = [(self.position[0],self.position[1]),
                        (self.position[0]+self.extent[0],self.position[1]),
                        (self.position[0]+self.extent[0],self.position[1]-self.extent[1]),
                        (self.position[0],self.position[1]-self.extent[1])]
        
        self.draw(win)
        
    def draw(self, win):
        pygame.draw.polygon(win,self.color,self.hitbox)

        
