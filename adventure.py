
from pprint import pprint
from location import Location
from activities import Activities
from inventory import Inventory

location = Location()

activities = Activities()

inventory = Inventory()

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

	activities.processInput(location, inventory)
