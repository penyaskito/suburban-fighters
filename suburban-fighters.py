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
    pygame.display.set_caption('Suburban-fighters')
    screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    timer = Timer(screen)
    scoreboard1 = ScoreBoard(screen, 20)
    scoreboard2 = ScoreBoard(screen, screen.get_width() - 220,False)
    player1 = fighter.Fighter('images/ima.png', 9, 5, 10, name='danigm', pos=[100,100])
    player2 = fighter.Fighter('images/ima.png', 9, 5, 10, name='chica', pos=[540,100])
    player2.flip()
    player1.set_scoreboard(scoreboard1)
    player2.set_scoreboard(scoreboard2)
    player2.set_keys((pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, 0, 0, 0))
    player1.set_other_player(player2)
    player2.set_other_player(player1)
    orientacion_normal = True
    
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
                    elif event.key == pygame.K_SPACE:
                        player1.hurt(5)
                    elif event.key == pygame.K_RETURN:
                        player2.hurt(5)
                    elif event.key == pygame.K_i:
                        fxs.add(effect.zoom_fx(player1.image, player1.rect.center,"in", 10))
                    elif event.key == pygame.K_o:
                        fxs.add(effect.zoom_fx(player1.image, player1.rect.center,"out", 10))

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

            player1.event_manager(event)
            player2.event_manager(event)

        #pintando el fondo de rojo
        screen.fill((255,0,0))
        player1.update()
        player2.update()

        #Mirando si se cruzan
        c1 = player1.center[0]
        c2 = player2.center[0]
        if orientacion_normal:
            if c1 > c2:
                player1.flip()
                player2.flip()
                orientacion_normal = False
        else:
            if c1 < c2:
                player1.flip()
                player2.flip()
                orientacion_normal = True
        
        fxs.update()
        screen.blit(player1.image, player1.rect)
        screen.blit(player2.image, player2.rect)
        scoreboard1.update()
        scoreboard2.update()
        timer.update(pygame.time.get_ticks())

        fxs.draw(screen)
        #refresco de pantalla
        pygame.display.flip()


#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
