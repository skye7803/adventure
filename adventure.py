
# house = False
# health = 50
# rocks = 200
# stone = 0
# sticks = 200
# wood = 0
# leaves = 0
# loop = True
# location = str()
# activity = str()
# prompt = "Enter command:"


#from .adventure_activity import activities
#from adventure_location import Location

#def dunes():
	#print("You find yourself on dunes next to the ocean. What do you do?")
	#activityRocky()

#def crater():
	#print("You find a small crater filled with surging water. As you get a closer look, you see tide pools teeming with wildlife. What do you do?")
	#activityRocky()

#def center():
	#print("You are back to the center of the island. You may build and craft items here, or rest.")
	#activityCenter()

#def beach():
	#activityBeach()
	#print("You burst through the trees and are blinded by the blaring sun. Your eyes adjust and you see yourself on a flat beach lottered with coconuts. You look up and see seagulls soaring above giant palm trees stretching near thr clouds. What do you do?")

# def myInput(userPrompt):
# 	return input(userPrompt).lower()

# def start():
	
#	print("You wake in a small woods with a map. To where do you head?")
#	print("A1")
#	print("A2")
#	print("A3")
#	print("B1")
#	print("B3")
#	print("C1")
#	print("C2")
#	print("C3")
	
#	desiredLocation = myInput(prompt)

#	location = Location()

#	print(location.move(desiredLocation))

# start()
from pprint import pprint

beachText = 'This is a pleasant beach with palm trees. You may check inventory, eat, pick up sticks, leaves, coconuts, or move'
dunesText = 'This is a hill filled area with lots of sand. You may check inventory, eat, pick up rocks or move'
craterText = 'This is a huge crater in the ground. You may check inventory, eat, pick up rocks or move'
centerText = 'These are the woods in which you woke up in. You may check inventory, eat, craft, rest, or move.'


regions = {
	'dunesa1': {
		'id': 'dunesa1',
		'name': 'a dune filled region',
		'text': dunesText,
		'east': 'dunesa2',
		'south': 'beachb1',
	},
	'dunesa2': {
		'id': 'dunesa2',
		'name': 'a dune filled region',
		'text': dunesText,
		'east': 'cratera3', 
		'south': 'centerb2', 
		'west': 'dunesa1',
	},
	'cratera3': {
		'id': 'cratera3',
		'name': 'a big crater', 
        'text': craterText,
		'south': 'beachb3', 
		'west': 'dunesa2',
	},
	'dunesb1': {
		'id': 'dunesb1',
		'name': 'a dune filled region', 
        'text': dunesText,             
		'north': 'dunesa1', 
		'east': 'centerb2', 
		'south': 'beachc1',
	},
	'centerb2': {
		'id': 'centerb2',
		'name': 'the center of the island', 
		'text':centerText,
		'north': 'dunesa2', 
		'east': 'beachb3', 
		'south': 'beachc2', 
		'west': 'beachb1',
		},
    'beachb3': {
		'id': 'beachb3',
		'name': 'a beachy region', 
		'text': beachText,
		'north': 'cratera3', 
		'south': 'beachc3', 
		'west': 'centerb2',
        },
	'beachc1': {
		'id': 'beachc1',
		'name': 'a beachy region', 
		'text': beachText,
		'north': 'dunesb1', 
		'east': 'beachc2',
        },
	'beachc2': {
		'id': 'beachc2',
		'name': 'a beachy region', 
		'text': beachText,
		'north': 'centerb2', 
		'east': 'beachc3', 
		'west': 'beachc1',                   
		},
	'beachc3': {
		'id': 'beachc3',
		'name': 'a beachy region', 
		'text': beachText,
		'north': 'beachb3', 
		'west': 'beachc2',
		},
}

actions = ['move', 'craft', 'rest', 'check inventory', 'pick up rocks', 'pick up sticks','pick up leaves', 'pick up coconuts','eat', 'quit']
directions = ['north', 'south', 'east', 'west']
currentRegion = regions['centerb2']
errorMessage = 'Sorry, you can\'t do that right now'
regionsRocky = ['dunesa1', 'dunesa2', 'cratera3', 'dunesb1']
regionsSafe = ['centerb2']
regionsBeachy = ['beachb3', 'beachc1', 'beachc2', 'beachc3']
startTextVar = True
health = 50
sticks = 0
rocks = 0
leaves = 0
coconuts = 0
wood = 0
stone = 0
string = 0

while True:
	print('You are in {}.'.format(currentRegion['name']))
	print(currentRegion['text'])
	if health <= 0:
		print('You died!')
		break
	else:
		print('Your health is ' + str(health))
	command = input('What do you do?').lower()
	if command.lower().strip() in actions:
		if command.lower().strip() == 'move':
			direction = input('Where do you go?').lower()
			if direction in directions:
				if direction in currentRegion:
					currentRegion = regions[currentRegion[direction]]
					health -= 5
				else:
					print("You can't go that way.")
			else:
				print("I don't understand that direction.")
		elif command.lower().strip() in ['eat']:
			if coconuts > 0:
				coconuts -= 1
				health += 2
				print('Your health is ' + str(health))
				print('You have ' + str(coconuts) + ' coconuts')
			else:
				print('You have no coconuts!')
		elif command.lower().strip() in ['craft', 'rest']:
			if currentRegion['id'] in regionsSafe:
				if command == 'rest':
					health = 50
					print('Your health is: ' + str(health))
				else:
					print('Error: Game unfinished')
			else:
				print(errorMessage)
		elif command.lower().strip() in ['pick up rocks', 'pick up sticks', 'pick up leaves', 'pick up coconuts']:
			if currentRegion['id'] in regionsRocky:
				if command.lower().strip() in ['pick up rocks']:
					rocks += 10
					print('You have ' + str(rocks) + ' rocks')
				else:
					print(errorMessage)
			elif currentRegion['id'] in regionsBeachy:
				if command.lower().strip() in ['pick up sticks']:
					sticks += 10
					print('You have ' + str(sticks) + ' sticks')
				elif command.lower().strip() in ['pick up leaves']:
					leaves += 10
					print('You have ' + str(leaves) + ' leaves')
				elif command.lower().strip() in ['pick up coconuts']:
					coconuts += 5
					print('You have ' + str(coconuts) + ' coconuts')
				else:
					print(errorMessage)
			else:
				print(errorMessage)
		else:
			break
	else:
		print('I don\'t understand')
