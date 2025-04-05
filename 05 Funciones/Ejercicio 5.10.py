def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
c = int(input("Ingresa un numero: "))
promedio = calcular_promedio(a,b,c)
print(f"El promedio entre {a}, {b} y {c} es: {promedio:.2f}")