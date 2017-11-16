"""
Copyright 2015-2017 Hermann Krumrey <hermann@krumreyh.com>

This file is part of roulette.

roulette is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

roulette is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with roulette.  If not, see <http://www.gnu.org/licenses/>.
"""

from player import Player
import re

def loginScreen(filer):
    players = []
    
    loggedIn = False
    login = True
    while login:
        userInputList = raw_input("Please enter you username:\n").split(" ")
        userInput = ""
        for part in userInputList: userInput = userInput + part
        fil = open(filer, "r")
        lines = [line.rstrip('\n') for line in fil]
        fil.close()
        userfound = False
        for line in lines:
            if re.compile(userInput + " [0-9]+").match(line):
                loggedIn = True
                userfound = True
                alreadyLoggedIn = False
                for player in players:
                    if player.name == userInput:
                        alreadyLoggedIn = True
                if alreadyLoggedIn:
                    print userInput + " is already logged in."   
                else:
                    print userInput + " logged in."
                    players.append(Player(userInput, int(line.split(" ")[1])))
        if not userfound:
            newUserLoop = True
            print "This user does not exist, do you want to create this user?"
            while newUserLoop:
                newInput = raw_input("")
                if newInput.lower() == "no":
                    newUserLoop = False
                elif newInput.lower() == "yes":
                    fil = open(filer, "a")
                    fil.write("\n" + userInput + " 5000")
                    fil.close
                    players.append(Player(userInput, 5000))
                    print userInput + " logged in."
                    loggedIn = True
                    newUserLoop = False
                else:
                    print "please enter either yes or no:\n"
        
        if loggedIn:
            continueLoop = True
            while continueLoop:
                continueInput = raw_input("Do you want to add another player?\n")
                if continueInput.lower() == "yes":
                    continueLoop = False
                elif continueInput.lower() == "no":
                    continueLoop = False
                    login = False
                else:
                    print "please enter either yes or no:\n"
                    
    return players