# Funcion operaciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# Programa principal
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
resultados = operaciones_basicas(a,b)
print(f"El resultado de sumar {a} y {b} es {resultados[0]}")
print(f"El resultado de restar {a} y {b} es {resultados[1]}")
print(f"El resultado de multiplicar {a} y {b} es {resultados[2]}")
print(f"El resultado de dividir {a} y {b} es {resultados[3]}")