from board import Board
from loginSystem import loginScreen
import re
import random
import sys

board = Board()
players = loginScreen(sys.argv[1])
        
playing = True

while playing:
    for player in players:
        betting = True
        while betting:
            print player.name + ", your current balance is: " + str(player.money)
            userInput = raw_input("Please enter your bets:\n")
            
            if userInput == "help":  
                print "List of commands:\n"
                print "<AMOUNT> (red|black|odds|evens)"
                print "<AMOUNT> [0-36] ([0-36] [0-36] [0-36])  (1, 2 or 4)"
                print "<AMOUNT> (first|second) half"
                print "<AMOUNT> (first|second|third) half"
                print "<AMOUNT> (first|second|third) row"
                print "spin"
            elif re.compile("[0-9]+ (red|black|odds|evens)").match(userInput):
                player.addBet(int(userInput.split(" ")[0]), userInput.split(" ")[1], board)       
            elif re.compile("[0-9^ ]+ [0-9]").match(userInput):
                if len(userInput.split(" ")) == 2 or len(userInput.split(" ")) == 3 or len(userInput.split(" ")) == 5:
                    inputRange = []
                    firstIgnoreBoolean = False
                    for stringPart in userInput.split(" "):
                        if firstIgnoreBoolean:
                            inputRange.append(int(stringPart))
                        else:
                            firstIgnoreBoolean = True
                    player.addBet(int(userInput.split(" ")[0]), inputRange, board)
                else:
                    print "Invalid Input"
            elif re.compile("[0-9]+ (first|second) half").match(userInput):
                player.addBet(int(userInput.split(" ")[0]), userInput.split(" ")[1] + " " + userInput.split(" ")[2], board) 
            elif re.compile("[0-9]+ (first|second|third) third").match(userInput):
                player.addBet(int(userInput.split(" ")[0]), userInput.split(" ")[1] + " " + userInput.split(" ")[2], board) 
            elif re.compile("[0-9]+ (first|second|third) row").match(userInput):
                player.addBet(int(userInput.split(" ")[0]), userInput.split(" ")[1] + " " + userInput.split(" ")[2], board) 
            elif userInput.lower() == "spin":
                betting = False
                print player.name + "'s have been placed. Your balance is now " + str(player.money)
            elif userInput.lower() == "quit":
                players.remove(player)
                print player.name + " has quit."
                betting = False
            else:
                print "Invalid input"
                continue
            
    if len(players) > 0:
        result = random.randrange(0, 37)
        print result
        for player in players:
            player.evaluateBets(result, sys.argv[1])
            if player.change > -1:
                print player.name + " won a total of " + str(player.change)
            else:
                print player.name + " lost a total of " + str(player.change)
            print player.name + " now has a balance of " + str(player.money) + "\n"
    else:
        playing = False
        print "The game has ended"
            
            
            
            
            