#!/usr/bin/env python3
"""A simple text adventure game"""

# Import all libraries needed for the game
from dataclasses import dataclass
from random import randint
from time import sleep


# Define the player class
@dataclass
class Mobs:
    name: str
    hp: int
    strength: int
    agility: int
    defense: int


def mob_generator(min_num: int ,max_num: int) -> object:
    """Generates a random mob from a list of mobs with random stats"""
    Mobs_list = [
    {"Name":"Skeleton", "hp": [1, 5], "strength": [1, 5], "agility": [1, 5], "defense": [1,1]},
    {"Name":"Slime", "hp": [1, 5], "strength": [1, 5], "agility": [1, 5], "defense": [1, 1]},
    {"Name":"Spider", "hp": [1, 5], "strength": [1, 5], "agility": [5, 7], "defense": [1, 5]},
    {"Name":"Bat", "hp": [1, 5], "strength": [1, 1], "agility": [5, 10], "defense": [1, 1]},
    {"Name":"Rat", "hp": [1, 5], "strength": [1, 1], "agility": [5, 10], "defense": [1, 1]},
    {"Name":"Goblin", "hp": [10, 25], "strength": [2, 10], "agility": [5, 10], "defense": [1, 5]},
    {"Name":"Orc", "hp": [40, 50], "strength": [10, 15], "agility": [1, 5], "defense": [5, 10]},
    {"Name":"Troll", "hp": [60, 80], "strength": [15, 20], "agility": [5, 10], "defense": [5, 10]},
    {"Name":"Ogre", "hp": [80, 100], "strength": [20, 25], "agility": [1, 3], "defense": [50, 80]},
    {"Name":"Cyclops", "hp": [80, 100], "strength": [20, 25], "agility": [1, 3], "defense": [50, 80]},
    {"Name":"Centaurs", "hp": [80, 100], "strength": [20, 25], "agility": [1, 3], "defense": [50, 80]},
    {"Name":"Dragon", "hp": [300, 500], "strength": [100, 150], "agility": [10, 15], "defense": [100, 150]}
]
    # Selects a random number between minimum and maximum
    rng = int(randint(min_num, max_num))
    
    # Generate a monster that matches the number above with random stats
    name = Mobs_list[rng]['Name']
    hp = randint(Mobs_list[rng]['hp'][0],Mobs_list[rng]['hp'][1])
    strength = randint(Mobs_list[rng]['strength'][0],Mobs_list[rng]['strength'][1])
    agility = randint(Mobs_list[rng]['agility'][0],Mobs_list[rng]['agility'][1])
    defense = randint(Mobs_list[rng]['defense'][0],Mobs_list[rng]['defense'][1])
    if name == "Dragon":
        print("Imminent death is upon you. The dragon has spotted you. You must fight it.")
    elif name == "Orge" or name == "Cyclops" or name == "Centaur":
        print("You have encountered a mythical creature.")
        sleep(1)
        print("Be careful.")
    return Mobs(name, hp, strength, agility, defense)


def initiate_player() -> object:
    """Initiate the player"""
    player_name = input("What is your name, mortal?\n")
    player = Mobs(player_name, randint(80,150), randint(5,15), randint(5,15), randint(1,10))
    return player


def battle_system(player: object,mob: object, score: int)-> object:
    """Battle system for the game"""
    if player.agility >= mob.agility:
        while player.hp > 0 or mob.hp > 0:
            print(f"You attack the {mob.name}")
            mob.hp = mob.hp - ((player.strength * player.agility) // mob.defense)
            if mob.hp <= 0:
                print(f"You have defeated the {mob.name}")
                if mob.name == "Dragon":
                    print("Congratulations, dragon slayer.")
                    sleep(1)
                    print(f"You open your eyes and you are back in your bed.\nIt was all a dream\n\n\nYour score is {score}!!")
                    exit()
                break
            else:
                print(f"The {mob.name} has {mob.hp} hp left")
                sleep(1)
                print(f"The {mob.name} attacks you")
                player.hp = player.hp - ((mob.strength * mob.agility) // player.defense) 
                print(f"You have {player.hp} hp left")
                sleep(1)
                if player.hp <= 0:
                    print(f"You have died\n\nYou score is {score}!!")
                    exit()
    else:
        while player.hp > 0 or mob.hp > 0:
            print(f"The {mob.name} attacks you")
            player.hp = player.hp - ((mob.strength * mob.agility) // player.defense)
            if player.hp <= 0:
                print(f"You have died\n\nYou score is {score}!!")
                exit()
            else:
                print(f"You have {player.hp} hp left")
                sleep(1)
                print(f"You attack the {mob.name}")
                mob.hp = (mob.hp - ((player.strength * player.agility) // mob.defense))
                sleep(1)
                if mob.hp <= 0:
                    if mob.name == "Dragon":
                        print("\n\nCongratulations, dragon slayer.\n")
                        sleep(1)
                        print(f"You open your eyes and you are back in your bed.\n")
                        sleep(1)
                        print("It was all a dream\n\n\nYour score is {score}!!")
                        exit()
                    print(f"\nYou have defeated the {mob.name}\n")
                    break
                print(f"The {mob.name} has {mob.hp} hp left")
    print(f"\n\nYou absorb the {mob.name}'s soul and you feel stronger\n")
    
    # Upgrade the player's stats
    player.hp += randint(score,1)
    player.strength += randint(1,mob.strength)
    player.agility += randint(1,mob.agility)
    player.defense += randint(1,mob.defense)
    return player


def fight(player, mob):
    """Fight a mob"""
    print(f"""
        You are fighting a {mob.name}
        HP: {mob.hp}
        Strength: {mob.strength}
        Agility: {mob.agility}
        Defense: {mob.defense}

        Your stats are:
        HP: {player.hp}
        Strength: {player.strength}
        Agility: {player.agility}
        Defense: {player.defense}
    """) 
    print("What would you like to do?")
    print("\t1. Fight")
    print("\t2. Run")
    print("\t3. Hide")
    choice = int(input("\n\n\n#: "))
    if choice == 1:
        battle_system(player, mob, score)
    elif choice == 2:
        rng =  randint(1, 10)
        if rng == 1:
            print(f"\nYou tried to run away but {mob.name} was able to catch you.")
            sleep(1)
            print("\n\nYou died")
            print(f"\nYour score is {score}!!")
            exit()
        else:
            print("\nYou have escaped this time. But you will have to fight again\n")
            return player
    elif choice == 3:
        hide(player, mob)
        return player
    else:
        print(f"You were panicked...")
        sleep(1)
        print(f"The {mob.name} was able to catch you off guard.")
        sleep(1)
        print("\n\nYou died")
        print(f"\nYour score is {score}!!")
        exit()

def movement(direction, cc, score):
    if direction=="north":
        cc=[cc[0],cc[1]+1]
    elif direction=="south":
        cc=[cc[0],cc[1]-1]
    elif direction=="east":
        cc=[cc[0]+1,cc[1]]
    elif direction=="west":
        cc=[cc[0]-1,cc[1]]
    else:
        print("You have lost your way and died")
        print(f"\nYour score is {score}!!")
        exit()
    return cc


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        hide (hides in the shadows)
        fight (fights the monster)
        quit (to end the game)
        help (to show this menu again)
    ''')

def command_check(command, cc, score):
    """Checks the command"""
    #if they type 'go' first
    if command[0] == 'go':
        direction = command[1]
        #check that they are allowed wherever they want to go
        if direction in move_check:
            # Change the coordinates of the player
            cc = movement(command[1],cc, score)
            return cc
        else:
            print("You have lost your way and died")
            print(f"\nYour score is {score}!!")
            exit()
    elif command[0] == "quit":
        print('Hahahaha, you can\'t quit. You are stuck here forever')
    elif command[0] == "help":
        showInstructions()
    else:
        print("Invalid command")
        showInstructions()
    return cc

def showStatus(croom,cc):
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ', croom)
    # Print the coordinates
    print("---------------------------")
    print(f"Your coordinates are: x: {cc[0]}, y: {cc[1]}")
    return

def hide(player,mob):
    """Hides the player in the shadows"""
    print("You hide in the shadows")
    rng = randint(1, 10)
    if rng == 1:
        print("You have been spotted")
        fight(player, mob)
    else:
        print("You have become one with the shadows. You can now move freely")
        return player

def spawn_mob(score):
    """Spawns a mob"""
    rng = randint(1, 9)
    if rng == 1:
        print("There are no monsters nearby.\nYou are safe, for now!\n")
        return None
    else:
        if score < 7:
            mob = mob_generator(0,5)
        elif score <= 12 and score >= 8:
            mob = mob_generator(6,7)
        elif score < 22 and score > 12:
            mob = mob_generator(7, 10)
        else:
            mob = mob_generator(7,11)
        print(f"You have encountered a {mob.name}")
        return mob


def create_room(Rooms: dict, cc: list, croom: str)-> str:
    """Creates a room"""
    # types of rooms
    room_names=["bedroom", "hallway", "basement", "prison",'balcony', "portal"]
    # Picks a type randomly
    rng = randint(0, 5)
    # Check if the room exists
    for k,v in Rooms.items():
        if v == cc:
            croom = k
            Rooms[croom] = [cc[0],cc[1]]
            return Rooms,croom
    else:
        croom = f"{room_names[rng]}{cc[0]},{cc[1]}"
        Rooms[croom] = [cc[0],cc[1]]
        return Rooms,croom

# list of coordinates [north, south, east, west]
cc = [0,0]
prev_cc = [0,0]

# an inventory, which is initially empty
inventory = [{"map": "A map of the castle"}]


# direction dictionary
Rooms= {
    "Great Hall": [0,0]
}

#list for movement check
move_check=["north", "south", "east", "west"]


# start the player in the Hall
croom = 'Great Hall'

# Initialize the score
score = 0

def game(score,cc, croom, Rooms):
    """This is the main function that runs the game"""
    print("""
          You have entered the castle. You are in the Great Hall.
          You do not know how you got here. You can't remember anything.
          Most importantly, you don't know how to get out.
          You must find a way to escape.
          """)
    player = initiate_player()
    showInstructions()
    while True:
        showStatus(croom, cc)
        # otherwise input will keep asking
        command = ''
        while command == '':  
            command = input('What\'s next?\n')    
        command = command.lower().split(" ", 1)
        # Check what command is issued and apply logic
        cc = command_check(command, cc, score)
        # Create a room
        Rooms,croom = create_room(Rooms,cc,croom)
        mob = spawn_mob(score)
        if mob != None:
            fight(player, mob)
        score += 1
        if score == 8:
            print("The stronger you get, the stronger the monsters get")
        elif score == 11:
            print("You have become too strong. You must escape now, the dragon is coming")
        elif score == 25:
            print("You have become too strong. You must leave!")
        elif score == 28:
            print("What are you still doing here? You are too strong for this place")
        elif score == 30:
            print("What is your purpose mortal?")
        elif score == 35:
            print("""
                You have become too strong; the monster you were trying to escape from. 
                Your humanity is now gone.
                You are trapped in the castle forever.
                """)
            print("\n\nYour score is: ", score)
            exit()
def main():
    """Main function"""
    game(score,cc, croom, Rooms)

if __name__ == "__main__":
    main()