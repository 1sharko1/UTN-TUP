# Pedimos al usuario ingresar un numero.
print("Ingrese un numero y devolveremos la cantidad de digitos: ")
num = int(input())

# Creamos una variable para almacenar el valor ingresasdo para luego mostrarlo en pantalla.
num_inicial = num

# Inicializamos el contador en 0.
digitos = 0

# Definimos un bucle con la condicion de que se ejecute solo mientras el numero sea distino a 0. 
while num != 0:

    # Contamos la cantidad de digitos basandonos en que tras cada iteracion el numero ira perdiendo un digito hasta llegar a 0 debido a la division baja que aplicamos al numero en cada iteracion.
    digitos += 1
    num = num // 10

# Se muestra en pantalla la cantidad de digitos del numero ingresado.
print("La cantidad de digitos de ", num_inicial, " es de: ", digitos)
