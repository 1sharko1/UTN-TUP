# Pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un numero par: "))

# Utilizamos el operador % llamado modulo, que nos devuelve el resto de una operacion
# En caso de ser 0 estamos hablando de un numero par
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Porfavor ingrese un numero par")