'''
This is a single module 2048 game program.
 
functions:
    show(Text)
    merge(line)
    newOrder(direction,firstTime=True)
    addRandomly()
 
The program works as follows:
    1: it create a list of lists (containing 0s and 2s),
    2: display the list as a grid,
    3: ask the user to input a direction to slide the grid,
    4: update the list based on the given direction 
    5: loop back to 2
'''
 
import random
import os
 
UP = [[[0, 3], [1, 3], [2, 3], [3, 3]],
      [[0, 2], [1, 2], [2, 2], [3, 2]],
      [[0, 1], [1, 1], [2, 1], [3, 1]],
      [[0, 0], [1, 0], [2, 0], [3, 0]]
      ]
DOWN = [[[3, 0], [2, 0], [1, 0], [0, 0]],
        [[3, 1], [2, 1], [1, 1], [0, 1]],
        [[3, 2], [2, 2], [1, 2], [0, 2]],
        [[3, 3], [2, 3], [1, 3], [0, 3]]
        ]
score = 0
biggestValue = 0
allLines = []
for row in range(4):
    allLines.append([])
    for column in range(4):
        allLines[row].append(0)
 
count = 0
while 1:
    rands = [random.randint(0, 3), random.randint(0, 3)]
    if allLines[rands[0]][rands[1]] == 0:
        allLines[rands[0]][rands[1]] = 2
        count += 1
        if count == 2:
            break
 
 
def show(text):
    '''
    This function display the games grid.
    Parameter:
        text(string) - a message to be displayed under the game grid
    '''
    os.system("cls" if os.name == "nt" else "clear")
    print("\n      ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    for row in allLines:
        line = ""
        for column in row:
            if column < 10:
                space1 = "  "
                space2 = "   "
            elif column < 100:
                space1 = "  "
                space2 = "  "
            elif column < 1000:
                space1 = " "
                space2 = "  "
            elif column < 10000:
                space1 = " "
                space2 = " "
            elif column < 100000:
                space1 = ""
                space2 = " "
            else:
                space1 = ""
                space2 = ""
            line += "|"+space1+str(column)+space2
        print("     "+line+"|")
    print("      ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("     Score = " + str(score)+" || Big Value = " +
          str(biggestValue) + (" || You Won" if biggestValue >= 2048 else ""))
    print("\n     "+text, end="")
 
 
def merge(line):
    '''
    This function accept a list and return a slid (to the left) form of it.
    Parameters:
        line(list of ints) - a list to be merged
    '''
    global score, biggestValue
    new_line = []
    column_before = 0
    for column in line:
        if column == 0:
            continue
        elif column == column_before:
            new_line[len(new_line)-1] = (2*column)
            column_before = 0
            score += 2*column
            if 2*column > biggestValue:
                biggestValue = 2*column
        else:
            new_line.append(column)
            column_before = column
    while len(new_line) < 4:
        new_line.append(0)
    return new_line
 
 
def newOrder(direction, firstTime=True):
    '''
    This function reorder and prepare the game list to the merge function
    Parameters:
        direction(string) - to which direction is the game slid
        firstTime(boolean) - if the ordering is before or after the merge (default to True)
    '''
    global allLines
    if direction == 4:
        updatedLines = allLines
    elif direction == 8 or direction == 2:
        if not firstTime:
            direction = 2 if direction == 8 else 8
        referenceList = UP if direction == 8 else DOWN
        updatedLines = []
        for row in range(4):
            updatedLines.append([])
            for column in range(4):
                upIndex = referenceList[row][column]
                updatedLines[row].append(allLines[upIndex[0]][upIndex[1]])
    else:
        for row in allLines:
            row.reverse()
        updatedLines = allLines
    allLines = updatedLines
 
 
def addRandomly():
    '''
    This function find all 0s in the game list and replace one of them by 2
    '''
    empty = []
    for row in range(4):
        for column in range(4):
            if allLines[row][column] == 0:
                empty.append([row, column])
    if empty:
        randomIndex = empty[random.randint(0, len(empty)-1)]
        allLines[randomIndex[0]][randomIndex[1]] = 2
 
 
validInputs = [4, 8, 6, 2]
 
show("Choose Direction (4[Left], 8[Up], 6[Right] or 2[Down])")
while 1:
    try:
        direction = int(input(": "))
    except:
        show("Please enter 4[Left], 8[Up], 6[Right] or 2[Down]")
        continue
    if not direction in validInputs:
        show("Please enter 4[Left], 8[Up], 6[Right] or 2[Down]")
        continue
    newOrder(direction)
    for line in range(4):
        allLines[line] = merge(allLines[line])
    newOrder(direction, False)
    addRandomly()
    show("Direction")
 
