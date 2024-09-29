import string

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateCards(inputDataArray):

    hands = []
    ranks = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 6,
        '6': 7,
        '8': 8,
        '9': 10,
        'T': 11,
        'J': 12,
        'Q': 13,
        'K': 14,
        'A': 15
    }
    baseRanks = []
    for line in inputDataArray:
        linesplit = line.split(' ')
        cards = [*linesplit[0]]
        score = int(linesplit[1])

        rank = 0

        if()
        print(cards)
    
    return 'abc'

if __name__ == '__main__':
    print(calculateCards(importData()))