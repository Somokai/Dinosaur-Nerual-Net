class Dinosaur:

    # Class Attributes
    state = 'default'
    velocity = 0
    time = 0
    falling = 1

    # Constructor   
    def __init__(self,position,dt):
        # self.image = image
        self.position = position
        self.dt = dt

    def updatePos(self,jump,gravity,ground):

        if jump == 1 and self.falling is not 1:
            self.velocity = self.velocity-50
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