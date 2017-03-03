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


def ExtraLanguage():
    speechBoolean = True
    while speechBoolean == True:
        extraLangQuery = input('You get to learn an extra language! \n\n%-20s %20s \n%-20s %20s \n%-20s %20s \n%-20s %20s \n\nPick the language that you would like to learn: ' % 
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
        ExtraLang()
        ExtraLanguage()

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
        ExtraLanguage()

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