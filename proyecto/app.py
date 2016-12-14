from flask import Flask, request

app = Flask(__name__)

# Se define la clave para conectarse al Api proporcionada por la página de OpenWeather y la unidad de la temperatura en Celsius
key = 'db7b6038d0c382e5f645bf41bfeeb8fc'
unidad = '&units=metric'
#ciudad = ""

# Determinando la ciudad en el url del api. Respuesta en formato Json
#@app.route('/urlCiudad')
def urlCiudad(self, ciudad):
    url = 'api.openweathermap.org/data/2.5/weather?q=Panama' + unidad + '&APPID=' + key
    # url = 'api.openweathermap.org/data/2.5/weather?' + 'q=' + str(ciudad) + unidad + '&APPID=' + key
    return url

# El api por defecto da una respuesta en formato Json. Se crea una función que genere una respuesta en html
#@app.route('/respHtml')
def respHtml(self, ciudad):
    formato_html = '&mode=html'
    url = 'api.openweathermap.org/data/2.5/weather?q=Panama' + unidad + formato_html + '&APPID=' + key
    # url = 'api.openweathermap.org/data/2.5/weather?' + 'q=' + str(ciudad) + unidad +  formato_html + '&APPID=' + key
    return url

opener_get = request.get('"' + urlCiudad(app,'Panama') + '"') #Obteniendo información del api en formato json
#opener_get = request.get('"' + respHtml(app,ciudad) + '"') #Obeniendo información del api en formato html
print (opener_get)

if __name__ == '__main__':
    app.run()
