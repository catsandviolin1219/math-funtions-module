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


def getFraction(frac_):
    frac = frac_
    numToAdd = 0
    a = [0, 1]
    b = [1, 1]
    print("Starting")
    print(frac)
    while True:
        new = [a[0] + b[0], a[1] + b[1]]
        if frac < new[0]/new[1]:
            b = new
        elif frac == new[0]/new[1]:
            return [new[0] + numToAdd * new[1], new[1]]
        elif frac == 0:
            return [0, 1]
        elif frac == 1:
            return [1, 1]
        else:
            a = new

print(getFraction(0.20749838396))