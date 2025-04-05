print("Ingrese un numero entero positivo:")
num = int(input())
suma = 0
# Definimos un bucle while que se ejecuta mientras el numero sea menor a 0.
while num < 0:
    print("Porfavor el numero a ingresar debe ser positivo: ")
    num = int(input())
# Definimos un bucle for que comienza luego de que el numero ingresado sea mayor a 0 y termina cuando se ingresa el 0.
for x in range (0, num + 1):
    suma += x
print("La suma de los numeros comprendidos entre 0 y ", num, " es: ", suma)