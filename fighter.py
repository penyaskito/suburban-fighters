# $Id$

import pygame
import AnimatedSprite

LEFT, RIGHT, UP, DOWN, PUNCH, KICK, PROTECT = range(7)

class Fighter(AnimatedSprite.AnimatedSprite):
    def __init__(self, image, filas, columnas, fps=10, name='figther', pos=[100,100]):
        AnimatedSprite.AnimatedSprite.__init__(self, image, filas, columnas, fps)
        # animaciones propias
        #self.parado = [15, 16, 17, 18, 19]
        self.dir = 'r'
        self.parado = [0, 1, 2, 3, 4]
        self.andando = [5, 6, 7, 8, 9]
        self.saltando = [10,11,12]
        # la posicion en pantalla
        self.center = pos
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
        
        self.name = name
        self.vida = 100

        self.scoreboard = 0
        self.other_player = 0
        #teclas de movimiento [izquierda, derecha, arriba, abajo, cate, patada, protegerse]
        self.keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, 0, 0, 0]

    def update(self):
        old_x = self.center[0]
        old_y = self.center[1]
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
        else:
            self.vel_caida = 0
            self.rect.bottom = self.suelo
            self.center[1] = self.rect.centery
        ###
        if self.en_suelo():
            self.animate(pygame.time.get_ticks())
        self.rect = self.image.get_rect()
        
        self.rect.center = self.center

        if self.andando_derecha:
            self.center[0] += self.velocidad
        elif self.andando_izquierda:
            self.center[0] -= self.velocidad

        if self.rect.colliderect(self.other_player.rect) and (self.en_suelo()):
            self.center[0], self.center[1] = old_x, old_y
            self.rect.center = self.center

    def en_suelo(self):
        return self.rect.bottom >= self.suelo

    def change_dir(self, dir):
        '''
        cambia la orientacion del jugador
        dir = r indica derecha
        dir = l indica izquierda
        '''
        if self.dir == dir or not dir in ['r','l']:
            return False
        else:
            self.dir = dir
            self.andando = map(self.masx, self.andando)
            self.parado = map(self.masx, self.parado)
            self.saltando = map(self.masx, self.saltando)
            return True

    def flip(self):
        '''
        Cambia el sentido
        '''
        self.dir = dir
        self.andando = map(self.masx, self.andando)
        self.parado = map(self.masx, self.parado)
        self.saltando = map(self.masx, self.saltando)

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


    def event_manager(self, event):
        '''
        Gestiona los eventos de teclado asociados al jugador
        '''

        if event.type == pygame.KEYDOWN:
            if event.key == self.keys[RIGHT]:
                self.andando_derecha = True
            elif event.key == self.keys[LEFT]:
                self.andando_izquierda = True
            elif event.key == self.keys[UP] and self.en_suelo():
                self.vel_caida = -20

        elif event.type == pygame.KEYUP:
            if event.key == self.keys[RIGHT]:
                self.andando_derecha = False
            elif event.key == self.keys[LEFT]:
                self.andando_izquierda = False

    def set_scoreboard(self, scoreboard):
        '''
        Asigna un ScoreBoard a un player
        '''
        self.scoreboard = scoreboard
        self.scoreboard.set_player_name(self.name)
        self.scoreboard.set_vida(self.vida)

    def hurt(self, power):
        '''
        Quita vida al jugador
        '''
        if self.scoreboard.hurt(power) == 0:
            self.die()

    def die(self):
        '''
        Se ejecuta cuando la vida del jugador llega a 0
        '''
        print "ha muerto " + self.name
        self.vida = 0

    def is_alive(self):
        '''
        Devuelve True si el jugador todavia esta vivo
        '''
        if self.vida > 0:
            return True
        else: return False


    def set_keys(self, keys_array):
        '''
        Asigna las teclas de movimiento para este jugador
        '''
        for i,key in enumerate(keys_array):
            self.keys[i] = key

    def set_other_player(self, other_player):
        '''
        Se asigna una referencia al otro jugador, para controlar
        colisiones, y demas tonterias
        '''
        self.other_player = other_player
