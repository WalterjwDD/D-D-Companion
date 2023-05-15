from typing import Self
from adventure import Adventuring
from character_creator import PlayerCreator
from character_viewer import ShowCharacter
from character_deleter import CharacterDeleter
from equipment import Equipment
from attack_roller import AttackRoller
from select_character import SelectCharacter

def main():
    while True:
        print("Please choose an option:")
        print("1. Select Character")
        print("2. Character Info")
        print("3. View List of Equipment")
        print("4. Roll Attack")
        print("5. Start Adventure")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            viewer = ShowCharacter()
            viewer.load_data("player_database.json")
            viewer.show_table()
            selector = SelectCharacter("player_database.json")
            selector.load_data()
            selector.select_character()
            #print("Would you like to edit character")
            #    selector.edit_stats(character)

        elif choice == "2":
            while True:
                print("Please choose an option:")
                print("1. View Character Database")
                print("2. Delete a Character")
                print("3. Create a Character")
                print("4. Return to Main Menu")

                char_choice = input("Enter choice: ")

                if char_choice == "1":
                    viewer = ShowCharacter()
                    #viewer.show_table()
                    viewer.load_data("player_database.json")
                    viewer.show_table()
                    #viewer.display_characters(name)

                elif char_choice == "2":
                    viewer = ShowCharacter()
                    viewer.load_data("player_database.json")
                    viewer.show_table()
                    name = input("Enter the name of the character you want to delete: ")
                    deleter = CharacterDeleter()
                    deleter.load_data("player_database.json")
                    deleter.delete_character(name)

                elif char_choice == "3":
                    creator = PlayerCreator()
                    #creator.create_character()
                
                elif char_choice == "4":
                    break
                    
        elif choice == "3":
            equipment = Equipment()
            equipment.choose_table()

        elif choice == "4":
            attack_roller = AttackRoller()
            weapon_name, weapon_stats = attack_roller.select_weapon()
            print(f"You selected the {weapon_name} with {weapon_stats['dice']}d{weapon_stats['sides']} damage dice.")
            attack_bonus = int(input("Enter your attack bonus: "))
            damage_bonus = int(input("Enter your damage bonus: "))
            attack_roll, damage_roll = attack_roller.roll_attack(weapon_stats)
            print(f"You rolled {attack_roll} to hit and dealt {damage_roll + damage_bonus} damage.")

        
        elif choice == "5":
            player = Adventuring()
            #player.load_character()
            while True:
                print("Please choose an option:")
                print("1. Roll Attack")
                print("2. Exit")
                
                choice = input("Enter choice: ")
                
                if choice == "1":
                    player.attack()
                elif choice == "2":\
                    
                    break
                    
        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
