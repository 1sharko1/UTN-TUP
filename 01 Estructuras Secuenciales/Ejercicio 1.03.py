# Pedimos datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
# Mostramos en pantalla los datos del usuario, concatenando strings colocando f antes de las commilas.
print(f"Usted es {nombre} {apellido}, tiene {edad} años, y vive en {residencia}.")