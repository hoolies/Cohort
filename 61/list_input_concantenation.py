#!/bin/python3
# Part 1
wordbank= ["indentation", "spaces"] 

# Part 2
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# Part 3
wordbank.append(4)

#Part 4 & 5
def get_number(message):
    while True: 
        try:
            number = int(input(message))
            if (number >= 0) and (number <=len(tlgstudents)):
                return number - 1
        except ValueError:
            print(f"Not an integer between 0 and {len(tlgstudents) - 1}")

num = get_number(f"Enter a number, between 0 and {len(tlgstudents) - 1}: ")

# Part 5b
student = tlgstudents[num]

# Part 6
print(f"{student} alwayse use {wordbank[-1]} {wordbank[1]} to indent.")
