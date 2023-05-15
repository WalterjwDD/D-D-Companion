import json

class SelectCharacter:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()

    def load_data(self):
        with open(self.filename) as f:
            self.db = json.load(f)

    def select_character(self):
        print("Available characters:")
        for character in self.db['characters']:
            print(f"- {character['name']}")
        
        name = input("Select character: ")
        for character in self.db['characters']:
            if character['name'].lower() == name.lower():
                current_player = {
                    "name": character['name'],
                    "race": character['race'],
                    "class": character['class'],
                    "level": character['level'],
                    "stats": character['stats'],
                    "exp": character['exp'],
                    "equipment": character['equipment'],
                    "spells": character['spells'],
                    "inventory": character['inventory'],
                    "max_hp": character['max_hp'],
                    "hp": character['hp'],
                    "ap": character['ap'],
                    "armor_class": character['armor_class']
                }
                with open('current_player.json', 'w') as f:
                    json.dump(current_player, f)
                return character
        
        print(f"No character found with name {name}.")
        return None
        
    def update_current_player(self, character):
        with open("current_player.json", "w") as f:
            json.dump(character, f)

    def update_player_database(self, character):
        for i, c in enumerate(self.db['characters']):
            if c['name'] == character['name']:
                self.db['characters'][i] = character
                with open(self.filename, "w") as f:
                    json.dump(self.db, f)
                break
    
    def edit_stats(self, character):
        print(f"{character['name']} is currently at Level {character['level']} with {character['exp']} experience points.")
        if character["level"] < 20:
            print("You can level up this character by spending experience points.")
            points = int(input("Enter the number of points you want to spend: "))
            while points <= 0:
                points = int(input("Invalid number. Enter a positive number of points: "))
            character["exp"] -= points
            character["exp"] = max(character["exp"], 0)
            character["level"] += 1
            character["max_hp"] += 2
            character["hp"] = character["max_hp"]
            character["ap"] += 1
            character["armor_class"] += 1
            print(f"{character['name']} is now Level {character['level']} with {character['exp']} experience points.")
            print(f"Max HP: {character['max_hp']}")
            print(f"Current HP: {character['hp']}")
            print(f"AP: {character['ap']}")
            print(f"Armor Class: {character['armor_class']}")
        else:
            print("This character is already at the maximum level of 20 and cannot be leveled up further.")
