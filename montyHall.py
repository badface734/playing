import math, random

def montyHall(yn):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    doorsdict = {i: doors[i] for i in range(3)}
    c = random.randint(0,2)
    choice = c+1

    for i in range(3):
        # x = val.index('goat')
        if i != c and doorsdict[i] == 'goat':
            x = i

    if yn == 'y':
        for i in doorsdict:
            if i != x or c:
                c = i

    return doorsdict[c]
#
# # create dictionary of door numbers(KEYS) and prizes(items) in random order
# doors = ['car','goat','goat']
# random.shuffle(doors)
# doorsdict= { i : doors[i] for i in range(3) }
#
# #explain game, ask for guess and validate input
# print(doorsdict)
# print('there are 3 doors, behind 2 of the doors are goats but behind the other door is a brand new car!\n' )
# while True:
#     try:
#         choice = int(input('please pick either door 1 2 or 3'))
#     except ValueError:
#         print('I dont think thats a number, try again')
#         continue
#     if 1<= choice <=3 :
#         break
#     else:
#         continue
#
# c = choice-1 # list items start at 0 so subtracting one from the players choice for the program logic
#
# # assign a 'goat' key that is not the players choice to the variable 'x'
# for i in range(3):
#     # x = val.index('goat')
#     if i != c and doorsdict[i] =='goat':
#             x = i
#
# px = x+1 #list items start at 0 so adding one to the variable for displaying it to the user
#
# #tell player which other door has a goat and ask if they want to change
# print('you chose door ('+ str(choice ) + ') I cant tell you if there is a car or a goat behind that door\n'
#                                         ' but I can tell you that there is a goat behind door (' +
#       str(px) + ')\nnow that we are down to two possible doors, would you like to keep your first choice \nor change '
#                  'your choice to the other door? (y) to change (n) to keep first choice')
# #validate input
# while True:
#     yn = input('(y)/(n)').lower()
#     if yn == 'y':
#         break
#     if yn == 'n':
#         break
#
# #change player choice to the other door by changing it to the dict key that is not the current choice or the  goat revealed door
# if yn == 'y':
#     for i in doorsdict:
#         if i != x or c:
#             c = i
#
# #print if they have won or not
# if doorsdict[c] == 'car':
#     print('congratulations, you won a brand new car!')
# if doorsdict[c] == 'goat':
#     print('sorry to say you got yourself a goat there bud.')
#
