## The multiplicative persistence of a number
def getMultiplicativePersistence(number):
    generations = 0
    num = number
    while (len(str(num)) != 1):
        newNum = 1
        for i in range(len(str(num))):
            newNum *= int(str(num)[i:i+1])
        num = newNum
        generations += 1
    return generations

## The number of generations in the 3x+1 sequence of a number OR the list of numbers in the 3x+1 sequence of a number
def simulate3xPlus1(number, isList=False):
    generations = 0
    num = number
    list_ = []
    while (num != 1):
        if (num % 2 == 0):
            num /= 2
            num = int(num)
        else:
            num = num * 3 + 1
        generations += 1
        if (isList == True):
            list_.append(num)
    if (isList == True):
        return list_
    else:
        return generations

## Simulates conway's game of life for A generations and B grid size. The grid will be a square
def simulateGameOfLife(generations, gridSize, *squaresOn):
    for i in range(generations):
        for x in range(gridSize):
            for y in range(gridSize):
                isAlive = False
                for arg in squaresOn:
                    if (arg == [x, y]):
                        isAlive = True
                neighbors = []
                neighbors.append([x+1, y+1])
                neighbors.append([x+1, y])
                neighbors.append([x+1, y-1])
                neighbors.append([x, y+1])
                neighbors.append([x, y-1])
                neighbors.append([x-1, y+1])
                neighbors.append([x-1, y])
                neighbors.append([x-1, y-1])
                numNeighbors = 0
                for n in neighbors:
                    for arg in squaresOn:
                        if (arg == n):
                            numNeighbors += 1
                if (numNeighbors < 2 & isAlive == True):
                    isAlive = False
                if (numNeighbors > 4 & isAlive == True):
                    isAlive = False
                if (numNeighbors == 3 & isAlive == False):
                    isAlive = True