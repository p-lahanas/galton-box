import random
import pygame
import math

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
        self.yvel = 0
        self.accel = 1
        self.xaccel = 0
        self.xvel = 0
        self.mag_vel = self.get_mag_vel()

    def draw(self, window):
        pygame.draw.circle(window, BALL_COLOUR, (self.x, self.y), self.RADIUS)


    def update(self, window):
        self.draw(window)
        self.mag_vel = self.get_mag_vel()

        if self.y + self.yvel< HEIGHT:
            self.y += int(self.yvel)
            self.yvel += self.accel
        
        self.x += int(self.xvel)
        self.xvel += self.xaccel
    def get_mag_vel(self):
        return math.sqrt(self.xvel**2+self.yvel**2)

    
class Grid:
    COLLISION_CONSTANT = 0.8

    def __init__(self, window):
        
        self.balls = [Ball(), Ball(), Ball(), Ball(), Ball(), Ball()]
        self.grid = create_grid(WIDTH, HEIGHT)
        self.window = window
        self.node_location = []
        self.coors_to_check = []

    def setup_nodes(self):
        """
        Used to setup the the triangular group of nodes
        """
        y_gap = HEIGHT//8
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
                    self.grid[y_gap][x_coor] = 'N'
                    self.node_location.append((x_coor, y_gap))
                    x_coor += SPACE
            
            nodes_in_row +=1 
            y_gap+=SPACE
        
       
        for node in self.node_location:
            for j, y in enumerate(self.grid[node[1]-5:node[1]+6]):
                for i, x in enumerate(y[node[0]-5:node[0]+6]):
                        if math.sqrt((5-j)**2 + (5-i)**2) <= 5:
                            self.coors_to_check.append((int(node[0]+i-5),int(node[1]+j-5)))

        yc = 0
        for xc in range(0,y_gap-40):
            if xc % 5 == 0:
                self.grid[yc][xc] = 'L'
                self.coors_to_check.append((xc,yc))
                yc += 1
        
        for xc in range(y_gap+20, WIDTH):
            if xc % 5 == 0:
                self.grid[yc][xc] = 'L'
                self.coors_to_check.append((xc,yc))
                yc += -1

    def update(self):

        for ball in self.balls:
            self.collision_check(ball)
            ball.update(self.window)
            
    
    def collision_check(self, ball):
        
        
        coors_to_check_ball = []
        for jb,yb in enumerate(self.grid[ball.y-5:ball.y+6]):
            for ib,xb in enumerate(yb[ball.x-5:ball.x+6]):
                if math.sqrt((5-ib)**2 + (5-jb)**2) <= ball.RADIUS:
                    coors_to_check_ball.append((int(ball.x+ib-5), int(ball.y+jb-5)))
                    
        for coor in self.coors_to_check:
            if coor in coors_to_check_ball:
                 
                direction_vector = (ball.x-coor[0], ball.y-coor[1])
                
                mag_direction_vector = math.sqrt((ball.y-coor[1])**2+(ball.x-coor[0])**2)
                if mag_direction_vector !=0:
                    unit_vector = (direction_vector[0]/mag_direction_vector, direction_vector[1]/mag_direction_vector)
                else:
                    unit_vector = direction_vector
                

                ball.xvel = int(unit_vector[0]*ball.mag_vel)#*self.COLLISION_CONSTANT)
                ball.yvel = int(unit_vector[1]*ball.mag_vel*self.COLLISION_CONSTANT)
                
                break