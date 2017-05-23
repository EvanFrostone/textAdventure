import time
import random
import os


class playerState:
    name = 'Name'
    race = 'Race'
    Class = 'Class'
    alignment = 'Alignment'
    background = 'Background'

    #This is the player's inventory. Add items to it using the .append() function.
    inventory =['Empty']

    health = 0
    gold = 0
    level = 1
    xp = 0
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
    
class race:
    name = "Race Name"
    #Stats
    strength = 0
    constitution = 0
    dexterity = 0
    intelligence = 0
    wisodom = 0
    charisma = 0
    maxHealth = 0
    armorClass = 0
    initiative = 0

    #Modifier
    strengthMod = 0
    constitutionMod = 0
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


  

class Dwarf():
    
    def __init__ (self):
        self.race = 'Dwarf'
        race.constitution += 2
        race.profbattleAxe = True
        race.profhandAxe = True
        race.profthrowingHammer = True
        race.profwarHammer = True
        race.speaksCommon = True
        race.speaksDwarvish = True
        race.profDarkVision = True

class HillDwarf(Dwarf):
    def __init__(self):
        self.race = 'Hill Dwarf'
        race.strength += 2
        race.profLightArmor = True
        race.profMediumArmor = True
        race.constitution += 2
        race.profbattleAxe = True
        race.profhandAxe = True
        race.profthrowingHammer = True
        race.profwarHammer = True
        race.speaksCommon = True
        race.speaksDwarvish = True
        race.profDarkVision = True

class Elf():
    def __init__(self):
        self.race = 'Elf'
        race.dexterity += 2
        race.profDarkVision = True
        race.profPerception = True
        race.profFeyAncestry = True
        race.speaksCommon = True
        race.speaksElvish = True

class HighElf(Elf):
    
    def __init__ (self):
        self.race = 'High Elf'
        race.proflongSword = True
        race.profshortBow = True
        race.proflongBow = True
        race.profshortSword = True
        race.intelligence += 1
        race.dexterity += 2
        race.profDarkVision = True
        race.profPerception = True
        race.profFeyAncestry = True
        race.speaksCommon = True
        race.speaksElvish = True
        Utilities.ExtraLanguage()

class WoodElf():
   
    def __init__ (self):
        self.race = 'High Elf'
        race.proflongSword = True
        race.profshortBow = True
        race.proflongBow = True
        race.profshortSword = True
        race.profmaskoftheWild = True
        race.wisdom += 1
        race.dexterity += 2
        race.prof.DarkVision = True
        race.profPerception = True
        race.profFeyAncestry = True
        race.speaksCommon = True
        race.speaksElvish = True

class Drow():
 
    def __init__ (self):
        self.race = 'Drow'
        race.profrapiers = True
        race.profshortSword = True
        race.profhandCrossbow = True
        race.profsupDarkVision = True
        race.charisma += 1
        race.dexterity += 2
        race.profDarkVision = True
        race.profPerception = True
        race.profFeyAncestry = True
        race.speaksCommon = True
        race.speaksElvish = True

class Halfling():
    def __init__ (self):
        self.race = 'Halfling'
        race.speaksHalfling = True
        race.dexterity += 2

class LightFootHalf():
    
    def __init__ (self):
        self.race = 'Lightfoot Halfling'
        race.charisma += 1
        race.speaksHalfling = True
        race.dexterity += 2

class StoutHalf(Halfling):

    def __init__(self):
        self.race = 'Stout Halfling'
        race.constitution += 1
        race.speaksHalfling = True
        race.dexterity += 2

class Human():
    #Not Done
    def __init__ (self):
        self.race = 'Human'
        race.strength += 1
        race.constitution += 1
        race.dexterity += 1
        race.intelligence += 1
        race.wisdom += 1
        race.charisma += 1
        Utilities.ExtraLanguage()

class Dragonborn():
    pass
    def __init__(self):
        self.race = 'Dragonborn'

class Gnome():
    def __init__(self):
        self.race = 'Gnome'
        race.profDarkVision = True
        race.intelligence += 2

class ForestGnome(Gnome):
    def __init__(self):
        self.race = 'Forest Gnome'
        race.dexterity += 1
        race.profDarkVision = True
        race.intelligence += 2

class RockGnome(Gnome):
    def __init__(self):
        self.race = 'Rock Gnome'
        race.profTinkerTools = True
        race.constitution += 1
        race.profDarkVision = True
        race.intelligence += 2

class HalfElf():
    #NOT Done
    def __init__(self):
        self.race = 'Half Elf'
        race.profDarkVision = True
        race.profFeyAncestry = True
        race.speaksCommon = True
        race.speaksElvish = True
        race.charisma += 2
        ExtraLanguage()
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
                            Player.strength += 1
                        elif statQuery1 == 'constitution': 
                            Player.constituion += 1
                        elif statQuery1 == 'dexterity': 
                            Player.dexterity += 1
                        elif statQuery1 == 'intelligence': 
                            Player.intelligence += 1
                        elif statQuery1 == 'wisdom':
                            Player.wisdom += 1
                        elif statQuery1 == 'charisma': 
                            Player.charisma += 1
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
                        player.strength = player.strength + 1
                    elif statQuery2 == 'constitution': 
                        player.constituion = player.constituion + 1
                    elif statQuery2 == 'dexterity': 
                        player.dexterity = player.dexterity + 1
                    elif statQuery2 == 'intelligence': 
                        player.wisdom = player.wisdom + 1
                    elif statQuery2 == 'wisdom':
                        player.wisdom = player.wisdom + 1
                    elif statQuery2 == 'charisma': 
                        player.charisma = player.charisma + 1
                    secondaryConfirmationError = False
                    checkStatQuery2 = False
                elif statQuery2query == 'no':
                    secondaryConfirmationError = False
                    checkStatQuery2 = True
                else:
                    print('Sorry, I didn\'t understand what you said. Please respond with (yes or no).')
                    textWait(2)
                    secondaryConfirmationError = True




def textWait(wait):
    #This is the average amount of pause between printed lines of text. Call this function to get pauses.
    time.sleep(wait)
    



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
    Utilities.clear()

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


class Utilities:
    

    def clear():
        #This function clears the screen of EVERYTHING. Use if the console is getting a little crowded
        os.system('cls')
        
    def yesnoErrorMessage():
        print('I\'m not quite sure what you said. Please answer with yes or no!')

    def errorMessage():
        print('I\'m not quite sure what you said. Please try again!')



    def dice(rolls,size):
    #This function rolls dice for you.
    #Put in the number of rolls and the size of dice you want rolled
    #dice( 10 , 5 ) to roll  10 D5's
        result = []
        processingRolls = rolls
        while processingRolls != 0:
            processingRolls -= 1
            result.append(random.randint( 0 , size ))

    def ExtraLanguage(self):
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
                    self.speaksThievesCant = True
                    speechBoolean = False
                
            elif extraLangQuery == 'dwarvish':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
            

                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks %s' % (extraLangQuery))
                    self.speaksDwarvish = True
                    speechBoolean = False


            elif extraLangQuery == 'halfling':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
        

                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks %s' % (extraLangQuery))
                    self.speaksHalfling = True
                    speechBoolean = False


            elif extraLangQuery == 'draconic':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))

                    
                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks %s!' % (extraLangQuery))
                    self.speaksDraconic = True
                    speechBoolean = False


            elif extraLangQuery == 'gnomish':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
                

                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks %s' % (extraLangQuery))
                    self.speaksGnomish = True
                    speechBoolean = False


            elif extraLangQuery == 'orcish':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))


                if confirmationQuery.lower() == 'yes':
                    print('Alright, your character now speaks %s' % (extraLangQuery))
                    self.speaksOrc = True
                    speechBoolean = False


            elif extraLangQuery == 'infernal':
                confirmationQuery = input('Are you sure you want to speak %s?\nAnswer yes or no: ' % (extraLangQuery))
            
                if confirmationQuery.lower() == 'yes':
                        print('Alright, your character now speaks %s' % (extraLangQuery))
                        self.speaksInfernal = True
                        speechBoolean = False

    class wholeLvlUp():
        
        def levelUp(Player):
            lvlUpTuple = ( 0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000 )

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
                
        def pStrMod(Player):
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

        def pConMod(Player):
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

        def pDexMod(Player):
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

        def pIntMod(Player):
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

        def pWisMod(Player):
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

        def pCharMod(Player):
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
        def profUp(Player):
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

    def pointBuy(playerNum):
        print('Alright Player', playerNum, ', you\'re first.')
        time.sleep(1)
        print('First things first, we\'re going to divy up attributes.')
        time.sleep(1)
        print('To make this easy, we\'ll do focuses. You will pick two attributes you want to be strong in, and the rest of the points will be equally spread out across the remaining attributes.')
        time.sleep(3)
        firstPick = input('Out of \n\n%-20s %15s \n%-20s %17s \n%-20s %20s %20s \n\nPick the skill you\'d like to be the strongest in: ' % 
                ('1. Strength ', '5. Wisdom ', '2. Dexterity', '6. Charisma ', '3. Constitution', '4. Intelligence', ''))
        while firstPick.lower != 'strength' or firstPick.lower != 'wisdom' or firstPick.lower != 'dexterity' or firstPick.lower != 'charisma' or firstPick.lower != 'constitution' or firstPick.lower != 'intelligence':
            firstPick = input('Error! What you said was not Strength, Dexterity, Constitution, Intelligence, Wisdom, or Charisma. Please try again: ')
        if firstPick == 'strength':
            return False

intro()