import random

WIDTH = 21
HEIGHT = 10
TRIANGLE_ROWS = 6

def create_grid(width, height):
    grids = []
    for x in range(0,width):
        temp = []
        for y in range(0, height):
            temp.append(' ')
        grids.append(temp)
    return grids



class Ball:

    def __init__(self):

        mid = round(WIDTH/2)
        self.x = random.randint(mid-WIDTH//5, mid+WIDTH//5)
        self.y = 0

    
class Grid:

    def __init__(self):
        
        self.balls = []
        self.grid = create_grid(WIDTH, HEIGHT)


    def setup_nodes(self):
        """
        Used to setup the the triangular group of nodes
        """
        y = HEIGHT//10
        centre_node = round(WIDTH/2)
        node_in_row = 1
        
        for row in range(0, TRIANGLE_ROWS):
            #check whether even or odd row
            either_side = node_in_row//2

            if node_in_row % 2 == 1:
                x_coor = centre_node-(2*either_side)
                
            elif node_in_row % 2 == 0:
                x_coor = centre_node-(2*either_side)+1
                
            for node in range(0, node_in_row):
                    self.grid[x_coor][y] = 'O'
                    x_coor +=2
            
            node_in_row +=1 
            y+=2



