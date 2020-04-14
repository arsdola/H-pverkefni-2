import math
import random
import sys
import numpy as np
import pygame
from pygame.locals import *
from Svaedi import *

WHITE = (255, 255, 255)

pygame.init()

xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()
    
n = 20

Rvk = Svaedi(n, 0, 0.5, 0.5, 0)
Ak = Svaedi(n, 0.5, 1, 1, 0.5)

while True:
    windowSurface.fill(WHITE)

    Rvk.move(xmax, ymax)
    Ak.move(xmax, ymax)

    Rvk.draw(windowSurface, xmax, ymax)
    Ak.draw(windowSurface, xmax, ymax)
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
