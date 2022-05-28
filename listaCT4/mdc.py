def mdc(a, b):
    div = a
    while a % div != 0 or b % div != 0:
        div = div - 1

    return div

print(mdc(42, 18))    

