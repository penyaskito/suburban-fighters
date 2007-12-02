# $Id$

import pygame
import AnimatedSprite

class Fighter(AnimatedSprite.AnimatedSprite):
    def __init__(self, image, filas, columnas, fps=10):
        AnimatedSprite.AnimatedSprite.__init__(self, image, filas, columnas, fps)
        # animaciones propias
        #self.parado = [15, 16, 17, 18, 19]
        self.dir = 0
        self.parado = [0, 1, 2, 3, 4]
        self.andando = [5, 6, 7, 8, 9]
        self.saltando = [10,11,12]
        # la posicion en pantalla
        self.center = [100,100]
        self.rect.center = self.center
        # flags de estados
        # TODO hacer esto con binarios
        self.andando_derecha = False
        self.andando_izquierda = False
        # velocidad de movimiento horizontal
        self.velocidad = 5
        # velocidad de movimiento vertical
        self.vel_caida = 0
        # aceleracion de vel_caida
        self.gravedad = 0.7
        # posicion del suelo, en pixels
        self.suelo = 460

    def update(self):
        self.set_animation(self.parado)
        if self.andando_derecha or self.andando_izquierda:
            self.set_animation(self.andando)

        # Callendo
        if not self.en_suelo() or self.vel_caida < 0:
            if self.vel_caida < -10:
                self.set_frame(self.saltando[0])
            elif self.vel_caida > 10:
                self.set_frame(self.saltando[2])
            else: self.set_frame(self.saltando[1])
            self.vel_caida += self.gravedad
            self.center[1] += self.vel_caida
        else: self.vel_caida = 0
        ###
        if self.en_suelo():
            self.animate(pygame.time.get_ticks())
        self.rect = self.image.get_rect()
        self.rect.center = self.center
            
        if self.andando_derecha:
            self.center[0] += self.velocidad
        elif self.andando_izquierda:
            self.center[0] -= self.velocidad


    def en_suelo(self):
        return self.rect.bottom >= self.suelo

    def change_dir(self, dir):
        '''
        cambia la orientacion del jugador
        dir = 0 indica derecha
        dir = 1 indica izquierda
        '''
        if self.dir == dir or not dir in [0,1]:
            return False
        else:
            self.dir = dir
            self.andando = map(self.masx, self.andando)
            self.parado = map(self.masx, self.parado)
            self.saltando = map(self.masx, self.saltando)
            print self.andando, self.parado, self.saltando
            return True
            
    def masx(self, num):
        '''
        Sirve para cuando tenemos las imagenes invertidas,
        si queremos los frames invertidos, tenemos que sumarle
        el numero de imagenes a las animaciones
        devuelve num + numimagenes si num < numimagenes
                 num - numimagenes si num >= numimagenes
        '''
        if num < self.nimages:
            return num + self.nimages
        else:
            return num - self.nimages

