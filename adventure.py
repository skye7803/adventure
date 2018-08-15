
from pprint import pprint
from adventure_location import Location
from adventure_player_inventory import Inventory

location = Location()

inventory = Inventory()

actions = ['move', 'craft', 'rest', 'check inventory', 'pick up rocks', 'pick up sticks','pick up leaves', 'pick up coconuts','eat', 'quit']
errorMessage = 'Sorry, you can\'t do that right now'
regionsRocky = ['dunesa1', 'dunesa2', 'cratera3', 'dunesb1']
regionsSafe = ['centerb2']
regionsBeachy = ['beachb3', 'beachc1', 'beachc2', 'beachc3']

while True:
	print('You are at {}.'.format(location.currentRegion['name']))
	print(location.currentRegion['text'])
	if inventory.playerInventory['health'] <= 0:
		print('You died!')
		break
	else:
		print('Your health is ' + str(inventory.playerInventory['health']))
	command = input('What do you do?').lower()
	if command.lower().strip() in actions:
		if command.lower().strip() == 'move':
			direction = input('Where do you go?').lower()
			if direction in location.directions:
				if direction in location.currentRegion.keys():
					location.currentRegion = location.regions[location.currentRegion[direction]]
					inventory.playerInventory['health'] -= 5
				else:
					print("You can't go that way.")
			else:
				print("I don't understand that direction.")
		elif command.lower().strip() in ['eat']:
			if inventory.playerInventory['coconuts'] >= 1:
				inventory.playerInventory['coconuts'] -= 1
				inventory.playerInventory['health'] += 2
				print('Your health is ' + str(inventory.playerInventory['health']))
				print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
			else:
				print('You have no coconuts!')
		elif command.lower().strip() in ['craft', 'rest']:
			if currentRegion['id'] in regionsSafe:
				if command == 'rest':
					if int(inventory.playerInventory['health']) < 50:
						health = 50
						print('Your health is: ' + str(health))
					else:
						print('Already feeling well!')
				else:
					print('Error: Game unfinished')
			else:
				print(errorMessage)
		elif command.lower().strip() in ['pick up rocks', 'pick up sticks', 'pick up leaves', 'pick up coconuts']:
			if currentRegion['id'] in regionsRocky:
				if command.lower().strip() in ['pick up rocks']:
					inventory.playerInventory['rocks'] += 10
					print('You have ' + str(inventory.playerInventory['rocks']) + ' rocks')
				else:
					print(errorMessage)
			elif currentRegion['id'] in regionsBeachy:
				if command.lower().strip() in ['pick up sticks']:
					inventory.playerInventory['sticks'] += 10
					print('You have ' + str(inventory.playerInventory['sticks']) + ' sticks')
				elif command.lower().strip() in ['pick up leaves']:
					inventory.playerInventory['leaves'] += 10
					print('You have ' + str(inventory.playerInventory['leaves']) + ' leaves')
				elif command.lower().strip() in ['pick up coconuts']:
					inventory.playerInventory['coconuts'] += 5
					print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
				else:
					print(errorMessage)
			else:
				print(errorMessage)
		elif command.lower().strip() in ['check inventory']:
			print('You have:')
			print
		else:
			break
	else:
		print('I don\'t understand')
