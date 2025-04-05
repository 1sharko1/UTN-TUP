# Pedimos al usuario ingresar dos numero.
num1 = int(input("Ingrese un numero entero distinto de 0: "))
num2 = int(input("Ingrese un segundo numero entero distinto de 0: "))
# Mostramos en pantalla las operaciones basicas entre estos dos numeros.
print(f"La suma entre {num1} y {num2} es: ", num1 + num2)
print(f"La resta entre {num1} y {num2} es: ", num1 - num2)
print(f"La multiplicacion entre {num1} y {num2} es: ", num1 * num2)
print(f"La division entre {num1} y {num2} es: ", round(num1 / num2, 2))