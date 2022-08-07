t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def calculaMedia(t):
    media = 0
    for i in t:
        media = media + i
    return media / len(t)

media = calculaMedia(t)

print(media)