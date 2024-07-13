"""
# Pedir al usuario que ingrese dos numeros
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

# Realizar la division y mostrar el resultado
resultado = num1 / num2
print("El resultado de la division es: ", resultado)
"""

try:
    # Pedir al usuario que ingrese dos numeros
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    # Realizar la division y mostrar el resultado
    resultado = num1 / num2
    print("El resultado de la division es: ", resultado)

except ZeroDivisionError:
    # Este bloque solo se ejecutara cuando hallan excepciones
    print("Error: No se puede dividir por cero.")

else:
    # Este bloque se ejecutara si no se produjo ninguna excepcion
    print(f"El resultado de la division es: {resultado}")

finally:
    # Este bloque se ejecutara siempre, sin emportar si hubo o no excepcion
    print("Gracias por usar la calculadora.")
