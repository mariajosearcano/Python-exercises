def main():
    palabra = input("Ingrese una palabra: ")
    resultado = twttrr(palabra)
    print("La palabra abreviada es: " + ''.join(resultado))#join une todos los elementos de una lista en una sola cadena de texto
    #para concatenar strings se usa +
#los metodos no hay que identarlos como si estuviesen dentro de el main
def twttrr(pal):
    pal = pal.lower()
    sal = []
    for z in range(len(pal)): #len() busca la longitud de una palabra
        if pal[z] not in ["a","e","i","o","u"," "]: #si la letra de la palabra no esta entre esa lista
            sal.append(pal[z])
    return sal
    
if __name__ == "__main__":
    main()
