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

    print(len(seedSplit))

    for x in range(len(seedSplit)):
        if x % 2 == 0:
            print(x)
            seedNum = int(seedSplit[x])
            seedRange = seedSplit[x+1]
            for num in range(int(seedRange)):
                seeds.append(seedNum + num)
        else:
            print('odd')
    
    print(f"number of seeds: {len(seeds)}")

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
    mapList.append(currentMap)

    # run through the maps

    for map in mapList:
        for x in range(len(seeds)):
            seedNum = seeds[x]
            for key in map:
                destination = key[0]
                source = key[1]
                rangeLength = key[2]
                difference = destination - source

                if (seedNum >= source) and (seedNum <= (source + rangeLength)):
                    seeds[x] = seedNum + difference
                    match = True
                    break
    
    print(seeds)

    return min(seeds)

if __name__ == '__main__':
    print(calculateSeeds(importData()))