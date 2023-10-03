# Import libraries
import random # Import a library for random numbers
import time   # For delay
import os         
                  
                  
# Create method to clear screen
clear = lambda: os.system('clear')
                  
# Creating a dictionary with the options
options = {1: "rock", 2: "paper", 3: "scissors"}                                                                                   
                  
print("Are you ready?")
time.sleep(1)     
clear()           
print("Let us play ROCK, PAPER, SCISSORS")
time.sleep(1)     
clear()           
print("3")        
time.sleep(1)     
clear()           
print("2")        
time.sleep(1)     
clear()           
print("1")        
time.sleep(1)     
clear()           
random_number = random.randint(1,3)
time.sleep(1)     
clear()           
if random_number == 1:
    print(options[1])
elif random_number == 2:
    print(options[2])
elif random_number == 3:
    print(options[3])
 
