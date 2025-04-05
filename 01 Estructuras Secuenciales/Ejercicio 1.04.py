# Al principio del programa necesitamos importar la librería math ya que la necesitaremos para utilizar el número pi.
import math

# Pedimos al usuario ingresar un radio.
radio = float(input("Ingrese un radio para que devolvamos su area y perimetro: ")) 

# Calculamos area y perimetro a partir del radio dado por el usuario.
area = math.pi * (radio)**2
perimetro = 2 * math.pi * radio 
print(f"El area del circulo es de {area} y el perimetro es de {perimetro}")