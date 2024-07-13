def main():

    n = int(input("Ingresa cantidad de numeros a agregar: "))
    datos = []
    for i in range(1,n+1):
        datos.append(input("Ingresa numero a anadir a la lista: "))
    print(bubble(datos))

def bubble(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
        n = n-1
    return lista

if __name__ == "__main__":
    main()
