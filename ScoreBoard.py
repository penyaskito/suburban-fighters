# $Id$

import pygame
import ResourceLoader

class ScoreBoard(pygame.sprite.Sprite):
    '''
    Clase encargada de pintar el marcador
    '''
    
    COLOR_FUERTE = (0,255,255)
    COLOR_AGONICO = (255, 100, 0)
    
    def __init__(self, screen, pos):
        self._screen = screen
        # pos es la posicion (x) donde empieza la barra
        self._pos = pos
        self._vida = 100
        pygame.draw.rect(self._screen, (0,0,255), (self._pos, 20, 200, 20))
        self._barraVida = pygame.draw.rect(self._screen, (0,255,255), \
                (self._pos + 2, 22, 196, 16))
    
    def update(self):
        # 196 es la barra llena de vida.
        width = (196 * self.get_vida()) / 100
        # el elemento 2 es el width, verdad?
        if (self._barraVida[2] != width):
            self._barraVida[2] -= 1
        if self._barraVida[2] > 30:
            color = self.COLOR_FUERTE 
        else:
            color = self.COLOR_AGONICO
        
        pygame.draw.rect(self._screen, (0,0,255), (self._pos, 20, 200, 20))
        pygame.draw.rect(self._screen, color, self._barraVida)
        
    def hurt (self, score):
        oldVida = self._vida
        self._vida -= score
        if (self._vida < 0):
            self._vida = 0
            
    def get_vida(self):
        return self._vida