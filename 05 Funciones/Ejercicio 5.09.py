def celsius_a_fahrenheit(celsius):
    return 9/5*celsius + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La equivalencia de {celsius} grados Celsius a fahrenheit seria: {fahrenheit:.2f}")
