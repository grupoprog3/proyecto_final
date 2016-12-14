#Diana
from flask import Flask, request

app = Flask(__name__)

# Se define la clave para conectarse al Api proporcionada por la página de OpenWeather y la unidad de la temperatura en Celsius
key = 'db7b6038d0c382e5f645bf41bfeeb8fc'
unidad = '&units=metric'
ciudad = ""

# Determinando la ciudad en el url del api. Respuesta en formato Json
@app.route('/urlCiudad')
def urlCiudad(self, ciudad):
    #url = 'api.openweathermap.org/data/2.5/weather?q=Panama' + unidad + '&APPID=' + key
    url = 'api.openweathermap.org/data/2.5/weather?' + 'q=' + str(ciudad) + unidad + '&APPID=' + key
    return url

#Consultando al Api
    print("***CONSULTAR CIUDAD***")
    print("\n1 CIUDAD DE PANAMA")
    print("\n 2 BOCAS DEL TORO")
    print("\n 3 CHIRIQUI")
    print("\n 4 VERAGUAS")
    print("\n 0 SALIR")
    respuesta = int(input("Opción: "))

    while respuesta != 0:

        if respuesta == 1:
            ciudad = "Ciudad de Panama"
            opener_get = request.get('"' + urlCiudad(ciudad) + '"') #Obeniendo información del api
            print(opener_get)

        elif respuesta == 2:
            ciudad = "Bocas del Toro"
            opener_get = request.get('"' + urlCiudad(ciudad) + '"')
            print(opener_get)

        elif respuesta == 3:
            ciudad = "Chiriqui"
            opener_get = request.get('"' + urlCiudad(ciudad) + '"')
            print(opener_get)

        elif respuesta == 4:
            ciudad = "Veraguas"
            opener_get = request.get('"' + urlCiudad(ciudad) + '"')
            print(opener_get)

    if respuesta == 0:
        pass

#Instrucción para ejecutar el api
if __name__ == '__main__':
    app.run()