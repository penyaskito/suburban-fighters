#!/usr/bin/python

"""
Suburban-fighters es un juego 2D de lucha
Suburban-fighters es una marca no registrada sugerida por penyaskito XD
author danigm <danigm@gmail.com>
date jue oct 11 22:06:01 CEST 2007
date 2007-10-11
"""

import sys
import pygame
import gettext #para traducir
from ResourceLoader import ResourceLoader

try:
    t = gettext.translation('suburban-fighters', './idiomas/')
    _ = t.ugettext
except:
    _ = gettext.gettext


def main():
    pygame.init()
    #inicializacion
    icon = ResourceLoader.load('icons/suburban-icon-64x64.png', cache = True)
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((800,600), pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Suburban-fighters')

    while 1:
        clock.tick(40) #40 frames por segundo

        #control de eventos
        # mousex, mousey = pygame.mouse.get_pos() #posicion del raton
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # si no es un evento de teclado o raton, lo ignoramos
            if not hasattr(event,'button') and not hasattr(event,'key'):
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                print _("boton") + str(event.button)
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_ESCAPE:
                    print event.key
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

        #pintando el fondo de rojo
        screen.fill((255,0,0))
        #refresco de pantalla
        pygame.display.flip()

#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
