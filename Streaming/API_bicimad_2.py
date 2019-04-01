import requests
import json
import time
import datetime


#Vamos a crear un bucle, para que el programa se ejecute haciendo llamadas a la API
while(1):
	API = 'https://rbdata.emtmadrid.es:8443/BiciMad/get_stations/WEB.SERV.cerrato.alvaro94@gmail.com/C34D9007-8326-4231-85DF-A3E4AB29FA68'

# Almacenamos en b la respuesta de la API
	b = requests.get(API)


# Almacenamos de la API la parte de data que esta en formato JSON
	data_of_stations = str(json.dumps(json.loads(b.json()['data'])))

#Almacenamos en formato str el momento actual, para incluirlo posteriormente en el fichero
	times = str(datetime.datetime.now())

#Concatenamos time con data_of_stations y lo estructuramos manualmente, para que sea en formato JSON
	list_of_stations = '{"time" : "' + times + '", "_station" : ' + data_of_stations + '}' 

#Eliminamos / que se establecen por defecto
	bicimad = list_of_stations.replace(("/"),(""))

#Creamosun archivo
	f = open("/home/acerrato/m3_indiv/def_data/dinamic_data/stations " + str(datetime.datetime.now()), "w+")

#Escribimos en el los resultados que hemos transformado de la API
	f.write(bicimad)

#Hacemos un dalay de 60seg hasta que el programa se vuelva a ejecutar
	time.sleep(60)


