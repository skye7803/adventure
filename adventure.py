
from pprint import pprint
from location import Location
from activities import Activities
from inventory import Inventory

location = Location()

activities = Activities()

inventory = Inventory()

crater = True

while True:
	
	print('You are at {}.'.format(location.currentRegion['name']))
	print(location.currentRegion['text'])
	
	if inventory.playerInventory['health'] <= 0:
		print('You died!')
		break
	else:
		print('Your health is ' + str(inventory.playerInventory['health']))
	
	if inventory.playerInventory['house'] == True:
		print('New crafting recipes learned!')
	
	if crater == True:
		gucci = 'yeet'
	else:
		if location.currentRegion == location.regions['cratera3']:
			print('The ground begins to crumble underneath you!')
			print('You fall and black out!')
			inventory.playerInventory['health'] /= 2
			location.currentRegion = location.regions['cavea3II']

	activities.process_activity_statement(location, inventory)
