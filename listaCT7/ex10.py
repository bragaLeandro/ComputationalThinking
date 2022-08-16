listA = [20, 45, 70, 85]
listB = [10, 24, 35, 43]

def intercalaListaOrdenada(listA, listB):
    listC = []
    i = 0
    j = 0
    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
            listC.append(listA[i])
            i += 1
        else:
            listC.append(listB[j])
            j += 1
    while i < len(listA):
        listC.append(listA[i])
        i += 1
    while j < len(listB):
        listC.append(listB[j])
        j += 1
    return listC

print(intercalaListaOrdenada(listA, listB))