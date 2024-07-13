def main():

    palabra = input("Ingrese una palabra: ")

    if palabra == palabra[::-1]:
        print("La palabra es palindroma")
    else:
        print("No es palindroma")

if __name__ == "__main__":
    main()
