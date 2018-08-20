import random
import pprint

class Activities:
    actions = ['move', 'craft', 'rest', 'check inventory', 'pick up rocks', 'pick up sticks', 'pick up leaves',
               'pick up coconuts', 'eat', 'quit', 'mine stone', 'mine wood', 'deploy ladder']
    errorMessage = 'Sorry, you can\'t do that right now'
    regionsRocky = ['dunesa1', 'dunesa2', 'cratera3', 'dunesb1', 'cavea3II', 'cavea2II', 'caveb3II', 'cavea4II']
    regionsSafe = ['centerb2', 'mineb2II']
    regionsBeachy = ['beachb3', 'beachc1', 'beachc2', 'beachc3']
    regionsCave = ['cavea3II', 'cavea2II', 'caveb3II', 'caveb4II']
    regionsMineControlStation = ['mineb2II']

    def __init__(self):
        self.inventory_new_recipes = 'Checked'
        self.crater = True

    def print_basic_crafting_text(self):
        print('What would you like to craft?')
        print('Stone cost: 2 rock --- crafting material')
        print('Wood cost: 2 sticks --- crafting material')
        print('String cost: 2 leaves --- crafting material')
        print('Coconut milk cost: 3 coconuts --- Heals 5 health')

    def battle(self, enemy, enemy_name, attackA, attackB, ammo, inventory, location):
        """

        :type inventory: object
        """
        battle_loop = True
        self.health_storage = enemy['health']
        while battle_loop == True:
            print('You have been encountered by a ' + str(enemy_name))
            print('Your health is at: ' + str(inventory.playerInventory['health']))
            print('What do you do?')
            print('Fight')
            print('Run')
            print('Item')
            command = input().lower().strip()
            if command == 'fight':
                percent_hit = random.randint(1, 20)
                if inventory.weapon['type'] == 'melee':
                    if percent_hit not in enemy['armor']:
                        enemy['health'] -= inventory.weapon['damage']
                        print('You attack!')
                elif inventory.weapon['type'] == 'ranged':
                    if ammo > 0:
                        if percent_hit not in enemy['armor'] + [19, 20]:
                            enemy['health'] -= inventory.weapon['damage']
                            print('You attack!')
                        ammo -= 1
                    else:
                        print('No ammo!')
                enemy_attack = random.randint(1, 3)
                if location.current_region in Activities().regionsCave:
                    if enemy_attack in [1, 2]:
                        inventory.playerInventory['health'] -= enemy[attackA]
                    else:
                        inventory.playerInventory['health'] -= enemy[attackB]
                    print('Enemy attacks!')
                    if inventory.playerInventory['health'] <= 0:
                        break
                    if enemy['health'] <= 0:
                        print('You defeated ' + str(enemy['id']))
                        inventory.playerInventory['EXP'] += enemy['EXP']
                        print('You have ' + str(inventory.playerInventory['EXP']) + ' EXP!')
                        battle_loop = False
                else:
                    if enemy_attack == 1:
                        inventory.playerInventory['health'] -= enemy[attackA]
                    else:
                        inventory.playerInventory['health'] -= enemy[attackB]
                    print('Enemy attacks!')
                    if inventory.playerInventory['health'] <= 0:
                        break
                    if enemy['health'] <= 0:
                        print('You defeated ' + str(enemy['id']))
                        inventory.playerInventory['EXP'] += enemy['EXP']
                        print('You have ' + str(inventory.playerInventory['EXP']) + ' EXP!')
                        battle_loop = False
            elif command == 'run':
                run_chance = random.randint(1, 2)
                if run_chance == 1:
                    battle_loop = False
                    print('Got away safely!')
                else:
                    print('Can\'t escape!')
                    enemy_attack = random.randint(1, 3)
                    if enemy_attack == 1:
                        inventory.playerInventory['health'] -= enemy[attackA]
                    else:
                        inventory.playerInventory['health'] -= enemy[attackB]
                    if inventory.playerInventory['health'] <= 0:
                        break
            elif command == 'item':
                print('Which item would you like to use?')
                print(inventory.playerInventory['items'])
                command = input().lower().strip()
                if command == 'coconut milk':
                    if inventory.playerInventory['items']['coconut milk'] > 0:
                        inventory.playerInventory['health'] += 5
                        inventory.playerInventory['items']['coconut milk'] -= 1
                        enemy_attack = random.randint(1, 3)
                        if enemy_attack == 1:
                            inventory.playerInventory['health'] -= enemy[attackA]
                        else:
                            inventory.playerInventory['health'] -= enemy[attackB]
                        if inventory.playerInventory['health'] <= 0:
                            print('You died!')
                            break
                    else:
                        print('No coconut milk!')
                elif command == 'coconuts':
                    if inventory.playerInventory['items']['coconuts'] > 0:
                        inventory.playerInventory['health'] += 5
                        inventory.playerInventory['items']['coconuts'] -= 1
                        enemy_attack = random.randint(1, 3)
                        if enemy_attack == 1:
                            inventory.playerInventory['health'] -= enemy[attackA]
                        else:
                            inventory.playerInventory['health'] -= enemy[attackB]
                        if inventory.playerInventory['health'] <= 0:
                            print('You died!')
                            break
                    else:
                        print('No coconuts!')
                else:
                    print('I don\'t understand')
            else:
                print('I don\'t understand')
        enemy['health'] = self.health_storage

    def get_resources(self, resource, resource_amount, inventory):
        if resource in ['rocks', 'sticks', 'leaves', 'stone', 'wood']:
            inventory.playerInventory[resource] += resource_amount
            inventory.world_resources[resource] -= resource_amount
            print('You have', str(inventory.playerInventory[resource]), str(resource))
        elif resource in ['coconuts']:
            inventory.playerInventory['items'][resource] += resource_amount
            inventory.world_resources[resource] -= resource_amount
            print('You have', str(inventory.playerInventory['items'][resource]), str(resource))


    def basic_crafting(self, inventory, conv_factor, item_to_craft):

        num_to_craft = int(input('How many? ').lower().strip())

        raw_material = inventory.crafting[item_to_craft]

        if item_to_craft not in inventory.playerInventory['items']['itemsids']:
            if inventory.playerInventory[raw_material] >= conv_factor * num_to_craft:
                inventory.playerInventory[raw_material] -= conv_factor * num_to_craft
                inventory.playerInventory[item_to_craft] += num_to_craft
            else:
                print('Not enough resources!')
        elif item_to_craft in inventory.playerInventory['items']['itemsids']:
            if inventory.playerInventory['items'][raw_material] >= conv_factor * num_to_craft:
                inventory.playerInventory['items'][raw_material] -= conv_factor * num_to_craft
                inventory.playerInventory['items'][item_to_craft] += num_to_craft

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

    def process_activity_statement(self, location, inventory, enemies):
        self.command = input('What do you do? ').lower()

        if self.command in Activities().actions:
            if self.command == 'move':
                self.direction = input('Where do you go? ').lower()
                if self.direction in location.directions:
                    if self.direction in location.current_region.keys():
                        if location.current_region in Activities().regionsCave:
                            battle_odds = random.randint(1, 3)
                            if battle_odds in [1, 2]:
                                battle(enemies.rat, 'rat', 'scratch', 'bite', inventory.weapon['ammo'],
                                       inventory, location)
                        location.current_region = location.regions[location.current_region[self.direction]]
                    else:
                        print("You can't go that way.")
                else:
                    print("I don't understand that direction.")
            elif self.command in ['eat']:
                if inventory.playerInventory['items']['coconuts'] > 0:
                    print('Coconuts: heals 1 health')
                if inventory.playerInventory['items']['coconut milk'] > 0:
                    print('Coconut milk: heals 5 health')
                self.command = input('What would you like to eat?').lower().strip()
                if self.command == 'coconuts':
                    if inventory.playerInventory['items']['coconuts'] >= 1:
                        inventory.playerInventory['items']['coconuts'] -= 1
                        inventory.playerInventory['health'] += 1
                        print('You have ' + str(inventory.playerInventory['items']['coconuts']) + ' coconuts')
                elif self.command == 'coconut milk':
                    if inventory.playerInventory['items']['coconut milk'] >= 1:
                        inventory.playerInventory['items']['coconut milk'] -= 1
                        inventory.playerInventory['health'] += 5
                        print('You have ' + str(inventory.playerInventory['items']['coconut milk']) + ' coconut milks')
                elif self.command == 'exotic butters':
                    inventory.playerInventory['health'] = 99999999
                    inventory.weapon['damage'] = 99999999
                else:
                    print('I don\'t understand')
            elif self.command in ['craft', 'rest']:
                if location.current_region['id'] in Activities.regionsSafe:
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
                            self.print_basic_crafting_text()
                            print('House cost: 20 wood, 20 stone, 20 string --- lets you rest up to 50 health')
                            self.command = input().lower().strip()

                            if self.command in ['stone', 'wood', 'string']:
                                self.basic_crafting(inventory, 2, self.command)
                            elif self.command in ['coconut milk']:
                                self.basic_crafting(inventory, 3, self.command)
                            else:
                                self.advanced_crafting('stone', 'wood', 'string', 'rocks', 'sticks',
                                                       20, 20, 20, 0, 0, 'house', inventory)
                                self.inventory_new_recipes = 'Unchecked'
                                inventory.playerInventory['crafting_table'] = False
                        elif inventory.playerInventory['crafting_table'] == False:
                            self.inventory_new_recipes = 'checked'
                            self.print_basic_crafting_text()
                            print('Crafting Table cost: 25 wood, 25 stone, 10 string --- lets you craft more items')
                            self.command = input().lower().strip()
                            if self.command in ['stone', 'wood', 'string']:
                                self.basic_crafting(inventory, 2, self.command)
                            elif self.command in ['coconut milk']:
                                self.basic_crafting(inventory, 3, self.command)
                            elif self.command in ['crafting table']:
                                self.advanced_crafting('stone', 'wood', 'string', 'rocks', 'sticks',
                                                       25, 25, 10, 0, 0, 'crafting_table', inventory)
                                self.inventory_new_recipes = 'Unchecked'
                                inventory.playerInventory['simple_pickaxe'] = False
                                inventory.playerInventory['simple_axe'] = False
                                inventory.playerInventory['simple_sword'] = False
                                inventory.playerInventory['ladder'] = False
                            else:
                                print('Invalid input')
                        else:
                            self.inventory_new_recipes = 'checked'
                            self.print_basic_crafting_text()
                            print('Simple Pickaxe cost: 10 wood, 10 stone, 5 string --- allows for better item harvesting')
                            print('Simple Axe cost: 10 wood, 10 stone, 5 string --- allows for better item harvesting')
                            print('Simple Sword cost: 10 wood, 10 stone, 5 string --- deals 3 damage')
                            print('Ladder cost: 50 wood, 10 string --- lets you get to high - or low - places')
                            self.command = input().lower().strip()
                            if self.command in ['simple pickaxe']:
                                self.advanced_crafting('wood', 'stone', 'string', 'sticks', 'rocks',
                                                       10, 10, 5, 0, 0, 'simple_pickaxe', inventory)
                            elif self.command in ['simple axe']:
                                self.advanced_crafting('wood', 'stone', 'string', 'sticks', 'rocks',
                                                       10, 10, 5, 0, 0, 'simple_axe', inventory)
                            elif self.command in ['simple sword']:
                                self.advanced_crafting('wood', 'stone', 'string', 'sticks', 'rocks',
                                                       10, 10, 5, 0, 0, 'simple_sword', inventory)
                            elif self.command in ['ladder']:
                                self.advanced_crafting('wood', 'stone', 'string', 'sticks', 'rocks',
                                                       50, 0, 10, 0, 0, 'ladder', inventory)
                            elif self.command in ['stone', 'wood', 'string']:
                                self.basic_crafting(inventory, 2, self.command)
                            elif self.command in ['coconut milk']:
                                self.basic_crafting(inventory, 3, self.command)
                            else:
                                print('Invalid Input')
                else:
                    print(Activities.errorMessage)
            elif self.command in ['pick up rocks', 'pick up sticks', 'pick up leaves', 'pick up coconuts']:
                if location.current_region['id'] in Activities.regionsRocky:
                    if self.command in ['pick up rocks']:
                        battle_odds = random.randint(1, 3)
                        if battle_odds == 1:
                            self.battle(
                                enemies.rattlesnake, 'rattlesnake', 'bite', 'venom_bite', inventory.weapon['ammo'],
                                inventory, location)
                        self.get_resources('rocks', 10, inventory)
                    else:
                        print(Activities.errorMessage)
                elif location.current_region['id'] in Activities.regionsBeachy:
                    if self.command in ['pick up sticks']:
                        battle_odds = random.randint(1, 3)
                        if battle_odds == 1:
                            self.battle(
                                enemies.crab, 'crab', 'pinch', 'double_pinch', inventory.weapon['ammo'],
                                inventory, location)
                        self.get_resources('sticks', 10, inventory)
                    elif self.command in ['pick up leaves']:
                        battle_odds = random.randint(1, 3)
                        if battle_odds == 1:
                            self.battle(
                                enemies.crab, 'crab', 'pinch', 'double_pinch', inventory.weapon['ammo'],
                                inventory, location)
                        self.get_resources('leaves', 15, inventory)
                    elif self.command in ['pick up coconuts']:
                        battle_odds = random.randint(1, 3)
                        if battle_odds == 1:
                            self.battle(
                                enemies.crab, 'crab', 'pinch', 'double_pinch', inventory.weapon['ammo'],
                                inventory, location)
                        self.get_resources('coconuts', 5, inventory)
                    else:
                        print(Activities.errorMessage)
                else:
                    print(Activities.errorMessage)
            elif self.command in ['mine stone', 'mine wood']:
                if 'simple_pickaxe' in inventory.playerInventory.keys():
                    if inventory.playerInventory['simple_pickaxe']:
                        if location.current_region['id'] in Activities().regionsRocky:
                            if self.command in ['mine stone']:
                                battle_odds = random.randint(1, 3)
                                if battle_odds == 1:
                                    self.battle(
                                        enemies.rattlesnake, 'rattlesnake', 'bite', 'venom_bite', inventory.weapon['ammo'],
                                        inventory, location)
                                self.get_resources('stone', 10, inventory)
                            else:
                                print(Activities.errorMessage)
                if 'simple_axe' in inventory.playerInventory.keys():
                    if inventory.playerInventory['simple_axe']:
                        if location.current_region['id'] in Activities().regionsBeachy:
                            if self.command in ['mine wood']:
                                battle_odds = random.randint(1, 3)
                                if battle_odds == 1:
                                    self.battle(
                                        enemies.crab, 'crab', 'pinch', 'double_pinch', inventory.weapon['ammo'],
                                        inventory, location)
                                self.get_resources('wood', 10, inventory)
                            else:
                                print(Activities.errorMessage)
                    else:
                        print(Activities.errorMessage)
            elif self.command in ['check inventory']:
                print('Your inventory is:')
                inventory.print_inventory()
                print('Your current weapon is:')
                print(inventory.weapon)
                self.command = input('Would you like to change weapons?').lower().strip()
                if self.command == 'yes':
                    print('Fists --- Melee weapon --- 1 damage')
                    if inventory.playerInventory['rocks'] > 0:
                        print('Rocks --- ranged item --- 2 damage')
                    if 'simple_sword' in inventory.playerInventory.keys():
                        if inventory.playerInventory['simple_sword']:
                            print('Simple sword --- Melee weapon --- 3 damage')
                    self.command = input('What would you like to switch to?').lower().strip()
                    if self.command == 'fists':
                        inventory.weapon['name'] = 'fists'
                        inventory.weapon['damage'] = 1
                        inventory.weapon['type'] = 'melee'
                        inventory.weapon['ammo'] = 'none'
                    elif self.command == 'rocks':
                        inventory.weapon['name'] = 'rocks'
                        inventory.weapon['damage'] = 2
                        inventory.weapon['type'] = 'ranged'
                        inventory.weapon['ammo'] = inventory.playerInventory['rocks']
                    elif 'simple_sword' in inventory.playerInventory.keys():
                        if inventory.playerInventory['simple_sword']:
                            if self.command == 'simple sword':
                                inventory.weapon['name'] = 'simple_sword'
                                inventory.weapon['damage'] = 3
                                inventory.weapon['type'] = 'melee'
                                inventory.weapon['ammo'] = 'none'
                    else:
                        print('I don\'t understand that command')
                elif self.command != 'no':
                    print('I don\'t undersand that command')
            elif self.command in ['deploy ladder']:
                if 'ladder' in inventory.playerInventory.keys():
                    if inventory.playerInventory['ladder']:
                        self.crater = False
            else:
                # TODO what happens here?  break only works in a loop...
                print('what?')
        # break
        else:
            print('I don\'t understand')
