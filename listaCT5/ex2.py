def separe(word):
    i = 0
    new = ""
    while i < len(word):
        new = new + word[i] + " "
        i = i + 1
    return new

print(separe("Teste"))