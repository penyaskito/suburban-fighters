# $Id$

import pygame
import ResourceLoader
import pdb

class AnimatedSprite(pygame.sprite.Sprite):
    '''
    AnimatedSprite hereda de Sprite, y tiene como objetivo
    simplificar la carga de sprites por tiles, ademas de la
    animacion de estos.
    '''
    def __init__(self, image, filas, columnas, fps = 10):
        '''
        Constructor de AnimatedSprite
        image: es la ruta hacia la imagen por tiles
        filas: el numero de imagenes en vertical
        columnas: el numero de imagenes en horizontal
        fps: frames por segundo de las animaciones
        '''
        pygame.sprite.Sprite.__init__(self)
        self._images = self.load(image, filas, columnas)
        self._animacion = [0]

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = self._animacion[0]

        self.image = self._images[self._frame]
        self.rect = self.image.get_rect()
        
        # Call update to set our first image.
        self.animate(pygame.time.get_ticks())

    def animate(self, t):
        '''
        Genera la animacion:
        t: debe ser pygame.time.get_ticks
        '''
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._animacion) + self._animacion[0]:
                self._frame = self._animacion[0]
            self.image = self._images[self._frame]
            self._last_update = t

    def load(self, path, filas, columnas, flip="True"):
        '''
        Carga una imagen de tipo tile, en un vector de imagenes.
        Devuelve un vector de imagenes.
        path: es la ruta a la imagen
        filas: es el numero de frames en vertical
        columnas: es el numero de frames en horizontal
        '''
        #TODO: tener la posibilidad de guardar el flip (inverso).

        images = []
        # cargamos la imagen
        img = ResourceLoader.ResourceLoader.load(path)
        if flip:
            img_flip = pygame.transform.flip(img, True, False)
        # el alto y el ancho de cada frame
        alto = img.get_height() / filas
        ancho = img.get_width() / columnas

        for i in range(filas):
            for j in range(columnas):
                aux_img = pygame.Surface((ancho, alto))
                # el area para recortar
                area = pygame.Rect(j*ancho, i*alto, ancho, alto)
                aux_img.blit(img, (0,0), area)
                aux_img = aux_img.convert()
                aux_img.set_colorkey(aux_img.get_at((0,0)))
                images.append(aux_img)

        if flip:
            for i in range(filas):
                for j in range(columnas):
                    aux_img = pygame.Surface((ancho, alto))
                    # el area para recortar
                    area = pygame.Rect(j*ancho, i*alto, ancho, alto)
                    aux_img.blit(img_flip, (0,0), area)
                    aux_img = aux_img.convert()
                    aux_img.set_colorkey(aux_img.get_at((0,0)))
                    images.append(aux_img)

        return images
        
    def set_frame(self, frame):
        '''
        Pone en self.image el frame seleccionado de la lista
        de imagenes self._images
        frame: un entero.
        '''

        self._frame = frame
        self.image = self._images[self._frame]
        
    def set_animation(self, animation):
        '''
        Pone una animacion a mostrar
        animation: una lista de enteros, donde estan los
        indices de los frames
        por ejemplo: [0,1,2,3] esto es una animacion de 4 frames
        '''
        
        self._animacion = animation
