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