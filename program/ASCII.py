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

import random
import time
import curses
import sys
from board import Board

def spinner(board):
    out = ""
    for parts in board.singles:
        out = out + "[" + str(parts.number) + "]"
        
    print out
    
    counter = 0
    
    curse = curses.initscr()
    
    while counter < 100:
        randomValue = random.randrange(0, 37)
        position = 0
        doublePosition = 0
        for parts in board.singles:
            if randomValue == parts.number:
                position = position + 1
                break
            else:
                if parts.number > 9:
                    doublePosition = doublePosition + 1
                else:
                    position = position + 1
                continue
        mover = " " + (position * "   ") + (doublePosition * "    ")
        mover = mover[:-3]
        curse.addString("\r" + mover + "^")
        counter = counter + 1
        time.sleep(0.1)
        
board = Board()
spinner(board)