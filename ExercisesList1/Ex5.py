#Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.
#Area = pi.r²
#Perimetro = 2.pi.r

pi = 3.141592
raio = float(input("Digite o raio do círculo: "))
diametro = raio*2
area = pi*raio**2
perimetro = 2*pi*raio

print("A área do círculo é" , area , "e o perímetro do círculo é" , perimetro)

