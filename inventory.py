from pprint import pprint


class Inventory:
    def __init__(self):
        self.playerInventory = {
            'health': 20,
            'sticks': 30,
            'rocks': 0,
            'leaves': 0,
            'wood': 0,
            'stone': 0,
            'string': 0,
            'items': {
                'itemsids': ['coconuts', 'coconut milk'],
                'coconut milk': 0,
                'coconuts': 0,
            },
            'house': True,
            'crafting_table': True,
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
            'type' : 'melee',
            'ammo' : 'none',
        }

    def print_inventory(self):
        pprint(self.playerInventory)
