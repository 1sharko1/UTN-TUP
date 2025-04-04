# Pedimos al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Comparamos el valor para asignarle una categoria
if magnitud < 3:
    print("Muy leve")
elif 3<= magnitud < 4:
    print("Leve")
elif 4<= magnitud < 5:
    print("Moderado")
elif 5<= magnitud < 6:
    print("Fuerte")
elif 6<= magnitud < 7:
    print("Muy Fuerte")
elif magnitud >=7:
    print("Extremo")