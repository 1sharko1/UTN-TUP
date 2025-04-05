# Opcion 1 (Trabajando el numero como un string.)
num = (input("Ingrese un numero: "))
# Revertimos el numero 
reverso = num[::-1] # Esto es una tecnica llamada slicing que nos permite sustraer pare te de un texto. Su sintaxis es: cadena[incio:fin:paso].
                    # En este caso al colocar [::-1] es decir valores vacios, estamos diciendo que comience desde el final y termine en el principio contando hacia atras debido a que indicamos el paso en -1.
print(reverso)

# Opcion 2 (Trabajando el numero como un entero)
num = int(input("Ingrese un numero: "))
invertido = 0
while num != 0:
    digito = num % 10 # Esto nos almacena el ultimo digito.
    invertido = invertido * 10 + digito # Esto agrega el digito almacenado al numero invertido.
    num = num // 10 # Esto quita el ultimo digito del numero original.
print("El numero invertido es: ", invertido)