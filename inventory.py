from pprint import pprint


class Inventory:
    def __init__(self):
        self.playerInventory = {
            'health': 20,
            'sticks': 0,
            'rocks': 0,
            'leaves': 0,
            'wood': 45,
            'stone': 45,
            'string': 30,
            'items': {
                'coconut milk': 0,
                'coconuts': 0,
            },
            'house': False,
            'EXP': 0,
        }
        self.crafting = {
            'wood': 'sticks',
            'stone': 'rocks',
            'string': 'leaves',
            'coconut milk': 'coconuts',
        }
        self.weapon = {
            'name': 'fists',
            'attack': 1,
        }

    def print_inventory(self):
        pprint(self.playerInventory)
