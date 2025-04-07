from math import pi
class Circulo: 
    def __init__(self, radio): 
        self.radio = radio
    def calcular_area(self):
        return pi * self.radio ** 2
    def calcular_perimetro(self):
        return 2 * pi * self.radio
valor_radio = float(input("Ingrese un radio: "))
circulo = Circulo(valor_radio)
print(f"El area del circulo es: {circulo.calcular_area():.2f}")
print(f"El perimetro del circulo es: {circulo.calcular_perimetro():.2f}")