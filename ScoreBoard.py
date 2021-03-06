# $Id$

import pygame
import ResourceLoader

class ScoreBoard(pygame.sprite.Sprite):
    '''
    Clase encargada de pintar el marcador
    '''
    
    COLOR_FUERTE = (0,255,255)
    COLOR_AGONICO = (255, 100, 0)
    
    #direccion=True -> pierde vida para la izq,  False-> pierde vida hacia la derecha
    def __init__(self, screen, pos, direccion=True):
        self._screen = screen
        # pos es la posicion (x) donde empieza la barra
        self._pos = pos
        self._vida = 100
        self._player_name_font = pygame.font.SysFont("Verdana",20)
        self._player_name = "La Mari"
        pygame.draw.rect(self._screen, (0,0,255), (self._pos, 20, 200, 20))
        self.direccion=direccion
        self._barraVida = pygame.draw.rect(self._screen, (0,255,255), \
                (self._pos + 2, 22, 196, 16))
    
    def update(self):
        # 196 es la barra llena de vida.
        width = (196 * self.get_vida()) / 100
        # el elemento 2 es el width, verdad?
        if (self._barraVida[2] != width):
            self._barraVida[2] -= 1
        offset = (196 -self._barraVida[2])
        if self._barraVida[2] > 30:
            color = self.COLOR_FUERTE 
        else:
            color = self.COLOR_AGONICO
        
        pygame.draw.rect(self._screen, (0,0,255), (self._pos, 20, 200, 20))
        if self.direccion:
            pygame.draw.rect(self._screen, color, self._barraVida)
            s = self._player_name_font.render(self.get_player_name(), True, (255,230,50))
            self._screen.blit (s, (self._pos, 40, 200, 20))
        else:
            barraVida2=pygame.draw.rect(self._screen, (0,255,255), \
                (self._pos + 2 + offset, 22, self._barraVida[2], 16))
            pygame.draw.rect(self._screen, color, barraVida2)
            s = self._player_name_font.render(self.get_player_name(), True, (255,230,50))
            self._screen.blit (s, (self._pos, 40, 200, 20))
        
        
    def hurt (self, score):
        oldVida = self._vida
        self._vida -= score
        if (self._vida < 0):
            self._vida = 0
        return self._vida
            
    def get_vida(self):
        return self._vida
    
    def set_vida(self, vida):
        self._vida = vida
    
    def get_player_name(self):
        return self._player_name

    def set_player_name(self, player_name):
        self._player_name = player_name
