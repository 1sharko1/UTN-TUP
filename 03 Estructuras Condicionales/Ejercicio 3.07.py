# Pedimos al usuario que ingrese una frase
string = input("Ingrese una frase o palabra: ")\
# Preguntamos si la ultima letra contiene una vocal
if string[-1] in "aeiouAEIOU":
    print(f"{string}!")
else:  
    print(string)