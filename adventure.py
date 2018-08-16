
from pprint import pprint
from adventure_location import Location
from adventure_activities import Activities
from adventure_player_inventory import Inventory

location = Location()

activities = Activities()

inventory = Inventory()

actions = ['move', 'craft', 'rest', 'check inventory', 'pick up rocks', 'pick up sticks','pick up leaves', 'pick up coconuts','eat', 'quit']
errorMessage = 'Sorry, you can\'t do that right now'
regionsRocky = ['dunesa1', 'dunesa2', 'cratera3', 'dunesb1']
regionsSafe = ['centerb2']
regionsBeachy = ['beachb3', 'beachc1', 'beachc2', 'beachc3']
house = False

while True:
	
	print('You are at {}.'.format(location.currentRegion['name']))
	print(location.currentRegion['text'])
	
	if inventory.playerInventory['health'] <= 0:
		print('You died!')
		break
	else:
		print('Your health is ' + str(inventory.playerInventory['health']))
	if house == True:
		print('New crafting recipes learned!')
