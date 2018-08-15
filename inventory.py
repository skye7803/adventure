from pprint import pprint

class Inventory:

    def __init__(self):
        self.house = False
        self.rocks = 200
        self.stone = 0
        self.sticks = 200
        self.wood = 0
        self.leaves = 0
    
    def drop(self, amount: int, material: str):
        """Drop some stuff

        Args:
            amount: Amount to drop
            material: Type of material to drop

        Returns:
            The message to show the user

        """
        if (material == 'rocks'):
            self.rocks -= amount
            return "Dropped {} rocks.".format(amount)
        elif (material == 'sticks'):
            self.sticks -= amount
            return "Dropped {} sticks.".format(amount)

        # TODO add the other materials
        # TODO check amount before dropping and return different message if user doesn't have enough to drop
        else:
            return "Don't know how to drop {} {}!".format(amount, material)

    # TODO add "pickup" function

    # TODO finish the following function, which will allow print(myInventory) to work
    def __str__(self):
        return str("""
You are carrying...
  stone:  {}
  sticks: {}
  rocks:  {}
  house:  {}
        """).format(self.stone, self.sticks, self.rocks, self.house)

''' Example Usage '''
# create a new inventory object
myInventory = Inventory()

# print amounts of current inventory for some materials
print('''
--------------------------------------------------
Starting Inventory:
''')
print('stone: ' + str(myInventory.stone))
print('sticks: ' + str(myInventory.sticks))
print('house: ' + str(myInventory.house))
print('rocks: ' + str(myInventory.rocks))
print('-' * 50)

# drop some rocks
print(myInventory.drop(25, 'rocks'))
print('rocks: ' + str(myInventory.rocks))
print('-' * 50)

# drop some unknown material
print(myInventory.drop(25, 'monkies'))

# show current inventory again (different way...)
print('-' * 50)
print("""
Current Inventory
stone:  {}
sticks: {}
rocks:  {}
house:  {}
""".format(myInventory.stone, myInventory.sticks, myInventory.rocks, myInventory.house))
print('-' * 50)

print(myInventory)