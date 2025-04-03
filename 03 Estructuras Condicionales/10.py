# Le pedimos al usuario si esta en el hemisferio norte o sur y el dia y mes en el que se encuentra.
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N = norte, S = sur): ").upper()
estacion = ""
dia = int(input("Ingrese en formato numero el dia en el que se encuentra: "))
mes = int(input("Ingrese en formato numero el mes en el que se encuentra: "))

# Validamos si el valor ingresado es correcto
if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Debe ser 'N' o 'S'.")
elif mes < 1 or mes > 12:
    print("Mes no válido. Debe ser un número entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día no válido. Debe ser un número entre 1 y 31 según el mes.")
    
# Asignamos la estacion a partir del dia y fecha en el que se encuentra, partiendo de que nos ubicamos en el hemisferio norte    
if hemisferio == "N":
    if mes in [1, 2]:
        estacion = "Invierno"
    elif mes in [4, 5]:
        estacion = "Primavera"
    elif mes in [7, 8]:
        estacion = "Verano"
    elif mes in[10, 11]:
        estacion = "Otoño"
    if mes == 12: 
        if dia < 21:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    if mes == 3:
        if dia < 21:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    if mes == 6:
        if dia < 21:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    if mes == 9:
        if dia < 21:
            estacion = "Verano"
        else:
            estacion = "Otoño"
# Asignamos la estacion a partir del dia y fecha en el que se encuentra, partiendo de que nos ubicamos en el hemisferio sur                
if hemisferio == "S":
    if mes in [1, 2]:
        estacion = "Verano"
    elif mes in [4, 5]:
        estacion = "Otoño"
    elif mes in [7, 8]:
        estacion = "Invierno"
    elif mes in[10, 11]:
        estacion = "Primavera"
    if mes == 12: 
        if dia < 21:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    if mes == 3:
        if dia < 21:
            estacion = "Verano"
        else:
            estacion = "Otoño"
    if mes == 6:
        if dia < 21:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    if mes == 9:
        if dia < 21:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
print(f"Usted se encuentra en {estacion}")
    

