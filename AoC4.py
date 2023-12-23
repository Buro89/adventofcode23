"""
Advent of Code 2023
Player: Buro89
Language: Python
Puzzle: Day 4 - Part 1, see here: https://adventofcode.com/2023/day/4

DISCLAIMER:
I have helped yet another Elf! 
Please be aware that I am a beginner and am using this challenge as a way to learn and grow. 

"""


# Import packages
import re
from contextlib import redirect_stdout


# Open this puzzle's input file
with open("input4.txt", "r") as file:
    lines = file.readlines()

# Remove the 'Card {number}:' in order to better process the file
cleaned_lines = []

for line in lines:
    parts = line.split(":")
    cleaned_line = parts[1].strip()
    cleaned_lines.append(cleaned_line)

for cleaned_line in cleaned_lines:
    print(cleaned_line)
    print("=======")
print("Totality, not per line:")
print(cleaned_lines)

# Make two lists of numbers for each line: winning numbers, and my numbers on the card
winning_numbers = []
my_numbers = []

for cleaned_line in cleaned_lines:
    parts2 = cleaned_line.split("|")
    winning = [int(number) for number in parts2[0].split() if number.strip()]
    mine = [int(number) for number in parts2[1].split() if number.strip()]

    winning_numbers.append(winning)
    my_numbers.append(mine)

# Print results
for i, (win, me) in enumerate(zip(winning_numbers, my_numbers), start=1):
    print(f"Card {i}:")
    print(f"Winning numbers: {win}")
    print(f"My numbers: {me}")
    globals()[f"my_numbers_{i}"] = me
    globals()[f"winning_numbers_{i}"] = win

# Optional: Testing
#print("\n&&&&&&&&&&&&&&&&&&Test")
#print(f"My numbers for card 3: {my_numbers_3}")
#print(f"Winning for card 3: {winning_numbers_3}")

# Check whether we have winning numbers in our cards, and if so, for which cards
with open('winners.txt', 'w') as newfile:
    with redirect_stdout(newfile):
        for i in range(1, 215):
            for nummertje in globals()[f"my_numbers_{i}"]:
                if nummertje in globals()[f"winning_numbers_{i}"]:
                    print(f"Card {i} won!")

# Let's filter only the card numbers from the 'winners' file I created previously. That'll work easier later.
with open('numbersonly.txt', 'w') as numbersonly:
       with redirect_stdout(numbersonly):
            with open('winners.txt', 'r') as winnersfile:
                for line in winnersfile:
                    words = line.split()
                    for i in words:
                        if(i.isdigit()):
                            print(i)

# Calculate the number of entries each card has in this 'numbersonly' file (i.e. the number of winning digits on the card)
digit_counts = {}

with open('numbersonly.txt', 'r') as numbersonly:
    for line in numbersonly:
        digit = int(line.strip())
        digit_counts[digit] = digit_counts.get(digit, 0) + 1

for digit, count in digit_counts.items():
    print(f"Digit {digit} has {count} occurrences.")

print(f"""
      
The dictionary:
      
{digit_counts}

""")

# Calculate the worth of the cards with winning digits
worths = []

for digit, count in digit_counts.items():
    counter = 1
    for i in range(2, count + 1):
        counter *= 2
    worths.append(counter)

        
print()
print(f"The cards' worths: {worths}")
print()

#And the solution is...
solution = sum(worths)
print(f"And the solution is... {solution}")
print()

#Ending
input("Press button to end this program. ")