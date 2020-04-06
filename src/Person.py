import math
import random
import sys
import numpy as np
import pygame
from pygame.locals import *

class Person:

    def __init__(self, health, speed):
        self.x = random.uniform(0,1)
        self.y = random.uniform(0,1)
        self.speed = speed
        self.vx = speed * random.uniform(0,1)
        self.vy = speed * random.uniform(0,1)
        self.health = health

    def draw(self, windowSurface, xmax, ymax, radius):
        x = self.x
        y = self.y
        pygame.draw.circle(windowSurface, self.health, (int(xmax * self.x), int(ymax * self.y)), radius, 0)

    def move(self):
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        self.x += self.vx
        self.y += self.vy

    


if __name__=="__main__":
    HEALTHY = (0, 0, 255)
    SICK = (0, 255, 0)
    WHITE = (255, 255, 255)

    pygame.init()

    xmax = 600
    ymax = 400
    windowSurface = pygame.display.set_mode((xmax, ymax))
    pygame.display.set_caption('Covid-19 hermir')

    FRAMES_PER_SECOND = 30
    fpsClock = pygame.time.Clock()
    
    n = 20
    speed = 0.01
    radius = 5

    persons = np.zeros(n, dtype = object)
    persons[0] = Person(SICK, speed)
    
    for i in range(1,n):
        persons[i] = Person(HEALTHY, speed)

    while True:
        for i in range(n):
            windowSurface.fill(WHITE)
        
        for i in range(n):
            persons[i].move()

        for i in range(n):
            for j in range(i+1, n):
                distance = math.hypot(int(persons[i].x * xmax)- int(persons[j].x * xmax), int(persons[i].y * ymax) - int(persons[j].y * ymax))
                if distance <= radius*2:
                    persons[i].vx = -1 * persons[i].vx
                    persons[i].vy = -1 * persons[i].vy
                    persons[j].vx = -1 * persons[j].vx
                    persons[j].vy = -1 * persons[j].vy
                    if persons[i].health == SICK:
                        persons[j].health = SICK
                    elif persons[j].health == SICK:
                        persons[i].health = SICK

        for i in range(n):
            persons[i].draw(windowSurface, xmax, ymax, radius)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
    
    
    
        
    
    
