#Imports
import sys
import time
import random
#Functions
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1) #change this to change speed
    print(' ') #dont touch this
    
def combat(player,weapn, battle,):
    if battle == 1:#Goblin Fight
        attack = 'Dagger'
        damage = weapon['Dagger']
        health = player
        hp = monster['Goblin']
        while health >= 1 and hp >= 1:
            if hp >= 1:
                slow_print (f"You have {health} health")
                choice = input("""What Do You Do?
1. Attack
2. Run Away
>>> """)
                if choice == '1':
                    slow_print (f"You Swing with your {attack}!")
                    hp -= damage
                    slow_print ("The Goblin Attacks!")
                    slow_print ("You lose 3 Health.")
                    health -= 3
                elif choice == '2':
                    found = random.randint(1, 5)
                    if found <= 3:
                        slow_print ("You Couldn't escape!")
                        slow_print ("The Goblin Attacks!")
                        slow_print ("You lose 5 Health.")
                        health -= 5
                    elif found >= 4:
                        slow_print ('You flee from the mighty monster. No one balmes you, but you failed')
                        print('Game Over')
                if hp <= 0:
                    slow_print (f"The Goblin Died!")
                if health <= 0:
                    slow_print ('You Died')
                    print ('Game Over')
                    quit()
    if battle == 2:#Orc Fight
        attack = 'Short Sword'
        damage = weapon['Short Sword']
        health = player
        hp = monster['Orc']
        while health >= 1 and hp >= 1:
            if hp >= 1:
                slow_print (f"You have {health} health")
                choice = input("""What Do You Do?
1. Attack
2. Run Away
>>> """)
                if choice == '1':
                    slow_print (f"You Swing with your {attack}!")
                    hp -= damage
                    slow_print ("The Orc Attacks!")
                    slow_print ("You lose 5 Health.")
                    health -= 5
                elif choice == '2':
                    found = random.randint(1, 5)
                    if found <= 3:
                        slow_print ("You Couldn't escape!")
                        slow_print ("The Orc Attacks!")
                        slow_print ("You lose 7 Health.")
                        health -= 7
                    elif found >= 4:
                        slow_print ('You flee from the mighty monster. No one balmes you, but you failed')
                        print('Game Over')
                if hp <= 0:
                    slow_print (f"The Orc Died!")
                if health <= 0:
                    slow_print ('You Died')
                    print ('Game Over')
                    quit()
    if battle == 3:#Dragon Fight
        attack = 'Club'
        damage = weapon['Club']
        health = player
        hp = monster['Dragon']
        while health >= 1 and hp >= 1:
            if hp >= 1:
                slow_print (f"You have {health} health")
                choice = input("""What Do You Do?
1. Attack
2. Run Away
>>> """)
                if choice == '1':
                    slow_print (f"You Swing with your {attack}!")
                    hp -= damage
                    attacks = ['Bites You', 'Claws You', "Whacks you with it's Tail"]
                    found = random.choice(attacks)
                    slow_print (f"The Dragon {found}!")
                    slow_print ("You lose 8 Health.")
                    health -= 8
                elif choice == '2':
                    found = random.randint(1, 5)
                    if found <= 3:
                        slow_print ("You Couldn't escape!")
                        slow_print ("The Orc Attacks!")
                        slow_print ("You lose 10 Health.")
                        health -= 10
                    elif found >= 4:
                        slow_print ('You flee from the mighty monster. No one balmes you, but you failed')
                        print('Game Over')
                        quit()
                if hp <= 0:
                    slow_print (f"The Orc Died!")
                if health <= 0:
                    slow_print ('You Died')
                    print ('Game Over')
                    quit()
weapon = { #Weapon dictionary with damage
    'Dagger': 2,
    'Short Sword': 5,
    'Club' : 20,
    'Glock': 999
}
monster = { #Monster dictionary with health
    'Goblin': 10,
    'Orc': 25,
    'Dragon': 100
}
location = ['Home', 'Town', 'Castle', 'Dungeon']#not used by game
choices = [] #all player choices
backpack = [] #players items
player = 50 #players health

#main code
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
choice = input("""What do you do?
1. confront the goblin
2. sneak around the goblin
>>>""")
if choice == '1':
    if 'Glock' in backpack:
        slow_print('Walking towards the goblin, you shoot it in the face and it dies on the spot.')
    elif 'Dagger' in backpack:
        slow_print('Brandishing your dagger,you walk up to the goblin and initiate combat')
        battle = 1
        combat(player, weapon, damage, battle,)
    print('You Gained the Goblins Short Sword')
    backpack.append('Short Sword')
    time.sleep(.5)
    slow_print('Releasing the townfolk, they give you food and water to heal up, before pointing you in the direction of the emperors castle')
    slow_print('"Oh please kind adventurer, free us from his tyranny!"')
