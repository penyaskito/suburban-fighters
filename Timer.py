# $Id$

import pygame
import time
import ResourceLoader

class Timer(pygame.sprite.Sprite):

    TIME = 60
    
    ESTADO_PARADO = 0
    ESTADO_CORRIENDO = 1
    
    COLOR_NORMAL = (255,230,50)
    COLOR_TERMINANDO = (255, 50, 0)
    
    def __init__(self, screen):
        self._posicion = (screen.get_width() / 2 - 20, 10)
        self._screen = screen
        self._inicial = time.time()
        self._estado = self.ESTADO_CORRIENDO
        self._seconds = self.TIME
        self._color = self.COLOR_NORMAL
        self._font = pygame.font.SysFont("Verdana",40)
        self._image = 0
        
    def update(self, t): 
        # actualiza el color
        if self._seconds < 6:
            self._color = self.COLOR_TERMINANDO
            
        self._image = self._font.render(str("%(var)02d" % {"var":self._seconds}),True, self._color)

        self._screen.blit (self._image, self._posicion)        
        if self._estado == self.ESTADO_CORRIENDO:
            self._seconds = self.TIME - (time.time() - self._inicial)
        if self._seconds < 0:
            self._seconds = 0
            self._estado = self.ESTADO_PARADO
    
    def get_seconds(self):
        return self._seconds

    def get_image_pos(self):
        return self._image, self._posicion
        
    def pause(self):
        self._estado = self.ESTADO_PARADO
        # almacenamos el instante en el que fue parado.
        self._stopped = time.time()
        
    def resume(self):
        # calcula por donde debe seguir la cuenta.
        self._inicial -= self._stopped - time.time()
        self._estado = self.ESTADO_CORRIENDO
