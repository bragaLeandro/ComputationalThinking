listA = [20, 45, 70, 85]
listB = [10, 24, 35, 43]

#TODO FIX THIS CODE

def intercala(listA, listB):
    orderedList = []
    for i in range (len(listA)):
        for j in range (len(listB)):
            if listA[i] < listB[j]:
                orderedList.append(listA[i])
            else:
                orderedList.append(listB[j])

    for i in range (len(listA)):
        orderedList.append(listA[i])
    for j in range (len(listB)):
        orderedList.append(listB[j])
    
    return orderedList


orderedList = intercala(listA, listB)

print(orderedList)

