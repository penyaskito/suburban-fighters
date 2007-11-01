# $Id$

import pygame
import time
import ResourceLoader

class Timer(pygame.sprite.Sprite):

    TIME = 60
    
    ESTADO_PARADO = 0
    ESTADO_CORRIENDO = 1
    
    def __init__(self, screen):
        self._posicion = (screen.get_width() / 2 - 20, 10)
        self._screen = screen
        self._inicial = time.time()
        self._estado = self.ESTADO_CORRIENDO
        self._seconds = self.TIME
        self._font = pygame.font.SysFont("Verdana",40)
        
    def update(self, t): 
        s = self._font.render(str("%(var)02d" % {"var":self._seconds}),True,(255,230,50))

        self._screen.blit (s, self._posicion)        
        if self._estado == self.ESTADO_CORRIENDO:
            self._seconds = self.TIME - (time.time() - self._inicial)
        if self._seconds < 0:
            self._seconds = 0
            self._estado = self.ESTADO_PARADO
    
    def get_seconds(self):
        return self._seconds
        
    def pause(self):
        self._estado = self.ESTADO_PARADO
        # almacenamos el instante en el que fue parado.
        self._stopped = time.time()
        
    def resume(self):
        # calcula por donde debe seguir la cuenta.
        self._inicial -= self._stopped - time.time()
        self._estado = self.ESTADO_CORRIENDO