# $Id$

import pygame

class FX(pygame.sprite.Sprite):
    def __init__(self, images, pos, fps=10):
        '''
        images: vector de imagenes a animar
        pos: posicion donde pintar el efecto
        fps: frames por segundo, velocidad del efecto
        '''
        pygame.sprite.Sprite.__init__(self)
        self._images = images
        self._animacion = range(len(self._images))

        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = self._animacion[0]

        self.image = self._images[self._frame]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        
    def update(self):
        t = pygame.time.get_ticks()
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._animacion) + self._animacion[0]:
                self.kill()
                return 0
            self.image = self._images[self._frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self._last_update = t


def zoom_fx(surface, pos, mode="out",frames=5):
    '''
    Recibe una superficie, y una posicion, y devuelve una
    animacion de zoom out de esa imagen.
    mode puede ser "in" u "out".
    '''
    images = []
    images.append(surface)
    alpha = 255
    dec_alpha = alpha / frames
    for i in range(1, frames):
        aux_image = pygame.transform.rotozoom(images[i-1], 0, 1.1)
        aux_image = aux_image.convert()
        aux_image.set_colorkey(aux_image.get_at((0,0)))
        alpha = alpha - dec_alpha
        aux_image.set_alpha(alpha)
        images.append(aux_image)
    if mode == "in":
        images.reverse()
    animacion = FX(images, pos, 20)
    return animacion
    
