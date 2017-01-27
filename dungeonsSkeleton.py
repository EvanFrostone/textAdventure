import time
import random
import os


#From this point on, declare ALL global variables and lists. This includes player stats,money, health, AC,  difficulty scores, monster stats, etc.
playerName = 'Null'
playerRace = 'Null'
playerClass = 'Null'
characterTraits = ['Name', 'Race', 'Class', 'Alignment', 'Background']
playerStats = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#The Player Stats Indicies are as follows: [Strength (0) , Constitution (1) , Dexterity (2) , Intelligence (3) , Wisdom (4) , Charisma (5) , Luck (6) , Level (7) , Health (8) , Gold (9), Armor Class (10), Level (11), XP (12) ]
playerMods = [ 0 ,0 ,0 ,0 ,0 ,0 ]
#The Player Modifier Indicies are as Follows[Strength (0). Consitituion(1), Dexterity (2), Intelligence (3) , Wisdom (4) , Charisma (5) ]
playerInventory =['Empty']
#This is the player's inventory. Add items to it using the .append() function.
def textWait():
    #This is the average amount of pause between printed lines of text. Call this function to get pauses.
    time.sleep(7)

    
def clear():
    #This function clears the screen of EVERYTHING. Use if the console is getting a little crowded
    os.system('cls')

def characterCreation():
    #In this function, the dialogue and machinery of character creation happens.
    #Character creation WILL change global variables, so this needs only be run ONCE, at the beginning of the game
    clear()



def combat():
    #This is the skeleton for combat.  There are gonna be several loops here
    clear()


def  game():
    #All the actual story for the game should go here
    clear()

def intro():
    #The title screen should go here
    print('')
    
clear()
