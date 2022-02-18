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
SIZE = WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Boss Rush")

FPS = 60
PAD = 25
BOSS_SIZE = BOSS_WIDTH, BOSS_HEIGHT = 900, 300
CHAR_SIZE = CHAR_WIDTH, CHAR_HEIGHT = 120, 180
CHAR_IMG_SIZE =  CHAR_WIDTH*10, CHAR_HEIGHT*10 #image has 10 down 10 across


frame_count = 1

#Creative Commons Image obtained from opengameart.org Author: jkjkke
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'JWDLx5AZBtI.jpg')), SIZE)
#Creative Commons Image obtained from opengameart.org Author: inosine
DRAGON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'dragon.png')), BOSS_SIZE)
#Creative Commons Image obtained from opengameart.org Artist: Calciumtrice
WIZARD_IMAGES = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'wizard.png')), CHAR_IMG_SIZE)

#game classes

#pygame functions
def draw_window():
    global frame_count
    WIN.blit(BACKGROUND_IMAGE, (0,0))
    
    #Animate wizard on screen
    char_step = frame_count//10
    char_frame = pygame.Rect(((char_step%10)*CHAR_WIDTH, 5*CHAR_HEIGHT), (CHAR_WIDTH, CHAR_HEIGHT))
    WIN.blit(WIZARD_IMAGES, (WIDTH//4 - CHAR_WIDTH//2, HEIGHT - CHAR_HEIGHT - PAD), char_frame)
    
    #Animate dragon on screen
    boss_step = frame_count//10
    boss_frame = pygame.Rect(((boss_step%3)*BOSS_WIDTH//3,0), (BOSS_WIDTH//3, BOSS_HEIGHT))
    WIN.blit(DRAGON_IMAGE, (WIDTH//2 + 3*PAD, HEIGHT - BOSS_HEIGHT - 2*PAD), boss_frame)
    
    frame_count += 1
    
    pygame.display.update()

#pygame run loop
def run():
    play = True
    clock = pygame.time.Clock()
    while play:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
        
        draw_window()

#run game
if __name__ == "__main__":
    run()