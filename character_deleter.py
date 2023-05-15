import json
from character_viewer import ShowCharacter

class CharacterDeleter:
    def __init__(self):
        self.characters = []

    def load_data(self, file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
            self.characters = data["characters"]

    def delete_character(self, name):
        viewer = ShowCharacter()
        viewer.load_data("player_database.json")
        if matches := viewer.find_characters(name):
            print(f"Found {len(matches)} characters with the name {name}.")
            print("Here are the characters:")
            for index, match in enumerate(matches, start=1):
                print(f"{index}. {match['name']}")
            choice = input("Which character do you want to delete? ")
            try:
                index = int(choice) - 1
                character = matches[index]
                confirm = input(f"Are you sure you want to delete {character['name']}? (y/n) ")
                if confirm.lower() == "y":
                    self.characters.remove(character)
                    with open("player_database.json", "w") as file:
                        json.dump({"characters": self.characters}, file, indent=4)
                    print(f"{character['name']} has been deleted.")
                else:
                    print("Deletion canceled.")
            except (ValueError, IndexError):
                print("Invalid choice. Deletion canceled.")
        else:
            print(f"No characters found with the name {name}.")
