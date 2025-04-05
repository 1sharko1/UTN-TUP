segundos = float(input("Ingrese una cantidad de segundos: "))

# Agregamos la funcion round para redondear y un dos tras la coma para que el resultado muestre solo dos decimales.

equivalenciaHora = round(segundos/3600, 2)
print(f"La cantidad de {segundos} segundos equivale a {equivalenciaHora} horas") 