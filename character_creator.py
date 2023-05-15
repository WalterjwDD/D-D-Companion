import json
import random
from prettytable import PrettyTable

class PlayerCreator:
    def __init__(self):  # sorcery skip: low-code-quality
        self.character_database = []  # initialize an empty list
        self.name = input("Enter character name: ")
        self.race = input("Enter character race: ")
        self.char_class = input("Enter character class: ")
        self.level = 1
        self.stats = []
        
        while True:
            use_base_stats = input("Use Generated stats? (y/n): ")
            if use_base_stats.lower() == 'y':
                self.generate_stats()
                break
            elif use_base_stats.lower() == 'n':
                self.stats = {
                    'Strength': int(input("Enter Strength stat: ")),
                    'Dexterity': int(input("Enter Dexterity stat: ")),
                    'Constitution': int(input("Enter Constitution stat: ")),
                    'Intelligence': int(input("Enter Intelligence stat: ")),
                    'Wisdom': int(input("Enter Wisdom stat: ")),
                    'Charisma': int(input("Enter Charisma stat: "))
                }
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                
        # Create a new dictionary object with the correct format
        stats_dict = {}
        if isinstance(self.stats, dict):
            stats_dict = self.stats
        elif isinstance(self.stats, list):
            stats_dict = {
            'Strength': self.stats[0],
            'Dexterity': self.stats[1],
            'Constitution': self.stats[2],
            'Intelligence': self.stats[3],
            'Wisdom': self.stats[4],
            'Charisma': self.stats[5]
            }
        
        # initialize the rest of the attributes after setting stats
        self.exp = 0
        self.equipment = {}
        self.spells = {}
        self.inventory = {}
        self.max_hp = 0
        self.hp = 0
        self.ap = 0
        self.armor_class = 0

        
            # Prompt the user to add equipment and items to the inventory
        while True:
            # Ask the user if they want to add equipment or items
            choice = input("Do you want to add (e)quipment, (s)pells, or (i)tems to the inventory? (Press ENTER to skip) ").lower()
            if choice == 'e':
                # Add equipment
                item = input("Enter the name of the equipment to add: ")
                count = int(input("Enter the quantity of the Equipment to add: "))
                self.equipment[item] = count
            elif choice == 's':
                spell = input("Enter the name of the spell to add: ")
                count = int(input("Enter the spell level: "))
                self.spells[spell] = count
            elif choice == 'i':
                # Add items to the inventory
                item = input("Enter the name of the item to add: ")
                count = int(input("Enter the quantity of the item to add: "))
                self.inventory[item] = count
            elif choice == '':
                # User is done adding equipment and items
                break
            else:
                print("Invalid choice. Please enter 'e', 's', 'i', or press ENTER to skip.")
        
        #self.set_stats()
        self.set_max_hp()
        self.set_ap()
        self.set_armor_class()
        
        character = {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "level": self.level,
            "stats": self.stats,
            "exp": self.exp,
            "equipment": self.equipment,
            "spells": self.spells,
            "inventory": self.inventory,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "ap": self.ap,
            "armor_class": self.armor_class
        }
        
        # Load the character database from file or create an empty list if the file doesn't exist
        # Save character to player_database.json
        with open("player_database.json", "r") as f:
            data = json.load(f)
        data["characters"].append({
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "level": self.level,
            "stats": self.stats,
            "exp": self.exp,
            "equipment": self.equipment,
            "spells": self.spells,
            "inventory": self.inventory,
            "max_hp":self.max_hp,
            "hp": self.hp,
            "ap": self.ap,
            "armor_class": self.armor_class
        })
        with open("player_database.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"Character '{self.name}' has been created.")

        
    def set_max_hp(self):
        self.max_hp = 18 + self.stats['Constitution']
        self.hp = self.max_hp - 10
        
    def set_ap(self):
        self.ap = 5 + (self.level // 2)
        return self.ap 
    
    #def set_armor_class(self):
    #    self.armor_class = self.calculate_modifier('Dexterity')
    #    return (10 + self.armor_class)
    
    def set_armor_class(self):
        self.armor_class = self.calculate_modifier(int(self.stats['Dexterity']))
        return (10 + self.armor_class)

    
    def roll_dice(self, num_dice, dice_size):
        
        return sum(random.randint(1, dice_size) for _ in range(num_dice))

    def calculate_ability_score(self):
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

    def calculate_hit_points(self):
        hit_points = self.roll_dice(self.level, 8) + self.calculate_modifier(self.stats['Constitution'])
        hit_points = max(hit_points, 1)
        return hit_points

    def calculate_modifier(self, ability_score):
        return ((ability_score - 10) // 2)

    def generate_stats(self):
        self.stats = {
            'Strength': self.calculate_ability_score(),
            'Dexterity': self.calculate_ability_score(),
            'Constitution': self.calculate_ability_score(),
            'Intelligence': self.calculate_ability_score(),
            'Wisdom': self.calculate_ability_score(),
            'Charisma': self.calculate_ability_score()
        }
        self.set_max_hp()
        self.set_armor_class()
        #self.set_proficiency_bonus()
        
        #Starts Character
        #character = PlayerCreator()
