import math
import random
import sys
import numpy as np
import pygame
import pygame_gui
import time
from pygame.locals import *
from Svaedi import *

WHITE = (255, 255, 255)

pygame.init()

xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

##
background = pygame.Surface((xmax, ymax))
background.fill(WHITE)

manager = pygame_gui.UIManager((xmax, ymax))

caption = pygame_gui.elements.ui_text_box.UITextBox('Texti hér....', pygame.Rect((10,20),(300,30)), manager = manager)


button_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 50), (200,50)), text = 'Takki 1 = Ekkert gert!', manager = manager)
button_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 110), (200,50)), text = 'Takki 2 = 4 svæði', manager = manager)


##

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

    
n = 20
n1 = 15
n2 = 5
n3 = 5

Ekkert = Svaedi(n, 0, 1, 1, 0)

Rvk = Svaedi(n, 0, 0.5, 0.5, 0)
Ak = Svaedi(n1, 0.5, 1, 1, 0.5)
Egils = Svaedi(n2, 0, 0.5, 1, 0.5)
Isafj = Svaedi(n3, 0.5, 1, 0.5, 0)

def button1():
    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Ekkert.move(xmax, ymax)
        Ekkert.draw(windowSurface, xmax, ymax)

        sick_persons = []
        for person in Ekkert.persons:
            if person.health == SICK:
                sick_persons.append(person)
        
        if len(sick_persons) == n:
            run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()
    
                
def button2():
    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Rvk.move(xmax, ymax)
        Ak.move(xmax, ymax)
        Egils.move(xmax, ymax)
        Isafj.move(xmax, ymax)


        Rvk.draw(windowSurface, xmax, ymax)
        Ak.draw(windowSurface, xmax, ymax)
        Egils.draw(windowSurface, xmax, ymax)
        Isafj.draw(windowSurface, xmax, ymax)

        sick_persons = []
        for person in Rvk.persons:
            if person.health == SICK:
                sick_persons.append(person)
        for person in Ak.persons:
            if person.health == SICK:
                sick_persons.append(person)
        for person in Egils.persons:
            if person.health == SICK:
                sick_persons.append(person)
        for person in Isafj.persons:
            if person.health == SICK:
                sick_persons.append(person)
                
        
        if len(sick_persons) == (n + n1 + n2 + n3):
            run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()

    
        
def run_loop():

    is_running = True

    while is_running:
        windowSurface.fill(WHITE)
        time_delta = fpsClock.tick(60)/100.0
   
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_1:
                        print('pressed button 1')
                        button1()
                
                    if event.ui_element == button_2:
                        print('pressed button 2')
                        button2()
                        
                        

                            
                        
                    
            manager.process_events(event)
        manager.update(time_delta)
    
        windowSurface.blit(background, (0,0))
        manager.draw_ui(windowSurface)
    
        pygame.display.update()
        #fpsClock.tick(FRAMES_PER_SECOND)

run_loop()


