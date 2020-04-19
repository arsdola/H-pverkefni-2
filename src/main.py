import math
import random
import sys
import numpy as np
import pygame
import pygame_gui
import time
from pygame.locals import *
from svaedi import *

WHITE = (255, 255, 255)
SICK = (0, 255, 0)

pygame.init()

xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

##
#background = pygame.Surface((800, 600))
background = pygame.Surface((xmax, ymax))
background.fill(WHITE)

#manager = pygame_gui.UIManager((800, 600))
manager = pygame_gui.UIManager((xmax, ymax))

caption = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((10,20),(400,30)), text = 'Hermun eftir Covid-19 í mismunandi aðstæðum: ',manager = manager)


button_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 90), (200,50)), text = 'Takki 1 = Ekkert gert!', manager = manager)
button_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 200), (200,50)), text = 'Takki 2 = 4 svæði', manager = manager)
button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 300), (200,50)), text = 'Takki 3 = Sóttkví?', manager = manager)

slider = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((250,80),(200,30)), text = 'Veldu fjölda persóna:',manager = manager)
horiz_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((250, 110), (200, 30)),start_value = 5, value_range=(2,50),manager=manager)

slider1 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((240,170),(170,20)), text = 'Fjöldi fyrir Svæði 1:',manager = manager)
slider2 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((420,170),(170,20)), text = 'Fjöldi fyrir Svæði 2:',manager = manager)
slider3 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((240,220),(170,20)), text = 'Fjöldi fyrir Svæði 3:',manager = manager)
slider4 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((420,220),(170,20)), text = 'Fjöldi fyrir Svæði 4:',manager = manager)

horiz_slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((240, 190), (160, 30)),start_value = 5, value_range=(2,10),manager=manager)
horiz_slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((420, 190), (160, 30)),start_value = 5, value_range=(2,10),manager=manager)
horiz_slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((240, 240), (160, 30)),start_value = 5, value_range=(2,10),manager=manager)
horiz_slider4 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((420, 240), (160, 30)),start_value = 5, value_range=(2,10),manager=manager)


##

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()


def button1():
    
    Ekkert = Svaedi(int(horiz_slider.get_current_value()), 0, 1, 1, 0)
    Ekkert.persons = np.delete(Ekkert.persons, 1)
    Ekkert.persons = np.append(Ekkert.persons, Person(SICK, Ekkert.speed, 0, 1, 1, 0))

    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Ekkert.move(xmax, ymax)
        Ekkert.draw(windowSurface, xmax, ymax)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()
    
                
def button2():

    n = int(horiz_slider1.get_current_value())
    n1 = int(horiz_slider2.get_current_value())
    n2 = int(horiz_slider3.get_current_value())
    n3 = int(horiz_slider4.get_current_value())

    Rvk = Svaedi(n, 0, 0.5, 0.5, 0)
    Ak = Svaedi(n1, 0.5, 1, 1, 0.5)
    Egils = Svaedi(n2, 0, 0.5, 1, 0.5)
    Isafj = Svaedi(n3, 0.5, 1, 0.5, 0)

    ## Byrja með einn sýktan í Rvk
    Rvk.persons = np.delete(Rvk.persons, 1)
    Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))

    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Rvk.move(xmax, ymax)
        Ak.move(xmax, ymax)
        Egils.move(xmax, ymax)
        Isafj.move(xmax, ymax)
        
        for i in range(Rvk.n):
            if Rvk.next_to_rightBorder(i) and (Rvk.n == n or Rvk.n > n):
                print('Rvk grænn og snertir hægri')
                Rvk.persons = np.delete(Rvk.persons, i)
                Rvk.n = Rvk.n-1
                Isafj.n = Isafj.n+1
                Isafj.persons = np.append(Isafj.persons, Person(SICK, Isafj.speed, 0.5, 1, 0.5, 0))

        
        for i in range(Rvk.n):
            if Rvk.next_to_bottomBorder(i) and (Rvk.n == n or Rvk.n > n):
                print('Rvk grænn og snertir niðri')
                Rvk.persons = np.delete(Rvk.persons, i)
                Rvk.n = Rvk.n-1
                Egils.n = Egils.n+1
                Egils.persons = np.append(Egils.persons, Person(SICK, Egils.speed, 0, 0.5, 1, 0.5))

        for i in range(Egils.n):
            if Egils.next_to_topBorder(i) and (Egils.n > n2 or Egils.n == n2):
                print('Egils grænn og snertir uppi')
                Egils.persons = np.delete(Egils.persons, i)
                Egils.n = Egils.n-1
                Rvk.n = Rvk.n+1
                Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))

        for i in range(Egils.n):
            if Egils.next_to_rightBorder(i) and (Egils.n > n2 or Egils.n == n2):
                print('Egils grænn og snertir hægri')
                Egils.persons = np.delete(Egils.persons, i)
                Egils.n = Egils.n-1
                Ak.n = Ak.n+1
                Ak.persons = np.append(Ak.persons, Person(SICK, Ak.speed, 0.5, 1, 1, 0.5))

        for i in range(Ak.n):
            if Ak.next_to_leftBorder(i) and (Ak.n > n1 or Ak.n == n1):
                print('Ak grænn og snertir vinstri')
                Ak.persons = np.delete(Ak.persons, i)
                Ak.n = Ak.n-1
                Egils.n = Egils.n+1
                Egils.persons = np.append(Egils.persons, Person(SICK, Egils.speed, 0, 0.5, 1, 0.5))

        for i in range(Ak.n):
            if Ak.next_to_topBorder(i) and (Ak.n > n1 or Ak.n == n1):
                print('Ak grænn og snertir uppi')
                Ak.persons = np.delete(Ak.persons, i)
                Ak.n = Ak.n-1
                Isafj.n = Isafj.n+1
                Isafj.persons = np.append(Isafj.persons, Person(SICK, Isafj.speed, 0.5, 1, 0.5, 0))

        for i in range(Isafj.n):
            if Isafj.next_to_bottomBorder(i) and (Isafj.n > n3 or Isafj.n == n3):
                print('Isafj grænn og snertir niðri')
                Isafj.persons = np.delete(Isafj.persons, i)
                Isafj.n = Isafj.n-1
                Ak.n = Ak.n+1
                Ak.persons = np.append(Ak.persons, Person(SICK, Ak.speed, 0.5, 1, 1, 0.5))

        for i in range(Isafj.n):
            if Isafj.next_to_leftBorder(i) and (Isafj.n > n3 or Isafj.n == n3):
                print('Isafj grænn og snertir vinstri')
                Isafj.persons = np.delete(Isafj.persons, i)
                Isafj.n = Isafj.n-1
                Rvk.n = Rvk.n+1
                Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))
        
        Rvk.draw(windowSurface, xmax, ymax)
        Ak.draw(windowSurface, xmax, ymax)
        Egils.draw(windowSurface, xmax, ymax)
        Isafj.draw(windowSurface, xmax, ymax)

        for event in pygame.event.get():
            if event.type == QUIT:
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
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_1:
                        print('pressed button 1')
                        button1()
                
                    if event.ui_element == button_2:
                        print('pressed button 2')
                        button2()

                    if event.ui_element == button_3:
                        print('pressed button 3')
                        #button3()

                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == horiz_slider:
                        value = int(horiz_slider.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider1:
                        value = int(horiz_slider1.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider2:
                        value = int(horiz_slider2.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider3:
                        value = int(horiz_slider3.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider4:
                        value = int(horiz_slider4.get_current_value())
                        print('value = ', value)

                    
                    
            manager.process_events(event)
        manager.update(time_delta)
    
        windowSurface.blit(background, (0,0))
        manager.draw_ui(windowSurface)
    
        pygame.display.update()
        #fpsClock.tick(FRAMES_PER_SECOND)

run_loop()


