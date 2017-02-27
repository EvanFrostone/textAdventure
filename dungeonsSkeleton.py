import time
import random
import os

#To Do List

#Make list to store Name, Race, Class, Background, Alignment
#From this point on, declare ALL global variables and lists. This includes player stats,money, health, AC,  difficulty scores, monster stats, etc.
#The Character Traits Indicies are as follows: ['Name', 'Race', 'Class', 'Alignment, 'Background']
characterTraits = ['Name', 'Race', 'Class', 'Alignment', 'Background']
#The Player Stats (Armor Class = AC)
playerStats = [ 'Strength' : 0, 'Constituion' : 0, 'Dexterity' : 0, 'Intelligence' : 0, 'Wisdom' : 0, 'Charisma' : 0, 
    'Health' : 0, 'Gold' : 0, 'AC' : 0, 'Level' : 1, 'XP' : 0, 'Initiative' : 0 ]

#The Player Modifier (Proficieny Bonus = PB)
playerMods = {'Strength' : 0, 'Constituion' : 0, 'Dexterity' : 0, 'Intelligence' : 0, 'Wisdom' : 0, 'Charisma' : 0, 'PB' : 0}

#The Player Skills Indicies are as follows: [Acrobatics (0), Animal Handling (1), Arcana(2), Athletics (3), Deception (4), History (5), Insight (6), Intimidation (7), Investigation (8), Medicine (9), Nature (10), Perception (11), Performance (12), Persuasion (13), Religion (14), Slight of Hand (15),#Stealth (16), Survival (17)]
playerSkills = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]

playerSavingThrows = [ 0 , 0 , 0 , 0 , 0 , 0 ]
#The Player Saving Throws Indicies are as follows:[Strength (0), Constituion(1), Dexterity (2), Intelligence (3), Wisdom (4), Charisma (5)]
playerInventory =['Empty']
#This is the player's inventory. Add items to it using the .append() function.

lvlUpTuple = ( 0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000 )
dwarfStats = [2, 'Medium', 'Dark Vision', 'Battleaxe', 'Handaxe', 'Throwing hammer', 'Warhammer', 'Common', 'Dwarvish']
#The Dwarvish stats are as follows: [+2 Constitution (0), Size (1), Dark Vision Ability (2), Batlleaxe Proficiency (3), Handaxe Proficiency (4), Throwing Hammer Proficiency (5), Warhammer Proficiency (6), Speaks Common (7), Speaks Dwarvish (8)]

#Here Be Proficiencies

#Here Be Language Proficiencies 
speaksCommon = True
speaksDwarvish = False
speaksElvish = False
speaksThievesCant = False
speaksHalfling = False
speaksDraconic = False
speaksGnomish = False
speaksOrc = False
speaksInfernal = False

#Here Be Misc Proficiencies 
profDarkVision = False

#Here Be Tool Proficiencies 
profAlchSups = False
profCaligSups = False
profCobblerSups = False
profCookUtils = False
profGlassBlowTools = False
profJewlerTools = False
profLeatherworkTools = False
profPainterSups = False
profPotterTools = False
profTinkerTools = False
profWeaverTools = False
profWoodcarversTools = False
profDisguiseKit = False
profForgeryKit = False
profGamingSet = False
profHerbalismKit = False
profBagpipes = False
profDrum = False
profDulcimer = False
profFlute = False
profLute = False
profLyre = False
profHorn = False
profPanFlute = False
profShawm = False
profViol = False
profNavigatorTools = False
profPosionerKit = False
profThievesTools = False
profVehicles = False 



#Here Be Armor Proficiences
profLightArmor = False
profMediumArmor = False
profHeavyArmor = False

#Here Be Weapon Proficiencies 

profbattleAxe = False
profclub = False
profdagger = False 
profgreatClub = False
profJavelin = False
proflightHammer = False
profhandAxe = False
profthrowingHammer = False
profwarHammer = False
proflongBow = False
proflongSword = False
profshortBow = False
profshortSword = False
profrapiers = False
profhandCrossbow = False
profshields = False
profsimpleWeapons = False
profmartialWeapons = False
profmace = False
profquarterStaff = False
profsickle = False
profspear = False
profunarmedStrike = False
profdart = False
profsling = False
profflail = False
profglaive = False
profgreatSword = False
profhalbred = False
proflance = False
profmaul = False
profmorningStar = False
profpike = False
profscimitar = False
proftrident = False
profwarPick = False
profwhip = False
profblowGun = False
profheavyCrossbow = False
profnet = False




#Here Be Skill Proficiencies
profAcrobatics = False
profAnimalHandling = False
profArcana = False
profAthletics = False
profDeception = False
profHistory = False
profInsight = False
profIntimidation = False
profInvestigation = False
profMedicine = False
profNature = False
profPerception = False
profPerformance = False
profPersuasion = False
profReligion = False
profSleightofHand = False
profStealth = False
profSurvival = False

#HereBeSpecialSkills
profDarkVision = False
profFeyAncestry = False
profmaskoftheWild = False
profsupDarkVision = False
#Here Be Races
def dwarf():
    global profbattleAxe
    global profhandAxe
    global profthrowingHammer
    global profwarHammer
    global speaksCommon
    global speaksDwarvish
    global profDarkVision
    profbattleAxe = True
    profhandAxe = True
    profthrowingHammer = True
    profwarHammer = True
    speaksCommon = True
    speaksDwarvish = True
    profDarkVision = True
    playerStats[1] = playerStats[1] + 2
def hillDwarf():
    global profLightArmor
    global profMediumArmor
    dwarf()
    profLightArmor = True
    profMediumArmor = True
    playerStats[0] = playerStats[0] + 2

def elf():
    global profDarkVision
    global profPerception
    global profFeyAncestry
    global speaksCommon
    global speaksElvish
    profDarkVision = True
    profPerception = True
    profFeyAncestry = True
    speaksCommon = True
    speaksElvish = True
    playerStats[2] = playerStats[2] + 2
def highElf():
    elf()
    global proflongSword
    global profshortBow
    global profshortSword
    global proflongBow
    global speaksCommon 
    global speaksDwarvish
    global speaksElvish
    global speaksThievesCant 
    global speaksHalfling
    global speaksDraconic 
    global speaksGnomish 
    global speaksOrc 
    global speaksInfernal 
    proflongSword = True
    profshortBow = True
    proflongBow = True
    profshortSword = True
    playerStats[3] = playerStats[3] + 1
    #High Elf needs a Cantrip (Come back once you've finished Spell Casting)
    
    #Here I ran into a sort of issue that got resolved
    #I need a way to reask the player the "What language?" question if they make a mistake, or otherwise change their mind
    #To do this, I created this very nested decision structure. The while is true from the start to run the loop. The player is asked their choice in language.abs
    #Then, the input is checked in a number of "if" statements. The first checks the language, asks a confirmation question, and the second actually sets variables and changes stuff

    speechBoolean = True
    while speechBoolean == True:
        extraLangQuery = input('You get to learn an extra language as a high elf! What language would you like to learn? Thieves\' Cant, Dwarvish, Halfling, Draconic, Gnomish, Orcish, or Infernal? ')
        extraLangQuery = extraLangQuery.lower()


        if extraLangQuery == 'thieves\' cant' or 'thieves\'cant':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksThievesCant = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'dwarvish':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksDwarvish = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'halfling':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksHalfling = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'draconic':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksDraconic = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'gnomish':
            confirmationQuery = input('Are you sure you want to speak Gnomish? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksGnomish = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'orcish':
            confirmationQuery = input('Are you sure you want to speak Orchish? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksOrc = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'infernal':
            confirmationQuery = input('Are you sure you want to speak Infernal? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksInfernal = True
                speechBoolean = False
            else:
                speechBoolean = True


        else:
            speechBoolean = True

def woodElf():
    elf()
    global proflongSword
    global profshortSword
    global profshortBow
    global proflongBow
    global profmaskoftheWild
    playerStats[4] = playerStats[4] + 1
    proflongSword = True
    profshortBow = True
    proflongBow = True
    profshortSword = True
    profmaskoftheWild = True
def drow():
    elf()
    #Drow needs disadvantage on attack rolls and perception rolls in direct sunlight
    #Drow also needs a hand full of cantrips
    global profrapiers
    global profshortSword
    global profhandCrossbow
    global profsupDarkVision
    profrapiers = True
    profshortSword = True
    profhandCrossbow = True
    profsupDarkVision = True
    playerStats[5] = playerStats[5] + 1

def halfling():
    #Halfling needs luck? On crit miss on attack, ability check, or saving  rolls, can reroll, but must stay with roll
    global speaksHalfling
    speaksHalfling = True
    playerStats[2] = playerStats[2] + 2
def lightfoothalf():
    halfling()
    #lightfoot needs naturally stealthy 
    playerStats[5] = playerStats[5] + 1
def stoutHalf():
    #Stout needs advantage on saving throws against poison and poison resitance
    halfling()
    playerStats[1] = playerStats[1] + 1
def human():
    playerStats[0] = playerStats[0] + 1
    playerStats[1] = playerStats[1] + 1
    playerStats[2] = playerStats[2] + 1
    playerStats[3] = playerStats[3] + 1
    playerStats[4] = playerStats[4] + 1
    playerStats[5] = playerStats[5] + 1
    global speaksCommon 
    global speaksDwarvish
    global speaksElvish
    global speaksThievesCant 
    global speaksHalfling
    global speaksDraconic 
    global speaksGnomish 
    global speaksOrc 
    global speaksInfernal 
    speechBoolean = True
    while speechBoolean == True:
        extraLangQuery = input('You get to learn an extra language as a human! What language would you like to learn? Thieves\' Cant, Dwarvish, Halfling, Draconic, Gnomish, Orcish, or Infernal? ')
        extraLangQuery = extraLangQuery.lower()


        if extraLangQuery == 'thieves\' cant' or 'thieves\'cant':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksThievesCant = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'dwarvish':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksDwarvish = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'halfling':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksHalfling = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'draconic':
            confirmationQuery = input('Are you sure you want to speak', extraLangQuery,'? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksDraconic = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'gnomish':
            confirmationQuery = input('Are you sure you want to speak Thieves\'s Cant? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksGnomish = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'orcish':
            confirmationQuery = input('Are you sure you want to speak Thieves\'s Cant? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksOrc = True
                speechBoolean = False
            else:
                speechBoolean = True


        elif extraLangQuery == 'infernal':
            confirmationQuery = input('Are you sure you want to speak Thieves\'s Cant? Answer yes or no. ')
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks',extraLangQuery,'!')
                speaksInfernal = True
                speechBoolean = False
            else:
                speechBoolean = True


        else:
            speechBoolean = True
def dragonborn():
    #Dragonborn probably requires spellcasting to actually work so, comeback later
    clear()
    




def gnome():
    global profDarkVision
    profDarkVision = True
    playerStats[3] = playerStats[3] + 2

def forestGnome():
    #Needs minor illusion cantrip
    gnome()
    playerStats[2] = playerStats[2] + 1

def rockGnome():
    global profTinkerTools
    profTinkerTools = True
    #clockwork device, gotta make sometime 
    gnome()
    #Artificers Lore, make history check related to magic, alchemical, or tech items, add 2x proficiency bonus
    playerStats[1] = playerStats[1] + 1

def halfElf():
    global profDarkVision 
    global profFeyAncestry
    global speaksCommon 
    global speaksDwarvish
    global speaksElvish
    global speaksThievesCant 
    global speaksHalfling
    global speaksDraconic 
    global speaksGnomish 
    global speaksOrc 
    global speaksInfernal
    global profAcrobatics
    global profAnimalHandling
    global profArcana
    global profAthletics 
    global profDeception 
    global profHistory 
    global profInsight 
    global profIntimidation 
    global profInvestigation 
    global profMedicine 
    global profNature 
    global profPerception 
    global profPerformance 
    global profPersuasion 
    global profReligion 
    global profSleightofHand 
    global profStealth
    global profSurvival 

    profDarkVision = True
    profFeyAncestry = True
    speaksCommon = True
    speaksElvish = True
    

    playerStats[5] = playerStats[5] + 2
    print('As a half elf, you have the ability to increase two of your ability scores by one.')

    checkStatQuery1 = True
    while checkStatQuery1:
        statQuery1 = input('Which do you wish to increase first?(Enter Strength, Constitution, Dexterity, Intelligence, Wisdom, or Charisma) ')
       
       
        printStatQuery1 = str(statQuery1.lower())
        if printStatQuery1 == 'strength' or printStatQuery1 == 'constitution' or printStatQuery1 == 'dexterity' or printStatQuery1 == 'intelligence' or printStatQuery1 == 'wisdom' or printStatQuery1 == 'charisma':
            secondaryConfirmationError = True
            while secondaryConfirmationError:
                statQuery1query = input('You want to increase your '+ printStatQuery1 +'? ')
                if statQuery1query.lower() == 'yes':
                    if statQuery1 == 'strength':
                        playerStats[0] = playerStats[0] + 1
                    elif statQuery1 == 'constitution': 
                        playerStats[1] = playerStats[1] + 1
                    elif statQuery1 == 'dexterity': 
                        playerStats[2] = playerStats[2] + 1
                    elif statQuery1 == 'intelligence': 
                        playerStats[3] = playerStats[3] + 1
                    elif statQuery1 == 'wisdom':
                        playerStats[4] = playerStats[4] + 1
                    elif statQuery1 == 'charisma': 
                        playerStats[5] = playerStats[5] + 1
                    secondaryConfirmationError = False
                    checkStatQuery1 = False
                elif statQuery1query == 'no':
                    secondaryConfirmationError = False
                    checkStatQuery1 = True
                else:
                    print('Sorry, I didn\'t understand what you said. Please respond with (yes or no).')
                    textWait(2)
                    secondaryConfirmationError = True
        else:
            errorMessage()
            checkStatQuery1 = True



    checkStatQuery2 = True
    while checkStatQuery2:
        statQuery2 = input('Which do you wish to increase second?(Enter Strength, Constitution, Dexterity, Intelligence, Wisdom, or Charisma) ')
    
        printStatQuery2 = str(statQuery2.lower())

        secondaryConfirmationError = True
        while secondaryConfirmationError:
            statQuery2query = input('You want to increase your '+ printStatQuery2 +'? ')
            if statQuery2query.lower() == 'yes':
                if statQuery2 == 'strength':
                    playerStats[0] = playerStats[0] + 1
                elif statQuery2 == 'constitution': 
                    playerStats[1] = playerStats[1] + 1
                elif statQuery2 == 'dexterity': 
                    playerStats[2] = playerStats[2] + 1
                elif statQuery2 == 'intelligence': 
                    playerStats[3] = playerStats[3] + 1
                elif statQuery2 == 'wisdom':
                    playerStats[4] = playerStats[4] + 1
                elif statQuery2 == 'charisma': 
                    playerStats[5] = playerStats[5] + 1
                secondaryConfirmationError = False
                checkStatQuery2 = False
            elif statQuery2query == 'no':
                secondaryConfirmationError = False
                checkStatQuery2 = True
            else:
                print('Sorry, I didn\'t understand what you said. Please respond with (yes or no).')
                textWait(2)
                secondaryConfirmationError = True
        speechBoolean = True
        while speechBoolean == True:
            extraLangQuery = input('You get to learn an extra language as a half elf! What language would you like to learn? Thieves\' Cant, Dwarvish, Halfling, Draconic, Gnomish, Orcish, or Infernal? ')
            extraLangQuery = extraLangQuery.lower()


            if extraLangQuery == 'thieves\' cant' or 'thieves\'cant':
                confirmationQuery = input('Are you sure you want to speak ' + extraLangQuery +'? Answer yes or no. ')
                
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery + '!')
                    speaksThievesCant = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'dwarvish':
                confirmationQuery = input('Are you sure you want to speak ' + extraLangQuery + '? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery +'!')
                    speaksDwarvish = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'halfling':
                confirmationQuery = input('Are you sure you want to speak ' + extraLangQuery + '? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks '+ extraLangQuery +'!')
                    speaksHalfling = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'draconic':
                confirmationQuery = input('Are you sure you want to speak ' + extraLangQuery + '? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery + '!')
                    speaksDraconic = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'gnomish':
                confirmationQuery = input('Are you sure you want to speak Gnomish? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery +'!')
                    speaksGnomish = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'orcish':
                confirmationQuery = input('Are you sure you want to speak Orchish? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery + '!')
                    speaksOrc = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            elif extraLangQuery == 'infernal':
                confirmationQuery = input('Are you sure you want to speak Infernal? Answer yes or no. ')
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks ' + extraLangQuery + '!')
                    speaksInfernal = True
                    speechBoolean = False
                else:
                    speechBoolean = True


            else:
                speechBoolean = True




    skillBoolean = True 
    while skillBoolean == True:
        print('As a half elf, you also get to become proficient in two skills of your choice.')
        textWait(3)
        print('What two skills would you like to become proficient in?')
        profQuery = input('You have a choice between Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuassion, Religion, Sleight of Hand, Stealth, and Survival')
        profQuery = profQuery.lower()
        if profQuery == 'acrobatics':
            profAcrobatics = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'animal handling':
            profAnimalHandling = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'arcana':
            profArcana = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'athletics':
            profAthletics = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'deception':
            profDeception = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'history':
            profHistory = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'insight':
            profInsight = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'medicine':
            profMedicine = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'nature':
            profNature = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'perception':
            profPerception = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'performance':
            profPerformance = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'persuasion':
            profPersuasion = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'sleight of hand':
            profSleightofHand = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'stealth':
            profStealth = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )


        elif profQuery == 'survival':
            profSurvival = True
            skillBoolean = False
            print('Alright, your character is now proficient in ' + profQuery )

        else:
            print('I\'m not quite sure what you said, please try again!')
            skillBoolean = True
            textWait(2)

                

  

#Here Be Weapons 
def dagger():

    clear()



def dwarfStats():
    global speaksCommon
    global speaksDwarvish
    speaksCommon = True
    speaksDwarvish = True
def levelUp():
    if playerStats[10] in range (lvlUpTuple[0], lvlUpTuple[1]):
        playerStats[9] = 1
    if playerStats[10] in range (lvlUpTuple[1] ,lvlUpTuple[2]):
        playerStats[9] = 2
    if playerStats[10] in range (lvlUpTuple[2] , lvlUpTuple[3]):
        playerStats[9] = 3
    if playerStats[10] in range (lvlUpTuple[3] , lvlUpTuple[4]):
        playerStats[9] = 4
    if playerStats[10] in range (lvlUpTuple[4] , lvlUpTuple[5]):
        playerStats[9] = 5
    if playerStats[10] in range (lvlUpTuple[5] , lvlUpTuple[6]):
        playerStats[9] = 6
    if playerStats[10] in range (lvlUpTuple[6] , lvlUpTuple[7]):
        playerStats[9] = 7
    if playerStats[10] in range (lvlUpTuple[7] , lvlUpTuple[8]):
        playerStats[9] = 8
    if playerStats[10] in range (lvlUpTuple[8] , lvlUpTuple[9]):
        playerStats[9] = 9
    if playerStats[10] in range (lvlUpTuple[9] , lvlUpTuple[10]):
        playerStats[9] = 10
    if playerStats[10] in range (lvlUpTuple[10] , lvlUpTuple[11]):
        playerStats[9] = 11
    if playerStats[10] in range (lvlUpTuple[11] , lvlUpTuple[12]):
        playerStats[9] = 12
    if playerStats[10] in range (lvlUpTuple[12] , lvlUpTuple[13]):
        playerStats[9] = 13
    if playerStats[10] in range (lvlUpTuple[12] , lvlUpTuple[13]):
        playerStats[9] = 14
    if playerStats[10] in range (lvlUpTuple[13] , lvlUpTuple[14]):
        playerStats[9] = 15
    if playerStats[10] in range (lvlUpTuple[14] , lvlUpTuple[15]):
        playerStats[9] = 16
    if playerStats[10] in range (lvlUpTuple[15] , lvlUpTuple[16]):
        playerStats[9] = 17
    if playerStats[10] in range (lvlUpTuple[16] , lvlUpTuple[17]):
        playerStats[9] = 18
    if playerStats[10] in range (lvlUpTuple[17] , lvlUpTuple[18]):
        playerStats[9] = 19
    if playerStats[10] in range (lvlUpTuple[18] , lvlUpTuple[19]):
        playerStats[9] = 20
        
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
def profUp():
    if playerStats[9] in range (1,4):
        playerMods[6] = 2
    if playerStats[9] in range (5,8):
        playerMods[6] = 3
    if playerStats[9] in range (9,12):
        playerMods[6] = 4
    if playerStats[9] in range (13,16):
        playerMods[6] = 5
    if playerStats[9] in range (17,20):
        playerMods[6] = 6
        

def wholeLvlUp():
    levelUp()
    pStrMod()
    pConMod()
    pDexMod()
    pIntMod()
    pWisMod()
    pCharMod()
    profUp()
    

def textWait(wait):
    #This is the average amount of pause between printed lines of text. Call this function to get pauses.
    time.sleep(wait)
    


def dice(rolls, size):
    #This function rolls dice for you.
    #Put in the number of rolls and the size of dice you want rolled
    #dice( 10 , 5 ) to roll  10 D5's
    result = []
    processingRolls = rolls
    while processingRolls != 0:
        processingRolls -= 1
        result.append(random.randint( 0 , size ))
    

def clear():
    #This function clears the screen of EVERYTHING. Use if the console is getting a little crowded
    os.system('cls')

def characterCreation():
    #In this function, the dialogue and machinery of character creation happens.
    #Character creation WILL change global variables, so this needs only be run ONCE, at the beginning of the game
    halfElf()



def combat():
        def attack(Weapon):
    #This is the skeleton for combat.  There are gonna be several loops here
            clear()


def  game():
    #All the actual story for the game should go here
    clear()

def intro():
    #The title screen should go here
    print('Welcome to my DnD Clone! ')
    startQuery = input('Do you wish to begin? Enter Yes or No ')
    startQuery = startQuery.lower()
    if startQuery == 'yes' or startQuery == 'y':
        
        characterCreation()
        game()

    else:
        input('')
def errorMessage():
    print('Sorry, I\'m not quite sure what you said. Please try again!')
def yesnoErrorMessage():
    print('I\'m not quite sure what you said. Please answer with yes or no!')
intro()
