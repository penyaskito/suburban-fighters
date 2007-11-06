#!/usr/bin/python

"""
Shooter2D
author danigm <danigm@gmail.com>
"""

import sys
import pygame
import menu

def main():
    # Inicializacion
    pygame.init()
    # pantalla a 640x480
    scrn_anch=640
    scrn_alto=480
    screen = pygame.display.set_mode((scrn_anch, scrn_alto), pygame.DOUBLEBUF | pygame.HWSURFACE)
    # relog para controlar los frames por segundo
    clock = pygame.time.Clock()
    # se asigna el nombre de la ventana
    pygame.display.set_caption('Menu')
    
    
    #Definir menu
    obj_menu=menu.Menu(screen,("Modo Historia","Modo Vs","Opciones","Creditos"),120,30)
    obj_menu.update()
    



    # Bucle principal
    while True:
            
        # control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # si no es un evento de teclado o raton, lo ignoramos
            if not hasattr(event,'button') and not hasattr(event,'key'):
                continue
            
            # Eventos de raton
            if event.type == pygame.MOUSEBUTTONDOWN:
                print "boton" + str(event.button)
            # Eventos de teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()     
                if event.key == pygame.K_SPACE:
                    print "espacio pulsado"
                if event.key == pygame.K_UP:
                    #print "^ _"
                    obj_menu.up()
                if event.key == pygame.K_DOWN:
                    #print "v _"
                    obj_menu.down()
                #if event.key == pygame.K_LEFT:
                #    obj_nave.moviendo_izquierda = True
                #if event.key == pygame.K_RIGHT:
                #    obj_nave.moviendo_derecha = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print "espacio soltado"
                #if event.key == pygame.K_UP:
                #    print "^ -"
                #if event.key == pygame.K_DOWN:
                #    print "v -"
                #if event.key == pygame.K_LEFT:
                #    obj_nave.moviendo_izquierda = True
                #if event.key == pygame.K_RIGHT:
                #    obj_nave.moviendo_derecha = True
    
        # Refresco de pantalla
        pygame.display.flip()

# Esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
