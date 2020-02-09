import pygame   
import pymunk
import pymunk.pygame_util
import random

WIDTH = 600
HEIGHT = 600
NODE_RAD = 7
COUNT = 0
BLACK = (0,0,0)
TRIANGLE_ROWS = 7

pygame.init()

#Setup pygame display window and create pymunk space
window = pygame.display.set_mode((WIDTH,HEIGHT))
drawing_options = pymunk.pygame_util.DrawOptions(window)

clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0.0,-1000.0)

def create_ball(radius, space, x,y):
    """
    Creates a pymunk body and shape to represent the balls in the simulation
    Parameters:
        radius (int): The radius of the ball
        space (pymunk.Space): The pymunk space for the simulation
        x (int): The starting x coordinate of the ball
        y (int): The starting y coordinate of the ball
    """

    inertia = pymunk.moment_for_circle(10,0, 25, (0,0))
    body = pymunk.Body(10,inertia)

    body.position = x,y
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.6
    shape.friction = 0.9
    space.add(body, shape)

def create_node(radius, space, x, y):
    """
    Creates a single node which is a static pymunk body
    """

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = x,y
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.5
    shape.friction = 0.9
    space.add(body, shape)

def create_node_triangle(rows, space):
    """
    Creates nodes in a triangular design
    Parameters:
        rows (int): The number of rows in the triangle
        space (pymunk.Space): The pymunk space to add the node to
    """

    mid = WIDTH//2
    spacing = WIDTH//13
    y = HEIGHT - (HEIGHT//9)
    
    for row_num in range(1, rows+1):
        #check for odd row
        if row_num%2 == 1:
            starting_x = mid - ((row_num//2)*spacing)
            
        #=check for even row
        else:
            starting_x = mid - ((row_num//2-1)*spacing) - spacing//2
        
        for node in range(0,row_num):
                create_node(NODE_RAD, space, starting_x, y)
                starting_x += spacing

        y -= spacing
    
def create_rails(space):
    """
    Creates the two top rails and bottom rail 
    """
    static_body = space.static_body
    rail_1 = pymunk.Segment(static_body, (0, HEIGHT-20), (210, HEIGHT-50), 2)
    rail_2 = pymunk.Segment(static_body, (WIDTH-210,HEIGHT-50), (WIDTH, HEIGHT-20), 2)
    rail_3 = pymunk.Segment(static_body, (0,10), (WIDTH, 10), 5)
    rail_1.elasticity = 0.9
    rail_2.elasticity = 0.9
    rail_1.friction = 0.05
    rail_2.friction = 0.05
    rail_3.elasticity = 0
    rail_3.friction = 10
    space.add(rail_1, rail_2, rail_3)

def create_vertical_rails(space):
    """
    Creates the vertical rails in the simulation
    """
    mid = WIDTH//2
    segment_width = (WIDTH-mid)//3
    vertical_lines = []

    static_body = space.static_body
    x = mid
    while x <= WIDTH:
        vertical_lines.append(pymunk.Segment(static_body, (x, 10), (x, 100), 2))
        x += segment_width
    x = mid
    while x >= 0:
        vertical_lines.append(pymunk.Segment(static_body, (x, 10), (x, 100), 2))
        x -= segment_width

    for line in vertical_lines:
        line.friction = 5
        line.elasticity = 0.4
        space.add(line)

def add_balls(space):
    """
    Adds balls every 30 cycles of the main loop 
    """
    if COUNT%30 == 0:
        for i in range(0,4):
            create_ball(5,space, random.randint(0,WIDTH), random.randint(HEIGHT-20,HEIGHT))
        

def init(space):
    """
    Initialises the simulation components
    """
    create_node_triangle(TRIANGLE_ROWS, space)
    create_rails(space)
    create_vertical_rails(space)


init(space)

if __name__ == "__main__":
    
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                

        add_balls(space)
        space.debug_draw(drawing_options)
        pygame.display.update()
        window.fill(BLACK)
        space.step(0.01)
        clock.tick(100)
        COUNT += 1

    pygame.quit()
