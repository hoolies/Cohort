#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""



def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print("---------------------------")

# movement function
def movement(direction, cc):
    if direction=="north":
        cc=[cc[0]+1,cc[1]]
    elif direction=="south":
        cc=[cc[0]-1,cc[1]]
    elif direction=="east":
        cc=[cc[0],cc[1]+1]
    elif direction=="west":
        cc=[cc[0],cc[1]-1]
    else:
        print("You died")
        return
    return cc


# list of coordinates [north, south, east, west]
cc = [0,0]
previous_coordinates = [0,0]

# an inventory, which is initially empty
inventory = []

# types of rooms
# room_names=["bedroom", "bathroom", "hallway", "kitchen", "sunroom", "basement", "dungeon"]

# direction dictionary
rooms= {
    "kitchen": [-1,0],
    "living room": [0,-1],
    "hall": [0,0],
    "bedroom": [1,0],
    "bathroom": [0,1],
    "garage": [0,2]
}

#list for movement check
move_check=["north", "south", "east", "west"]


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()


# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')    
    move = move.lower().split(" ", 1)
    #if they type 'go' first
    if move[0] == 'go':
        direction = move[1]
        #check that they are allowed wherever they want to go
        if direction in move_check:
            previous_coordinates = cc
            cc=movement(direction,cc)
            if cc in rooms.values():
                for k,v in rooms.items():
                    if v == cc:
                        currentRoom=k
            else:
                print("You have died!")
                exit()
    else:
        print("select from:\n", *move_check)
