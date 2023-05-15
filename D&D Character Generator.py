import random

class PlayerName:
    def __init__(self):
        self.name = ""
    
    def get_name(self):
        self.name = input("Enter your character's name: ")
        
class Race:
    def __init__(self, name, ability_score_modifiers, speed):
        self.name = name
        self.ability_score_modifiers = ability_score_modifiers
        self.speed = speed

class Human(Race):
    def __init__(self):
        super().__init__("Human", {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1}, 30)

class Elf(Race):
    def __init__(self):
        super().__init__("Elf", {"Dexterity": 2, "Intelligence": 1}, 30)

class Dwarf(Race):
    def __init__(self):
        super().__init__("Dwarf", {"Constitution": 2, "Wisdom": 1}, 25)

class Halfling(Race):
    def __init__(self):
        super().__init__("Halfling", {"Dexterity": 2, "Charisma": 1}, 25)

class Character:
    def __init__(self, race, char_class, level, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, armor_class):
        self.race = race
        self.char_class = char_class
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_points = hit_points
        self.armor_class = armor_class

    #def __str__(self):
    #    return f"{self.race} {self.char_class} level {self.level}"
    
            
    def __str__(self):
        box_width = 38
        race_name = f"{self.race} {self.char_class}"
        box_contents = [f"Level {self.level} {race_name.center(box_width - len(race_name))}",
                        f"Strength: {self.strength}",
                        f"Dexterity: {self.dexterity}",
                        f"Constitution: {self.constitution}",
                        f"Intelligence: {self.intelligence}",
                        f"Wisdom: {self.wisdom}",
                        f"Charisma: {self.charisma}",
                        f"Hit Points: {self.hit_points}",
                        f"Armor Class: {self.armor_class}"]
        box_top = "+" + "-" * (box_width - 2) + "+"
        box_bottom = "+" + "-" * (box_width - 2) + "+"
        box_contents = [f"| {s.ljust(box_width - 4)} |" for s in box_contents]
        box_contents = "\n".join(box_contents)
        return f"{box_top}\n{box_contents}\n{box_bottom}"
    
    def roll_dice(self, num_dice, dice_size):
        return sum(random.randint(1, dice_size) for _ in range(num_dice))

    def calculate_ability_score(self):
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

    def calculate_hit_points(self):
        hit_points = self.roll_dice(self.level, 8) + self.calculate_modifier(self.constitution)
        hit_points = max(hit_points, 1)
        return hit_points

    def calculate_modifier(self, ability_score):
        return (ability_score - 10) // 2

    def calculate_armor_class(self):
        return 10 + self.calculate_modifier(self.dexterity)

    def generate_stats(self):
        self.strength = self.calculate_ability_score()
        self.dexterity = self.calculate_ability_score()
        self.constitution = self.calculate_ability_score()
        self.intelligence = self.calculate_ability_score()
        self.wisdom = self.calculate_ability_score()
        self.charisma = self.calculate_ability_score()
        self.hit_points = self.calculate_hit_points()
        self.armor_class = self.calculate_armor_class()
        
#Create a Player Name Instance and get the name
player_name = PlayerName()
player_name.get_name()

# Choose random race, class, and level for the character
races = ["Human", "Elf", "Dwarf", "Halfling"]
char_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
race = random.choice(races)
char_class = random.choice(char_classes)
level = random.randint(1, 20)

# Generate stats for the character
new_character = Character(race, char_class, level, 0, 0, 0, 0, 0, 0, 0, 0)
new_character.generate_stats()
"Race: {new_character.race}"
"Class: {new_character.char_class}"
"Level: {new_character.level}"
"Strength: {new_character.strength}"
"Dexterity: {new_character.dexterity}"
"Constitution: {new_character.constitution}"
"Intelligence: {new_character.intelligence}"
"Wisdom: {new_character.wisdom}"
"Charisma: {new_character.charisma}"
"Hit Points: {new_character.hit_points}"
"Armor Class: {new_character.armor_class}"

# Print the character's stats
print("\n")
print(f"New Character Created: {player_name.name}")
print(new_character)

