import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculateBoatRace(inputDataArray):

    times = ''
    distances = ''

    for time in inputDataArray[0].split(' '):
        if time.isdigit():
            times += time

    for dist in inputDataArray[1].split(' '):
        if dist.isdigit():
            distances += dist

    racesWins = []

    time = int(times)
    distance = int(distances)

    print(f"race, time: {time}, dist: {distance}")

    wins = 0

    for y in range(time):
            
        holdTime = y+1
        travelTime = time - (y+1)

        if(holdTime * travelTime) > distance:
            print(f"race - hold: {holdTime}, travel: {travelTime}. result: {holdTime * travelTime} - higher than: {distance}")
            wins += 1
        
    print(f"{wins} wins")
    racesWins.append(wins)
    
    print(racesWins)
    
    finalScore = 1

    for x in racesWins:
        finalScore = finalScore * x
    
    return finalScore

if __name__ == '__main__':
    print(calculateBoatRace(importData()))