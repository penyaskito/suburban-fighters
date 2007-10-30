# $Id$

import pygame
import sys

class ResourceLoader():
    '''
    Clase encargada de gestionar la carga de imagenes. Cachea estas si es necesario.
    '''
    images = {}
        
    @staticmethod
    def load (uri, cache = False):
        '''
        Carga una imagen (uri). Permite el cacheo si cache=True.
        '''
        img = None
        if uri in ResourceLoader.images:
            img = ResourceLoader.images[uri]
        else:
            try:
                img = pygame.image.load(uri)
                if cache:
                    ResourceLoader.images[uri] = img
            except Exception:
                print "Error loading: ",uri
                sys.exit(1)
            
        return img
