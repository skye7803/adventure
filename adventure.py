from pprint import pprint
from location import Location
from activities import Activities
from inventory import Inventory
from enemies import Enemies


activities = Activities()

inventory = Inventory()

location = Location()

enemies = Enemies()

while True:

    print('You are at ' + location.get_current_region_text(inventory, activities))

    if inventory.playerInventory['health'] <= 0:
        print('You died!')
        print('You had ' + str(inventory.playerInventory['EXP']) + ' EXP!')
    else:
        print('Your health is ' + str(inventory.playerInventory['health']))

    if inventory.playerInventory['house']:
        if activities.inventory_new_recipes == 'Unchecked':
            print('New crafting recipes learned!')

    if activities.crater == False:
        if location.current_region == location.regions['cratera3']:
            print('The ground begins to crumble underneath you!')
            print('You fall and black out!')
            inventory.playerInventory['health'] //= 2
            location.current_region = location.regions['cavea3II']
            cave()

    activities.process_activity_statement(location, inventory, enemies)
