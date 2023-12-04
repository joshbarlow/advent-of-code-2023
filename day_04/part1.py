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

    for line in inputDataArray:
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
        score = 0

        for num in resultsNumbers:
            if num in winningNumbers:
                wincount +=1
        
        for x in range(wincount):
            if score == 0:
                score += 1
            else:
                score = score * 2
        
        total += score
    
    return total

if __name__ == '__main__':
    print(calculateScratchcards(importData()))