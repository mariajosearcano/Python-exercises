camel_case = input("Ingrese un nombre de variable en camelCase: ")
snake_case = ""

for i in range(len(camel_case)):
    if camel_case[i].isupper():
        snake_case += "_" + camel_case[i].lower()
    else:
        snake_case += camel_case[i]

print("El nombre de la variable en snake_case es: ", snake_case) #la coma sirve para seprar los argumentos que se van a imprimir NO PARA CONCATENAR

# para hacer una division entera en python se usa //
