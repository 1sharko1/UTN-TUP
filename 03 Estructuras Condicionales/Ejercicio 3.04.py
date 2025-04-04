# Le pedimos al usuario que ingrese su edad.
edad = int(input("Ingresa tu edad: "))
categoria = ""
# Evaluamos los rangos de edades y le asignamos una categoria
if edad >= 0 and edad < 12: 
    categoria = "Niño/a"
elif edad >= 12 and edad < 18:
    categoria = "Adolescente"
elif edad >= 18 and edad < 30:
    categoria = "Adulto/a joven"
elif edad >= 30:
    categoria = "Adulto"
else:
    print("Ingrese una edad valida")
print(categoria)
