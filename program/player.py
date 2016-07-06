from bet import Bet
from boardPart import BoardPart
import sys

class Player(object):
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.money2 = money
        self.bets = []
        
    def addBet(self, value, betType, board):
        
        self.money = self.money - value
        if betType == "red":
            self.bets.append(Bet(value, board.reds, 2))
        elif betType == "black":
            self.bets.append(Bet(value, board.blacks, 2))
        elif betType == "odds":
            self.bets.append(Bet(value, board.odds, 2))
        elif betType == "evens":
            self.bets.append(Bet(value, board.evens, 2))
        elif betType == "first half":
            self.bets.append(Bet(value, board.firstHalf, 2))
        elif betType == "second half":
            self.bets.append(Bet(value, board.secondHalf, 2))
        elif betType == "first third":
            self.bets.append(Bet(value, board.firstThird, 3))
        elif betType == "second third":
            self.bets.append(Bet(value, board.secondThird, 3))
        elif betType == "third third":
            self.bets.append(Bet(value, board.thirdThird, 3))
        elif betType == "first row":
            self.bets.append(Bet(value, board.firstRow, 3))
        elif betType == "second row":
            self.bets.append(Bet(value, board.secondRow, 3))
        elif betType == "third row":
            self.bets.append(Bet(value, board.thirdRow, 3))
        elif len(betType) == 1:
            singleRange = []
            singleRange.append(BoardPart(int(betType[0]), "undef"))
            self.bets.append(Bet(value, singleRange, 36))
        elif len(betType) == 2:
            singleRange = []
            singleRange.append(BoardPart(int(betType[0]), "undef"))
            singleRange.append(BoardPart(int(betType[1]), "undef"))
            self.bets.append(Bet(value, singleRange, 18))
        elif len(betType) == 4:
            singleRange = []
            singleRange.append(BoardPart(int(betType[0]), "undef"))
            singleRange.append(BoardPart(int(betType[1]), "undef"))
            singleRange.append(BoardPart(int(betType[2]), "undef"))
            singleRange.append(BoardPart(int(betType[3]), "undef"))
            self.bets.append(Bet(value, singleRange, 9))
        else:
            print "Error while betting"
            sys.exit(1)

    def evaluateBets(self, result, userFile):
        for bet in self.bets:
            for value in bet.boardRange:
                if value.number == result:
                    print self.name + " success"
                    profit = bet.multiplier * bet.value
                    self.money = self.money + profit
        self.change = self.money - self.money2
        
        self.flushBets()
        fil = open(userFile, "r")
        lines = [line.rstrip('\n') for line in fil]
        fil.close()
        fil = open(userFile, "w")
        fil.close()
        fil = open(userFile, "a")
        firstLine = True
        for line in lines:
            if not firstLine:
                newLine = "\n"
            else:
                newLine = ""
                firstLine = False
            if line == (self.name + " " + str(self.money2)):
                fil.write(newLine + self.name + " " + str(self.money))
            else:
                fil.write(newLine + line)               
        self.money2 = self.money
            
    def flushBets(self):
        self.bets = []