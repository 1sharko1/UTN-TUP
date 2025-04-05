# Pedimos al usuario ingresar dos numeros enteros.
print("Ingrese dos numero entero: ")
num1 = int(input())
num2 = int(input())

# Inicializamos las variables mayor y menor para poder actualizar su valor segun los numeros ingresados.
mayor = -1000
menor = 1000

# Inicializamos el contador suma en 0
suma = 0

# Comparamos los numeros y se asigna el numero mas grande a la variable mayor, el mas pequeno a la variable menor y en caso de que sean iguales no se inicia el bucle.
if num1 == num2:
    print("No hay suma de valores entre los numeros ingresados ya que son iguales")
else: 
    if num1 > num2:
        mayor = num1
        menor = num2
    else: 
        mayor = num2
        menor = num1
        
# Definimos un bucle que va recorrer desde el numero menor + 1 (ya que se pide no incluir el numero mas pequeno) hasta el mayor (por defecto la funcion range no incluye el numero final).
# El valor de suma va a actualizarse sumandose el valor de x a la par que se actualiza nuestra variable x, dandonos como resultado la suma entre los dos valores comprendidos de los numeros ingresados.
    for x in range (menor + 1, mayor):
        suma += x
    print("La suma total entre los valores comprendidos de los dos numeros ingresados es: ",suma)