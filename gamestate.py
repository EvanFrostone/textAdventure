import player
import race
import Utilities
import time

def characterCreation(playerNum):
    #In this function, the dialogue and machinery of character creation happens.
    #Character creation WILL change global variables, so this needs only be run ONCE, at the beginning of the game
    index = 0
    num = playerNum
    workNum = playerNum
    players = {'player1' : 0, 'player2' : 0, 'player3' : 0, 'player4' : 0}
    while (num < 0) or (num > 4):
        num = int(input("Error! Only Supports 1-4 Players! How Many Players Are There: "))

    if num == 1:
        players['player1'] = player.playerState()
        players['player1'].name = 'Player1'
    elif num == 2:
        players['player1'] = player.playerState()
        players['player1'].name = 'Player1'
        players['player2'] = player.playerState()
        players['player2'].name = 'Player2'
    elif num == 3:
        players['player1'] = player.playerState()
        players['player1'].name = 'Player1'
        players['player2'] = player.playerState()
        players['player2'].name = 'Player2'
        players['player3'] = player.playerState()
        players['player3'].name = 'Player3'
    elif num == 3:
        players['player1'] = player.playerState()
        players['player1'].name = 'Player1'
        players['player2'] = player.playerState()
        players['player2'].name = 'Player2'
        players['player3'] = player.playerState()
        players['player3'].name = 'Player3'
        players['player4'] = player.playerState()
        players['player4'].name = 'Player4'

    while workNum in range(1,num):
        print('Now you get to choose the race of your character(s).')
        if num > 1:
            print('I see you have a party, this may take some time.')
        



print('Welcome to Dungeons and Dragons: The Python Version')
startQuery = input('Would you like to begin? Enter Yes or No: ')
startQuery = startQuery.lower()

if startQuery == 'yes':
    print('Game started.')
    #time.sleep(1)
    Utilities.clear()
    #characterCreation(int(input('How many players are there?')))
    Utilities.pointBuy(1)

elif startQuery == 'no':
    print('Game didn\'t start')

else:
    Utilities.yesnoErrorMessage()


