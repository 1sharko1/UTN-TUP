# Creamos un bucle que recorre desde 100 a 0 con un indicador de que se cuente de dos en dos. Esto lo hacemos colocando una coma y el numero que indica como debe recorrer los valores (luego de definir los dos valores de inicio y fin del for), en este caso -2 ya que nos piden que sea en orden decreciente.
# Cada iteracion mostrara en pantalla el decremento del valor de la variable x, lo que dara como resultado una lista de los numeros pares comprendidos entre 0 y 100 en orden decreciente.
for x in range (100, -1, -2):
    print(x)