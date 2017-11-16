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

from boardPart import BoardPart
class Board(object):
    
    def __init__(self):

        boardParts = []
        
        boardParts.append(BoardPart("green", 0))
        boardParts.append(BoardPart("red", 32))
        boardParts.append(BoardPart("black", 15)) 
        boardParts.append(BoardPart("red", 19))
        boardParts.append(BoardPart("black", 4))
        boardParts.append(BoardPart("red", 21))
        boardParts.append(BoardPart("black", 2))
        boardParts.append(BoardPart("red", 25))
        boardParts.append(BoardPart("black", 17))
        boardParts.append(BoardPart("red", 34))
        boardParts.append(BoardPart("black", 6))
        boardParts.append(BoardPart("red", 27))
        boardParts.append(BoardPart("black", 13))
        boardParts.append(BoardPart("red", 36))
        boardParts.append(BoardPart("black", 11))
        boardParts.append(BoardPart("red", 30))
        boardParts.append(BoardPart("black", 8))
        boardParts.append(BoardPart("red", 23))
        boardParts.append(BoardPart("black", 10))
        boardParts.append(BoardPart("red", 5))
        boardParts.append(BoardPart("black", 24))
        boardParts.append(BoardPart("red", 16))
        boardParts.append(BoardPart("black", 33))
        boardParts.append(BoardPart("red", 1))
        boardParts.append(BoardPart("black", 20))
        boardParts.append(BoardPart("red", 14))
        boardParts.append(BoardPart("black", 31))
        boardParts.append(BoardPart("red", 9))
        boardParts.append(BoardPart("black", 22))
        boardParts.append(BoardPart("red", 18))
        boardParts.append(BoardPart("black", 29))
        boardParts.append(BoardPart("red", 7))
        boardParts.append(BoardPart("black", 28))
        boardParts.append(BoardPart("red", 12))
        boardParts.append(BoardPart("black", 35))
        boardParts.append(BoardPart("red", 3))
        boardParts.append(BoardPart("black", 26))
        
        self.singles = boardParts
        self.evens = []
        self.odds = []
        self.reds = []
        self.blacks = []
        self.firstRow = []
        self.secondRow = []
        self.thirdRow = []
        self.firstThird = []
        self.secondThird = []
        self.thirdThird = []
        self.firstHalf = []
        self.secondHalf = []
        
        for part in boardParts:
            
            if (part.number % 2) == 0 and part.number != 0:
                self.evens.append(part)
            elif (part.number % 2) == 1:
                self.odds.append(part)
            
            if part.colour == "red":
                self.reds.append(part)
            elif part.colour == "black":
                self.blacks.append(part)
            
            if (part.number % 3) == 1:
                self.firstRow.append(part)
            elif (part.number % 3) == 2:
                self.secondRow.append(part)
            elif (part.number % 3) == 0 and part.number != 0:
                self.thirdRow.append(part)
            
            if part.number > 0 and part.number < 13:
                self.firstThird.append(part)
            elif part.number > 12 and part.number < 25:
                self.secondThird.append(part)
            elif part.number > 24 and part.number < 37:
                self.thirdThird.append(part)
                
            if part.number > 0 and part.number < 19:
                self.firstHalf.append(part)
            elif part.number > 18 and part.number < 37:
                self.secondHalf.append(part)
        