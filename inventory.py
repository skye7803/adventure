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
                'itemsids': ['coconuts', 'coconut milk'],
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
            'type' : 'melee',
            'ammo' : 'none',
        }
        self.world_resources = {
            'sticks': 500,
            'rocks': 500,
            'leaves': 500,
            'coconuts': 50,
            'stone': 500,
            'wood': 500,

        }

    def print_inventory(self):
        pprint(self.playerInventory)
