#Imports
import sys
import time
#Functions
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1) #change this to change speed
    print(' ') #dont touch this
#Dictionarys
weapon = {
    'Dagger': 2,
    'Short Sword': 5,
    'Glock': 999
}
monster = {
    'Goblin': 10,
    'Orc': 25,
    'Dragon': 100
}
location = ['Home', 'Town', 'Castle', 'Dungeon']
choices = []
backpack = []
player = 50

slow_print('You wake up')
slow_print("You're at home. but which home?")
slow_print("There's a Dagger on your bedside table.")
choice =input('''Grab it?
1. Yes
2. No
>>>''')
if choice == '1':
    backpack.append('Dagger')
    slow_print('You Grab the Dagger and put it in your pack')
elif choice == '2':
    print('')
elif choice == '3':
    slow_print('Investigating the room, you find a closet with a Glock!')
    backpack.append('Glock')
else:
    slow_print('Goodjob, Dumbass. Restart!')
choices.append(choice)
slow_print('Leaving the house, you see town in the distance, with a Castle behind it.')
slow_print('Heading into town, you see a horde of goblins leaving town, and the remaining townsfolk gaurded by a single remaining goblin.')
