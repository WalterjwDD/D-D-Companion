import json
from attack_roller import AttackRoller

class Adventuring:
    def __init__(self):
        self.player_data = None
        self.load_data()

    def load_data(self):
        with open('current_player.json', 'r') as f:
            self.player_data = json.load(f)

        with open('weapons.json', 'r') as f:
            weapons_data = json.load(f)
        weapon_list = {}
        for weapon_type, weapon_data in weapons_data['Equipment']['Weapons']['Weapons List'].items():
            for weapon in weapon_data['table']:
                name, weight = weapon
                weapon_list[name.lower()] = {
                    #'dice': dice,
                    'weight': weight,
                    #'cost': cost
                }
        return weapon_list

    def attack(self):
        print(f"\n{self.player_data['name']}, choose your weapon to attack:")
        for i, weapon in enumerate(self.player_data['equipment']):
            print(f"{int(i)+1}. {weapon['name']}")

        choice = int(input("\nEnter the number of the weapon you want to use: "))

        selected_weapon = self.player_data['equipment'][choice-1]
        weapon_stats = self.weapons[selected_weapon['name']]
        attack_roller = AttackRoller()

        print(f"\nYou have selected {selected_weapon['name']}")

        attack_modifier = self.calculate_attack_modifier(selected_weapon)

        attack_roll = attack_roller.roll(20) + attack_modifier

        if attack_roll >= weapon_stats['attack']:
            damage = attack_roller.roll(weapon_stats['damage']) + self.player_data['stats']['strength']
            print(f"You hit for {damage} damage!")
        else:
            print("You missed!")

    def calculate_attack_modifier(self, weapon):
        attack_modifier = 0

        if 'finesse' in weapon['properties'] and self.player_data['stats']['dexterity'] > self.player_data['stats']['strength']:
            attack_modifier += self.player_data['stats']['dexterity']
        else:
            attack_modifier += self.player_data['stats']['strength']

        if weapon['type'] == 'ranged' and 'ammunition' in weapon['properties']:
            ammunition_name = weapon['properties']['ammunition']
            if ammunition := next(
                (
                    item
                    for item in self.player_data['equipment']
                    if item["name"] == ammunition_name
                ),
                None,
            ):
                ammunition_count = ammunition.get('count', 0)
                if ammunition_count > 0:
                    ammunition['count'] -= 1
                    print(f"You have {ammunition_count-1} {ammunition_name} left.")
                else:
                    print("You are out of ammunition and cannot attack with this weapon.")

        return attack_modifier
