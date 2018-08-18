from pprint import pprint


class Inventory:
    def __init__(self):
        self.playerInventory = {
            'health': 20,
            'sticks': 0,
            'rocks': 0,
            'leaves': 0,
            'wood': 0,
            'stone': 0,
            'string': 0,
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
            'damage': 1,
            'ammo' : 'none'
        }

    def print_inventory(self):
        pprint(self.playerInventory)
