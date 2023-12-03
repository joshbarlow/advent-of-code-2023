import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateEngine(inputDataArray):

    engineLayout = engineLayoutGrid(inputDataArray)

    xWidth = len(inputDataArray[0])
    yWidth = len(inputDataArray)
    
    # build numbers
    numberItems = []
    currentNum = ''
    currentCoords = []

    for y in range(yWidth):

        if currentNum:
                    numberItems.append(numberItem(currentNum,currentCoords))
                    currentNum = ''
                    currentCoords = []
        
        for x in range(xWidth):
            currentItem = engineLayout.getItem(x,y)
            if currentItem.isdigit():
                currentNum += currentItem
                currentCoords.append([x,y])
            else:
                if currentNum:
                    numberItems.append(numberItem(currentNum,currentCoords))
                    currentNum = ''
                    currentCoords = []

    total = 0

    for item in numberItems:
        print(f"checking {item.number}")
        valid = False
        for coord in item.coords:
            print(engineLayout.checkAdjacent(coord[0],coord[1]))
            if engineLayout.checkAdjacent(coord[0],coord[1]):
                valid = True
    
        if valid:
            print(f"item {item.number} is valid")
            total += item.number

    print(engineLayout.symbols)

    return total

class numberItem:
    def __init__(self, num, coords):
        self.number = int(num)
        self.coords = coords

class engineLayoutGrid:
    def __init__(self, inputDataArray):
        self.inputDataArray = inputDataArray
        self.inputDataArray.reverse()
        self.xWidth = len(inputDataArray[0])
        self.yWidth = len(inputDataArray)

        self.LayoutGrid = []
        for line in self.inputDataArray:
            row = [*line]
            self.LayoutGrid.append(row)
        
        self.symbols = []
        for x in range(self.xWidth):
            for y in range(self.yWidth):
                item = self.LayoutGrid[y][x]
                if not item.isdigit():
                    if item != '.':
                        self.symbols.append(item)
        
        self.symbols = set(self.symbols)
                        
    def getItem(self,x,y):
        item = self.LayoutGrid[y][x]
        return item

    def checkAdjacent(self,x,y):
        isSymbol = False
        changes = [-1,0,1]
        for xChange in changes:
            for yChange in changes:
                newX = x + xChange
                newY = y + yChange
                item = '.'
                try:
                    item = self.LayoutGrid[newY][newX]
                except:
                    # print('out of range')
                    a = 'a'
                
                if item in self.symbols:
                    print(f"found: {item}")
                    isSymbol = True
                    return isSymbol

        return isSymbol

if __name__ == '__main__':
    print(calculateEngine(importData()))