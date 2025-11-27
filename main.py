# Import the requests module
import requests
from tkinter import*

def DataGet():
    cityName = input("Nom de la ville : ")
    if ' ' in cityName :
        cityName = cityName.replace(' ', '+')

    url = ('https://api.openweathermap.org/data/2.5/weather?q=###,fr&appid=7585221fbcead099c4e4c4bb6fd3b68f')
    url = url.replace('###', cityName)
    # Send a GET request to the desired API URL
    response = requests.get(url)

    # Parse the response and print it
    reponse = response.json()

DataGet()
