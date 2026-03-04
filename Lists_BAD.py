#Imports
import sys
import time
import random
#Functions
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05) #change this to change speed
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
                choices.append(choice)
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
                choices.append(choice)
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
                choices.append(choice)
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
                    slow_print (f"The Dragon Died!")
                if health <= 0:
                    slow_print ('You Died')
                    print ('Game Over')
                    quit()
weapon = { #Weapon dictionary with damage
    'Dagger': 2,
    'Short Sword': 5,
    'Club' : 20,
    'Glock': 999,
    'Great Claw' : 200
}
monster = { #Monster dictionary with health
    'Goblin': 10,
    'Orc': 25,
    'Dragon': 100,
    'The Deep': 1000
}
location = ['Home', 'Town', 'Castle', 'Dungeon', 'The Woods']#not used by game
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
choices.append(choice)
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
    quit()
    
slow_print('Leaving the house, you see town in the distance, with a Castle behind it.')
slow_print('Heading into town, you see a horde of goblins leaving, and the remaining townsfolk gaurded by a single remaining goblin.')

choice = input("""What do you do?
1. confront the goblin
2. sneak around the goblin
>>>""")
choices.append(choice)
if choice == '1':
    if 'Glock' in backpack:
        slow_print('Walking towards the goblin, you shoot it in the face and it dies on the spot.')
    else:
        slow_print('Brandishing your dagger,you walk up to the goblin and initiate combat')
        battle = 3
        combat(player, weapon, battle,)
        
elif choice == '2':
    slow_print('You slowly make your way around the cage, and move to follow the receding horde')
    slow_print('Unfortunatley for you, there was another goblin hiding around the back of the people')
    battle = 1
    combat(player, weapon, battle,)
else:
    slow_print('Goodjob, Dumbass. Restart!')
    quit()
print('You Gained the Goblins Short Sword')
backpack.append('Short Sword')

time.sleep(.5)
slow_print('Releasing the townfolk, they give you food and water to heal up, before pointing you in the direction of the emperors castle')
slow_print('"Oh please kind adventurer, free us from his tyranny!"')

time.sleep(.5)
slow_print('Making your way to the castle, Short Sword in hand, you encounter a fork in the road.')
slow_print('Ahaed of you, the castle awaits atop its treachorous hill.')
slow_print('To your right, a secluded path through the woods, full of a dense fog, and promise of adventure.')

choice = input("""Where do you go:
1. To the castle
2. Through the woods
>>> """)
choices.append(choice)
if choice == '2':
    slow_print("Turning towards the woods, you go to take a step forwards, when you're knocked on your ass by a gust of wind")
    slow_print('A loud voice echoes through the trees, "Thou contain not the knowledge nor power to enter these woods."')
    slow_print('You decide to leave. For now...')
elif choice == '1':
    slow_print('Walking towards the castle, you easily take out a couple of Goblins.')
    slow_print('Reaching the base of the hill, you see the large footprints of an Orc')
    slow_print('Turning around, the ugly beast stands before you.')
    if 'Glock' in backpack:
        slow_print('Aiming your glock, the shot misses the slobering beast, before ricocheting off a tree, and nailing the beast in the nuts.')
    else:
        battle = 2
        combat(player, weapon, battle)
else:
    slow_print('Goodjob, Dumbass. Restart!')
    quit()
print("You gained the Orc's Club!")
time.sleep(.5)

slow_print('Walking past the crumpled body of the Orc with your new found club, you make your way to the summit and enter the castle.')
slow_print('Walking inside the throne room, you see his majesty in all his horrid glory, sitting atop his seat.')
slow_print('"So." he says, "You have come to challenge me. well I promise it would not be an easy fight, but I have no intention to fight you myself."')
slow_print('The Emperor reaches behind his throne, and pulls a rope you had previously disregarded.')
slow_print('The floor beneath you drops out, and you land in the dungeons.')
slow_print('You wake in a dark room. Seemingly a large chamber, you can hear every breath echo back at you.')
slow_print('Sitting up, you see a line of lanterns light up along the walls of what seems to be an ancient ball room.')
slow_print('As you make to leave, you hear a loud roar echo behind you.')

choice = input("""What do you do?
1. Rush out of the room
2. Turn toward the thunderous noise
>>> """)
choices.append(choice)
if choice == '1':
    slow_print('Sprinting out of the room, you find yourself in front of a massive Dragon, roaring into a tube.')
elif choice == '2':
    slow_print('Cautiously mking your way towards the end of the room, you see, hidden in the shadows, a large horn, through which the roar eminates.')
    slow_print("Turning around, you see the Dragon exit it's room")
else:
    slow_print('Goodjob, Dumbass. Restart!')
    quit()
slow_print("The dragon spots you, and prepares for it's snack.")
if 'Glock' in backpack:
    slow_print('You Take out your Glock and nail the dragon right between the eyes.')
else:
    battle = 3
    combat(player, weapon, battle)

slow_print('Deafeating the dragon, you see it disintigrate before your eyes, until all that remains is one of the beasts claws, attached to a long hilt.')
print("You gained the Great Claw!")
time.sleep(.5)
slow_print('Walking out of the dungeon, you exit behind the throne room, next to the king.')

choice = input ('''What do you do?:
1. Kill the King and rejoice with the villagers
2. Leave the King to his plans and head home
>>> ''')
choices.append(choice)
if choice == '1':    
    slow_print('You slit the kings throat with the Dragons claw. you see his head drop to the floor.')
    slow_print('Gripping the Rulers scalp, you make your way out of the castle and down the hill.')
    slow_print('Reaching town, the villagers celebrate late into the night. Rejoicing over there new found freedom.')
    time.sleep(1)
    slow_print('But peace cannot last forever. Without a ruler, the town falls to anarchy.')
elif choice == '2':
    slow_print('You and the king talk. Land cannot maintain peace without a common aspect. A king to rule. A tyrant to hate.')
    slow_print('You could have ended this. But you chose to listen to him. You return home. The townsfolk cheer at your return, but see you empty handed.')
    slow_print('You are jeered and ridiculed. How could you do this? Leave them under his boot?')
    time.sleep(1)
    slow_print('But the land remains intact. War comes through, but the peolpe fight under 1 banner.')
    slow_print('The king doesnt live forever. Eventually he is replaced, but you are never forgiven.')
elif choice == '3':
    if 'Glock' in backpack:
        slow_print('You take out your trusty glock. only 1 shot left.')
        slow_print('You end his life with the same weapon that has taken down even a mighty Dragon')
        slow_print('Heading down the hill, you remember those strange woods.')
        slow_print('Approaching the crossroads, you see the fog that once settled over the path has dissipated.')
        slow_print('You follow this overgrown path. Long forgotten, but still maintaned.')
        slow_print('"Very few have found this place. Fewer have been able to walk it."')
        slow_print('"Yet you, who have killed and slaughtered. You walk this trail, without knowing its purpose, and as such, will never find it'"'"'s end"')
        slow_print('You turn around and see the start of the path right behind you. You go to leave, but find you move nary an inch.')
        slow_print("You're stuck. Doomed to stay and watch. Never able to interfere.'")
    else:
        slow_print('Goodjob, Dumbass. Restart!')
        quit()
else:
    slow_print('Goodjob, Dumbass. Restart!')
    quit()
