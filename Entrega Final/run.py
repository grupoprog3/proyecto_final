"""
Esta aplicación muestra el nombre de una ciudad y su respectiva temperatura real y relativa en °F y °C"
Módulos principales para leer datos de URLs en Python: urllib y urllib2.
"""
import urllib.request
import urllib.error
import json

class run:

    def __init__(self, zip):
         self.zip = zip


    """
    Introduciendo el ZipCode junto con la llave del api, se realiza una consulta a la api de wundergrond.com,
    la clase Request define objetos que encapsulan toda la información relativa a una petición.
    La función urlopen la usamos para crear nuestros pseudo-archivos. Posterior le damos lectura al objeto f,
    con el metodo f.read(), y descargamos - ordenamos en json_string en busca de las variables que nos interesa mostrar.
    """
    zip = input('Para que codigo postal le gustaria ver el tiempo? ')

    def consultaApi(self,zip):
        key = '825c5d1711422429'
        while 1:

            url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/' + zip + '.json'
            f = urllib.request.urlopen(url)
            json_string = f.read().decode('utf-8')
            parsed_json = json.loads(json_string)
            city = parsed_json['location']['city']
            state = parsed_json['location']['state']
            weather = parsed_json['current_observation']['weather']
            temperature_string = parsed_json['current_observation']['temperature_string']
            feelslike_string = parsed_json['current_observation']['feelslike_string']

            print ("Tiempo en %s, %s: %s. \nLa temp. es %s, pero se siente como %s." %(city,state,weather.lower(),temperature_string,feelslike_string))
            f.close()
