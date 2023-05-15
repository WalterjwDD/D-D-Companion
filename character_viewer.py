import json
from prettytable import PrettyTable

class ShowCharacter:
    def __init__(self):
        self.characters = []

    def load_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.characters = data["characters"]

    def show_table(self):
        table = PrettyTable()
        table.field_names = ["Name", "Race", "Class", "Level", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "Max HP", "HP", "AP", "Armor Class"]
        for character in self.characters:
            name = character["name"]
            race = character["race"]
            class_ = character["class"]
            level = character["level"]
            stats = character["stats"]
            strength = stats["Strength"]
            dexterity = stats["Dexterity"]
            constitution = stats["Constitution"]
            intelligence = stats["Intelligence"]
            wisdom = stats["Wisdom"]
            charisma = stats["Charisma"]
            max_hp = character["max_hp"]
            hp = character["hp"]
            ap = character["ap"]
            armor_class = character["armor_class"]
            table.add_row([name, race, class_, level, strength, dexterity, constitution, intelligence, wisdom, charisma, max_hp, hp, ap, armor_class])
        print(table)
        
    def find_characters(self, name):
        return [
            character for character in self.characters if character["name"].lower() == name.lower()
        ]


    def display_characters(self, name):
        if matches := self.find_characters(name):
            print(f"Found {len(matches)} characters with the name {name}.")
            for index, match in enumerate(matches, start=1):
                print(f"{index}. {match['name']} - {match['race']} {match['class']} Level {match['level']}")
        else:
            print(f"No characters found with the name {name}.")

#if __name__ == '__main__':
#    viewer = ShowCharacter()
#    viewer.load_data("player_database.json")
#    viewer.show_table()
