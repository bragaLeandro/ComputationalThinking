myOrderedList = [20,30,60,70]
myUnorderedList = [20, 60, 30, 40]

def verifyOrdered(list):
    for i in range (len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


isOrdered = verifyOrdered(myOrderedList)
isOrdered1 = verifyOrdered(myUnorderedList)

print(isOrdered, isOrdered1)