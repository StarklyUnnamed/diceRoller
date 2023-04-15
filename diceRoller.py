import random

dieArt = {

    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

dieHeight = len(dieArt[1])
dieWidth = len(dieArt[1][0])
dieFaceSeparator = " "


def numberOfRolls():
    inputStr = input('How many times would you like to roll? [1-10]')
    if inputStr.strip() in {'1','2','3','4','5','6','7','8','9','10'}:
        return int(inputStr)
    print('Please enter only a number 1-10.')
    numberOfRolls()

def numberOfDice():
    inputStr = input('How many dice would you like to roll? [1-6]')
    if inputStr.strip() in {'1','2','3','4','5','6'}:
        return int(inputStr)
    print('Please enter only a number 1-6.')
    numberOfDice()

def roll_dice(numDice):
    return [random.randint(1,6) for _ in range(numDice)]

def generate_die_faces(dieValues):
    dieFaces = [dieArt[value] for value in dieValues]
    dieFaceRows = []
    for row_idx in range(dieHeight):
        rowComponents = [die[row_idx] for die in dieFaces]
        rowStr = dieFaceSeparator.join(rowComponents)
        dieFaceRows.append(rowStr)
    width = len(dieFaceRows[0])
    diagramHeader = ' Results '.center(width, '~')
    return '\n'.join([diagramHeader] + dieFaceRows)

numberOfRolls = numberOfRolls()
for _ in range(numberOfRolls):
    numDice = numberOfDice()
    dieValues = roll_dice(numDice)
    print(generate_die_faces(dieValues))