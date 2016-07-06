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