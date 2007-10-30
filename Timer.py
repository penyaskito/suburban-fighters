# $Id$

import pygame
import ResourceLoader

class Timer(pygame.sprite.Sprite):
    def __init__(self, screen, fps=40):
        self.seconds = 60
        self.screen = screen
        self._delay = 1000 / fps
        self._last_update = 0
        self.font = pygame.font.SysFont("Verdana",40)
        
    def update(self, t): 
        s = self.font.render(str(self.seconds),True,(255,230,50))

        if t - self._last_update > self._delay:
            self.seconds -= 1
        print "Secs: ",self.seconds
        self.screen.blit (s, (380, 10))        
        self._last_update = t
