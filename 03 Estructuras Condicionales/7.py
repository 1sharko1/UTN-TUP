string = input("Ingrese una frase o palabra: ")
if string[-1] in "aeiouAEIOU":
    print(f"{string}!")
else:  
    print(string)