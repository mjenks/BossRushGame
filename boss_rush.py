# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:13:55 2022

Simple game to learn pygame 
Idea from game puzzle in Advent of Code 2015 day 22

@author: mjenks
"""

import pygame
import os

#initialize pygame
pygame.font.init()

#Colors
WHITE = (255, 255, 255)

#Constants
SIZE = WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Boss Rush")


#game classes

#pygame functions
def draw_window():
    WIN.fill(WHITE)
    
    pygame.display.update()

#pygame run loop
def run():
    play = True
    while play:
        
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                play = False
                pygame.quit()
        
        draw_window()

#run game
if __name__ == "__main__":
    run()