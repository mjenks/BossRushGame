# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:13:55 2022

Simple game to learn pygame 
Idea from game puzzle in Advent of Code 2015 day 22

@author: mjenks
"""

import pygame
import os
import player
import boss

#initialize pygame
pygame.font.init()

#Colors
WHITE = (255, 255, 255)

#Constants
SIZE = WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Boss Rush")

STAT_FONT = pygame.font.SysFont('comicsans', 40)
SPELL_FONT = pygame.font.SysFont('brushscript', 25)
SPELL_SELECTED_FONT = pygame.font.SysFont('brushscript', 25)
SPELL_SELECTED_FONT.set_underline(True)

FPS = 60
PAD = 25
BOSS_SIZE = BOSS_WIDTH, BOSS_HEIGHT = 900, 300
CHAR_SIZE = CHAR_WIDTH, CHAR_HEIGHT = 125, 150
CHAR_IMG_SIZE =  CHAR_WIDTH*10, CHAR_HEIGHT*10 #image has 10 down 10 across


frame_count = 1
choice = 0
dragons_slain = 0

#Creative Commons Image obtained from opengameart.org Author: jkjkke
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'JWDLx5AZBtI.jpg')), SIZE)
#Creative Commons Image obtained from opengameart.org Author: inosine
DRAGON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'dragon.png')), BOSS_SIZE)
#Creative Commons Image obtained from opengameart.org Artist: Calciumtrice
WIZARD_IMAGES = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'wizard.png')), CHAR_IMG_SIZE)

#game functions
def take_turn(p1, dragon):
    global choice
    #player casts selected spell
    p1.spells[choice](dragon)
    #Boss turn
    p1.turn_start(dragon)
    dragon.attack(p1)
    #Begining of turn effects for player
    p1.turn_start(dragon)
    p1.can_cast()
    choice = 0
    
    

#pygame functions
def move_selection(keys_pressed, p1):
    global choice
    if keys_pressed[pygame.K_UP] and choice > 0:  # UP
        choice -= 1
    if keys_pressed[pygame.K_DOWN] and choice < len(p1.spells)-1:  # DOWN
        choice += 1

def draw_window(p1, dragon):
    global frame_count
    global choice
    WIN.blit(BACKGROUND_IMAGE, (0,0))
    
    #display player and boss stats
    p1_health_text = STAT_FONT.render("HP: " + str(p1.health), 1, WHITE)
    p1_mana_text = STAT_FONT.render("Mana: " + str(p1.mana), 1, WHITE)
    dragon_health_text = STAT_FONT.render("Health: " + str(dragon.health), 1, WHITE)
    WIN.blit(p1_health_text, (PAD, PAD))
    WIN.blit(p1_mana_text, (PAD, PAD + p1_health_text.get_height()))
    WIN.blit(dragon_health_text, (WIDTH - dragon_health_text.get_width() - PAD, PAD))
    
    #Animate wizard on screen
    char_step = frame_count//10
    char_frame = pygame.Rect(((char_step%10)*CHAR_WIDTH, 5*CHAR_HEIGHT), (CHAR_WIDTH, CHAR_HEIGHT))
    WIN.blit(WIZARD_IMAGES, (WIDTH//4 - CHAR_WIDTH//2, HEIGHT - CHAR_HEIGHT - PAD), char_frame)
    
    #Animate dragon on screen
    boss_step = frame_count//10
    boss_frame = pygame.Rect(((boss_step%3)*BOSS_WIDTH//3,0), (BOSS_WIDTH//3, BOSS_HEIGHT))
    WIN.blit(DRAGON_IMAGE, (WIDTH//2 + 3*PAD, HEIGHT - BOSS_HEIGHT - 2*PAD), boss_frame)
    
    #Show current spell list
    spell_text_height = HEIGHT//2
    index = 0
    for spell in p1.spell_text:
        if index == choice:
            spell_text = SPELL_SELECTED_FONT.render(spell, 1, WHITE)
        else:
            spell_text = SPELL_FONT.render(spell, 1, WHITE)
        WIN.blit(spell_text, (PAD, spell_text_height))
        spell_text_height += spell_text.get_height()
        index += 1
    
    frame_count += 1
    
    pygame.display.update()

#pygame run loop
def run():
    p1 = player.Wizard()
    dragon = boss.Boss()  
    p1.turn_start(dragon)
    p1.can_cast()
    
    global choice
    global dragons_slain
    
    play = True
    clock = pygame.time.Clock()
    while play:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP) and choice > 0:
                    choice -= 1
                if (event.key == pygame.K_DOWN) and choice < len(p1.spells)-1:  # DOWN
                    choice += 1
                if event.key == pygame.K_RETURN:
                    take_turn(p1, dragon)
        
        
        draw_window(p1, dragon)

#run game
if __name__ == "__main__":
    run()