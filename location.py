
class Location:
	
	def __init__(self):
		self.directions = ['north', 'south', 'east', 'west']

		self.beachText = 'This is a pleasant beach with palm trees. You may check inventory, eat, pick up sticks, leaves, coconuts, or move'
		self.dunesText = 'This is a hill filled area with lots of sand. You may check inventory, eat, pick up rocks or move'
		self.craterText = 'This is a huge crater in the ground. You may check inventory, eat, pick up rocks or move'
		self.centerText = 'These are the woods in which you woke up in. You may check inventory, eat, craft, rest, or move.'
		self.caveText = 'This is a deep, dark, ominous cave. You may check inventory, eat, pick up rocks or move'
		self.mineText = 'This is a very long and sketchy abandoned mineshaft. You may check inventory, eat, pick up rocks or move'

		self.regions = {
			'dunesa1': {
				'id': 'dunesa1',
				'name': 'a dune filled region',
				'text': self.dunesText,
				'east': 'dunesa2',
				'south': 'dunesb1',
			},
			'dunesa2': {
				'id': 'dunesa2',
				'name': 'a dune filled region',
				'text': self.dunesText,
				'east': 'cratera3', 
				'south': 'centerb2', 
				'west': 'dunesa1',
			},
			'cratera3': {
				'id': 'cratera3',
				'name': 'a big crater', 
				'text': self.craterText,
				'south': 'beachb3', 
				'west': 'dunesa2',
			},
			'dunesb1': {
				'id': 'dunesb1',
				'name': 'a dune filled region', 
				'text': self.dunesText,             
				'north': 'dunesa1', 
				'east': 'centerb2', 
				'south': 'beachc1',
			},
			'centerb2': {
				'id': 'centerb2',
				'name': 'the center of the island', 
				'text': self.centerText,
				'north': 'dunesa2', 
				'east': 'beachb3', 
				'south': 'beachc2', 
				'west': 'dunesb1',
			},
			'beachb3': {
				'id': 'beachb3',
				'name': 'a beachy region', 
				'text': self.beachText,
				'north': 'cratera3', 
				'south': 'beachc3', 
				'west': 'centerb2',
			},
			'beachc1': {
				'id': 'beachc1',
				'name': 'a beachy region', 
				'text': self.beachText,
				'north': 'dunesb1', 
				'east': 'beachc2',
			},
			'beachc2': {
				'id': 'beachc2',
				'name': 'a beachy region', 
				'text': self.beachText,
				'north': 'centerb2', 
				'east': 'beachc3', 
				'west': 'beachc1',                   
			},
			'beachc3': {
				'id': 'beachc3',
				'name': 'a beachy region', 
				'text': self.beachText,
				'north': 'beachb3', 
				'west': 'beachc2',
			},
			'cavea3II': {
				'id': 'cavea3II',
				'name':'a deep dark cave',
				'text': self.caveText,
				'south': 'caveb3II',
				'west': 'cavea2II',
			},
			'cavea2II': {
				'id': 'caveawII',
				'name':'a deep dark cave',
				'text': self.caveText,
				'east': 'cavea3II',
				'south': 'mineb2II',
			},
			'caveb3II': {
				'id': 'caveb3II',
				'name':'a deep dark cave',
				'text': self.caveText,
				'north': 'cavea3II',
				'east': 'caveb4II',
				'west': 'mineb2II',
			},
			'caveb4II': {
				'id': 'caveb4II',
				'name':'a deep dark cave',
				'text': self.caveText,
				'west': 'caveb3II',
			},
			'mineb2II': {
				'id': 'mineb2II',
				'name':'a creepy abandoned mineshaft',
				'text': self.mineText,
				'north': 'cavea2II',
				'east': 'caveb3II',
			},
		}

		self.currentRegion = self.regions['centerb2']