# $Id$

import pygame
import ResourceLoader

class ScoreBoard(pygame.sprite.Sprite):
    '''
    Clase encargada de pintar el marcador
    '''
    def __init__(self, screen, pos):
        self.screen = screen
        # pos es la posicion (x) donde empieza la barra
        self.pos = pos
        self.vida = 100
        pygame.draw.rect(self.screen, (0,0,255), (self.pos, 20, 200, 20))
        pygame.draw.rect(self.screen, (0,255,255), (self.pos + 2, 22, 196, 16))
    
    def update(self):
        # 196 es la barra llena de vida.
        width = (196 * self.vida) / 100
        pygame.draw.rect(self.screen, (0,0,255), (self.pos, 20, 200, 20))
        pygame.draw.rect(self.screen, (0,255,255), (self.pos + 2, 22, width, 16))
        
    def hurt (self, score):        
        self.vida -= score
        if (self.vida < 0):
            self.vida = 0        
