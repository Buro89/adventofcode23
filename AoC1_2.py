"""
Advent of Code 2023
Player: Buro89
Language: Python
Puzzle: Day 1 - Part 2, see here: https://adventofcode.com/2023/day/1

DISCLAIMER:
Please be aware that I am a beginner and am using this challenge as a way to learn and grow. If my code appears
ugly or longwinded, please bear with me as I am still unaware of a lot. That said, I enjoyed the challenge a lot
and it really helps my learning. I am doing this challenge next to a busy life, and will upload new solutions
whenever I have the time and energy.

Credits to Fuglede's code, which guided me on this one. Whew! https://github.com/fuglede/adventofcode/blob/master/2023/day01/solutions.py 

"""

# Open file

with open("input") as f:
    content = f.read().strip()


# Download the required packages
import re


# Placing the actual digit inbetween two words, prevents that the number would collide with another number (e.g. four9 would turn 49)
# With help from https://github.com/fuglede/adventofcode/blob/master/2023/day01/solutions.py

modified_content = (
    content.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)

# Check
print(content)

# Save to new file
with open("file_new.txt", 'w') as file:
    file.write(modified_content)

# Open new file
file = open("file_new.txt", "r")
content=file.readlines()

# Close original file
f.close()



## Now that the problem with the nun-numeric digits is solved, we can repeat the same process as with Part 1



# Save each list item in a separate variable to work with more easily, and separate characters
# with a space in order to be able to later split and filter numerics
counter=0
for i in content:
    globals()[f"variable{counter}"] = " ".join(content[counter])
    counter += 1
    if counter > len(content):
        break


# Split and filter numerics for each variable
counter=0
while counter < len(content):
    globals()[f"res{counter}"] = [int(i) for i in globals()[f"variable{counter}"].split() if i.isdigit()]
    counter += 1
    if counter > len(content):
        break

print(f"""
      
===============================

Checking several things so far.
      
    Variable1 is: {variable1}

    Splitted variable is res1, so it's: {res1}

===============================


      """)



# In this puzzle, a "treb7uchet" would give 77 and not a 7. So we'll go with this:
counter=0
while counter < len(content):
    globals()[f"newres{counter}"] = [globals()[f"res{counter}"][0], globals()[f"res{counter}"][-1]]
    counter += 1


# Now that only the numerics are left, convert the lists into actual numbers [8, 7] into 87 for each variable
def convert(list):
    stringetje = [str(i) for i in list]
    leftover = int("".join(stringetje))
    return(leftover)

counter=0
while counter < len(content):
    list = globals()[f"newres{counter}"]
    globals()[f"number{counter}"] = convert(list)
    counter += 1

# Now put these final numbers in a list for summing up
numberrange = []

for i in range(0,1000):
    numberrange.append(globals()[f"number{i}"])

print("\n\n\n\nThe filtered, final list with only numbers is here:\n\n" + str(numberrange) + "\n\n\n\n")

# Calculate the outcome

solution = sum(numberrange)

# And the solution is...
print("\n\nAnd the solution is (the sum total of all these abovementioned numbers)... " + str(solution) + "\n\n")


file.close()
