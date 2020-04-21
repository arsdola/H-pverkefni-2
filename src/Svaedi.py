import math
import random
import sys
import numpy as np
import pygame
from pygame.locals import *
from Person import *



class Svaedi:
    
    def __init__(self, n, leftX, rightX, topY, bottomY, speed=0.01):
        self.n = n
        self.speed = speed
        self.persons = np.zeros(n, dtype = object)
        
        self.leftX = leftX
        self.rightX = rightX
        self.topY = topY
        self.bottomY = bottomY
        
        for i in range(n):
            self.persons[i] = Person(HEALTHY, speed, leftX, rightX, topY, bottomY)


    def next_to_leftBorder(self, i):
        #random_nr = random.uniform(0,1)
        #if random_nr < 0.05 or random_nr == 0.05:
        if i < self.n:
            if self.persons[i].health == SICK:
                if self.persons[i].x < self.leftX and self.leftX != 0:
                    return True
        else:
            return False

    def next_to_rightBorder(self, i):
        #random_nr = random.uniform(0,1)
        #if random_nr < 0.05 or random_nr == 0.05:
        if i < self.n:
            if self.persons[i].health == SICK:
                if self.persons[i].x > self.rightX and self.rightX != 1:
                    return True
        else:
            return False
            
    def next_to_bottomBorder(self, i):
        #random_nr = random.uniform(0,1)
        #if random_nr < 0.05 or random_nr == 0.05:
        if i < self.n:
            if self.persons[i].health == SICK:
                if self.persons[i].y > self.topY and self.topY != 1:
                    return True
        else:
            return False
            
    def next_to_topBorder(self, i):
        #random_nr = random.uniform(0,1)
        #if random_nr < 0.05 or random_nr == 0.05:
        if i < self.n:
            if self.persons[i].health == SICK:
                if self.persons[i].y < self.bottomY  and self.bottomY != 0:
                    return True
        else:
            return False
                
            
    
    def move(self, xmax, ymax):
        for i in range(self.n):
            self.persons[i].move()

        for i in range(self.n):
            self.persons[i].update()

        
        for i in range(self.n):
            if self.persons[i].x < self.leftX or self.persons[i].x > self.rightX:
                self.persons[i].vx = -1 * self.persons[i].vx
            if self.persons[i].y < self.bottomY or self.persons[i].y > self.topY:
                self.persons[i].vy = -1 * self.persons[i].vy
            self.persons[i].x += self.persons[i].vx
            self.persons[i].y += self.persons[i].vy

        for i in range(self.n):
            for j in range(i+1, self.n):
                distance = math.hypot(int(self.persons[i].x * xmax)-int(self.persons[j].x * xmax), int(self.persons[i].y * ymax) - int(self.persons[j].y * ymax))
                if distance <= RADIUS*2:
                    self.persons[i].vx = -1 * self.persons[i].vx
                    self.persons[i].vy = -1 * self.persons[i].vy
                    self.persons[j].vx = -1 * self.persons[j].vx
                    self.persons[j].vy = -1 * self.persons[j].vy
                    if self.persons[i].health == SICK:
                        self.persons[j].set_sick()
                    elif self.persons[j].health == SICK:
                        self.persons[i].set_sick()

                      
    def draw(self, windowSurface, xmax, ymax):
        for i in range(self.n):
            self.persons[i].draw(windowSurface, xmax, ymax)

        pygame.draw.line(windowSurface, (0,0,0), (self.leftX*xmax, self.topY*ymax), (self.rightX*xmax, self.topY*ymax), 2)
        pygame.draw.line(windowSurface, (0,0,0), (self.leftX*xmax, self.bottomY*ymax), (self.rightX*xmax, self.bottomY*ymax), 2)

        pygame.draw.line(windowSurface, (0,0,0), (self.leftX*xmax, self.topY*ymax), (self.leftX*xmax, self.bottomY*ymax), 2)
        pygame.draw.line(windowSurface, (0,0,0), (self.rightX*xmax, self.topY*ymax), (self.rightX*xmax, self.bottomY*ymax), 2)
