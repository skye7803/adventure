
class Location:

    def __init__(self):
        self.directions = ['north', 'south', 'east', 'west']

        self.default_text = '. You may check inventory, eat, move,'

        self.beachText = 'This is a pleasant beach with palm trees. You may check inventory, eat, pick up sticks, leaves, coconuts, or move'
        self.dunesText = 'This is a hill filled area with lots of sand. You may check inventory, eat, pick up rocks or move'
        self.craterText = 'This is a huge crater in the ground. You may check inventory, eat, pick up rocks or move'
        self.centerText = 'These are the woods in which you woke up in. You may check inventory, eat, craft, rest, or move.'
        self.caveText = 'This is a deep, dark, ominous cave. You may check inventory, eat, pick up rocks or move'
        self.mineText = 'This is a very long and sketchy abandoned mineshaft. You may check inventory, eat, pick up rocks or move'

        self.regions = {
            'dunesa1': {
                'id': 'dunesa1',
                'type' : 'dunes',
                'name': 'a dune filled region',
                'east': 'dunesa2',
                'south': 'dunesb1',
            },
            'dunesa2': {
                'id': 'dunesa2',
                'type' : 'dunes',
                'name': 'a dune filled region',
                'east': 'cratera3',
                'south': 'centerb2',
                'west': 'dunesa1',
            },
            'cratera3': {
                'id': 'cratera3',
                'type' : 'crater',
                'name': 'a big crater',
                'south': 'beachb3',
                'west': 'dunesa2',
            },
            'dunesb1': {
                'id': 'dunesb1',
                'type' : 'dunes',
                'name': 'a dune filled region',
                'north': 'dunesa1',
                'east': 'centerb2',
                'south': 'beachc1',
            },
            'centerb2': {
                'id': 'centerb2',
                'type' : 'center',
                'name': 'the center of the island',
                'north': 'dunesa2',
                'east': 'beachb3',
                'south': 'beachc2',
                'west': 'dunesb1',
            },
            'beachb3': {
                'id': 'beachb3',
                'type' : 'beach',
                'name': 'a beachy region',
                'north': 'cratera3',
                'south': 'beachc3',
                'west': 'centerb2',
            },
            'beachc1': {
                'id': 'beachc1',
                'type' : 'beach',
                'name': 'a beachy region',
                'north': 'dunesb1',
                'east': 'beachc2',
            },
            'beachc2': {
                'id': 'beachc2',
                'type' : 'beach',
                'name': 'a beachy region',
                'north': 'centerb2',
                'east': 'beachc3',
                'west': 'beachc1',
            },
            'beachc3': {
                'id': 'beachc3',
                'type' : 'beach',
                'name': 'a beachy region',
                'north': 'beachb3',
                'west': 'beachc2',
            },
            'cavea3II': {
                'id': 'cavea3II',
                'type' : 'cave',
                'name': 'a deep dark cave',
                'south': 'caveb3II',
                'west': 'cavea2II',
            },
            'cavea2II': {
                'id': 'caveawII',
                'type' : 'cave',
                'name': 'a deep dark cave',
                'east': 'cavea3II',
                'south': 'mineb2II',
            },
            'caveb3II': {
                'id': 'caveb3II',
                'type' : 'cave',
                'name': 'a deep dark cave',
                'north': 'cavea3II',
                'east': 'caveb4II',
                'west': 'mineb2II',
            },
            'caveb4II': {
                'id': 'caveb4II',
                'type' : 'cave',
                'name': 'a deep dark cave',
                'west': 'caveb3II',
            },
            'mineb2II': {
                'id': 'mineb2II',
                'type' : 'mine',
                'name': 'a creepy abandoned mineshaft',
                'north': 'cavea2II',
                'east': 'caveb3II',
            },
        }

        self.current_region = self.regions['centerb2']


    def get_current_region_text(self, inventory, activities):
        if self.current_region['id'] in activities.regionsRocky + activities.regionsCave:
            if self.current_region['id'] == 'cratera3':
                if 'ladder' in inventory.playerInventory.keys():
                    if inventory.playerInventory['ladder'] == True:
                        if inventory.playerInventory['pickaxe']:
                            return self.current_region['name'] + self.default_text + 'mine stone, or deploy ladder'
                        else:
                            return self.current_region['name'] + self.default_text + 'pick up rocks, or deploy ladder'
            if 'pickaxe' in inventory.playerInventory.keys():
                if inventory.playerInventory['pickaxe'] == True:
                    return self.current_region['name'] + self.default_text + ' mine stone'
                else:
                    return self.current_region['name'] + self.default_text + ' or pick up rocks.'
            else:
                return self.current_region['name'] + self.default_text + ' or pick up rocks.'
        elif self.current_region['id'] in activities.regionsBeachy + activities.regionsMine:
            if 'axe' in inventory.playerInventory.keys():
                if inventory.playerInventory['axe'] == True:
                    return self.current_region['name'] + self.default_text + ' mine wood, pick up leaves, or pick up coconuts.'
                else:
                    return self.current_region['name'] + self.default_text + ' pick up sticks, pick up leaves, or pick up coconuts'
            else:
                return self.current_region['name'] + self.default_text + ' pick up sticks, pick up leaves, or pick up coconuts'
        elif self.current_region['id'] in activities.regionsSafe:
            return self.current_region['name'] + self.default_text + ' craft, or rest.'


