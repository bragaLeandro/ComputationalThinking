n = int(input("Informe n: "))
aux = 0
ultimo = 1
penultimo = 1

if n == 1 or n == 2:
    fn = 1
else:
    aux = 3
    while aux <= n:
        fn = ultimo + penultimo
        penultimo = ultimo
        ultimo = fn
        aux = aux+1

print(fn)

