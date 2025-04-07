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

