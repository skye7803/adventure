from pprint import pprint
from location import Location
from activities import Activities
from inventory import Inventory
from enemies import Enemies

location = Location()

activities = Activities()

inventory = Inventory()

enemies = Enemies()

crater = True

while True:

    print('You are at {}.'.format(location.currentRegion['name']))
    print(location.currentRegion['text'])

    if inventory.playerInventory['health'] <= 0:
        print('You died!')
        break
    else:
        print('Your health is ' + str(inventory.playerInventory['health']))

    if inventory.playerInventory['house']:
        if activities.inventory_new_recipes == 'Unchecked':
            print('New crafting recipes learned!')

    if crater == True:
        if location.currentRegion == location.regions['cratera3']:
            print('The ground begins to crumble underneath you!')
            print('You fall and black out!')
            inventory.playerInventory['health'] /= 2
            location.currentRegion = location.regions['cavea3II']

    if inventory.playerInventory['house']:
        if inventory.playerInventory['crafting_table']:
            if inventory.playerInventory['simple_sword'] == True:
                inventory.weapon['name'] = 'simple_sword'
                inventory.weapon['attack'] = 3

    activities.process_activity_statement(location, inventory, enemies)
