import json
from tabulate import tabulate


class Equipment:
    @staticmethod
    def coin_value(coin_str):
        values = {"cp": 0.01, "sp": 0.1, "ep": 0.5, "gp": 1, "pp": 10}
        return float(coin_str.split()[0]) * values[coin_str.split()[1]]

    def __init__(self):
        with open('04 equipment.json', encoding='utf-8') as f:
            self.equipment_data = json.load(f)
            
    def get_light_armor(self):       
        return self.equipment_data["Equipment"]["Armor"]["Armor List"]["Light Armor"]["table"]
    
    def get_medium_armor(self):       
        return self.equipment_data["Equipment"]["Armor"]["Armor List"]["Medium Armor"]["table"]
    
    def get_heavy_armor(self):       
        return self.equipment_data["Equipment"]["Armor"]["Armor List"]["Heavy Armor"]["table"]
    
    def get_shield_armor(self):       
        return self.equipment_data["Equipment"]["Armor"]["Armor List"]["Shield"]["table"]

    def get_simple_melee_weapons(self):
        return self.equipment_data["Equipment"]["Weapons"]["Weapons List"]["Simple Melee Weapons"]["table"]
    
    def get_simple_range_weapons(self):       
        return self.equipment_data["Equipment"]["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]
    
    def get_martial_melee_weapons(self):       
        return self.equipment_data["Equipment"]["Weapons"]["Weapons List"]["Martial Melee Weapons"]["table"]
    
    def get_martial_range_weapons(self):       
        return self.equipment_data["Equipment"]["Weapons"]["Weapons List"]["Martial Ranged Weapons"]["table"]
    
    def table(self, data_func):
        data = data_func()
        headers = []
        rows = []

        if isinstance(data, dict):
            data = list(data.values())

        for i, row in enumerate(data):
            if i == 0:
                headers = row
            else:
                rows.append(row)

        return tabulate(rows, headers=headers, tablefmt="fancy_grid", numalign="right", stralign="left")

    def choose_table(self):
        print("Which table do you want to display?")
        print("1. Light Armor")
        print("2. Medium Armor")
        print("3. Heavy Armor")
        print("4. Shields")
        print("5. Simple Melee Weapons")
        print("6. Simple Ranged Weapons")
        print("7. Martial Melee Weapons")
        print("8. Martial Ranged Weapons")
        
        choice = int(input("Enter the number of the table you want to display: "))
        
        if choice == 1:
            print(self.table(self.get_light_armor))
        elif choice == 2:
            print(self.table(self.get_medium_armor))
        elif choice == 3:
            print(self.table(self.get_heavy_armor))
        elif choice == 4:
            print(self.table(self.get_shield_armor))
        elif choice == 5:
            print(self.table(self.get_simple_melee_weapons))
        elif choice == 6:
            print(self.table(self.get_simple_range_weapons))
        elif choice == 7:
            print(self.table(self.get_martial_melee_weapons))
        elif choice == 8:
            print(self.table(self.get_martial_range_weapons))
        else:
            print("Invalid choice.")

#Testing        
#equipment = Equipment()
#equipment.choose_table()

# Examples:
#print(equipment.table(equipment.get_light_armor))
#print(equipment.table(equipment.get_medium_armor))
#print(equipment.table(equipment.get_heavy_armor))
#print(equipment.table(equipment.get_shield_armor))
#print(equipment.table(equipment.get_simple_melee_weapons))
#print(equipment.table(equipment.get_simple_range_weapons))
#print(equipment.table(equipment.get_martial_melee_weapons))
#print(equipment.table(equipment.get_martial_range_weapons))
