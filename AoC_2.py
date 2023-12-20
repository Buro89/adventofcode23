"""
Advent of Code 2023
Player: Buro89
Language: Python
Puzzle: Day 2 - Part 1, see here: https://adventofcode.com/2023/day/2

DISCLAIMER:
Please be aware that I am a beginner and am using this challenge as a way to learn and grow. This one seemed easy,
but there were lots of hidden rabbit holes a beginner like me got lost in! In the end I solved it with many filter
variables (in the form of lists) and I'm going to return at some point to see if I can solve it more elegantly.
Anyway: I caught the solution.

"""


# Import packages
from logging.handlers import WatchedFileHandler
import re



# RED cubes

# Function to extract red counts from a line
def extract_red_counts(line):
    return [int(match.group(1)) for match in re.finditer(r"(\d+) red", line)]

# Read the file and process each line
file_path = "input2.txt"  
red_counts_list = []

with open(file_path, "r") as file:
    for line in file:
        red_counts_list.append(extract_red_counts(line))

# Print the extracted red counts
print("Red cubes: ")
print(red_counts_list)

# Extra check against 'empty' games: Print the extracted red counts for each line
for i, red_counts in enumerate(red_counts_list, 1):
    print(f"Game {i}: {red_counts}")



# GREEN cubes

# Function to extract green counts from a line
def extract_green_counts(line):
    return [int(match.group(1)) for match in re.finditer(r"(\d+) green", line)]

# Read the file and process each line
file_path = "input2.txt"  
green_counts_list = []

with open(file_path, "r") as file:
    for line in file:
        green_counts_list.append(extract_green_counts(line))

# Print the extracted green counts
print("Green cubes: ")
print(green_counts_list)

# Extra check against 'empty' games: Print the extracted green counts for each line
for i, green_counts in enumerate(green_counts_list, 1):
    print(f"Game {i}: {green_counts}")



# BLUE cubes

# Function to extract blue counts from a line
def extract_blue_counts(line):
    return [int(match.group(1)) for match in re.finditer(r"(\d+) blue", line)]

# Read the file and process each line
file_path = "input2.txt"  
blue_counts_list = []

with open(file_path, "r") as file:
    for line in file:
        blue_counts_list.append(extract_blue_counts(line))

# Print the extracted blue counts
print("Blue cubes: ")
print(blue_counts_list)

# Extra check against 'empty' games: Print the extracted blue counts for each line
for i, blue_counts in enumerate(blue_counts_list, 1):
    print(f"Game {i}: {blue_counts}")

print(blue_counts_list)



# ALL cubes

# Combine the lists
allgames = [red_counts_list]
allgames.append(green_counts_list)
allgames.append(blue_counts_list)

print(f"Everything: {allgames}")
print(f"Only the red counts: {allgames[0]}")
print(f"Only the green counts: {allgames[1]}")
print(f"Only the blue counts: {allgames[2]}")

# Check whether this variable does what it needs to do: combine all the colors in sublists in one big list
print("\n")
for i, number in enumerate(allgames[0], 1):
    print(f"RED counts for game {i}: {number}")
print("\n")
for i, number in enumerate(allgames[1], 1):
    print(f"GREEN counts for game {i}: {number}")
print("\n")
for i, number in enumerate(allgames[2], 1):
    print(f"BLUE counts for game {i}: {number}")





# Make a condition test to see which games would have been possible if the back had only...
# 12 red
# 13 green
# 14 blue
# Somehow embedded if-statements didn't work, probably due to how I organized the for-loops. Something I need to study further, but for now, I choose an inelegant way out using filter variables.


# Check for the "maximally 12 red cubes" condition and specify filter variable (games that satisfy it, go through with their game ID as value, others get a zero)
try:
    for i, number in enumerate(allgames[0], 1):
        if all(number < 13 for number in allgames[0][i-1]):
            print("\n=============nEW: In this game, the number of red cubes was fewer than 13 ({number}). Therefore this game (so far) seems possible.=============\n")
            globals()[f"game{i}"] = int(i)
            print(globals()[f"game{i}"])
        else:
            print("\n=============In this game, the number of red cubes was not always fewer than 13 ({number}). Therefore, this game is not possible.=============\n")
            globals()[f"game{i}"] = 0

except IndexError:
    print("IndexError: The loop went out of range.")

# Continue with the rest of the code in case of an Index Error
print("Program continues...")


# Check: List the games that didn't meet the above condition:
print("Didn't meet the red cube requirement:")
for i, number in enumerate(allgames[0], 1):
        if globals()[f"game{i}"] == 0:

            print(f"{i}")

# Check: List the games that DID meet the above condition:
print("DID meet the red cube requirement:")
for i, number in enumerate(allgames[0], 1):
        if globals()[f"game{i}"] != 0:
            print(f"{i}")


# Make a filter to keep only the games that met the requirement above
selectie1 = []

for i, number in enumerate(allgames[0], 1):
        if globals()[f"game{i}"] != 0:
            selectie1.append(i)

print(selectie1)

# Test the "maximally 13 green cubes" condition
try:
    for i, number in enumerate(allgames[1], 1):
        if all(number < 14 for number in allgames[1][i-1]):
            print("\n=============nEW: In this game, the number of green cubes was fewer than 14 ({number}). Therefore this game (so far) seems possible.=============\n")
            globals()[f"game{i}"] = int(i)
            print(globals()[f"game{i}"])
        else:
            print("\n=============In this game, the number of green cubes was not always fewer than 14 ({number}). Therefore, this game is not possible.=============\n")
            globals()[f"game{i}"] = 0

except IndexError:
    print("IndexError: The loop went out of range.")

# Continue with the rest of the code in case of an Index Error
print("Program continues...")



# Check: List the games that didn't meet the above condition:
print("Didn't meet the green cube requirement:")
for i, number in enumerate(allgames[1], 1):
        if globals()[f"game{i}"] == 0:
            print(f"{i}")

# Check List the games that DID meet the above condition:
print("DID meet the green cube requirement:")
for i, number in enumerate(allgames[1], 1):
        if globals()[f"game{i}"] != 0:
            print(f"{i}")

# Make a filter to keep only the games that met the requirement above
selectie2 = []

for i, number in enumerate(allgames[1], 1):
        if globals()[f"game{i}"] != 0:
            selectie2.append(i)

print(selectie2)


# Test the "maximally 14 blue cubes" condition  condition

try:
    for i, number in enumerate(allgames[2], 1):
        if all(number < 15 for number in allgames[2][i-1]):
            print("\n=============nEW: In this game, the number of blue cubes was fewer than 15 ({number}). Therefore this game (so far) seems possible.=============\n")
            globals()[f"game{i}"] = int(i)
            print(globals()[f"game{i}"])
        else:
            print("\n=============In this game, the number of blue cubes was not always fewer than 15 ({number}). Therefore, this game is not possible.=============\n")
            globals()[f"game{i}"] = 0

except IndexError:
    print("IndexError: The loop went out of range.")

# Continue with the rest of the code in case of an Index Error
print("Program continues...")


# Check: List the games that didn't meet the above condition:
print("Didn't meet the blue cube requirement:")
for i, number in enumerate(allgames[2], 1):
        if globals()[f"game{i}"] == 0:
            print(f"{i}")

# Check List the games that DID meet the above condition:
print("DID meet the blue cube requirement:")
for i, number in enumerate(allgames[2], 1):
        if globals()[f"game{i}"] != 0:
            print(f"{i}")

# Make a filter to keep only the games that met the requirement above
selectie3 = []

for i, number in enumerate(allgames[2], 1):
        if globals()[f"game{i}"] != 0:
            selectie3.append(i)

print(selectie3)


# See what game ID's are in all three selection variables (fit all three requirements)
print(f"Selectie1: {selectie1}")
print(f"Selectie2: {selectie2}")
print(f"Selectie3: {selectie3}")


for i in range(1, 101):
    if i in selectie1 and i in selectie2 and i in selectie3:
         print(f"{i} in all lists")
    else:
         print(f"{i} not in all lists")


# Save only the ones that are in each list, in a new list
selectiefinal = []

for i in range(1, 101):
    if i in selectie1 and i in selectie2 and i in selectie3:
            selectiefinal.append(i)

print(selectiefinal)


# And the solution is...

solution = sum(selectiefinal)

print(f"The solution: {solution}")
