from pprint import pprint


class Inventory:
    def __init__(self):
        self.playerInventory = {
            'health' : 50,
            'sticks' : 0,
            'rocks' : 0,
            'leaves' : 0,
            'coconuts' : 0,
            'wood' : 0,
            'stone' : 0,
            'string' : 0,
            'coconut milk' : 0,
        }

    def print_inventory(self):
        pprint(self.playerInventory)
        # print('You have:')
        # if self.playerInventory['sticks'] >= 1:
        #     print(str(self.playerInventory['sticks']) + ' sticks')
        # else:
        #     print('[]')
        # if self.playerInventory['rocks'] >= 1:
        #     print(str(self.playerInventory['rocks']) + ' rocks')
        # else:
        #     print('[]')
        # if self.playerInventory['wood'] >= 1:
        #     print(str(self.playerInventory['wood']) + ' wood')
        # else:
        #     print('[]')
        # if self.playerInventory['stone'] >= 1:
        #     print(str(self.playerInventory['stone']) + ' stone')
        # else:
        #     print('[]')
        # if self.playerInventory['leaves'] >= 1:
        #     print(str(self.playerInventory['leaves']) + ' leaves')
        # else:
        #     print('[]')
        # if self.playerInventory['coconuts'] >= 1:
        #     print(str(self.playerInventory['coconuts']) + ' coconuts')
        # else:
        #     print('[]')
        # if self.playerInventory['string'] >= 1:
        #     print(str(self.playerInventory['string']) + ' string')
        # else:
        #     print('[]')
        # if self.playerInventory['coconut milk'] >= 1:
        #     print(str(self.playerInventory['coconut milk']))
        # else:
        #     print([])
        # if self.playerInventory['health'] >= 1:
        #     print(str(self.playerInventory['health']) + ' health')
        # else:
        #     print('You\'ve broken the game. Good job.')

    


