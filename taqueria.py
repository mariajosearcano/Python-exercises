def main(): #convencion para definir el punto de entrada principal de un programa
    
    menu = {
        "BAJA TACO" : 4.00,
        "BURRITO" : 7.50,
        "BOWL" : 8.50,
        "NACHOS" : 11.00,
        "QUESADILLA" : 8.50,
        "SUPER BURRITO" : 8.50,
        "SUPER QUESADILLA" : 9.50,
        "TACO" : 1.00,
        "TORTILLA SALAD" : 8.00
    }
    order_total = 0.0
    while True:
        try:
            item = input("Ingrese un articulo de su pedido: ")
        except EOFError:
            break
        item = item.upper()
        if item in menu:
            order_total += menu[item]
            print(f"${order_total:.2f}")
        elif item == "CONTROL-D":
            print(f"El total de su pedido es ${order_total:.2f}")
            #.2f indica que pueden haber 2 decimales despues del punto y se formatea como un numero punto-flotante
            break
        else:
            print("Articulo invalido")

    #el cuerpo tiene que estar bien identado dentro del main

if __name__ == "__main__":
    main()
    