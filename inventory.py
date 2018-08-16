from pprint import pprint


class Inventory:
	def __init__(self):
		self.playerInventory = {
			'health' : 20,
			'sticks' : 0,
			'rocks' : 0,
			'leaves' : 0,
			'coconuts' : 0,
			'wood' : 20,
			'stone' : 20,
			'string' : 20,
			'coconut milk' : 0,
			'house' : False,
			'craftingTable' : False,
		}
		self.crafting = {
			'wood' : 'sticks',
			'stone' : 'rocks',
			'string' : 'leaves',
			'coconut milk' : 'coconuts',
		}

	def print_inventory(self):
		pprint(self.playerInventory)
