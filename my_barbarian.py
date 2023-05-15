import random

class Barbarian:
    def __init__(self, name):
        self.name = name
        self.hit_die = 12
        self.primary_ability = "Strength"
        self.saving_throws = ["Strength", "Constitution"]
        self.starting_equipment = [
            {"name": "Greataxe", "quantity": 1},
            {"name": "Handaxe", "quantity": 2},
            {"name": "Javelin", "quantity": 4},
            {"name": "Explorer's pack", "quantity": 1}
        ]
        self.armor_proficiencies = [
            "Light armor",
            "Medium armor",
            "Shields"
        ]
        self.weapon_proficiencies = [
            "Simple weapons",
            "Martial weapons"
        ]
        self.tool_proficiencies = []
        self.skill_choices = [
            {
                "choose": 2,
                "from": [
                    "Animal Handling",
                    "Athletics",
                    "Intimidation",
                    "Nature",
                    "Perception",
                    "Survival"
                ]
            }
        ]
        self.level = 1
        self.proficiency_bonus = 2
        self.rages = 2
        self.rage_damage = 2

    def level_up(self):
        self.level += 1
        if self.level <= 4:
            self.proficiency_bonus = 2
        elif self.level <= 8:
            self.proficiency_bonus = 3
        elif self.level <= 12:
            self.proficiency_bonus = 4
        elif self.level <= 16:
            self.proficiency_bonus = 5
        else:
            self.proficiency_bonus = 6
        
        for rage in self.rages_table:
            if rage["Level"] == self.level:
                self.rages = rage["Rages"]
        
        for damage in self.rage_damage_table:
            if damage["Level"] == self.level:
                self.rage_damage = damage["Rage Damage"]
    
    def roll_hitpoints(self):
        return random.randint(1, self.hit_die) + self.modifier(self.primary_ability)
    
    def modifier(self, ability_score):
        return (ability_score - 10) // 2
    
    def print_character_sheet(self):
        print(f"Name: {self.name}")
        print("Class: Barbarian")
        print(f"Level: {str(self.level)}")
        print(f"Hit Points: {str(self.roll_hitpoints())}")
        print(f"Proficiency Bonus: +{str(self.proficiency_bonus)}")
        print(f"Rages per Day: {str(self.rages)}")
        print("Rage Damage Bonus: +" + str(self.rage_damage))
        print("Saving Throws: " + ", ".join(self.saving_throws))
        print("Armor Proficiencies: " + ", ".join(self.armor_proficiencies))
        print("Weapon Proficiencies: " + ", ".join(self.weapon_proficiencies))
        print("Tool Proficiencies: " + ", ".join(self.tool_proficiencies))
        print("Skills: Choose " + str(self.skill_choices[0]["choose"]) + " from " + ", ".join(self.skill_choices[0]["from"]))
        print("Equipment:")
        for item in self.starting_equipment:
            print("- " + str(item["quantity"]) + " " + item["name"])

my_barbarian = Barbarian("Gronk")
my_barbarian.print_character_sheet
