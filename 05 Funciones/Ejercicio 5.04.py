# Funcion 1
from math import pi
def calcular_area_circulo(radio):
    area = pi * radio**2
    print(f"El area del circulo a partir de que el radio sea {radio} es: {area}")

# Funcion 2
def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * pi
    print(f"El perimetro del circulo a partir de que el radio sea {radio} es: {perimetro}")

radio = float(input("Ingresa el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

