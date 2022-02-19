# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:44:23 2022

@author: mjenks
"""

import random

#boss class with attack action
class Boss:
    """boss character"""
    hp_range = range(70, 130, 5)
    dmg_range = range(3, 11)
    
    def __init__(self):
        self.health = random.choice(self.hp_range)
        self.damage = random.choice(self.dmg_range)
        
    def attack(self, player):
        player.health -= max(1, self.damage - player.armor)