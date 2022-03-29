#Uma equação de 2°grau é da forma: ax² + bx + c = 0, onde a !=0. Escreva um algoritmo que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível. Use a seguinte fórmula para resolver a equação:
import math

a = float(input("Informe o coefiente A: "))
b = float(input("Informe o coefiente B: "))
c = float(input("Informe o coefiente C: "))

calculo_delta = b**2 - 4*a*c
calculo_x1 = (-b + math.sqrt(calculo_delta))/2*a
calculo_x2 = (-b - math.sqrt(calculo_delta))/2*a

print("O valor de x1 é:", calculo_x1, "e o valor de x2 é:", calculo_x2)
