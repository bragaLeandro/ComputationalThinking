def primo(n):
    if n == 1:
        return False
    else:
        div = 2
        while n % div != 0:
            div = div + 1
        if div == n:
            return True
        else:
            return False
        
print(primo(2))