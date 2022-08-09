n = 10

def createReversedList(n):
    myList = []
    for i in range(n):
        word = input("Enter the {}° word: ".format(i+1))
        myList.append(word)
    myList.reverse()
    return myList

reversedList = createReversedList(n)

print(reversedList)


