# Pedimos al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")
num = int(input("Elegi 1 en caso de querer tu nombre en mayusculas, 2 en caso de quererlo en minusculas y 3 en caso de querer solo la primer letra mayuscula: "))

# Con la funcion upper todo el string se convierte en mayuscula.
if num == 1:
    print(nombre.upper())

# Con la funcion lower todo el string se convierte en minuscula.
elif num == 2: 
    print(nombre.lower())

# Con la funcion tittle la primer letra del string se convierte en mayuscula.
elif num == 3: 
    print(nombre.title())
else:
    print("Porfavor, el numero a ingresar debe ser 1 o 2 o 3")