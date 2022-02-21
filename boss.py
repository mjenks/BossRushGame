# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:44:23 2022

@author: mjenks
"""

import random

#boss class with attack action
class Boss:
    """boss character"""
    hp_range = range(50, 100, 5)
    dmg_range = range(3, 11)
    
    def __init__(self):
        self.health = random.choice(self.hp_range)
        self.damage = random.choice(self.dmg_range)
        self.ticks = []
        
    def attack(self, player):
        dmg = max(1, self.damage - player.armor)
        player.health -= dmg
        player.ticks.append("Dmg", dmg)