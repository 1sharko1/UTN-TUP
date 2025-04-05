# Le pedimos al usuario que ingrese su contrasena
contrasena = input("Ingrese su contrasena de entre 8 y 14 caracteres: ")

# Utilizamos la funcion len() para verificar la cantidad de caracteres del string ingresado.
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contrasena correcta")
else:
    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")