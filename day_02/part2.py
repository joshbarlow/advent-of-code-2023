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

    total = 0

    for line in inputDataArray:

        possible = True

        minCubes = {
            'red': 0,
            'green': 0,
            'blue': 0
            }

        linesplit = line.split(':')
        gameNum = int(linesplit[0][5:])
        print('Game: ' + str(gameNum))
        rounds = linesplit[1].split(',')
        for round in rounds:
            colors = round.split(';')
            for colorInput in colors:

                col = getColor(colorInput)
                num = getNumber(colorInput)

                if num > minCubes[col]:
                    minCubes[col] = num
        
        power = minCubes['red'] * minCubes['green'] * minCubes['blue']
        total += power

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