import random

class character:
    
    def __init__(self, name, class_type, strength, inventory=None, unit_id=None):
        
        self.inventory = inventory
        self.name = name
        self.health = 100
        self.mana = 100
        self.class_type = class_type
        self.main_level = 1
        
        # character stats
        self.strength = strength
        self.wisdom = 4
        self.dexterity = 4
        self.constituion = 4
        
        ### minior stats 
        self.iniative = random.randint(1, 20)
        self.luck = random.randint(1, 20)
        self.accuracy = random.randint(1, 20)
        
        
        
        # TODO:
        self.equipment_stats = None
               
        self.status = {
            "stunned": False,
            "poisoned": False,
            "burned": False,
            "frozen": False,
            "silenced": False,
            "defeated" : False,
        }
        
    def get_status(self, detailed=False):
        return self.name+" (" + self.class_type+ ")"+ " HP: " + str(self.health)