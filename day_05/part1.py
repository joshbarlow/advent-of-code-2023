import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateSeeds(inputDataArray):

    seedSplit = inputDataArray[0].split(': ')[1].split(' ')

    print(seedSplit)

    seeds = []

    for x in seedSplit:
        seeds.append(int(x))

    inputDataArray = inputDataArray[3:]
    mapList = []
    currentMap = []

    for line in inputDataArray:
        if 'map' in line:
            mapList.append(currentMap)
            currentMap = []
            continue

        if line == '':
            continue
        
        currentEntry = []

        lineSplit = line.split(' ')
        for x in lineSplit:
            currentEntry.append(int(x))
        currentMap.append(currentEntry)

    mapLookups =[]
    currentLookup = {}

    for map in mapList:
        for key in map:
            destination = key[0]
            source = key[1]
            rangeLength = key[2]

            for x in range(rangeLength):
                currentLookup[(source + x)] = (destination + x)
        mapLookups.append(currentLookup)
        currentLookup = {}
    
    # run through the maps

    for map in mapLookups:
        for x in range(len(seeds)):
            seedNum = seeds[x]
            if seedNum in map.keys():
                seedNum = map[seedNum]
            else:
                seedNum = seedNum
            seeds[x] = seedNum
    
    print(seeds)

    return min(seeds)

if __name__ == '__main__':
    print(calculateSeeds(importData()))