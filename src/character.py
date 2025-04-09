import random

class character:
    
    def __init__(self, name, class_type, strength, inventory=None, unit_id=None):
        
        if unit_id is None:
            self.unit_id = random.randint(1, 1000)
        else:
            self.unit_id = unit_id
        
        # commands given to the character
        self.action_queue = []
        
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
        
        
        self.equipment_stats = None
               
        self.status = {
            "stunned": False,
            "poisoned": False,
            "burned": False,
            "frozen": False,
            "silenced": False,
            "defeated" : False,
        }
     
    def update_health_bar(self):
        #data = [########--]
        pass
        
    def get_status(self, detailed=False):
        return self.name+" (" + self.class_type+ ")"+ " HP: " + str(self.health)
    
    
    
    def get_detailed_status(self):
        self.generate_health_bar
        
        line_one = self.name+" (" + self.class_type+ ")"+ " HP: " + str(self.health)