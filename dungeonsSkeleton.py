import time
import random
import os

#To Do List

#For all inputs should include error checking to make sure valid input is given

lvlUpTuple = ( 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000 )

#Make player class
class Player:

    name = 'Name'
    race = Race()
    _class = 'Class'
    alignment = 'Alignment'
    background = 'Background'

    #This is the player's inventory. Add items to it using the .append() function.
    inventory =['Empty']
    
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

#Initialize the Player class
player = Player()

class Race:

    name = "Race Name"

    #Stats
    strength = 0
    constituion = 0
    dexterity = 0
    intelligence = 0
    wisodom = 0
    charisma = 0
    wisodom = 0
    health = 0
    gold = 0
    armorClass = 0
    level = 1
    xp = 0
    initiative = 0

    #Modifier
    strengthMod = 0
    constituionMod = 0
    dexterityMod = 0
    intelligenceMod = 0
    wisdomMod = 0
    charismaMod = 0
    proficiencyBonus = 0

    #Skill
    acrobatics = 0
    animalHandling = 0
    arcana = 0
    athletics = 0
    deception = 0
    history = 0
    insight = 0
    intimidation = 0
    investigation = 0
    medicine = 0
    nature = 0
    perception = 0
    performance = 0
    persuasion = 0
    religion = 0
    slightOfHand = 0
    stealth = 0
    survival = 0

    #Saving Throws
    savingThrows = {'Strength' : 0, 'Constituion' : 0, 'Dexterity' : 0, 'Intelligence' : 0, 'Wisdom' : 0, 'Charisma' : 0}

class Dwarf(Race):
    
    def __init__ (self)
        self.constitution += 2
   
    profbattleAxe = True
    profhandAxe = True
    profthrowingHammer = True
    profwarHammer = True
    speaksCommon = True
    speaksDwarvish = True
    profDarkVision = True

>>>>>>> origin/master
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
    playerStats['Constituion'] = playerStats['Constituion'] + 2
def hillDwarf():
    global profLightArmor
    global profMediumArmor
    dwarf()
    profLightArmor = True
    profMediumArmor = True
    playerStats['Strength'] = playerStats['Strength'] + 2

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
    playerStats['Dexterity'] = playerStats['Dexterity'] + 2
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
    playerStats['Intelligence'] = playerStats['Intelligence'] + 1
    #High Elf needs a Cantrip (Come back once you've finished Spell Casting)
    
    #Here I ran into a sort of issue that got resolved
    #I need a way to reask the player the "What language?" question if they make a mistake, or otherwise change their mind
    #To do this, I created this very nested decision structure. The while is true from the start to run the loop. The player is asked their choice in language.abs
    #Then, the input is checked in a number of "if" statements. The first checks the language, asks a confirmation question, and the second actually sets variables and changes stuff

    speechBoolean = True
    while speechBoolean == True:
        extraLangQuery = input('You get to learn an extra language as a high elf! \n\n%-20s %20s \n%-20s %20s \n%-20s %20s \n%-20s %20s \n\nPick the language that you would like to learn: ' % 
            ('1. Thieves\' Cant', '5. Gnomish ', '2. Dwarvish', '6. Orchish ', '3. Halfling', '7. Infernal', '4. Draconic', '')) #last string is formatting place holder
        extraLangQuery = extraLangQuery.lower()

        if extraLangQuery == '1':
            extraLangQuery = 'thieves\'cant'
        elif extraLangQuery == '2':
            extraLangQuery = 'Dwarvish'
        elif extraLangQuery == '3':
            extraLangQuery = 'Halfling'
        elif extraLangQuery == '4':
            extraLangQuery = 'Draconic'
        elif extraLangQuery == '5':
            extraLangQuery = 'Gnomish'
        elif extraLangQuery == '6':
            extraLangQuery= 'Orchish'
        elif extraLangQuery == '7':
            extraLangQuery = 'Inferal'

        if extraLangQuery == 'thieves\' cant' or 'thieves\'cant':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksThievesCant = True
                speechBoolean = False
            
        elif extraLangQuery == 'dwarvish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
        

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksDwarvish = True
                speechBoolean = False


        elif extraLangQuery == 'halfling':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
    

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksHalfling = True
                speechBoolean = False


        elif extraLangQuery == 'draconic':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))

                
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s!' % (extraLangQuery))
                speaksDraconic = True
                speechBoolean = False


        elif extraLangQuery == 'gnomish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
            
   
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksGnomish = True
                speechBoolean = False


        elif extraLangQuery == 'orcish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))


            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksOrc = True
                speechBoolean = False


        elif extraLangQuery == 'infernal':
           confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
        
           if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksInfernal = True
                speechBoolean = False

def woodElf():
    elf()
    global proflongSword
    global profshortSword
    global profshortBow
    global proflongBow
    global profmaskoftheWild
    playerStats['Wisdom'] = playerStats['Wisdom'] + 1
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
    playerStats['Charisma'] = playerStats['Charisma'] + 1

def halfling():
    #Halfling needs luck? On crit miss on attack, ability check, or saving  rolls, can reroll, but must stay with roll
    global speaksHalfling
    speaksHalfling = True
    playerStats['Dexterity'] = playerStats['Dexterity'] + 2
def lightfoothalf():
    halfling()
    #lightfoot needs naturally stealthy 
    playerStats['Charisma'] = playerStats['Charisma'] + 1
def stoutHalf():
    #Stout needs advantage on saving throws against poison and poison resitance
    halfling()
    playerStats['Constituion'] = playerStats['Constituion'] + 1

def human():
    playerStats['Strength'] = playerStats['Strength'] + 1
    playerStats['Constituion'] = playerStats['Constituion'] + 1
    playerStats['Dexterity'] = playerStats['Dexterity'] + 1
    playerStats['Intelligence'] = playerStats['Intelligence'] + 1
    playerStats['Wisdom'] = playerStats['Wisdom'] + 1
    playerStats['Charisma'] = playerStats['Charisma'] + 1
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
        extraLangQuery = input('You get to learn an extra language as a human! \n\n%-20s %20s \n%-20s %20s \n%-20s %20s \n%-20s %20s \n\nPick the language that you would like to learn: ' % 
            ('1. Thieves\' Cant', '5. Gnomish ', '2. Dwarvish', '6. Orchish ', '3. Halfling', '7. Infernal', '4. Draconic', '')) #last string is formatting place holder
        extraLangQuery = extraLangQuery.lower()

        if extraLangQuery == '1':
            extraLangQuery = 'thieves\'cant'
        elif extraLangQuery == '2':
            extraLangQuery = 'Dwarvish'
        elif extraLangQuery == '3':
            extraLangQuery = 'Halfling'
        elif extraLangQuery == '4':
            extraLangQuery = 'Draconic'
        elif extraLangQuery == '5':
            extraLangQuery = 'Gnomish'
        elif extraLangQuery == '6':
            extraLangQuery= 'Orchish'
        elif extraLangQuery == '7':
            extraLangQuery = 'Inferal'

        if extraLangQuery == 'thieves\' cant' or 'thieves\'cant':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksThievesCant = True
                speechBoolean = False
            
        elif extraLangQuery == 'dwarvish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
        

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksDwarvish = True
                speechBoolean = False


        elif extraLangQuery == 'halfling':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
    

            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksHalfling = True
                speechBoolean = False


        elif extraLangQuery == 'draconic':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))

                
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s!' % (extraLangQuery))
                speaksDraconic = True
                speechBoolean = False


        elif extraLangQuery == 'gnomish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
            
   
            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksGnomish = True
                speechBoolean = False


        elif extraLangQuery == 'orcish':
            confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))


            if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksOrc = True
                speechBoolean = False


        elif extraLangQuery == 'infernal':
           confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
        
           if confirmationQuery.lower() == 'yes':
                print('Alright, your character now speaks %s' % (extraLangQuery))
                speaksInfernal = True
                speechBoolean = False


def dragonborn():
    #Dragonborn probably requires spellcasting to actually work so, comeback later
    clear()
    




def gnome():
    global profDarkVision
    profDarkVision = True
    playerStats['Intelligence'] = playerStats['Intelligence'] + 2

def forestGnome():
    #Needs minor illusion cantrip
    gnome()
    playerStats['Dexterity'] = playerStats['Dexterity'] + 1

def rockGnome():
    global profTinkerTools
    profTinkerTools = True
    #clockwork device, gotta make sometime 
    gnome()
    #Artificers Lore, make history check related to magic, alchemical, or tech items, add 2x proficiency bonus
    playerStats['Constituion'] = playerStats['Constituion'] + 1

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
    

    playerStats['Charisma'] = playerStats['Charisma'] + 2
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
                        playerStats['Strength'] = playerStats['Strength'] + 1
                    elif statQuery1 == 'constitution': 
                        playerStats['Constituion'] = playerStats['Constituion'] + 1
                    elif statQuery1 == 'dexterity': 
                        playerStats['Dexterity'] = playerStats['Dexterity'] + 1
                    elif statQuery1 == 'intelligence': 
                        playerStats['Intelligence'] = playerStats['Intelligence'] + 1
                    elif statQuery1 == 'wisdom':
                        playerStats['Wisdom'] = playerStats['Wisdom'] + 1
                    elif statQuery1 == 'charisma': 
                        playerStats['Charisma'] = playerStats['Charisma'] + 1
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
                    playerStats['Strength'] = playerStats['Strength'] + 1
                elif statQuery2 == 'constitution': 
                    playerStats['Constituion'] = playerStats['Constituion'] + 1
                elif statQuery2 == 'dexterity': 
                    playerStats['Dexterity'] = playerStats['Dexterity'] + 1
                elif statQuery2 == 'intelligence': 
                    playerStats['Intelligence'] = playerStats['Intelligence'] + 1
                elif statQuery2 == 'wisdom':
                    playerStats['Wisdom'] = playerStats['Wisdom'] + 1
                elif statQuery2 == 'charisma': 
                    playerStats['Charisma'] = playerStats['Charisma'] + 1
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
    if playerStats['XP'] in range (lvlUpTuple[0], lvlUpTuple[1]):
        playerStats['Level'] = 1
    if playerStats['XP'] in range (lvlUpTuple[1] ,lvlUpTuple[2]):
        playerStats['Level'] = 2
    if playerStats['XP'] in range (lvlUpTuple[2] , lvlUpTuple[3]):
        playerStats['Level'] = 3
    if playerStats['XP'] in range (lvlUpTuple[3] , lvlUpTuple[4]):
        playerStats['Level'] = 4
    if playerStats['XP'] in range (lvlUpTuple[4] , lvlUpTuple[5]):
        playerStats['Level'] = 5
    if playerStats['XP'] in range (lvlUpTuple[5] , lvlUpTuple[6]):
        playerStats['Level'] = 6
    if playerStats['XP'] in range (lvlUpTuple[6] , lvlUpTuple[7]):
        playerStats['Level'] = 7
    if playerStats['XP'] in range (lvlUpTuple[7] , lvlUpTuple[8]):
        playerStats['Level'] = 8
    if playerStats['XP'] in range (lvlUpTuple[8] , lvlUpTuple[9]):
        playerStats['Level'] = 9
    if playerStats['XP'] in range (lvlUpTuple[9] , lvlUpTuple[10]):
        playerStats['Level'] = 10
    if playerStats['XP'] in range (lvlUpTuple[10] , lvlUpTuple[11]):
        playerStats['Level'] = 11
    if playerStats['XP'] in range (lvlUpTuple[11] , lvlUpTuple[12]):
        playerStats['Level'] = 12
    if playerStats['XP'] in range (lvlUpTuple[12] , lvlUpTuple[13]):
        playerStats['Level'] = 13
    if playerStats['XP'] in range (lvlUpTuple[12] , lvlUpTuple[13]):
        playerStats['Level'] = 14
    if playerStats['XP'] in range (lvlUpTuple[13] , lvlUpTuple[14]):
        playerStats['Level'] = 15
    if playerStats['XP'] in range (lvlUpTuple[14] , lvlUpTuple[15]):
        playerStats['Level'] = 16
    if playerStats['XP'] in range (lvlUpTuple[15] , lvlUpTuple[16]):
        playerStats['Level'] = 17
    if playerStats['XP'] in range (lvlUpTuple[16] , lvlUpTuple[17]):
        playerStats['Level'] = 18
    if playerStats['XP'] in range (lvlUpTuple[17] , lvlUpTuple[18]):
        playerStats['Level'] = 19
    if playerStats['XP'] in range (lvlUpTuple[18] , lvlUpTuple[19]):
        playerStats['Level'] = 20
        
def pStrMod():
    if playerStats['Strength'] == 1:
        playerMods[0] = -5
    elif playerStats['Strength']  == 2 or  playerStats['Strength'] == 3:
        playerMods[0] = -4
    elif playerStats['Strength'] == 4 or playerStats['Strength'] == 5:
        playerMods[0] = -3
    elif playerStats['Strength'] == 6 or playerStats['Strength'] == 7:
        playerMods[0] = -2
    elif playerStats['Strength'] == 8 or playerStats['Strength'] == 9:
        playerMods[0] = -1
    elif playerStats['Strength'] == 9 or playerStats['Strength'] == 10:
        playerMods[0] = 0
    elif playerStats['Strength'] == 11 or playerStats['Strength'] == 12:
        playerMods[0] = 1
    elif playerStats['Strength'] == 13 or playerStats['Strength'] == 14:
        playerMods[0] = 2
    elif playerStats['Strength'] == 15 or playerStats['Strength'] == 16:
        playerMods[0] = 3
    elif playerStats['Strength'] == 17 or playerStats['Strength'] == 18:
        playerMods[0] = 4
    elif playerStats['Strength'] == 19 or playerStats['Strength'] == 20:
        playerMods[0] = 5
    elif playerStat[0] == 21 or playerStats['Strength'] == 22:
        playerMods[0] = 6
    elif playerStats['Strength'] == 23 or playerStats['Strength'] == 24:
        playerMods[0] = 7
    elif playerStats['Strength'] == 25 or playerStats['Strength'] == 26:
        playerMods[0] = 8
    elif playerStats['Strength'] == 27 or playerStats['Strength'] == 28:
        playerMods[0] = 8
    elif playerStats['Strength'] == 29 or playerStats['Strength'] == 30:
        playerMods[0] = 9

def pConMod():
    if playerStats['Constituion'] == 1:
        playerMods[1] = -5
    elif playerStats['Constituion']  == 2 or  playerStats['Strength'] == 3:
        playerMods[1] = -4
    elif playerStats['Constituion'] == 4 or playerStats['Strength'] == 5:
        playerMods[1] = -3
    elif playerStats['Constituion'] == 6 or playerStats['Strength'] == 7:
        playerMods[1] = -2
    elif playerStats['Constituion'] == 8 or playerStats['Strength'] == 9:
        playerMods[1] = -1
    elif playerStats['Constituion'] == 9 or playerStats['Strength'] == 10:
        playerMods[1] = 0
    elif playerStats['Constituion'] == 11 or playerStats['Strength'] == 12:
        playerMods[1] = 1
    elif playerStats['Constituion'] == 13 or playerStats['Strength'] == 14:
        playerMods[1] = 2
    elif playerStats['Constituion'] == 15 or playerStats['Strength'] == 16:
        playerMods[1] = 3
    elif playerStats['Constituion'] == 17 or playerStats['Strength'] == 18:
        playerMods[1] = 4
    elif playerStats['Constituion'] == 19 or playerStats['Strength'] == 20:
        playerMods[1] = 5
    elif playerStat[1] == 21 or playerStats['Strength'] == 22:
        playerMods[1] = 6
    elif playerStats['Constituion'] == 23 or playerStats['Strength'] == 24:
        playerMods[1] = 7
    elif playerStats['Constituion'] == 25 or playerStats['Strength'] == 26:
        playerMods[1] = 8
    elif playerStats['Constituion'] == 27 or playerStats['Strength'] == 28:
        playerMods[1] = 8
    elif playerStats['Constituion'] == 29 or playerStats['Strength'] == 30:
        playerMods[1] = 9

def pDexMod():
    if playerStats['Dexterity'] == 1:
        playerMods[2] = -5
    elif playerStats['Dexterity']  == 2 or  playerStats['Strength'] == 3:
        playerMods[2] = -4
    elif playerStats['Dexterity'] == 4 or playerStats['Strength'] == 5:
        playerMods[2] = -3
    elif playerStats['Dexterity'] == 6 or playerStats['Strength'] == 7:
        playerMods[2] = -2
    elif playerStats['Dexterity'] == 8 or playerStats['Strength'] == 9:
        playerMods[2] = -1
    elif playerStats['Dexterity'] == 9 or playerStats['Strength'] == 10:
        playerMods[2] = 0
    elif playerStats['Dexterity'] == 11 or playerStats['Strength'] == 12:
        playerMods[2] = 1
    elif playerStats['Dexterity'] == 13 or playerStats['Strength'] == 14:
        playerMods[2] = 2
    elif playerStats['Dexterity'] == 15 or playerStats['Strength'] == 16:
        playerMods[2] = 3
    elif playerStats['Constituion'] == 17 or playerStats['Strength'] == 18:
        playerMods[2] = 4
    elif playerStats['Dexterity'] == 19 or playerStats['Strength'] == 20:
        playerMods[2] = 5
    elif playerStat[2] == 21 or playerStats['Strength'] == 22:
        playerMods[2] = 6
    elif playerStats['Dexterity'] == 23 or playerStats['Strength'] == 24:
        playerMods[2] = 7
    elif playerStats['Dexterity'] == 25 or playerStats['Strength'] == 26:
        playerMods[2] = 8
    elif playerStats['Dexterity'] == 27 or playerStats['Strength'] == 28:
        playerMods[2] = 8
    elif playerStats['Dexterity'] == 29 or playerStats['Strength'] == 30:
        playerMods[2] = 9

def pIntMod():
    if playerStats['Intelligence'] == 1:
        playerMods[3] = -5
    elif playerStats['Intelligence']  == 2 or  playerStats['Strength'] == 3:
        playerMods[3] = -4
    elif playerStats['Intelligence'] == 4 or playerStats['Strength'] == 5:
        playerMods[3] = -3
    elif playerStats['Intelligence'] == 6 or playerStats['Strength'] == 7:
        playerMods[3] = -2
    elif playerStats['Intelligence'] == 8 or playerStats['Strength'] == 9:
        playerMods[3] = -1
    elif playerStats['Intelligence'] == 9 or playerStats['Strength'] == 10:
        playerMods[3] = 0
    elif playerStats['Intelligence'] == 11 or playerStats['Strength'] == 12:
        playerMods[3] = 1
    elif playerStats['Intelligence'] == 13 or playerStats['Strength'] == 14:
        playerMods[3] = 2
    elif playerStats['Intelligence'] == 15 or playerStats['Strength'] == 16:
        playerMods[3] = 3
    elif playerStats['Intelligence'] == 17 or playerStats['Strength'] == 18:
        playerMods[3] = 4
    elif playerStats['Intelligence'] == 19 or playerStats['Strength'] == 20:
        playerMods[3] = 5
    elif playerStat[3] == 21 or playerStats['Strength'] == 22:
        playerMods[3] = 6
    elif playerStats['Intelligence'] == 23 or playerStats['Strength'] == 24:
        playerMods[3] = 7
    elif playerStats['Intelligence'] == 25 or playerStats['Strength'] == 26:
        playerMods[3] = 8
    elif playerStats['Intelligence'] == 27 or playerStats['Strength'] == 28:
        playerMods[3] = 8
    elif playerStats['Intelligence'] == 29 or playerStats['Strength'] == 30:
        playerMods[3] = 9

def pWisMod():
    if playerStats['Wisdom'] == 1:
        playerMods[4] = -5
    elif playerStats['Wisdom']  == 2 or  playerStats['Strength'] == 3:
        playerMods[4] = -4
    elif playerStats['Wisdom'] == 4 or playerStats['Strength'] == 5:
        playerMods[4] = -3
    elif playerStats['Wisdom'] == 6 or playerStats['Strength'] == 7:
        playerMods[4] = -2
    elif playerStats['Wisdom'] == 8 or playerStats['Strength'] == 9:
        playerMods[4] = -1
    elif playerStats['Wisdom'] == 9 or playerStats['Strength'] == 10:
        playerMods[4] = 0
    elif playerStats['Wisdom'] == 11 or playerStats['Strength'] == 12:
        playerMods[4] = 1
    elif playerStats['Wisdom'] == 13 or playerStats['Strength'] == 14:
        playerMods[4] = 2
    elif playerStats['Wisdom'] == 15 or playerStats['Strength'] == 16:
        playerMods[4] = 3
    elif playerStats['Wisdom'] == 17 or playerStats['Strength'] == 18:
        playerMods[4] = 4
    elif playerStats['Wisdom'] == 19 or playerStats['Strength'] == 20:
        playerMods[4] = 5
    elif playerStat[4] == 21 or playerStats['Strength'] == 22:
        playerMods[4] = 6
    elif playerStats['Wisdom'] == 23 or playerStats['Strength'] == 24:
        playerMods[4] = 7
    elif playerStats['Wisdom'] == 25 or playerStats['Strength'] == 26:
        playerMods[4] = 8
    elif playerStats['Wisdom'] == 27 or playerStats['Strength'] == 28:
        playerMods[4] = 8
    elif playerStats['Wisdom'] == 29 or playerStats['Strength'] == 30:
        playerMods[4] = 9

def pCharMod():

    if playerStats['Charisma'] == 1:
        playerMods[5] = -5
    elif playerStats['Charisma']  == 2 or  playerStats['Strength'] == 3:
        playerMods[5] = -4
    elif playerStats['Charisma'] == 4 or playerStats['Strength'] == 5:
        playerMods[5] = -3
    elif playerStats['Charisma'] == 6 or playerStats['Strength'] == 7:
        playerMods[5] = -2
    elif playerStats['Charisma'] == 8 or playerStats['Strength'] == 9:
        playerMods[5] = -1
    elif playerStats['Charisma'] == 9 or playerStats['Strength'] == 10:
        playerMods[5] = 0
    elif playerStats['Charisma'] == 11 or playerStats['Strength'] == 12:
        playerMods[5] = 1
    elif playerStats['Charisma'] == 13 or playerStats['Strength'] == 14:
        playerMods[5] = 2
    elif playerStats['Charisma'] == 15 or playerStats['Strength'] == 16:
        playerMods[5] = 3
    elif playerStats['Charisma'] == 17 or playerStats['Strength'] == 18:
        playerMods[5] = 4
    elif playerStats['Charisma'] == 19 or playerStats['Strength'] == 20:
        playerMods[5] = 5
    elif playerStat[5] == 21 or playerStats['Strength'] == 22:
        playerMods[5] = 6
    elif playerStats['Charisma'] == 23 or playerStats['Strength'] == 24:
        playerMods[5] = 7
    elif playerStats['Charisma'] == 25 or playerStats['Strength'] == 26:
        playerMods[5] = 8
    elif playerStats['Charisma'] == 27 or playerStats['Strength'] == 28:
        playerMods[5] = 8
    elif playerStats['Charisma'] == 29 or playerStats['Strength'] == 30:
        playerMods[5] = 9
def profUp():
    if playerStats['Level'] in range (1,4):
        playerMods[6] = 2
    if playerStats['Level'] in range (5,8):
        playerMods[6] = 3
    if playerStats['Level'] in range (9,12):
        playerMods[6] = 4
    if playerStats['Level'] in range (13,16):
        playerMods[6] = 5
    if playerStats['Level'] in range (17,20):
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
    human()



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
