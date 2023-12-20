"""
Advent of Code 2023
Player: Buro89
Language: Python
Puzzle: Day 2 - Part 2, see here: https://adventofcode.com/2023/day/2

DISCLAIMER:
Please be aware that I am a beginner and am using this challenge as a way to learn and grow. I improved a bit of the code
I used in Part 1 here, and added an automatic check (in a while loop) that finishes the program only when each game has
a valid (non-missing) value for each color.

"""


# Import packages
from logging.handlers import WatchedFileHandler
import re


# ================ Data prepping

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

# Check the extracted red counts list
print("\n\n")
print("Let's check the data we have.")
print("\n\n")
print("====RED CUBES====")
print("\n\n")
print("Red cubes list: ")
print(red_counts_list)
print("\n\n")

# Check: count if there's 100 games for red cubes
for i, red_counts in enumerate(red_counts_list, 1):
    print(f"Red cubes in Game {i}: {red_counts}")
    pass
print("\nTotal games with red cubes (should be 100):", i)

# Extract the highest number of red cubes for each game
max_values_red_list = []

for i in red_counts_list:
    max_value_red = max(i)
    max_values_red_list.append(max_value_red)
print("\nThe list of highest number of red cubes for each game:", max_values_red_list)

# Double check if this list of max values has 100 items
for i, max_value_red in enumerate(max_values_red_list, 1):
    pass
print("\nTotal games in list with a valid item for maximal no. of red cubes (should be 100):", i)
number_of_redgames = i

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

# Check the extracted green counts list
print("\n\n")
print("====GREEN CUBES====")
print("\n\n")
print("Green cubes list: ")
print(green_counts_list)
print("\n\n")

# Check: count if there's 100 games for green cubes
for i, green_counts in enumerate(green_counts_list, 1):
    print(f"Green cubes in Game {i}: {green_counts}")
    pass
print("\nTotal games with green cubes (should be 100):", i)

# Extract the highest number of green cubes for each game
max_values_green_list = []

for i in green_counts_list:
    max_value_green = max(i)
    max_values_green_list.append(max_value_green)
print("\nThe list of highest number of green cubes for each game:", max_values_green_list)

# Double check if this list of max values has 100 items
for i, max_value_green in enumerate(max_values_green_list, 1):
    pass
print("\nTotal games in list with a valid item for maximal no. of green cubes (should be 100):", i)
number_of_greengames = i


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

# Check the extracted blue counts list
print("\n\n")
print("====BLUE CUBES====")
print("\n\n")
print("Blue cubes list: ")
print(blue_counts_list)
print("\n\n")

# Check: count if there's 100 games for blue cubes
for i, blue_counts in enumerate(blue_counts_list, 1):
    print(f"Blue cubes in Game {i}: {blue_counts}")
    pass
print("\nTotal games with blue cubes (should be 100):", i)

# Extract the highest number of blue cubes for each game
max_values_blue_list = []

for i in blue_counts_list:
    max_value_blue = max(i)
    max_values_blue_list.append(max_value_blue)
print("\nThe list of highest number of blue cubes for each game:", max_values_blue_list)

# Double check if this list of max values has 100 items
for i, max_value_blue in enumerate(max_values_blue_list, 1):
    pass
print("\nTotal games in list with a valid item for maximal no. of blue cubes (should be 100):", i)
number_of_bluegames = i



# ================ Calculation

print("\n\n")
print("Let's calculate towards the solution.")
print("\n\n")

# Get the products of the highest number of red, green and blue cubes for each game
while number_of_redgames == 100 and number_of_greengames == 100 and number_of_bluegames == 100:
    result = [a * b * c for a, b, c in zip(max_values_red_list, max_values_green_list, max_values_blue_list)]
    break
print(f"\n\nThe products of the highest number of red, green and blue cubes for each game, are: {result}\n\n")

# Calculate the sum of all these products... The solution, then, is...
solution = sum(result)
print(f"\n\n================= And the solution is: {solution} =================\n\n")
input("Press a key to end this program. ")