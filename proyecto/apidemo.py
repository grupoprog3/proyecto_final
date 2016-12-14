from urllib import urlopen

url= "http://lorempixel.com/400/200"
resultado = urlopen(url)
lectura = resultado.read()
f = open("holder.jpg")
f.write(lectura)
f.close()