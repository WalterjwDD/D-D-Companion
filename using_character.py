import json
import random
from prettytable import PrettyTable
from DD import Player

# Load the character database from file
with open('player_database.json', 'r') as f:
    character_database = json.load(f)

class UsingCharacter:
    def __init__(self, name):
        self.character = self.select_character(name)
        if self.character is None:
            raise ValueError(f"No character named '{name}' found in the database.")
        self.level_up()

    def select_character(self, name):
        return next(
            (
                character
                for character in character_database
                if character['name'] == name
            ),
            None,
        )

    def level_up(self):
        # Calculate the required exp to level up
        current_level = self.character['level']
        next_level_exp = (current_level + 1) ** 3 * 1000

        if self.character['exp'] >= next_level_exp:
            self.character['level'] += 1
            self.character['hp'] += 10
            self.character['ap'] += 5
            self.character['exp'] -= next_level_exp
            print(f"{self.character['name']} has leveled up to level {self.character['level']}!")

    def show_character(self):
        # Create a table to display the character's stats
        table = PrettyTable()
        table.field_names = ["Name", "Race", "Class", "Level", "Experience", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "HP", "AP", "Equipment", "Spells", "Inventory"]
        stats = [self.character['name'], self.character['race'], self.character['class'], self.character['level'], self.character['exp']]
        stats.extend(iter(self.character['stats'].values()))
        stats.extend([self.character['hp'], self.character['ap'], self.character['equipment'], self.character['spells'], self.character['inventory']])
        table.add_row(stats)
        print(table)

        # Print the equipment and spells the player is using
        print("\nEquipment:")
        for item in self.character['equipment']:
            print(f"- {item}")
        print("Spells:")
        for spell in self.character['spells']:
            print(f"- {spell}")

        # Print the items in the player's inventory
        print("\nInventory:")
        for item, count in self.character['inventory'].items():
            print(f"- {item}: {count}")

    def level_up_menu(self):  # sorcery skip: extract-duplicate-method
        print("\nLevel Up Menu")
        print("1. Increase Strength")
        print("2. Increase Dexterity")
        print("3. Increase Constitution")
        print("4. Increase Intelligence")
        print("5. Increase Wisdom")
        print("6. Increase Charisma")
        print("7. Return to Main Menu")

        choice = input("Enter choice: ")
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            choice = input("Invalid choice. Enter choice: ")

        if choice == "1":
            self._extracted_from_level_up_menu_16('strength', "'s strength increased to ")
        elif choice == "2":
            self._extracted_from_level_up_menu_21(
                'dexterity',
                'armor_class',
                "'s dexterity increased to ",
                'dexterity',
            )
        elif choice == "3":
            self._extracted_from_level_up_menu_16(
                'constitution', "'s constitution increased to "
            )
        elif choice == "4":
            self.character['stats']['intelligence'] += 1
            print(f"{self.character['name']}'s intelligence increased to {self.character['stats']['intelligence']}.")
        elif choice == "5":
            self.character['stats']['wisdom'] += 1
            self._extracted_from_level_up_menu_21(
                'spell_save_dc',
                'spell_attack_bonus',
                "'s wisdom increased to ",
                'wisdom',
            )
        elif choice == "6":
            self._extracted_from_level_up_menu_21(
                'charisma',
                'persuasion_bonus',
                "'s charisma increased to ",
                'charisma',
            )
        else:
            print("Returning to Main Menu.")

    # TODO Rename this here and in `level_up_menu`
    def _extracted_from_level_up_menu_16(self, arg0, arg1):
        self.character['stats'][arg0] += 1
        self.character['stats']['max_hp'] += max(1, (self.character['stats']['level'] + 1) * 2 + self.character['stats']['constitution'] - 10) - max(1, self.character['stats']['level'] * 2 + self.character['stats']['constitution'] - 10)
        self.character['stats']['current_hp'] = self.character['stats']['max_hp']
        print(f"{self.character['name']}{arg1}{self.character['stats'][arg0]}.")

    # TODO Rename this here and in `level_up_menu`
    def _extracted_from_level_up_menu_21(self, arg0, arg1, arg2, arg3):
        self.character['stats'][arg0] += 1
        self.character['stats'][arg1] += 1
        print(f"{self.character['name']}{arg2}{self.character['stats'][arg3]}.")

    def attack(self):
        # Calculate the attack modifier
        attack_mod = self.character['stats']['strength'] // 2

        # Roll the attack
        attack_roll = random.randint(1, 20)
        total_attack = attack_roll + attack_mod

        print(f"{self.character['name']} attacks with a total of {total_attack} ({attack_roll} + {attack_mod})!")

    def roll(self):
        # Roll a d20
        roll = random.randint(1, 20)
        print(f"{self.character['name']} rolls a {roll}!")

        # Calculate the modifier
        mod = input("Enter modifier: ")
        while not mod.isnumeric():
            mod = input("Invalid modifier. Enter modifier: ")
        mod = int(mod)

        total_roll = roll + mod

        print(f"{self.character['name']} rolls a total of {total_roll} ({roll} + {mod})!")

    def chance(self):
        # Roll a percentage
        percent = random.randint(1, 100)

        print(f"{self.character['name']} has a {percent}% chance of success.")

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Show Character")
            print("2. Level Up")
            print("3. Attack")
            print("4. Roll")
            print("5. Chance")
            print("6. Quit")

            choice = input("Enter choice: ")
            while choice not in ["1", "2", "3", "4", "5", "6"]:
                choice = input("Invalid choice. Enter choice: ")

            if choice == "1":
                self.show_character()
            elif choice == "2":
                self.level_up_menu()
            elif choice == "3":
                self.attack()
            elif choice == "4":
                self.roll()
            elif choice == "5":
                self.chance()
            elif choice == "6":
                print("Goodbye!")
                break
            
    #Starts Play
#Ask the user to enter the name of the character they want to select
character_name = input("Enter the name of the character you want to select: ")

# Create a new instance of the UsingCharacter class using the selected character name
using_character = UsingCharacter(character_name)

# Show the selected character's stats
using_character.show_character()

# Show the main menu to select options
using_character.main_menu()