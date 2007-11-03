#!/usr/bin/python
# $Id$

"""
Suburban-fighters es un juego 2D de lucha
Suburban-fighters es una marca no registrada sugerida por penyaskito XD
author danigm <danigm@gmail.com>
date jue oct 11 22:06:01 CEST 2007
date 2007-10-11
"""

import pdb
import sys
import pygame
import gettext #para traducir
from ResourceLoader import ResourceLoader
import fighter
from ScoreBoard import ScoreBoard
from Timer import Timer
import effect

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
    screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    timer = Timer(screen)
    scoreboard1 = ScoreBoard(screen, 20)
    scoreboard2 = ScoreBoard(screen, screen.get_width() - 220)
    pygame.display.set_caption('Suburban-fighters')

    chica = fighter.Fighter('images/ima.png', 9, 5, 14)
    
    fxs = pygame.sprite.Group()

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
                    if event.key == pygame.K_p:
                        pdb.set_trace()
                    if event.key == pygame.K_RIGHT:
                        chica.andando_derecha = True
                    elif event.key == pygame.K_LEFT:
                        chica.andando_izquierda = True
                    elif event.key == pygame.K_SPACE:
                        scoreboard1.hurt(5)
                    elif event.key == pygame.K_RETURN:
                        scoreboard2.hurt(5)
                    elif event.key == pygame.K_UP and chica.en_suelo():
                        chica.vel_caida = -20
                    elif event.key == pygame.K_i:
                        fxs.add(effect.zoom_fx(chica.image, chica.rect.center,"in", 10))
                    elif event.key == pygame.K_o:
                        fxs.add(effect.zoom_fx(chica.image, chica.rect.center,"out", 10))

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    chica.andando_derecha = False
                elif event.key == pygame.K_LEFT:
                    chica.andando_izquierda = False

        #pintando el fondo de rojo
        screen.fill((255,0,0))
        chica.update()
        fxs.update()
        screen.blit(chica.image, chica.rect)
        scoreboard1.update()
        scoreboard2.update()
        timer.update(pygame.time.get_ticks())
        fxs.draw(screen)
        #refresco de pantalla
        pygame.display.flip()


#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
