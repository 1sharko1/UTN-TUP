# Funcion segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
equivalencia_segundos_a_horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {equivalencia_segundos_a_horas} horas.")