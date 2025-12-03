# Import the requests module
import requests
from tkinter import*
from iso_3166 import*

def DataGet():
    Pays = ISO_CTR(input("Pays de recherche : "))
    cityName = input("Nom de la ville : ")
    if ' ' in cityName :
        cityName = cityName.replace(' ', '+')
    url = ('https://api.openweathermap.org/data/2.5/weather?q=###,++&appid=7585221fbcead099c4e4c4bb6fd3b68f')
    url = url.replace('###', cityName)
    url = url.replace('++', Pays)

    response = requests.get(url)
    response = response.json()
    if response['cod'] == '404':
        return response('message')
    else:
        return(response)

DATA = DataGet()

openstreetmap = 'https://www.openstreetmap.org/relation/108394#map=13/###/+++'
openstreetmap = openstreetmap.replace('###', str(DATA['coord']['lat']))
openstreetmap = openstreetmap.replace('+++', str(DATA['coord']['lon']))

Weather = DATA[]