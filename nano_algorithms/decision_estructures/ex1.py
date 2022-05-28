n1 = float(input("Inform the first number: "))
n2 = float(input("Inform the second number: "))

while n1 == n2:
    print("The second number cannot be equals to the first number")
    n2 = float(input("Inform the second number: "))

if n1 > n2:
    print("The highest number is {}".format(n1))
elif n1 < n2:
    print("The highest number is {}".format(n2))