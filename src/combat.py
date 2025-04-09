from character import character
import random

class combat:
    
    def __init__(self):
        self.team_a = None
        self.team_b = None
        self.team_c = None
    
    
    """
    team_a = player team
    team_b = enemy team
    team_c = optional third team (e.g. neutral or allied characters or units)
    """
    def start_combat(self, team_a, team_b, team_c = None):
        # Start combat between two teams
        self.team_a = team_a
        self.team_b = team_b
        self.team_c = team_c
        

        
        # Start the combat loop
        self.run_combat()
    
    
    
    def roll_dice(self, sides=20):
        # roll a dice with the specified number of sides
        return random.randint(1, sides)
       
    def resolve_attack(self, attacker: character, target: character):
        # determine hit or miss 
        
        # calculate chance of a critical attack
        
        # roll for damage 
        
        
        # calculate damage based on attacker's strength and target's armor
        
        # roll for chance of a critical block 
        
        
        # apply damage to target
        
        
        pass
    
    
    def defend(self, defender, attacker):
        pass
        
        
    def heal(self, healer, target):
        pass
    
    def area_of_effect(self, caster, targets):
        pass
    
    
    def special(self, attacker, target):
        pass