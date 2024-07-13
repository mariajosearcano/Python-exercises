def main():

    num = int(input("Ingresa un numero para hallarle un factorial: "))#hay que especificar el tipo de dato para inputs que no son strings

    mul = 1
    for i in range(1,num+1):
        mul = mul * i

    print("El factorial es: ", mul)

if __name__ == "__main__":
    main()
