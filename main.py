from tarfile import data_filter
from datetime import time
import requests
from tkinter import *
from iso_3166 import *
from API import *
from art import *
from desc import *

running = True
block_text = text2art("Weather's Call", font='big')
print(block_text)

cityName = ''

while running:
    def DataGet():
        global cityName
        Pays = ISO_CTR(input("Pays de recherche : "))
        if Pays == "Recherche abandonnée." :
            return(0)
        cityName = search_city(Pays)
        if cityName == "Recherche abandonnée." :
            return(0)

        if ' ' in cityName :
            cityName = cityName.replace(' ', '+')
        url = ('https://api.openweathermap.org/data/2.5/weather?q=###,++&appid=7585221fbcead099c4e4c4bb6fd3b68f&units=metric')
        url = url.replace('###', cityName)
        url = url.replace('++', Pays)

        response = requests.get(url)
        response = response.json()
        if response['cod'] == '404':
            return response('message')
        else:
            return(response)

    DATA = DataGet()
    if DATA != 0:
        openstreetmap = 'https://www.openstreetmap.org/relation/108394#map=13/###/+++'
        openstreetmap = openstreetmap.replace('###', str(DATA['coord']['lat']))
        openstreetmap = openstreetmap.replace('+++', str(DATA['coord']['lon']))

        print(f'\nVoici les dernières informations météo sur la commune de {cityName} :\n')
        print(f'\U0001F4CD Voici la localisation de la ville : {openstreetmap}\n')
        print(f'Données météo :\n\U0001F321 La temperature à {cityName} est de {DATA["main"]["temp"]}°C.\n\U0001F9E5 Le ressenti est cependant de {DATA["main"]["feels_like"]}°C.\n')
        print(f'\U0001F4C8 La temperature maximale est de {DATA["main"]["temp_max"]}°C.\n\U0001F4C9 La temperature minimale est de {DATA["main"]["temp_min"]}°C.\n')
        print(f'\U0001F321 La pression atmosphérique est de {DATA["main"]["pressure"]} hPa.\n')
        print(f'\U0001F321 Les precipitations sont de {DATA['rain']['1h']} mm sur la dernière heure.' if 'rain' in DATA and '1h' in DATA['rain'] else 'Aucune donnée concernant les precipitations.')
        print(f'\U0001F321 Il est tombé {DATA['snow']['1h']} mm de neige sur la dernière heure.' if 'snow' in DATA and '1h' in DATA['snow'] else 'Aucune donnée concernant la neige.')
        print(f"\U0001F4A7 L'humidité de l'air est de {DATA['main']['humidity']}%.")
        weathermain = weathermain(DATA['weather'][0]['main'])
        weathericon = weatheremoji(DATA['weather'][0]['icon'])
        description= description(DATA['weather'][0]['description'])
        print(f"\U0001F321 Conditions météo :\n- Description générale : {weathermain}\n- Description détaillée : {description} / {weathericon}\n")
        print(f'\U0001F311 La visibilitée est de {DATA["visibility"]}m. (Max 10km)')

        if DATA['wind']['deg'] >= 337.5 or DATA['wind']['deg'] < 22.5:
            direction = ' du Nord'
            emojiwind = '➡️'
        elif DATA['wind']['deg'] >= 22.5 and DATA['wind']['deg'] < 67.5:
            direction = ' du Nord-Est'
            emojiwind = '↗️'
        elif DATA['wind']['deg'] >= 67.5 and DATA['wind']['deg'] < 112.5:
            direction = " de l'Est"
            emojiwind = '➡️'
        elif DATA['wind']['deg'] >= 112.5 and DATA['wind']['deg'] < 157.5:
            direction = ' du Sud-Est'
            emojiwind = '↘️'
        elif DATA['wind']['deg'] >= 157.5 and DATA['wind']['deg'] < 202.5:
            direction = ' du Sud'
            emojiwind = '⬇️'
        elif DATA['wind']['deg'] >= 202.5 and DATA['wind']['deg'] < 247.5:
            direction = ' du Sud-Ouest'
            emojiwind = '↙️'
        elif DATA['wind']['deg'] >= 247.5 and DATA['wind']['deg'] < 292.5:
            direction = " de l'Ouest"
            emojiwind = '⬅️'
        else:
            direction = ' du Nord-Ouest'
            emojiwind = '↖️'

        print(f'\U0001F310 Le vent souffle a {DATA["wind"]["speed"]*3.6} km/h.\n{emojiwind} Le vent souffle en direction de {direction}.\n')
        print(f'\U00002601 La couverture nuageuse est de {DATA["clouds"]["all"]}%.\n')



    reboot = input('Voulez vous faire une nouvelle recherche ? O / N : ')
    if reboot == 'n' or reboot == 'N':
        running = False
        block_text = text2art("Closing...", font='big')
        print(block_text)
