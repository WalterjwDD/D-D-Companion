import json

class AttackRoller:

    def __init__(self):
        self.weapons = {}
        self.load()

    def roll_damage(self, weapon_name):
        weapon = self.weapons.get(weapon_name)
        if weapon is None:
            raise ValueError("Weapon {} not found.".format(weapon_name))
        damage_dice = weapon.get("dice")
        if damage_dice is None:
            raise ValueError("Weapon {} does not have a damage dice.".format(weapon_name))
        return random.randint(1, damage_dice)

    def load(self):
        with open('weapons.json', 'r') as f:
            self.weapons = json.load(f)


# Example usage

attack_roller = AttackRoller()

# Roll damage for a club
damage = attack_roller.roll_damage('club')
print("You rolled {} damage.".format(damage))

# Roll damage for a longbow
damage = attack_roller.roll_damage('longbow')
print("You rolled {} damage.".format(damage))
