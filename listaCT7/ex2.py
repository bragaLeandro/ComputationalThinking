import random

n = 29

def createRandomList(n):
    myList = []
    for i in range(n):
        numero = random.randint(1, 1001)
        myList.append(numero)
    return myList

randomList = createRandomList(n)

print(randomList)
