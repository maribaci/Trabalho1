#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        print('Setup Start')

        print('Setup End')

        print('Loop Start')
        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit() # Close window
                    quit() # End pygame
