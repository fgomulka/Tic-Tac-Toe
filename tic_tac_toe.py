#!/usr/bin/env python3
import random
import math
from datetime import datetime, timedelta

def login (username):
    with open("stats.txt", "r") as f:
        lines = f.readlines()
        found = False
        for line in lines:
            line = line.strip()
            splitline = line.split("~")
            if splitline[0] == username:
                passwordinput = input("Input your password: ")
                if passwordinput == splitline[3]:
                    return True
                else:
                    return False
    with open("stats.txt", "a") as f:
        response = input("Hello new user! please input a password you would like to use. ")
        newline = username + "~" + "0" + "~" + "0" + "~" + response + "\n"
        f.write(newline)

def recordwin (winner, loser):
    with open("stats.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0) 
        f.truncate(0)
        found = False
        for line in lines:
            line = line.strip()
            splitline = line.split("~")
            if splitline[0] == winner:
                wins = int(splitline[1]) + 1
                level = str(int(math.sqrt(wins)))
                print(F"{winner} is currently level: {level}")
                winstreak = int(splitline[2]) + 1
                currenctwinstreak = str(winstreak)
                print(F"Winner's current winstreak: {currenctwinstreak}")
                newline = winner + "~" + str(wins) + "~" + str(winstreak) + "~" + str(splitline[3]) + "\n"
                f.write(newline)
                found = True
            elif splitline[0] == loser:
                wins = int(splitline[1]) 
                winstreak = 0
                newline = loser + "~" + str(wins) + "~" + str(winstreak) + "~" + str(splitline[3]) + "\n"
                f.write(newline)
            else:
                line = line + "\n"
                f.write(line)
        if found == False:
            newline = winner + "~" + "1" + "~" + "1" + "~" + str(splitline[3]) + "\n"
            f.write(newline)
            print("I see you have no previous wins, congrats on the win! Your wins can be found in the appropriate place and your winstreak is now 1")
def printtoprow (p1moves, p2moves):    
    print("  ", end="")
    if("tl" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("tl" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("tm" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("tm" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("tr" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("tr" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("")

def printmiddlerow (p1moves, p2moves):    
    print("  ", end="")
    if("ml" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("ml" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("mm" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("mm" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("mr" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("mr" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("")

def printbottomrow (p1moves, p2moves):    
    print("  ", end="")
    if("bl" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("bl" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("bm" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("bm" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("|  ", end="")
    if("br" in p1moves):
        print("X", end="")
        print("  ", end="")
    elif("br" in p2moves):
        print("O", end="")
        print("  ", end="")
    else:
        print("   ", end="")
    print("")

'''
     |     |
** **|** **|** ** 
_____|_____|_____
     |     |     
** **|** **|** **   
_____|_____|_____
     |     |     
** **|** **|** **    
     |     |
'''

def printboard (p1moves, p2moves):     
    print("     |     |")     
    printtoprow(p1moves, p2moves)
    print("_____|_____|_____")     
    print("     |     |")     
    printmiddlerow(p1moves, p2moves)
    print("_____|_____|_____")   
    print("     |     |")     
    printbottomrow(p1moves, p2moves)
    print("     |     |")   

def checkforresult (p1, p2, p1moves, p2moves):
    winningconditions = [{"br", "mr", "tr"}, {"bl", "ml", "tl"}, {"bm", "mm", "tm" }, {"tl", "mm", "br"}, {"tr", "mm", "bl"}, {"tl", "tm", "tr"}, {"ml", "mm", "mr"}, {"bl", "bm", "br"}]
    if(len(p1moves) + len(p2moves) >= 9):
        print("You have tied each other! There is no winner")
        return True
    for w in winningconditions:
        if w.issubset(p1moves):
            print(F"{p1} wins")
            recordwin(p1, p2)
            print(F"{p1} you have won this match! *note every time you win match you will gain +1 to your wins and +1 to your winstreak")
            return True
        elif w.issubset(p2moves):
            print(F"{p2} wns") 
            recordwin(p2, p1)
            print(F"{p2} you have won this match! *note every time you win match you will gain +1 to your wins and +1 to your winstreak")
            return True
    return False


if __name__ == "__main__": 
    startupmessages = ["welcome to tic tac toe", "this is tic tac hand not tic tac toe, wdym", "tic tac toe? never heard of it", "What kind of breath mint can help you get a lot of xoxo? A Tic Tac Toe", ' "You must always look twice before you cross," I advised my son. I take Tic-Tac-Toe very seriously. ']
    print (random.choice(startupmessages))    
    stillplaying = True
    while(stillplaying == True):

        p1 = input("Enter player 1's username ") 
        result = login (p1)
        while(result == False):
            print("That password is incorrect, please try again")
            result = login (p1)
        print("Password correctly and successfully inputed!")
        p2 = input("Enter player 2's username ")
        result = login (p2)
        while(result == False):
            print("That password is incorrect, please try again")
            result = login (p2)
        print("Password correctly and successfully inputed!")
        start = datetime.now()
        Player1TurnCounter = 0
        Player2TurnCounter = 0       
        TotalTurnCounter = 0
        p1time = []
        p2time = []
        p1moves = set()
        p2moves = set()
        while (True):
            printboard(p1moves, p2moves)
            if TotalTurnCounter % 2 == 0:
                print(f"{p1}'s turn ") 
                print(p1moves)
                p1start = datetime.now()
                p1move = input("Please input your move: ")                
                p1moves.add(p1move)
                p1end = datetime.now()
                p1time.append(p1end - p1start)
                Player1TurnCounter += 1
            else:      
                print(f"{p2}'s turn ")
                print(p2moves)
                p2start = datetime.now()
                p2move = input("Please input your move: ")
                p2moves.add(p2move)
                p2end = datetime.now()
                p2time.append(p2end - p2start)
                Player2TurnCounter += 1 
            result = checkforresult(p1, p2, p1moves, p2moves)
            TotalTurnCounter += 1
            if result == True:
                printboard(p1moves, p2moves)
                break
        end = datetime.now()
        print(f"During the match {end - start} was the total time spent between both players")
        print(f"During the match {(list(map(datetime.strptime, p1time)))} was the time player 1 spent on each move")
        print(f"During the match {sum(p1time, timedelta())} was the total time player 1 spent")
        print(f"During the match {p2time} was the time player 2 spent on each move")
        print(f"During the match {sum(p2time, timedelta())} was the total time player 2 spent")
        print(f"During the game, between both players, {TotalTurnCounter} moves were made")
        print(f"Player 1 made {Player1TurnCounter} moves in total" )
        print(f"Player 2 made {Player2TurnCounter} moves in total" )
        playorquit = input("would you like to play again or quit?, type play again to play again and type quit if you want to quit ")
        if (playorquit == "quit"):
            stillplaying = False
            print ("Thanks for playing tic tac toe! -Lucas")