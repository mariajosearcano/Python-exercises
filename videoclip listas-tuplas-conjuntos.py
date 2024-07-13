# Para crear listas utilizamos [listas]
# Para crear tuplas utilizamos (tuplas)
# Para crear conjuntos {conjuntos}
# Para crear diccionarios :

#listas
frutas = ["manzana", "pera", "durazno"]
print(frutas)
    #puede contener elementos de distintos tipos de datos a la vez

#tuplas
materias = ("espa;ol", "matematicas", "historia")
print(materias)
    #las tuplas son para guardar elementos inmutables
    #pueden contener elementos de distintos tipos de datos

#conjuntos
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
c = a|b #| es la union en conjuntos
print(c)
    #& interseccion
    #- diferencia
    #^ diferencia simetrica

#diccionarios
ingles = {"azul":"blue", "blanco":"white", "verde":"green"}
print(ingles)
    #permite almacenar informacion en pares clave-valor: utiles para acceder a informacion sin la posicion
