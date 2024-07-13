peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = peso / (altura**2) #dos asteriscos en python es como una potencia

if imc < 18.5:
    resultado = "Bajo peso"
elif imc > 25:
    resultado = "Sobrepeso"
else:
    resultado = "Normal"

print(f"Su indice de masa corporal es {imc}. Usted tiene {resultado} ")
