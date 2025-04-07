# Ejercicio 1: Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios: ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300

precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva':1450
}
precios_frutas.update({
    "Naranja" : 1200,
    "Manzana" : 1500,
    "Pera" : 2300,
})
print(precios_frutas)

# -----------------------------------------------------------

# Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: ● Banana = 1330 ● Manzana = 1700 ● Melón = 2800

precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva':1450,
    "Naranja" : 1200,
    "Manzana" : 1500,
    "Pera" : 2300,
}
precios_frutas.update({
    'Banana': 1330, 
    "Manzana" : 1700,
    'Melón': 2800, 
})
print(precios_frutas)

# -----------------------------------------------------------

# Ejercicio 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {
    'Banana': 1330, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450,
    "Naranja" : 1200,
    "Manzana" : 1700,
    "Pera" : 2800,
}
lista_frutas = list(precios_frutas.keys())
print(f"La lista de las frutas son: {lista_frutas}")

# -----------------------------------------------------------

# Ejercicio 4: Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."

class Persona:
    def __init__(self, nombre, apellido, nacionalidad, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.edad = edad
        
    def saludar (self):
        return print(f"Hola soy {self.nombre} {self.apellido}, vivo en {self.nacionalidad} y tengo {self.edad} años" )

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nacionalidad = input("Ingresa tu nacionalidad: ")
edad = input("Ingresa tu edad: ")
persona = Persona(nombre, apellido, nacionalidad, edad)
persona.saludar()

# -----------------------------------------------------------

# Ejercicio 5: Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.

from math import pi
class Circulo: 
    def __init__(self, radio): 
        self.radio = radio
    def calcular_area(self):
        return pi * self.radio ** 2
    def calcular_perimetro(self):
        return 2 * pi * self.radio
valor_radio = float(input("Ingrese un radio: "))
circulo = Circulo(valor_radio)
print(f"El area del circulo es: {circulo.calcular_area():.2f}")
print(f"El perimetro del circulo es: {circulo.calcular_perimetro():.2f}")

# -----------------------------------------------------------

# Ejercicio 6: Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

# -----------------------------------------------------------

# Ejercicio 7: Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: ● Agregar clientes (encolar). ● Atender clientes (desencolar). ● Mostrar el siguiente cliente en la fila.

# -----------------------------------------------------------

# Ejercicio 8: Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.

# -----------------------------------------------------------

# Ejercicio 9:  Dada una lista enlazada, implementa una función para invertirla.

