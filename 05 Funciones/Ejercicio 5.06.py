# Funcion tabla de multiplicar.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)
