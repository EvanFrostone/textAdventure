import time
import random
import os

#To Do List

#Make list to store Name, Race, Class, Background, Alignment
#From this point on, declare ALL global variables and lists. This includes player stats,money, health, AC,  difficulty scores, monster stats, etc.
characterTraits = ['Name', 'Race', 'Class', 'Alignment', 'Background']
#The Character Traits Indicies are as follows: ['Name', 'Race', 'Class', 'Alignment, 'Background']
playerStats = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ]
#The Player Stats Indicies are as follows: [Strength (0) , Constitution (1) , Dexterity (2) , Intelligence (3) , Wisdom (4) , Charisma (5) , Health (6) , Gold (7), Armor Class (8), Level (9), XP (10), Initiative (11) ]
playerMods = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#The Player Modifier Indicies are as Follows[Strength (0). Consitituion(1), Dexterity (2), Intelligence (3) , Wisdom (4) , Charisma (5), Proficieny Bonus(6) ]
playerSkills = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#The Player Skills Indicies are as follows: [Acrobatics (0), Animal Handling (1), Arcana(2), Athletics (3), Deception (4), History (5), Insight (6), Intimidation (7), Investigation (8), Medicine (9), Nature (10), Perception (11), Performance (12), Persuasion (13), Religion (14), Slight of Hand (15),#Stealth (16), Survival (17)]
playerSavingThrows = [ 0 , 0 , 0 , 0 , 0 , 0 ]
#The Player Saving Throws Indicies are as follows:[Strength (0), Constituion(1), Dexterity (2), Intelligence (3), Wisdom (4), Charisma (5)]
playerInventory =['Empty']
#This is the player's inventory. Add items to it using the .append() function.
lvlUpTuple = (300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000)

def pStrMod():
    if playerStats[0] == 1:
        playerMods[0] = -5
    elif playerStats[0]  == 2 or  playerStats[0] == 3:
        playerMods[0] = -4
    elif playerStats[0] == 4 or playerStats[0] == 5:
        playerMods[0] = -3
    elif playerStats[0] == 6 or playerStats[0] == 7:
        playerMods[0] = -2
    elif playerStats[0] == 8 or playerStats[0] == 9:
        playerMods[0] = -1
    elif playerStats[0] == 9 or playerStats[0] == 10:
        playerMods[0] = 0
    elif playerStats[0] == 11 or playerStats[0] == 12:
        playerMods[0] = 1
    elif playerStats[0] == 13 or playerStats[0] == 14:
        playerMods[0] = 2
    elif playerStats[0] == 15 or playerStats[0] == 16:
        playerMods[0] = 3
    elif playerStats[0] == 17 or playerStats[0] == 18:
        playerMods[0] = 4
    elif playerStats[0] == 19 or playerStats[0] == 20:
        playerMods[0] = 5
    elif playerStat[0] == 21 or playerStats[0] == 22:
        playerMods[0] = 6
    elif playerStats[0] == 23 or playerStats[0] == 24:
        playerMods[0] = 7
    elif playerStats[0] == 25 or playerStats[0] == 26:
        playerMods[0] = 8
    elif playerStats[0] == 27 or playerStats[0] == 28:
        playerMods[0] = 8
    elif playerStats[0] == 29 or playerStats[0] == 30:
        playerMods[0] = 9

def pConMod():
    if playerStats[1] == 1:
        playerMods[1] = -5
    elif playerStats[1]  == 2 or  playerStats[0] == 3:
        playerMods[1] = -4
    elif playerStats[1] == 4 or playerStats[0] == 5:
        playerMods[1] = -3
    elif playerStats[1] == 6 or playerStats[0] == 7:
        playerMods[1] = -2
    elif playerStats[1] == 8 or playerStats[0] == 9:
        playerMods[1] = -1
    elif playerStats[1] == 9 or playerStats[0] == 10:
        playerMods[1] = 0
    elif playerStats[1] == 11 or playerStats[0] == 12:
        playerMods[1] = 1
    elif playerStats[1] == 13 or playerStats[0] == 14:
        playerMods[1] = 2
    elif playerStats[1] == 15 or playerStats[0] == 16:
        playerMods[1] = 3
    elif playerStats[1] == 17 or playerStats[0] == 18:
        playerMods[1] = 4
    elif playerStats[1] == 19 or playerStats[0] == 20:
        playerMods[1] = 5
    elif playerStat[1] == 21 or playerStats[0] == 22:
        playerMods[1] = 6
    elif playerStats[1] == 23 or playerStats[0] == 24:
        playerMods[1] = 7
    elif playerStats[1] == 25 or playerStats[0] == 26:
        playerMods[1] = 8
    elif playerStats[1] == 27 or playerStats[0] == 28:
        playerMods[1] = 8
    elif playerStats[1] == 29 or playerStats[0] == 30:
        playerMods[1] = 9

def pDexMod():
    if playerStats[2] == 1:
        playerMods[2] = -5
    elif playerStats[2]  == 2 or  playerStats[0] == 3:
        playerMods[2] = -4
    elif playerStats[2] == 4 or playerStats[0] == 5:
        playerMods[2] = -3
    elif playerStats[2] == 6 or playerStats[0] == 7:
        playerMods[2] = -2
    elif playerStats[2] == 8 or playerStats[0] == 9:
        playerMods[2] = -1
    elif playerStats[2] == 9 or playerStats[0] == 10:
        playerMods[2] = 0
    elif playerStats[2] == 11 or playerStats[0] == 12:
        playerMods[2] = 1
    elif playerStats[2] == 13 or playerStats[0] == 14:
        playerMods[2] = 2
    elif playerStats[2] == 15 or playerStats[0] == 16:
        playerMods[2] = 3
    elif playerStats[1] == 17 or playerStats[0] == 18:
        playerMods[2] = 4
    elif playerStats[2] == 19 or playerStats[0] == 20:
        playerMods[2] = 5
    elif playerStat[2] == 21 or playerStats[0] == 22:
        playerMods[2] = 6
    elif playerStats[2] == 23 or playerStats[0] == 24:
        playerMods[2] = 7
    elif playerStats[2] == 25 or playerStats[0] == 26:
        playerMods[2] = 8
    elif playerStats[2] == 27 or playerStats[0] == 28:
        playerMods[2] = 8
    elif playerStats[2] == 29 or playerStats[0] == 30:
        playerMods[2] = 9

def pIntMod():
    if playerStats[3] == 1:
        playerMods[3] = -5
    elif playerStats[3]  == 2 or  playerStats[0] == 3:
        playerMods[3] = -4
    elif playerStats[3] == 4 or playerStats[0] == 5:
        playerMods[3] = -3
    elif playerStats[3] == 6 or playerStats[0] == 7:
        playerMods[3] = -2
    elif playerStats[3] == 8 or playerStats[0] == 9:
        playerMods[3] = -1
    elif playerStats[3] == 9 or playerStats[0] == 10:
        playerMods[3] = 0
    elif playerStats[3] == 11 or playerStats[0] == 12:
        playerMods[3] = 1
    elif playerStats[3] == 13 or playerStats[0] == 14:
        playerMods[3] = 2
    elif playerStats[3] == 15 or playerStats[0] == 16:
        playerMods[3] = 3
    elif playerStats[3] == 17 or playerStats[0] == 18:
        playerMods[3] = 4
    elif playerStats[3] == 19 or playerStats[0] == 20:
        playerMods[3] = 5
    elif playerStat[3] == 21 or playerStats[0] == 22:
        playerMods[3] = 6
    elif playerStats[3] == 23 or playerStats[0] == 24:
        playerMods[3] = 7
    elif playerStats[3] == 25 or playerStats[0] == 26:
        playerMods[3] = 8
    elif playerStats[3] == 27 or playerStats[0] == 28:
        playerMods[3] = 8
    elif playerStats[3] == 29 or playerStats[0] == 30:
        playerMods[3] = 9

def pWisMod():
    if playerStats[4] == 1:
        playerMods[4] = -5
    elif playerStats[4]  == 2 or  playerStats[0] == 3:
        playerMods[4] = -4
    elif playerStats[4] == 4 or playerStats[0] == 5:
        playerMods[4] = -3
    elif playerStats[4] == 6 or playerStats[0] == 7:
        playerMods[4] = -2
    elif playerStats[4] == 8 or playerStats[0] == 9:
        playerMods[4] = -1
    elif playerStats[4] == 9 or playerStats[0] == 10:
        playerMods[4] = 0
    elif playerStats[4] == 11 or playerStats[0] == 12:
        playerMods[4] = 1
    elif playerStats[4] == 13 or playerStats[0] == 14:
        playerMods[4] = 2
    elif playerStats[4] == 15 or playerStats[0] == 16:
        playerMods[4] = 3
    elif playerStats[4] == 17 or playerStats[0] == 18:
        playerMods[4] = 4
    elif playerStats[4] == 19 or playerStats[0] == 20:
        playerMods[4] = 5
    elif playerStat[4] == 21 or playerStats[0] == 22:
        playerMods[4] = 6
    elif playerStats[4] == 23 or playerStats[0] == 24:
        playerMods[4] = 7
    elif playerStats[4] == 25 or playerStats[0] == 26:
        playerMods[4] = 8
    elif playerStats[4] == 27 or playerStats[0] == 28:
        playerMods[4] = 8
    elif playerStats[4] == 29 or playerStats[0] == 30:
        playerMods[4] = 9

def pCharMod():
    if playerStats[5] == 1:
        playerMods[5] = -5
    elif playerStats[5]  == 2 or  playerStats[0] == 3:
        playerMods[5] = -4
    elif playerStats[5] == 4 or playerStats[0] == 5:
        playerMods[5] = -3
    elif playerStats[5] == 6 or playerStats[0] == 7:
        playerMods[5] = -2
    elif playerStats[5] == 8 or playerStats[0] == 9:
        playerMods[5] = -1
    elif playerStats[5] == 9 or playerStats[0] == 10:
        playerMods[5] = 0
    elif playerStats[5] == 11 or playerStats[0] == 12:
        playerMods[5] = 1
    elif playerStats[5] == 13 or playerStats[0] == 14:
        playerMods[5] = 2
    elif playerStats[5] == 15 or playerStats[0] == 16:
        playerMods[5] = 3
    elif playerStats[5] == 17 or playerStats[0] == 18:
        playerMods[5] = 4
    elif playerStats[5] == 19 or playerStats[0] == 20:
        playerMods[5] = 5
    elif playerStat[5] == 21 or playerStats[0] == 22:
        playerMods[5] = 6
    elif playerStats[5] == 23 or playerStats[0] == 24:
        playerMods[5] = 7
    elif playerStats[5] == 25 or playerStats[0] == 26:
        playerMods[5] = 8
    elif playerStats[5] == 27 or playerStats[0] == 28:
        playerMods[5] = 8
    elif playerStats[5] == 29 or playerStats[0] == 30:
        playerMods[5] = 9
def levelUp():
    if playerStats[10] in lvlUpTuple:
        playerStats[9] = playerStats[9] + 1

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
