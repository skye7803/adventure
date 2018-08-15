    
# class activities:   
#     def activityRocky():
#         while loop == True:
#             print("Pick up rocks, check inventory, or move?")
#             activityRocky = myInput(prompt)
#             if activityRocky == str("Pick up rocks"):
#                 global rocks
#                 rocks += 10
#                 print("You have", rocks, "rocks")
#             elif activityRocky == str("move"):
#                 locationCheck()
#             elif activityRocky == str("check inventory"):
#                 print("You have:")
#                 print(rocks, "rocks")
#                 print(sticks, "sticks")
#                 print(stone, "stone")
#                 print(wood, "wood")
#             else:
#                 print("invalid input")

#     def activityCenter():
#         while loop == True:
#             print("build, rest, check inventory, or move?")
#             activityCenter = myInput(prompt)
#             if activityCenter == str("build"):
#                 print("You can build")
#                 print("Stone", "Cost: 5 Rock")
#                 print("Wood", "Cost: 5 Sticks")
#                 print("House", "Cost: 100 Stone, 100 Wood")
#                 print("Type 'back' to go back")
#                 item = myInput(prompt)
                
#                 global stone
#                 global wood
#                 global house

#                 if item == str("stone"):
#                     global rocks
#                     if rocks - 5 > 0:
#                         stone += 1
#                         rocks -= 5
#                         print(("You have", stone, "stone"))
#                     else:
#                         print("Not enough resources!")
#                 elif item == str("wood"):
#                     global sticks
#                     if sticks - 5 > 0:
#                         wood += 1
#                         sticks -= 5
#                         print("You have", wood, "wood")
#                     else:
#                         print("Not enough resources!")
#                 elif item == str("house"):
#                     if stone - 100 > 0:
#                         if wood - 100 > 0:
#                             stone -= 100
#                             wood -= 100
#                             house = True
#                         else:
#                             print("Not enough resources!")
#                     else:
#                         print("Not enough resources!")
#                 else:
#                     print("Invalid Input!")

#             elif activityCenter == str("rest"):
#                 if house == True:
#                     global health
#                     health += 20
#                 else:
#                     health += 10
#             elif activityCenter == str("back"):
#                 print()
#             elif activityCenter == str("move"):
#                 locationCheck()
#             elif activityCenter == str("check inventory"):
#                 print("You have:")
#                 print(rocks, "rocks")
#                 print(sticks, "sticks")
#                 print(stone, "stone")
#                 print(wood, "wood")
#             else:
#                 print("Invalid input")

#     def activityBeach():
#         while loop == True:
#             print("Pick up sticks, check inventory, or move?")
#             activityBeach = myInput(prompt)
#             global sticks
#             if activityBeach == str("Pick up sticks"):
#                 sticks += 10
#                 print("You have", sticks, "sticks")
#             elif activityBeach == str("move"):
#                 locationCheck()
#             elif activityBeach == str("check inventory"):
#                 print("You have:")
#                 print(rocks, "rocks")
#                 print(sticks, "sticks")
#                 print(stone, "stone")
#                 print(wood, "wood")
#             else:
#                 print("invalid input")