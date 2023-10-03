# Import libraries
import random # Import a library for random numbers
import time   # For delay
import os         

# Create method to clear screen
def os_clear_wait():
    if os.name == 'posix':
        time.sleep(1)
        clear = lambda: os.system('clear')
    else:
        time.sleep(1)
        clear = lambda: os.system('cls')

# Shoot!!
def shoot():
    # Creating a dictionary with the options
    options = {1: "rock", 2: "paper", 3: "scissors"}
    print("Are you ready?")
    os_clear_wait()
    print("Let us play ROCK, PAPER, SCISSORS")
    # Creating a random numbe
    random_number = random.randint(1,3)           
    os_clear_wait()
    for i in (3,2,1):
        print(i)
        os_clear_wait()
    if random_number == 1:
        print(options[1])
    elif random_number == 2:
        print(options[2])
    elif random_number == 3:
        print(options[3])

def main():
    again = True
    while again == True:
        shoot()
        again = input("Would you to play again? (y/n)")
        if again == "y":
            again = True
        else:
            again = False
            break

if __name__ == "__main__":
    main()
