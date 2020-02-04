import model
import pygame   

BLACK = (0,0,0)
RED = (200,0,0)

pygame.init()


window = pygame.display.set_mode((model.WIDTH,model.HEIGHT))

active = True

grid = model.Grid(window)
grid.setup_nodes()



while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            pygame.quit()

    for y, j in enumerate(grid.grid):
        for x,i in enumerate(j):
            if i == "N":
                pygame.draw.circle(window, RED, (x,y), 5)
    
    grid.update()
    pygame.display.update()
    window.fill(BLACK)
