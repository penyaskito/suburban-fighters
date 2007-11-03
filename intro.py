#!/usr/bin/python
# $Id$

import pygame
import sys
import suburbanfighters
from ResourceLoader import ResourceLoader
import fighter

class Intro():
    def __init__(self):
        self.icon = ResourceLoader.load('icons/suburban-icon-64x64.png', cache = True)
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background = ResourceLoader.load('images/suburban-icon-640x480.png', cache = True)

        self.clock = pygame.time.Clock()
        self.end = False

    def run(self):
        pygame.display.set_caption('Suburban-fighters')
        self.chica = fighter.Fighter('images/ima.png', 9, 5, 14)
        self.chico = fighter.Fighter('images/boceto2.png', 3, 5, 10)
        self.chico.center = [600,100]
        self.chico.rect.center = self.chico.center

        
        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.clock.tick(40)
            t = pygame.time.get_ticks() 
            if t > 1000 and t < 1040:
                self.step1()
            elif t > 1500 and t < 1540:
                self.step2()
            elif t > 3000 and t < 3040:
                self.step3()
            elif t > 5000 and t < 5400:
                self.step4()
            elif t > 6000 and t < 6400:
                self.step5()
            elif t > 8000:
                sys.exit()
            self.chica.update()
            self.chico.update()
            self.screen.fill((255,255,255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.chico.image, self.chico.rect)
            self.screen.blit(self.chica.image, self.chica.rect)

            pygame.display.flip()

    def step1(self):
        self.chica.andando_derecha = True
        
    def step2(self):
        self.chica.vel_caida = -20
    
    def step3(self):
        self.chica.andando_derecha = False
        self.chica.vel_caida = -20
    
    def step4(self):
        self.chica.andando_izquierda = True        

    def step5(self):
        self.chica.andando_izquierda = False

        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    pygame.init()
    intro = Intro()
    intro.run()
    

