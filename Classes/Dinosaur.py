import pygame

class Dinosaur:

    # Class Attributes
    extent = [15,35]
    velocity = 0
    time = 0
    falling = 1
    color = pygame.Color(255,255,255)

    # Constructor   
    def __init__(self,position,dt):
        # self.image = image
        self.position = position
        self.dt = dt
        self.hitbox = [(self.position[0],self.position[1]),
                (self.position[0]+self.extent[0],self.position[1]),
                (self.position[0]+self.extent[0],self.position[1]-self.extent[1]),
                (self.position[0],self.position[1]-self.extent[1])]

    def updatePos(self,jump,gravity,ground,win):

        if jump == 1 and self.falling is not 1:
            self.velocity = self.velocity-30
            self.falling = 1
        else:
            self.velocity = self.velocity + gravity*self.time
        
        self.time = self.time+self.dt
            
        dy = 1/2*gravity*self.time*self.time+self.velocity*self.time
        
        if self.position[1] >= ground and jump == 0:
            self.position[1] = ground
            self.velocity = 0
            self.time = 0
            self.falling = 0 
        else: 
            self.position[1] = min(self.position[1]+dy,ground)
            
        self.hitbox = [(self.position[0],self.position[1]),
                (self.position[0]+self.extent[0],self.position[1]),
                (self.position[0]+self.extent[0],self.position[1]-self.extent[1]),
                (self.position[0],self.position[1]-self.extent[1])]
            
        self.draw(win)
    
    def draw(self, win):
        pygame.draw.polygon(win,self.color,self.hitbox)