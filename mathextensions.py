import math

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

## Returns random number between min and max (inclusive)
def psuedoRandomNumberGenerator(min, max, seed, depth=5):
    if (depth == 0):
        x = str(seed**3)
        x = x[0:6]
        i = int(x)
        while (i > max):
            i -= max
        while (i < min):
            i += min
        return i
    else:
        x = str(seed**3)
        x = x[2:6]
        i = int(x)
        return psuedoRandomNumberGenerator(min, max, i, depth-1)

## Converts between bases. By default only works with 16 digits: 0123456789abcdef but can work with any number of digits if specified. Can also have different digits in/out.
def convBase(n, baseIn=10, baseOut=16, digitsIn="0123456789abcdef",digitsOut="0123456789abcdef"):
    curNumber = 0
    for x in range(0, len(n)):
        i=len(n)-x-1
        for y in range(0, len(digitsIn)):
            if (n[x:x+1]==digitsIn[y:y+1]):
                curNumber=(baseIn**i)*int(y)+curNumber
    result = ''
    while curNumber != 0:
        remainder = curNumber % baseOut
        curNumber = int((curNumber-remainder)/baseOut)
        result = digitsOut[remainder:remainder+1]+result
    return result

print()