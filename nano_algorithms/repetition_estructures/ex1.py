#Sum of even numbers

#n = int(input("Inform n"))

n = int(input("Inform n: "))
even_sum = 0
aux = 1

while aux <= n:
    if aux % 2 == 0:
        even_sum = even_sum + aux
    aux = aux + 1

print("The sum of all even numbers until {} is {}".format(n, even_sum))
