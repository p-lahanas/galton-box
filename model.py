import random
import pygame

WIDTH = 600
HEIGHT = 600
TRIANGLE_ROWS = 6
BALL_COLOUR = (255,52,179)

def create_grid(width, height):
    grids = []
    for y in range(0,height):
        temp = []
        for x in range(0, width):
            temp.append(' ')
        grids.append(temp)
    return grids



class Ball:
    RADIUS = 4
    def __init__(self):

        mid = round(WIDTH/2)
        self.x = random.randint(mid-WIDTH//5, mid+WIDTH//5)
        self.y = 0
        self.yvel = 5
        self.accel = 0.01
        self.xvel = 0

    def draw(self, window):
        pygame.draw.circle(window, BALL_COLOUR, (self.x, self.y), self.RADIUS)


    def update(self, window):
        self.draw(window)

        if self.y + self.yvel< HEIGHT:
            self.y += int(self.yvel)
            self.yvel += self.accel
        
        self.x += self.xvel
        

    
class Grid:

    def __init__(self, window):
        
        self.balls = [Ball(), Ball(), Ball()]
        self.grid = create_grid(WIDTH, HEIGHT)
        self.window = window

    def setup_nodes(self):
        """
        Used to setup the the triangular group of nodes
        """
        y = HEIGHT//8
        centre_node = round(WIDTH/2)
        nodes_in_row = 1
        SPACE = 40
        for row in range(0, TRIANGLE_ROWS):
            
            either_side = nodes_in_row//2 #determine how many nodes either side of the middle node

            #check whether even or odd row
            if nodes_in_row % 2 == 1:
                x_coor = centre_node-(SPACE*either_side)
                
            elif nodes_in_row % 2 == 0:
                x_coor = centre_node-(SPACE*either_side) + SPACE//2
                
            for node in range(0, nodes_in_row):
                    self.grid[y][x_coor] = 'N'
                    x_coor += SPACE
            
            nodes_in_row +=1 
            y+=SPACE

    def update(self):

        for ball in self.balls:
            ball.update(self.window)
    
    def collision_check(self, ball):
        coors_to_check = []
        for j,y in enumerate(self.grid):
            for i,x in enumerate(x):
                if x =='N':
                    pass
                    #coors_to_check.append()

