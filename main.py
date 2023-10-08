from random import randint
board = [[0 for x in range(10)] for x in range(10)]
# Creates a 10 by 10 array full of zeros using list comprehension

def add_bombs(board):
    for x in range(0,15):# Repeats 15 times for 15 bombs
        x = randint(0,10)# picks a random number from 1 to 10 for x coord
        y = randint(0,10)# and for the y cord 
        board[x][y] = 1# sets it to 1 so that when the player is on 1, the game knows a bomb is in that spot
    return board

class player:
    def __init__(self, lives, coins):#add xp and levels (copy from dank.py)
        self.lives = lives
        self.coins = coins

    def lose_life(self,lives):
        print(f"Uh oh! You hit a bomb and lost a life!\nYou now have {f'{self.lives} lives left' if self.lives > 1 else '1 life left'}")

    def dead(self):
        print("You just died! Game over.")
        #Will add more stuff here sometime soon

me = player(3,10)
