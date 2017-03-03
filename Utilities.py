import random
import dungeonsSkeleton

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