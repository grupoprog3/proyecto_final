from unittest import TestCase
import urllib.request
import urllib.error
import json
from run import run


class TestConsultaApi(TestCase):
    def test_consultaApi(self):
        a = run
        #Consultando al api y generando un json del zip a probar
        key = "825c5d1711422429"
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/' + '10001' + '.json'
        f = urllib.request.urlopen(url)
        json_string = f.read().decode('utf-8')
        parsed_json = json.loads(json_string)

        #Comparando la respuesta del zip 10001 con el json generado anteriormente
        self.assertEqual(a.consultaApi(a, 10001), parsed_json)
        self.fail()
