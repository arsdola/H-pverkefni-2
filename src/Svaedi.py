import math
import random
import sys
import numpy as np
import pygame
from pygame.locals import *
from Person import *

HEALTHY = (0, 0, 255)
SICK = (0, 255, 0)

class Svaedi:
    
    def __init__(self, n, leftX, rightX, topY, bottomY, speed=0.01):
        self.n = n
        self.speed = speed
        self.persons = np.zeros(n, dtype = object)
        
        self.leftX = leftX
        self.rightX = rightX
        self.topY = topY
        self.bottomY = bottomY
        
        self.persons[0] = Person(SICK, speed, leftX, rightX, topY, bottomY)
        for i in range(1,n):
            self.persons[i] = Person(HEALTHY, speed, leftX, rightX, topY, bottomY)
                

        
    
    def move(self, xmax, ymax):
        for i in range(self.n):
            self.persons[i].move()

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
                        self.persons[j].health = SICK
                    elif self.persons[j].health == SICK:
                        self.persons[i].health = SICK

                      
    def draw(self, windowSurface, xmax, ymax):
        for i in range(self.n):
            self.persons[i].draw(windowSurface, xmax, ymax)



