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

## Shorthand for convBase(n, 16)
def dec2Hex(n):
    return convBase(n, 16)

## Converts any decimal number into any base. By default it converts decimal to hexadecimal. Also able to specify custom digits.
def convBase(n, baseOut, digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']):
    if (n == 0):
        return '0'
    result = ''
    curNumber = n
    while curNumber != 0:
        remainder = curNumber % baseOut
        curNumber = int((curNumber-remainder)/baseOut)
        result = digits[remainder]+result
    return result