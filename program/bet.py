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

class Bet(object):
    
    def __init__(self, value, boardRange, multiplier):
        
        self.value = value
        self.boardRange = boardRange
        self.multiplier = multiplier