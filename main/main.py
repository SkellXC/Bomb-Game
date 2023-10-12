from random import randint
# Creates a 10 by 10 array full of zeros using list comprehension
#def create_board():
    #return [[me.map for x in range(10)] for x in range(10)]
    # Creates a 10x10 array full of whatever is stored in me.map.
def create_board():
    local_board = [[me.map for x in range(10)] for x in range(10)]

    for x in range(0,20):# Repeats 15 times for 15 bombs   
        x = randint(0,9)# picks a random number from 1 to 10 for x&y coord
        y = randint(0,9)# 
        local_board[y][x] = 1 # sets it to 1 so that when the player is on 1, the game knows a bomb is in that spot
    local_board[0][0], local_board[9][9] = "x",0# spawn point can't have a bomb
    #board[9][9] = 0# end point can't have a bomb

    return local_board

def showboard(board):
    for item in board:
        item = [str(x) for x in item]# Turns each item in the board into a string
        print(" ".join(item))
        # Goes through each item in the board and prints it neatly

class player:
    def __init__(self, lives, coins, position,map):# Add xp and levels (copy from dank.py)
        self.lives = lives
        self.coins = coins
        #self.position = [0,0]# Starts the player at 0,0
        self.position = position
        self.control_scheme = True
        self.udlr = False
        self.wasd = True
        self.map = map


    def get_coords(self):
        return [self.position[0],self.position[1]]
    def lose_life(self,board):
        self.lives -= 1# Take away lives from the player
        print(f"Uh oh! You hit a bomb and lost a life!\nYou now have {f'{self.lives} lives left' if self.lives != 1 else f'{self.lives} life left'}")
        if self.lives == 0:# check if the player should be dead
            #print(self.lives)
            self.dead(board)
            
        
    def dead(self,board):
        print("You just died! Game Over.")
        board[position[0]][position[1]] = self.map# Removes the 'x' from the end position
        self.position = [0,0]# Resets the player position
        
        exit()    
        # Will add more stuff here sometime soon


    def navigate(self, position, move,board,start = False):
        board[position[0]][position[1]] = self.map
        # Since "x" replaces the 0 to point out where the player is, this resets the previous position to 0
        # before we move the player to the new position
        
        self.control_scheme = "wasd" if self.wasd else "udlr" 
        commands = {"wasd": {"w": [-1, 0], "a": [0, -1], "s": [1, 0], "d": [0, 1]},
                    "udlr": {"u": [-1, 0], "d": [1, 0], "l": [0, -1], "r": [0, 1]}}
        #showboard(board)
        if move in commands[self.control_scheme]:# Checks to see if the move is in the dictionary by using the key stored in "control scheme"
            pos_change = commands[self.control_scheme][move]# Adds the vector to the position
            new_pos = [position[0] + pos_change[0], position[1] + pos_change[1]]# Split it so its easier to read
            if not self.is_valid_position(new_pos,board):
                print("You cannot move there")
                return
            self.position = new_pos# Puts the player on the new position bing bong
            print(f"Moved successfully. You are now at {self.position[1]},{self.position[0]}")# x,y as self.position is in the form y,x
            if board[self.position[0]][self.position[1]] == 1:# Checks for bombs and takes away lives
                self.lose_life(board)
            board[self.position[0]][self.position[1]] = "x"# Marks player position with an 'x'
            showboard(board)                               # this is reset at the start of the function
            print("|---------------------------|")
        else:
            print("This is not a valid move")
        if self.position[0] == 9 and self.position[1] == 9:# Checks if the player has won
            print("|---------------------------|")
            showboard(board)
            self.coins += 10
            print(f"You have reached the end! You now have {self.coins} coins!")
            print("|---------------------------|")
            print("Would you like to play again or return to the main menu?\n1. Play again\n2. Main Menu")
            board[position[0]][position[1]] = self.map # Removes the 'x' from the end position
            self.position = [0,0]# Resets the player position
            ans = input("")
            if ans == "1":
                play()
            else:
                menu()

    def is_valid_position(self, position,board):
        y, x = position
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or board[y][x] == "X":
            return False
        # Ensures that the position is within the confines of the board (10x10) and returns a boolean
        return True




me = player(10,10,[0,0],"-") #Creates a player
#me.navigate(me.position,"u")
def settings():
    print("[+] Settings [+]")
    print("1. Controls\
          \n2. Exit")# The \ is used to continue the string on the next line
    
    ans = input("What would you like to change? ").lower()
    if ans == "1":
        print("[+] Settings -> Controls [+]")
        print("1. WASD")
        print("2. UDLR")
        ans = input("Which mode would you like to it change to? ").lower()
        if ans == "1" or ans == "wasd":
            me.control_scheme = True
            me.udlr, me.wasd = False, True
            print("Mode changed to WASD")
            menu()
        elif ans == "2" or ans == "udlr":
            me.control_scheme = False
            me.udlr,me.wasd = True, False
            print("Mode changed to UDLR")
            menu()
        else:
            print("That is not a valid choice")
            menu()

def menu():# Basic if/else menu
    print("-- Main Menu --\n")
    print("1. Play")
    print("2. Settings")
    print("3. Exit")
    while True:
        choice = input("What would you like to do? ")
        if choice == "1":
            play()
        elif choice == "2":
            settings()
        elif choice == "3":
            print("Hope you had fun!")
            exit()
        else:
            print("That is not a valid choice")


#board:list = create_board()
#add_bombs(board)
def play():
   
   local_board = create_board()
   showboard(local_board) 
   print(f"Which direction do you want to move in? Use {f'WASD' if me.wasd else f'UDLR'} to move.")
   while True:
        move = input("").lower()
        me.navigate(me.position,move,local_board)

print("Welcome to the bomb game!\n")            
menu()
#11:12 no longer know what I'm doing
"""
Custom controls
Levels and xp
Harder modes
nxn boards
customize character (name, color, etc)
customize board
maps
Blind character and only allow them to see a certain area around them
Chain bombs
"""
