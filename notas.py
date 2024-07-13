grades = []
while True:
    grade = input("Ingresa una calificacion (o 'salir' para terminar): ")
    if grade.lower() == 'salir':
        break
    else:
        grades.append(float(grade))

average = sum(grades)/len(grades)
print("El promedio de notas es: ", average) #+ es para concatenar valores
#, es para concatenar varios y los separa automaticamente
