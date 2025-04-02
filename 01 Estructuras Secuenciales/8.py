altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso: "))
imc = round(peso / altura**2, 2)
print(f"Tu IMC es {imc}")