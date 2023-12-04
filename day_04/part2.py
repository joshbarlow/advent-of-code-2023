import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateScratchcards(inputDataArray):

    total = 0

    scratchCardAmmountList = []
    scratchCardWinList = []

    for x in range(len(inputDataArray)):
        scratchCardAmmountList.append(1)
        scratchCardWinList.append(0)
    
    print(scratchCardAmmountList)
    
    for x in range(len(inputDataArray)):
        line = inputDataArray[x]
        lineSplit = line.split(':')
        cardText = lineSplit[0]

        winningText = lineSplit[1].split('|')[0]
        resultsText = lineSplit[1].split('|')[1]

        winningText = winningText.split(' ')

        winningNumbers = []
        for num in winningText:
            if num.isdigit():
                winningNumbers.append(int(num))
        
        resultsText = resultsText.split(' ')

        resultsNumbers = []
        for num in resultsText:
            if num.isdigit():
                resultsNumbers.append(int(num))
        
        wincount = 0

        for num in resultsNumbers:
            if num in winningNumbers:
                wincount +=1
        
        scratchCardWinList[x] = wincount
    
    for x in range(len(inputDataArray)):
        numCards = scratchCardAmmountList[x]
        cardScore = scratchCardWinList[x]

        for y in range(cardScore):
            scratchCardAmmountList[x+(y+1)] += numCards

    print(scratchCardAmmountList)

    total = sum(scratchCardAmmountList)

    return total

if __name__ == '__main__':
    print(calculateScratchcards(importData()))