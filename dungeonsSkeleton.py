import time
import random
import os
import Utilities
import race
import player

#To Do List

#For all inputs should include error checking to make sure valid input is given


#Make player class



#Initialize the Player class

    


#Weapons
class Weapon:
    pass

class Dagger(Weapon):
    pass


#Race Functions That are Being made to classes

        
class wholeLvlUp(Race, Player):
    def levelUp():
        if Player.xp in range (lvlUpTuple[0], lvlUpTuple[1]):
            Player.level = 1
        if Player.xp in range (lvlUpTuple[1] ,lvlUpTuple[2]):
            Player.level = 2
        if Player.xp in range (lvlUpTuple[2] , lvlUpTuple[3]):
            Player.level = 3
        if Player.xp in range (lvlUpTuple[3] , lvlUpTuple[4]):
            Player.level = 4
        if Player.xp in range (lvlUpTuple[4] , lvlUpTuple[5]):
            Player.level = 5
        if Player.xp in range (lvlUpTuple[5] , lvlUpTuple[6]):
            Player.level = 6
        if Player.xp in range (lvlUpTuple[6] , lvlUpTuple[7]):
            Player.level = 7
        if Player.xp in range (lvlUpTuple[7] , lvlUpTuple[8]):
            Player.level = 8
        if Player.xp in range (lvlUpTuple[8] , lvlUpTuple[9]):
            Player.level = 9
        if Player.xp in range (lvlUpTuple[9] , lvlUpTuple[10]):
            Player.level = 10
        if Player.xp in range (lvlUpTuple[10] , lvlUpTuple[11]):
            Player.level = 11
        if Player.xp in range (lvlUpTuple[11] , lvlUpTuple[12]):
            Player.level = 12
        if Player.xp in range (lvlUpTuple[12] , lvlUpTuple[13]):
            Player.level = 13
        if Player.xp in range (lvlUpTuple[12] , lvlUpTuple[13]):
            Player.level = 14
        if Player.xp in range (lvlUpTuple[13] , lvlUpTuple[14]):
            Player.level = 15
        if Player.xp in range (lvlUpTuple[14] , lvlUpTuple[15]):
            Player.level = 16
        if Player.xp in range (lvlUpTuple[15] , lvlUpTuple[16]):
            Player.level = 17
        if Player.xp in range (lvlUpTuple[16] , lvlUpTuple[17]):
            Player.level = 18
        if Player.xp in range (lvlUpTuple[17] , lvlUpTuple[18]):
            Player.level = 19
        if Player.xp in range (lvlUpTuple[18] , lvlUpTuple[19]):
            Player.level = 20
            
    def pStrMod():
        if Player.strength == 1:
            Player.strengthMod = -5
        elif Player.strength  == 2 or  Player.strength == 3:
            Player.strengthMod = -4
        elif Player.strength == 4 or Player.strength == 5:
            Player.strengthMod = -3
        elif Player.strength == 6 or Player.strength == 7:
            Player.strengthMod = -2
        elif Player.strength == 8 or Player.strength == 9:
            Player.strengthMod = -1
        elif Player.strength == 9 or Player.strength == 10:
            Player.strengthMod = 0
        elif Player.strength == 11 or Player.strength == 12:
            Player.strengthMod = 1
        elif Player.strength == 13 or Player.strength == 14:
            Player.strengthMod = 2
        elif Player.strength == 15 or Player.strength == 16:
            Player.strengthMod = 3
        elif Player.strength == 17 or Player.strength == 18:
            Player.strengthMod = 4
        elif Player.strength == 19 or Player.strength == 20:
            Player.strengthMod = 5
        elif player.strength == 21 or Player.strength == 22:
            Player.strengthMod = 6
        elif Player.strength == 23 or Player.strength == 24:
            Player.strengthMod = 7
        elif Player.strength == 25 or Player.strength == 26:
            Player.strengthMod = 8
        elif Player.strength == 27 or Player.strength == 28:
            Player.strengthMod = 8
        elif Player.strength == 29 or Player.strength == 30:
            Player.strengthModMod = 9

    def pConMod():
        if player.constituion == 1:
            player.constitutionMod = -5
        elif player.constituion  == 2 or  Player.constitution == 3:
            player.constitutionMod = -4
        elif player.constituion == 4 or Player.constitution == 5:
            player.constitutionMod = -3
        elif player.constituion == 6 or Player.constitution == 7:
            player.constitutionMod = -2
        elif player.constituion == 8 or Player.constitution == 9:
            player.constitutionMod = -1
        elif player.constituion == 9 or Player.constitution == 10:
            player.constitutionMod = 0
        elif player.constituion == 11 or Player.constitution == 12:
            player.constitutionMod = 1
        elif player.constituion == 13 or Player.constitution == 14:
            player.constitutionMod = 2
        elif player.constituion == 15 or Player.constitution == 16:
            player.constitutionMod = 3
        elif player.constituion == 17 or Player.constitution == 18:
            player.constitutionMod = 4
        elif player.constituion == 19 or Player.constitution == 20:
            player.constitutionMod = 5
        elif playerStat[1] == 21 or Player.constitution == 22:
            player.constitutionMod = 6
        elif player.constituion == 23 or Player.constitution == 24:
            player.constitutionMod = 7
        elif player.constituion == 25 or Player.constitution == 26:
            player.constitutionMod = 8
        elif player.constituion == 27 or Player.constitution == 28:
            player.constitutionMod = 8
        elif player.constituion == 29 or Player.constitution == 30:
            player.constitutionMod = 9

    def pDexMod():
        if player.dexterity == 1:
            player.dexterityMod = -5
        elif player.dexterity  == 2 or  Player.dexterity == 3:
            player.dexterityMod = -4
        elif player.dexterity == 4 or Player.dexterity == 5:
            player.dexterityMod = -3
        elif player.dexterity == 6 or Player.dexterity == 7:
            player.dexterityMod = -2
        elif player.dexterity == 8 or Player.dexterity == 9:
            player.dexterityMod = -1
        elif player.dexterity == 9 or Player.dexterity == 10:
            player.dexterityMod = 0
        elif player.dexterity == 11 or Player.dexterity == 12:
            player.dexterityMod = 1
        elif player.dexterity == 13 or Player.dexterity == 14:
            player.dexterityMod = 2
        elif player.dexterity == 15 or Player.dexterity == 16:
            player.dexterityMod = 3
        elif player.constituion == 17 or Player.dexterity == 18:
            player.dexterityMod = 4
        elif player.dexterity == 19 or Player.dexterity == 20:
            player.dexterityMod = 5
        elif playerStat[2] == 21 or Player.dexterity == 22:
            player.dexterityMod = 6
        elif player.dexterity == 23 or Player.dexterity == 24:
            player.dexterityMod = 7
        elif player.dexterity == 25 or Player.dexterity == 26:
            player.dexterityMod = 8
        elif player.dexterity == 27 or Player.dexterity == 28:
            player.dexterityMod = 8
        elif player.dexterity == 29 or Player.dexterity == 30:
            player.dexterityMod = 9

    def pIntMod():
        if player.wisdom == 1:
            player.intelligenceMod = -5
        elif player.wisdom  == 2 or  Player.intelligence == 3:
            player.intelligenceMod = -4
        elif player.wisdom == 4 or Player.intelligence == 5:
            player.intelligenceMod = -3
        elif player.wisdom == 6 or Player.intelligence == 7:
            player.intelligenceMod = -2
        elif player.wisdom == 8 or Player.intelligence == 9:
            player.intelligenceMod = -1
        elif player.wisdom == 9 or Player.intelligence == 10:
            player.intelligenceMod = 0
        elif player.wisdom == 11 or Player.intelligence == 12:
            player.intelligenceMod = 1
        elif player.wisdom == 13 or Player.intelligence == 14:
            player.intelligenceMod = 2
        elif player.wisdom == 15 or Player.intelligence == 16:
            player.intelligenceMod = 3
        elif player.wisdom == 17 or Player.intelligence == 18:
            player.intelligenceMod = 4
        elif player.wisdom == 19 or Player.intelligence == 20:
            player.intelligenceMod = 5
        elif playerStat[3] == 21 or Player.intelligence == 22:
            player.intelligenceMod = 6
        elif player.wisdom == 23 or Player.intelligence == 24:
            player.intelligenceMod = 7
        elif player.wisdom == 25 or Player.intelligence == 26:
            player.intelligenceMod = 8
        elif player.wisdom == 27 or Player.intelligence == 28:
            player.intelligenceMod = 8
        elif player.wisdom == 29 or Player.intelligence == 30:
            player.intelligenceMod = 9

    def pWisMod():
        if player.wisdom == 1:
            player.wisdomMod = -5
        elif player.wisdom  == 2 or  Player.wisdom == 3:
            player.wisdomMod = -4
        elif player.wisdom == 4 or Player.wisdom == 5:
            player.wisdomMod = -3
        elif player.wisdom == 6 or Player.wisdom == 7:
            player.wisdomMod = -2
        elif player.wisdom == 8 or Player.wisdom == 9:
            player.wisdomMod = -1
        elif player.wisdom == 9 or Player.wisdom == 10:
            player.wisdomMod = 0
        elif player.wisdom == 11 or Player.wisdom == 12:
            player.wisdomMod = 1
        elif player.wisdom == 13 or Player.wisdom == 14:
            player.wisdomMod = 2
        elif player.wisdom == 15 or Player.wisdom == 16:
            player.wisdomMod = 3
        elif player.wisdom == 17 or Player.wisdom == 18:
            player.wisdomMod = 4
        elif player.wisdom == 19 or Player.wisdom == 20:
            player.wisdomMod = 5
        elif playerStat[4] == 21 or Player.wisdom == 22:
            player.wisdomMod = 6
        elif player.wisdom == 23 or Player.wisdom == 24:
            player.wisdomMod = 7
        elif player.wisdom == 25 or Player.wisdom == 26:
            player.wisdomMod = 8
        elif player.wisdom == 27 or Player.wisdom == 28:
            player.wisdomMod = 8
        elif player.wisdom == 29 or Player.wisdom == 30:
            player.wisdomMod = 9

    def pCharMod():

        if Player.charisma == 1:
            player.charismaMod = -5
        elif Player.charisma  == 2 or  Player.charisma == 3:
            player.charismaMod = -4
        elif Player.charisma == 4 or Player.charisma == 5:
            player.charismaMod = -3
        elif Player.charisma == 6 or Player.charisma == 7:
            player.charismaMod = -2
        elif Player.charisma == 8 or Player.charisma == 9:
            player.charismaMod = -1
        elif Player.charisma == 9 or Player.charisma == 10:
            player.charismaMod = 0
        elif Player.charisma == 11 or Player.charisma == 12:
            player.charismaMod = 1
        elif Player.charisma == 13 or Player.charisma == 14:
            player.charismaMod = 2
        elif Player.charisma == 15 or Player.charisma == 16:
            player.charismaMod = 3
        elif Player.charisma == 17 or Player.charisma == 18:
            player.charismaMod = 4
        elif Player.charisma == 19 or Player.charisma == 20:
            player.charismaMod = 5
        elif Player.charisma == 21 or Player.charisma == 22:
            player.charismaMod = 6
        elif Player.charisma == 23 or Player.charisma == 24:
            player.charismaMod = 7
        elif Player.charisma == 25 or Player.charisma == 26:
            player.charismaMod = 8
        elif Player.charisma == 27 or Player.charisma == 28:
            player.charismaMod = 8
        elif Player.charisma == 29 or Player.Charisma == 30:
            player.charismaMod = 9
    def profUp():
        if Player.level in range (1,4):
            Player.proficiency = 2
        if Player.level in range (5,8):
            player.proficiency = 3
        if Player.level in range (9,12):
            player.proficiency = 4
        if Player.level in range (13,16):
            player.proficiency = 5
        if Player.level in range (17,20):
            player.proficiency = 6
      

 


def characterCreation(playerNum):
    #In this function, the dialogue and machinery of character creation happens.
    #Character creation WILL change global variables, so this needs only be run ONCE, at the beginning of the game
    index = 0
    num = playerNum
    players = {'player1' : 0, 'player2' : 0, 'player3' : 0, 'player4' : 0}
    while (num < 0) or (num > 4):
        num = int(input("Error! Only Supports 1-4 Players! How Many Players Are There: "))

    if num == 1:
        players['player1'] = Player()
        players['player1'].name = 'Player1'
    elif num == 2:
        players['player1'] = Player()
        players['player1'].name = 'Player1'
        players['player2'] = Player()
        players['player2'].name = 'Player2'
    elif num == 3:
        players['player1'] = Player()
        players['player1'].name = 'Player1'
        players['player2'] = Player()
        players['player2'].name = 'Player2'
        players['player3'] = Player()
        players['player3'].name = 'Player3'
    elif num == 3:
        players['player1'] = Player()
        players['player1'].name = 'Player1'
        players['player2'] = Player()
        players['player2'].name = 'Player2'
        players['player3'] = Player()
        players['player3'].name = 'Player3'
        players['player4'] = Player()
        players['player4'].name = 'Player4'


def combat():
        def attack(Weapon):
    #This is the skeleton for combat.  There are gonna be several loops here
            clear()


def  game():
    #All the actual story for the game should go here
    Utilities.ExtraLanguage(Race)
    #Utilities.clear()
    time.sleep(1)

def testPlace():
#The title screen should go here
    print('Welcome to my DnD Clone! ')
    startQuery = input('Do you wish to begin? Enter Yes or No ')
    startQuery = startQuery.lower()
    if startQuery == 'yes' or startQuery == 'y':
        
        #characterCreation(int(input('How Many Players Are There (1-4): ')))
        #game()
      
        Utilities.wholeLvlUp.levelUp(player.playerState)
        print(player.playerState.level)
    else:
        input('')


testPlace()