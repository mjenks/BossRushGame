# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:38:44 2022

@author: mjenks
"""

#player as a class with spells as functions
class Wizard:
    """player character"""
    
    def __init__(self):
        self.health = 50
        self.mana = 500
        self.armor = 0
        self.shield_turns = 0
        self.poison_turns = 0
        self.recharge_turns = 0
        
        
    def turn_start(self, boss):
        #While shield is active, your armor is increased by 7.
        if self.shield_turns != 0:
            self.shield_turns -= 1
        else:
            self.armor = 0
            
        #At the start of each turn while poison is active, it deals the boss 3 damage.
        if self.poison_turns != 0:
            self.poison_turns -= 1
            boss.health -= 3
        
        #At the start of each turn while recharge is active, it gives you 101 new mana.
        if self.recharge_turns != 0:
            self.recharge_turns -= 1
            self.mana += 101
        
        
    def magic_missile(self, boss):
        #Magic Missile costs 53 mana. It instantly does 4 damage.
        self.mana -= 53
        boss.health -= 4
        
    def drain(self, boss):
        #Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
        self.mana -= 73
        self.health += 2
        boss.health -= 2
        
    def shield(self, boss):
        #Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
        #While shield is active, your armor is increased by 7.
        self.mana -= 113
        self.armor = 7
        self.shield_turns = 6
        
    def poison(self, boss):
        #Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
        self.mana -= 173
        self.poison_turns = 6
        
    def recharge(self, boss):
        #Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
        self.mana -= 229
        self.recharge_turns = 5
        
    def cure(self, boss):
        #Cure cost 276 mana. It instantly heals you for 12 hit points.
        self.mana -= 276
        self.health += 12
        
    def can_cast(self):
        self.spells = []
        if self.mana >= 53:
            self.spells.append(self.magic_missile)
        if self.mana >= 73:
            self.spells.append(self.drain)
        if self.mana >= 113 and self.shield_turns == 0:
            self.spells.append(self.shield)
        if self.mana >= 173 and self.poison_turns == 0:
            self.spells.append(self.poison)
        if self.mana >= 229 and self.recharge_turns == 0:
            self.spells.append(self.recharge)
        if self.mana >= 276:
            self.spells.append(self.cure)
        