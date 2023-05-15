import json

class Player:
    def __init__(self, name):
        self.name = name
        self.load_data()

    def load_data(self):
        with open('player_database.json', 'r') as f:
            data = json.load(f)
            characters = data['characters']
            for character in characters:
                if character['name'] == self.name:
                    self.race = character['race']
                    self.char_class = character['class']
                    self.level = character['level']
                    self.stats = character['stats']
                    self.exp = character['exp']
                    self.equipment = character['equipment']
                    self.spells = character['spells']
                    self.inventory = character['inventory']
                    self.hp = character['hp']
                    self.ap = character['ap']
                    break
            else:
                raise ValueError(f'Character with name "{self.name}" not found in database.')

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f'{name} not found in character data')

    def __str__(self):
        return self.name
