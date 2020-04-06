import sys
import numpy as np
import pygame
from pygame.locals import *

# set up the colors (RGB - red-green-blue values)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# set up pygame
pygame.init()

#set uppp window
xboundary = 600
yboundary = 400
windowSurface = pygame.display.set_mode((xboundary, yboundary))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()



# Initial coordinates are uniformly random in (0, 1)
x = np.random.rand(n)
y = np.random.rand(n)

# Point velocity is uniformly random in (0, speed)
vx = speed * np.random.rand(n)
vy = speed * np.random.rand(n)
for i in range(int(frozen*n)):
    vx[i] = 0
    vy[i] = 0


class svaedi:
    n = 50 # Number of points
    frozen = 0.5 # Fraction of points that do not move
    p_unfreeze = 0.01 # Probability of a frozen point going on the move
    speed = 0.01
    radius = 5
    
    def __init__(self, xmin, ymin, xmax, ymax):
        #self.box = (xmin, ymin, xmax,ymax)
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        

#ætti einstaingu að koma í staðinn
    #def speed(self):?
        
    

# Update positions
    def move(self):
        for i in range(n):
            if x[i] < self.xmax or x[i] > self.xmin:
                vx[i] = -1 * vx[i]
            if y[i] < self.ymax or y[i] > self.ymin:
                vy[i] = -1 * vy[i]
            x[i] += vx[i]
            y[i] += vy[i]

    #def out_of_boundary(self):
        #Hvenær fara einstaklinga milli landsvæða?


    def draw(self):
        for i in range(n):
            pygame.draw.circle(windowSurface, BLUE, \
                            (int(self.xmax * x[i]), int(self.ymax * y[i])), self.radius, 0)

# Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)



#reykjavik = Svaedi(100, 200, 400, 400)
#reykjavík.move
#reykjavik.draw

