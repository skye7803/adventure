
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
house = False

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
					inventory.playerInventory['health'] -= 2
				else:
					print("You can't go that way.")
			else:
				print("I don't understand that direction.")
		elif command.lower().strip() in ['eat']:
			if inventory.playerInventory['coconuts'] >= 1:
				inventory.playerInventory['coconuts'] -= 1
				inventory.playerInventory['health'] += 1
				print('Your health is ' + str(inventory.playerInventory['health']))
				print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
			else:
				print('You have no coconuts!')
		elif command.lower().strip() in ['craft', 'rest']:
			if location.currentRegion['id'] in regionsSafe:
				if command == 'rest':
					if inventory.playerInventory['health'] < 50:
						if house == False:
							if int(inventory.playerInventory['health']) < 20:
								inventory.playerInventory['health'] = 20
								print('Your health is: ' + str(inventory.playerInventory['health']))
							else:
								print('Already feeling well!')
						else:
							inventory.playerInventory['health'] = 50
							print('Your health is: ' + str(inventory.playerInventory['health']))
					else:
						print('Already feeling well!')
				else:
					print('What would you like to craft?')
					print('Stone cost: 5 rock --- crafting material')
					print('Wood cost: 5 sticks --- crafting material')
					print('String cost: 5 leaves --- crafting material')
					print('Coconut milk cost: 3 coconuts --- Heals 5 health')
					print('House cost: 20 wood, 20 stone, 20 string --- lets you rest up to 50 health')
					command = input().lower().strip()
					amount = input('How many?')
					if command in ['stone', 'wood', 'string', 'coconut milk']:
						if command in ['stone']:
							if inventory.playerInventory['rocks'] >= 5 * int(amount):
								inventory.playerInventory[str(command)] += 1 * int(amount)
								inventory.playerInventory['rocks'] -= 5 * int(amount)
						elif command in ['wood']:
							if inventory.playerInventory['sticks'] >= 5 * int(amount):
								inventory.playerInventory[str(command)] += 1 * int(amount)
								inventory.playerInventory['sticks'] -= 5 * int(amount)
						elif command in ['string']:
							if inventory.playerInventory['string'] >= 5 * int(amount):
								inventory.playerInventory[str(command)] += 1 * int(amount)
								inventory.playerInventory['string'] -= 5 * int(amount)
						elif command in ['coconut milk']:
							if inventory.playerInventory['coconuts'] >= 3 * int(amount):
								inventory.playerInventory[str(command)] += 1 * int(amount)
								inventory.playerInventory['coconuts'] -= 3 * int(amount)
						else:
							if inventory.playerInventory['wood'] >= 20 * int(amount) and inventory.playerInventory['stone'] >= 20 * int(amount) and inventory.playerInventory['string'] >= 20 * int(amount):
								inventory.playerInventory['wood'] -= 20
								inventory.playerInventory['stone'] -= 20
								inventory.playerInventory['string'] -=20
								house = True
					else:
						print(errorMessage)
			else:
				print(errorMessage)
		elif command.lower().strip() in ['pick up rocks', 'pick up sticks', 'pick up leaves', 'pick up coconuts']:
			if location.currentRegion['id'] in regionsRocky:
				if command.lower().strip() in ['pick up rocks']:
					inventory.playerInventory['rocks'] += 10
					inventory.playerInventory['health'] -= 2
					print('You have ' + str(inventory.playerInventory['rocks']) + ' rocks')
				else:
					print(errorMessage)
			elif location.currentRegion['id'] in regionsBeachy:
				if command.lower().strip() in ['pick up sticks']:
					inventory.playerInventory['sticks'] += 10
					inventory.playerInventory['health'] -= 2
					print('You have ' + str(inventory.playerInventory['sticks']) + ' sticks')
				elif command.lower().strip() in ['pick up leaves']:
					inventory.playerInventory['leaves'] += 10
					inventory.playerInventory['health'] -= 2
					print('You have ' + str(inventory.playerInventory['leaves']) + ' leaves')
				elif command.lower().strip() in ['pick up coconuts']:
					inventory.playerInventory['coconuts'] += 5
					inventory.playerInventory['health'] -= 2
					print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
				else:
					print(errorMessage)
			else:
				print(errorMessage)
		elif command.lower().strip() in ['check inventory']:
			inventory.print_inventory()
		else:
			break
	else:
		print('I don\'t understand')
