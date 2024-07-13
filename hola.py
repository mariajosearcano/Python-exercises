from flask import Flask #importamos la clase Flask del modulo flask
app = Flask(__name__) #se crea una instancia de la clase Flask y se le asigna a la variable app
    #__name__ es una variables especial de python que representa el nombre del modulo actual

@app.route('/') #'define una ruta para la aplicacion', con '/' se le indica que en la ruta raiz. O sea que cada vez que alguien entre se ejecutara la funcion acontinuacion
def hello_world():
    return 'Hola, mundo!'

if __name__ == '__main__': #verifica si el modulo actual se esta ejecutando como el programa principal, y no se vaya a inicializar si solo se esta importando como biblioteca
    app.run() #inicia el servidor web integrado de flask
