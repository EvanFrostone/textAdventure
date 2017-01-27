import time
import random
import os

#To Do List

#Make list to store Name, Race, Class, Background, Alignment
#From this point on, declare ALL global variables and lists. This includes player stats,money, health, AC,  difficulty scores, monster stats, etc.
playerName = 'Null'
playerRace = 'Null'
playerClass = 'Null'

playerStats = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#The Player Stats Indicies are as follows: [Strength (0) , Dexterity (1), Constitution (2), Intelligence (3) , Wisdom (4) , Charisma (5) , Level (6) , Health (7) , Gold (8), Armor Class (9) ]
playerMods = [ 0 , 0  , 0  , 0 , 0 , 0  ]
#The Player Modifier Indicies are as Follows[Strength (0) , Dexterity (1), Constitution (2), Intelligence (3) , Wisdom (4) , Charisma (5) ]
playerInventory =['Empty']
#This is the player's inventory. Add items to it using the .append() function.  The first item to be added must be added like playerInventory[0] = 'Insert Item Name Here'
def textWait():
    #This is the average amount of pause between printed lines of text. Call this function to get pauses.
    time.sleep(7)

    
def clear():
    #This function clears the screen of EVERYTHING. Use if the console is getting a little crowded
    os.system('cls')

def characterCreation():
    #In this function, the dialogue and machinery of character creation happens.
    #Character creation WILL change global variables, so this needs only be run ONCE, at the beginning of the game


    print('Adventurer, we need to find out who you will be in this world of Dungeons and Dragons')
    textWait()
    print('The first step towards your new adventure is to learn what your name is!') 



def combat():
    #This is the skeleton for combat.  There are gonna be several loops here
    clear()


def  game():
    #All the actual story for the game should go here
    clear()

def intro():
    #The title screen should go here
    print('Welcome to my DnD Clone')
    startQuery = input('Do you wish to begin? Enter Yes or No')
    if startQuery == 'yes' or startQuery == 'Yes' or startQuery == 'y' or startQuery == 'Y':
        characterCreation()
        game()

    else:
        input('')
intro()
