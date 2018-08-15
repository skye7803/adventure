
# locationPrompt = str("Where would you like to go?")

# def myInput(userPrompt):
# 	return input(userPrompt).lower()

# class Location:

#     def __init__(self):
#         self.location = "b2"

#     def __str__(self):
#         return self.location

#     def updateLocation(self, desiredLocation: str):
#         self.location = desiredLocation
#         return("You are at " + str(self.location))
    
#     def move(self, desiredLocation: str):
#         '''How the player moves
        
#         Args: 
#             desiredLocation: Where the player is going
        
#         Returns:
#             Text to show the player
#         '''
#         self.desiredLocation = myInput(locationPrompt)
        
#         self.updateLocation()
        
        # if desiredLocation == "a1":
        #     print(self.updateLocation())
        #     #dunes()
        # elif desiredLocation == "a2":
        #     print(self.updateLocation())
        #     #dunes()
        # elif desiredLocation == "a3":
        #     print(self.updateLocation())
        #     #dunes()
        # elif desiredLocation == "b1":
        #     print(self.updateLocation())
        #     #beach()
        # elif desiredLocation == "b2":
        #     print(self.updateLocation())
        #     #center()
        # elif desiredLocation == "b3":
        #     print(self.updateLocation())
        #     #crater()
        # elif desiredLocation == "c1":
        #     print(self.updateLocation())
        #     #beach()
        # elif desiredLocation == "c2":
        #     print(self.updateLocation())
        #     #beach()
        # elif desiredLocation == "c3":
        #     print(self.updateLocation())
        #     #beach()
        # else:
        #     print("Invalid Input")

    # rooms = {'empty': {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple', 'contents': [],
    #     'text': 'The stone floors and walls are cold and damp.'},
    # 'temple': {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
    #     'text': 'This seems to be a place of worship and deep contemplation.', 
    #     'contents': ['bench', 'bench', 'bench', 'statue']},
    # 'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom', 'contents': ['chains', 'thumbscrews'],
    #     'text': 'There is a rack and an iron maiden against the wall\naand some dark stains on the floor.'},
    # 'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty', 'contents': ['sheets', 'bed'],
    #     'text': 'This is clearly a bedroom, but no one has slept\nhere in a long time.'}}
    # directions = ['north', 'south', 'east', 'west']
    # current_room = rooms['empty']
    # carrying = []
             