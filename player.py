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
        self.ticks = []
        
        
    def turn_start(self, boss):
        #While shield is active, your armor is increased by 7.
        if self.shield_turns != 0:
            self.shield_turns -= 1
            if self.shield_turns == 0: self.ticks.append(("Arm", -7))
        else:
            self.armor = 0
            
        #At the start of each turn while poison is active, it deals the boss 3 damage.
        if self.poison_turns != 0:
            self.poison_turns -= 1
            boss.health -= 3
            boss.ticks.append(("Dmg", 3))
        
        #At the start of each turn while recharge is active, it gives you 101 new mana.
        if self.recharge_turns != 0:
            self.recharge_turns -= 1
            self.mana += 101
            self.ticks.append(("Mana", 101))
        
        
    def magic_missile(self, boss):
        #Magic Missile costs 25 mana. It instantly does 4 damage.
        self.mana -= 25
        boss.health -= 4
        boss.ticks.append(("Dmg", 4))
        
    def drain(self, boss):
        #Drain costs 50 mana. It instantly does 2 damage and heals you for 2 hit points.
        self.mana -= 50
        self.health += 2
        boss.health -= 2
        boss.ticks.append(("Dmg", 4))
        
    def shield(self, boss):
        #Shield costs 75 mana. It starts an effect that lasts for 8 turns. 
        #While shield is active, your armor is increased by 7.
        self.mana -= 75
        self.armor = 7
        self.shield_turns = 8
        
        
    def poison(self, boss):
        #Poison costs 125 mana. It starts an effect that lasts for 8 turns. 
        self.mana -= 125
        self.poison_turns = 8
        
    def recharge(self, boss):
        #Recharge costs 175 mana. It starts an effect that lasts for 7 turns. 
        self.mana -= 175
        self.recharge_turns = 7
        
    def cure(self, boss):
        #Cure cost 200 mana. It instantly heals you for 15 hit points.
        self.mana -= 200
        self.health += 15
        self.ticks.append(("Heal", 15))
        
    def can_cast(self):
        self.spells = []
        self.spell_text = []
        if self.mana >= 25:
            self.spells.append(self.magic_missile)
            self.spell_text.append("Magic Missile    25")
        if self.mana >= 50:
            self.spells.append(self.drain)
            self.spell_text.append("Drain    50")
        if self.mana >= 75 and self.shield_turns == 0:
            self.spells.append(self.shield)
            self.spell_text.append("Shield    75")
        if self.mana >= 125 and self.poison_turns == 0:
            self.spells.append(self.poison)
            self.spell_text.append("Poison    125")
        if self.mana >= 175 and self.recharge_turns == 0:
            self.spells.append(self.recharge)
            self.spell_text.append("Recharge    175")
        if self.mana >= 200:
            self.spells.append(self.cure)
            self.spell_text.append("Cure    200")
        