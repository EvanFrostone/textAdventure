import random
import os

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
    import dungeonsSkeleton
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
