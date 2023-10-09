from math import e
from random import randint
from turtle import pos
board = [[0 for x in range(10)] for x in range(10)]
# Creates a 10 by 10 array full of zeros using list comprehension

def add_bombs(board):
    for x in range(0,15):# Repeats 15 times for 15 bombs
        x = randint(0,9)# picks a random number from 1 to 10 for x&y coord
        y = randint(0,9)# 
        #print(x,y)
        board[y][x] = 1 # sets it to 1 so that when the player is on 1, the game knows a bomb is in that spot
    board[0][0] = 0# spawn point can't have a bomb
    board[9][9] = 0# end point can't have a bomb
    return board

def showboard(board):
    for item in board:
        print(item)
        # Goes through each item in the board and prints it neatly

class player:
    def __init__(self, lives, coins, position):# Add xp and levels (copy from dank.py)
        self.lives = lives
        self.coins = coins
        #self.position = [0,0]# Starts the player at 0,0
        self.position = position
    def get_coords(self):
        return [self.position[0],self.position[1]]
    def lose_life(self):
        self.lives -= 1# Take away lives from the player
        print(f"Uh oh! You hit a bomb and lost a life!\nYou now have {f'{self.lives} lives left' if self.lives != 1 else f'{self.lives} life left'}")
        if self.lives == 0:# check if the player should be dead
            #print(self.lives)
            self.dead()
            
        
    def dead(self):
        print("You just died! Game Over.")
        exit()
        
        # Will add more stuff here sometime soon

    def traverse(self,position,move):# Coords in the form y,x
        if move == "l":# left
            if position[1] == 0:
                print("You can't go any further left")
            else:
                self.position[1] -= 1
                print(f"Moved successfully. You are now at {self.position} (y,x)")
            
            
        elif move == "r":# right
            if position[1] == 9:
                print("You can't go any further right")
            else:
                self.position[1] += 1
                print(f"Moved successfully. You are now at {self.position} (y,x)")
            
        elif move == "u":# up
            if position[0] == 0:
                print("You can't go any further up")
            else:
                self.position[0] -= 1
                print(f"Moved successfully. You are now at {self.position} (y,x)")

        elif move == "d":# down
             if position[0] == 9:
                print("You can't go any further down")
             else:
                self.position[0] += 1
                print(f"Moved successfully. You are now at {self.position} (y,x)")

        else:
            print("This is not a valid move")
            #move = input("Use U/D/L/R\n").lower()
        if board[self.position[0]][self.position[1]] == 1:
            self.lose_life()
        if position[0] == 9 and position[1] == 9:
            self.coins += 10
            print(f"You have reached the end! You now have {self.coins} coins!")
            exit()


add_bombs(board)
showboard(board)


me = player(1,10,[0,0])
#me.lose_life()
me.traverse(me.position,"u")
def play():
   print("Which direction do you want to move in? Use U/D/L/R")
   while True:
        move = input("").lower()
        me.traverse(me.position,move)

            
play()
