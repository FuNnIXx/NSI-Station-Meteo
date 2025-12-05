import requests
import difflib
import dict
import tkinter as tk
from tkinter import messagebox
import webbrowser

city = '' # Nom de la ville de recherche
country = '' # Nom du pays de recherche
countryiso = '' # Nom du pays de recherche sous la forme ISO_3166 2C

ctr_search = ''
city_data = ''
iso_search = ''

data = '' # Données météo de la ville

def get_data(countryiso, city): # Retourne les données météo de la ville, sous la forme d'un dictionnaire
    if ' ' in city:
        city = city.replace(' ', '+')
    url = (
        'https://api.openweathermap.org/data/2.5/weather?q=###,++&appid=7585221fbcead099c4e4c4bb6fd3b68f&units=metric')
    url = url.replace('###', city)
    url = url.replace('++', countryiso)
    data = requests.get(url)
    data = data.json()
    if data['cod'] == '404':
        return('error 404 : City not found')
    else:
        return(data)

def get_map_link(data): # Retourne le lien de la carte de la ville
    openstreetmap = 'https://www.openstreetmap.org/#map=13/###/+++'
    openstreetmap = openstreetmap.replace('###', str(data['coord']['lat']))
    openstreetmap = openstreetmap.replace('+++', str(data['coord']['lon']))
    return(openstreetmap)

def country_search(ctr_search): # Retourne la liste des pays correspondants à la recherche
    global ctr_research
    list = dict.ctr_to_iso()
    ctr_research = difflib.get_close_matches(ctr_search, list.keys(), n=10, cutoff=0.5)

def country_to_iso(country): # Retourne le code ISO_3166
    global countryiso
    list = dict.ctr_to_iso()
    countryiso = list[country]

def city_data_get(country): # Retourne la liste des villes correspondantes à la recherche
    global city_data
    url = "https://countriesnow.space/api/v0.1/countries/cities"
    payload = {"country": country}
    headers = {}
    city_data = requests.request("POST", url, headers=headers, data=payload)

def city_search():
    global city
    list = city_data.json()
    city = difflib.get_close


# Il faut tout refaire, c'est bon pour du cli mais pas pour TK