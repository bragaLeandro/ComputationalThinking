def primo(n):
    if n == 1:
        return "Não é primo"
    else:
        div = 2
        while n % div != 0:
            div = div + 1
        if div == n:
            return n
        else:
            return "Não é primo"

print(primo(2))