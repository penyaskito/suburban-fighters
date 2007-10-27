# $Id$

import pygame
import sys

class ResourceLoader():
    '''
    Clase encargada de gestionar la carga de imagenes. Cachea estas si es necesario.
    '''
    images = {}
        
    def load (self, uri, cache = False):
        '''
        Carga una imagen (uri). Permite el cacheo si cache=True.
        '''
        img = None
        if uri in self.images:
            img = ResourceLoader.images[uri]
        else:
            img = pygame.image.load(uri)
            if cache:
                ResourceLoader.images[uri] = img
        return img
