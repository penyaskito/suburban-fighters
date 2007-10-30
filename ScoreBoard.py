# $Id$

import pygame
import ResourceLoader

class ScoreBoard(pygame.sprite.Sprite):
    '''
    Clase encargada de pintar el marcador
    '''
    def __init__(self, screen):
        self.screen = screen
        self.vida = 100
        pygame.draw.rect(self.screen, (0,0,255), (20, 20, 200, 20))
        pygame.draw.rect(self.screen, (0,255,255), (22, 22, 196, 16))
    
    def update(self):
        # 196 es la barra llena de vida.
        width = (196 * self.vida) / 100
        pygame.draw.rect(self.screen, (0,0,255), (20, 20, 200, 20))
        pygame.draw.rect(self.screen, (0,255,255), (22, 22, width, 16))
        
    def hurt (self, score):        
        self.vida -= score
        if (self.vida < 0):
            self.vida = 0        
