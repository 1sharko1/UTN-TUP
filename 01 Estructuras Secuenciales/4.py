# Al principio del programa necesitamos importar la librería math ya que la necesitaremos para utilizar el número pi
import math

radio = float(input("Ingrese un radio para que devolvamos su area y perimetro: ")) 
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio 
print(f"El area del circulo es de {area} y el perimetro es de {perimetro}")