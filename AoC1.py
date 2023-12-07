"""
Advent of Code 2023
Player: Buro89
Language: Python
Puzzle: Day 1 - Part 1, see here: https://adventofcode.com/2023/day/1

DISCLAIMER:
Please be aware that I am a beginner and am using this challenge as a way to learn and grow. If my code appears
ugly or longwinded, please bear with me as I am still unaware of a lot. That said, I enjoyed the challenge a lot
and it really helps my learning. I am doing this challenge next to a busy life, and will upload new solutions
whenever I have the time and energy.

"""

file = open("input", "r")
content=file.readlines()

## Optional: Printing some information about the original list (file "input") for my own overview.
# print("\n\n\n\nThe raw list is:\n\n" + str(content) + "\n\n")
# print(f"\n\nThere are {len(content)} items in this list.\n\n")

# Save each list item in a separate variable to work with more easily, and separate characters
# with a space in order to be able to later split and filter numerics
counter=0
for i in content:
    globals()[f"variable{counter}"] = " ".join(content[counter])
    counter += 1
    if counter > 1000:
        break


# Split and filter numerics for each variable
counter=0
while counter < len(content):
    globals()[f"res{counter}"] = [int(i) for i in globals()[f"variable{counter}"].split() if i.isdigit()]
    counter += 1


# Now filter only first and last digit

## Optional: In case you want to have strings with just one digit "treb7uchet" to have just one digit, 7, you would do the following
# counter=0
# while counter < len(content):
#    lengte = len(globals()[f"res{counter}"])
#    if lengte == 1:
#        globals()[f"newres{counter}"] = globals()[f"res{counter}"]
#    else:
#        globals()[f"newres{counter}"] = [globals()[f"res{counter}"][0], globals()[f"res{counter}"][-1]]
#    counter += 1

# But in this puzzle, a "treb7uchet" would give 77 and not a 7. So we'll go with this:
counter=0
while counter < len(content):
    globals()[f"newres{counter}"] = [globals()[f"res{counter}"][0], globals()[f"res{counter}"][-1]]
    counter += 1

## Optional: printing a test sample as a double-check:
# print("This is a test sample to see if it all proceeded as intended.")
# print(f"This is res1: {res1}")
# print(f"This is newres1: {newres1}")
# print(f"This is res2: {res2}")
# print(f"This is newres2: {newres2}")
# print(f"This is res99: {res99}")
# print(f"This is newres99: {newres99}")


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