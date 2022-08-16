def arrumaPortas(pes, portas):
    for numPorta in range(1, 1001):
        if numPorta % pes == 0:
            if portas[numPorta] == False:
                portas[numPorta] = True
            else:
                portas[numPorta] = False

doors = [False] * 1001

for person in range(1, 1001):
    arrumaPortas(person, doors)

for num in range(1, 1001):
    if doors[num]:
        print(doors[num])