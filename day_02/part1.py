import re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateGames(inputDataArray):

    overlapCount = 0

    maximumCubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    total = 0

    for line in inputDataArray:

        possible = True
        num = 0

        linesplit = line.split(':')
        gameNum = int(linesplit[0][5:])
        print('Game: ' + str(gameNum))
        rounds = linesplit[1].split(',')
        for round in rounds:
            colors = round.split(';')
            for colorInput in colors:
                col = getColor(colorInput)
                num = getNumber(colorInput)

                # print(col)
                # print(num)

                if num > maximumCubes[col]:
                    print(str(num) + ' ' + col + ' is greater than max')
                    possible = False
        
        if possible: total += gameNum

    return total

def getColor(inputString):

    output = False

    pattern = r'\b[a-zA-Z]+\b'

    matches = re.findall(pattern, inputString)

    if matches:
        output = matches[0]
        
    return output

def getNumber(inputString):

    output = False

    pattern = r'\b\d+\b'

    matches = re.findall(pattern, inputString)

    if matches:
        output = int(matches[0])
        
    return output

if __name__ == '__main__':
    print(calculateGames(importData()))