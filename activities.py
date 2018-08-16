from location import Location
from inventory import Inventory


class Activities:
    actions = ['move', 'craft', 'rest', 'check inventory', 'pick up rocks', 'pick up sticks', 'pick up leaves',
               'pick up coconuts', 'eat', 'quit']
    errorMessage = 'Sorry, you can\'t do that right now'
    regionsRocky = ['dunesa1', 'dunesa2', 'cratera3', 'dunesb1', 'cavea3II', 'cavea2II', 'caveb3II', 'cavea4II']
    regionsSafe = ['centerb2', 'mineb2II']
    regionsBeachy = ['beachb3', 'beachc1', 'beachc2', 'beachc3']

    ###

    inventoryAfterHouse = 'Unchecked'

    ###

    def basic_crafting(self, inventory, conv_factor, item_to_craft):

        num_to_craft = int(input('How many? ').lower().strip())

        raw_material = inventory.crafting[item_to_craft]

        if inventory.playerInventory[raw_material] >= conv_factor * num_to_craft:
            inventory.playerInventory[raw_material] -= conv_factor * num_to_craft
            inventory.playerInventory[item_to_craft] += num_to_craft
        else:
            print('Not enough resources!')

    def advanced_crafting(self, raw_materialA, raw_materialB, raw_materialC, raw_materialD, raw_materialE, costA, costB, costC,
                          costD, costE, item_to_craft, inventory):
        if inventory.playerInventory[raw_materialA] >= costA and \
                inventory.playerInventory[raw_materialB] >= costB and \
                inventory.playerInventory[raw_materialC] >= costC and \
                inventory.playerInventory[raw_materialD] >= costD and \
                inventory.playerInventory[raw_materialE] >= costE:
            inventory.playerInventory[raw_materialA] -= costA
            inventory.playerInventory[raw_materialB] -= costB
            inventory.playerInventory[raw_materialC] -= costC
            inventory.playerInventory[raw_materialD] -= costD
            inventory.playerInventory[raw_materialE] -= costE
            inventory.playerInventory[item_to_craft] = True
        else:
            print('Not enough resources')

    def process_activity_statement(self, location, inventory):
        self.command = input('What do you do? ').lower()

        if self.command in Activities.actions:
            if self.command == 'move':
                self.direction = input('Where do you go? ').lower()
                if self.direction in location.directions:
                    if self.direction in location.currentRegion.keys():
                        location.currentRegion = location.regions[location.currentRegion[self.direction]]
                        inventory.playerInventory['health'] -= 2
                    else:
                        print("You can't go that way.")
                else:
                    print("I don't understand that direction.")
            elif self.command in ['eat']:
                if inventory.playerInventory['coconuts'] >= 1:
                    inventory.playerInventory['coconuts'] -= 1
                    inventory.playerInventory['health'] += 1
                    print('Your health is ' + str(inventory.playerInventory['health']))
                    print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
                else:
                    print('You have no coconuts!')
            elif self.command in ['craft', 'rest']:

                #WHY ISNT THIS WORKING?!?!?!?!?

                global inventoryAfterHouse
                inventoryAfterHouse = 'checked'

                ###

                if location.currentRegion['id'] in Activities.regionsSafe:
                    if self.command == 'rest':
                        if inventory.playerInventory['health'] < 50:
                            if inventory.playerInventory['house'] == False:
                                if int(inventory.playerInventory['health']) < 20:
                                    inventory.playerInventory['health'] = 20
                                else:
                                    print('Already feeling well!')
                            else:
                                inventory.playerInventory['health'] = 50
                        else:
                            print('Already feeling well!')
                    else:
                        if inventory.playerInventory['house'] == False:
                            print('What would you like to craft?')
                            print('Stone cost: 2 rock --- crafting material')
                            print('Wood cost: 2 sticks --- crafting material')
                            print('String cost: 2 leaves --- crafting material')
                            print('Coconut milk cost: 3 coconuts --- Heals 5 health')
                            print('House cost: 20 wood, 20 stone, 20 string --- lets you rest up to 50 health')
                            self.command = input().lower().strip()

                            if self.command in ['stone', 'wood', 'string']:
                                self.basic_crafting(inventory, 2, self.command)
                            elif self.command in ['coconut milk']:
                                self.basic_crafting(inventory, 3, self.command)
                            else:
                                self.advanced_crafting('stone', 'wood', 'string', 'rocks', 'sticks',
                                                       20, 20, 20, 0, 0, 'house', inventory)
                        else:
                            print('What would you like to craft?')
                            print('Stone cost: 5 rock --- crafting material')
                            print('Wood cost: 5 sticks --- crafting material')
                            print('String cost: 5 leaves --- crafting material')
                            print('Coconut milk cost: 3 coconuts --- Heals 5 health')
                            print('Crafting Table cost: 25 wood, 25 stone, 10 string --- lets you craft more items')
                            self.command = input().lower().strip()
                            if self.command in ['stone', 'wood', 'string', 'coconut milk']:
                                if self.command in ['stone']:
                                    amount = input('How many? ')
                                    if inventory.playerInventory['rocks'] >= 2 * int(amount):
                                        inventory.playerInventory[str(self.command)] += 1 * int(amount)
                                        inventory.playerInventory['rocks'] -= 2 * int(amount)
                                elif self.command in ['wood']:
                                    amount = input('How many? ')
                                    if inventory.playerInventory['sticks'] >= 2 * int(amount):
                                        inventory.playerInventory[str(self.command)] += 1 * int(amount)
                                        inventory.playerInventory['sticks'] -= 2 * int(amount)
                                elif self.command in ['string']:
                                    amount = input('How many? ')
                                    if inventory.playerInventory['leaves'] >= 2 * int(amount):
                                        inventory.playerInventory[str(self.command)] += 1 * int(amount)
                                        inventory.playerInventory['leaves'] -= 2 * int(amount)
                                elif self.command in ['coconut milk']:
                                    amount = input('How many? ')
                                    if inventory.playerInventory['coconuts'] >= 3 * int(amount):
                                        inventory.playerInventory[str(self.command)] += 1 * int(amount)
                                        inventory.playerInventory['coconuts'] -= 3 * int(amount)
                                else:
                                    if inventory.playerInventory['wood'] >= 25 and inventory.playerInventory[
                                        'stone'] >= 20 and inventory.playerInventory['string'] >= 20:
                                        inventory.playerInventory['wood'] -= 25
                                        inventory.playerInventory['stone'] -= 25
                                        inventory.playerInventory['string'] -= 10
                                        inventory.playerInventory['craftingTable'] = True

                else:
                    print(Activities.errorMessage)
            elif self.command in ['pick up rocks', 'pick up sticks', 'pick up leaves', 'pick up coconuts']:
                if location.currentRegion['id'] in Activities.regionsRocky:
                    if self.command in ['pick up rocks']:
                        inventory.playerInventory['rocks'] += 10
                        inventory.playerInventory['health'] -= 1
                        print('You have ' + str(inventory.playerInventory['rocks']) + ' rocks')
                    else:
                        print(Activities.errorMessage)
                elif location.currentRegion['id'] in Activities.regionsBeachy:
                    if self.command in ['pick up sticks']:
                        inventory.playerInventory['sticks'] += 10
                        inventory.playerInventory['health'] -= 1
                        print('You have ' + str(inventory.playerInventory['sticks']) + ' sticks')
                    elif self.command in ['pick up leaves']:
                        inventory.playerInventory['leaves'] += 10
                        inventory.playerInventory['health'] -= 1
                        print('You have ' + str(inventory.playerInventory['leaves']) + ' leaves')
                    elif self.command in ['pick up coconuts']:
                        inventory.playerInventory['coconuts'] += 5
                        inventory.playerInventory['health'] -= 1
                        print('You have ' + str(inventory.playerInventory['coconuts']) + ' coconuts')
                    else:
                        print(Activities.errorMessage)
                else:
                    print(Activities.errorMessage)
            elif self.command in ['check inventory']:
                inventory.print_inventory()
            else:
                # TODO what happens here?  break only works in a loop...
                print('what?')
        # break
        else:
            print('I don\'t understand')
