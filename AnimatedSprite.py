# $Id$

import pygame
import ResourceLoader
import pdb

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, image, filas, columnas, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = self.load(image, filas, columnas)
        self.parado = [0, 1, 2, 3, 4]
        self.andando = [5, 6, 7, 8, 9]
        self.animacion = self.parado

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = self.animacion[0]

        self.image = self._images[self._frame]
        self.rect = self.image.get_rect()
        self.center = [100,100]
        self.rect.center = self.center
        self.andando_derecha = False
        self.andando_izquierda = False
        self.velocidad = 5
        # Call update to set our first image.
        self.update(pygame.time.get_ticks())

    def update(self, t):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        self.animacion = self.parado
        if self.andando_derecha:
            self.animacion = self.andando
            self.frame = 0
        elif self.andando_izquierda:
            self.animacion = self.andando
            self.frame = 0
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self.animacion) + self.animacion[0]: self._frame = self.animacion[0]
            self.image = self._images[self._frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.center
            
            if self.andando_derecha:
                self.center[0] += self.velocidad
            elif self.andando_izquierda:
                self.center[0] -= self.velocidad

            self._last_update = t

    def load(self, path, filas, columnas):
        """
        Carga una imagen de tipo tile, en un vector de imagenes.
        Devuelve un vector de imagenes.
        path es la ruta a la imagen
        filas es el numero de frames en una columna
        columnas es el numero de frames en una fila
        """
        images = []
        img = ResourceLoader.ResourceLoader.load(path)
        img = pygame.transform.rotozoom(img, 0, 3)
        alto = img.get_height() / filas
        ancho = img.get_width() / columnas
        aux_img = pygame.Surface((ancho, alto))

        for i in range(filas):
            for j in range(columnas):
                aux_img = pygame.Surface((ancho, alto))
                area = pygame.Rect(j*ancho, i*alto, ancho, alto)
                aux_img.blit(img, (0,0), area)
                aux_img = aux_img.convert()
                aux_img.set_colorkey(aux_img.get_at((0,0)))
                images.append(aux_img)

        return images
