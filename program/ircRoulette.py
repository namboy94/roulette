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

import socket
import sys
import threading 

server = "irc.rizon.net"
channel = "#bots"
botnick = "pynambo"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to server"
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n")
irc.send("NICK "+ botnick +"\n")
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("JOIN "+ channel +"\n")

while 1:
    text=irc.recv(2040)
    print text

    if text.find('PING') != -1:
        irc.send('PONG ' + text.split() [1] + '\r\n')

    if "start roulette" in text.lower():
        print "Roulette!"
        preUser = text.split("!")[0]
        user = preUser.split(":")[1]
        irc.send('PRIVMSG ' + user + ' :OK' + '\r\n')