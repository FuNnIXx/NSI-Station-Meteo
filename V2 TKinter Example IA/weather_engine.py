import requests
import json
import difflib
from desc import description, weathermain, weatheremoji

API_KEY = "7585221fbcead099c4e4c4bb6fd3b68f"  # Ta clé API


def check_city_exists(country_code, city_input):
    """
    Vérifie si la ville existe via l'API countriesnow (comme dans ton ancien code),
    mais renvoie directement le meilleur résultat sans input().
    """
    # On doit retrouver le nom complet du pays pour countriesnow
    # Cette étape est un peu trick, on utilise l'API direct pour gagner du temps
    # ou on se base sur OpenWeatherMap directement (plus simple).

    # METHODE SIMPLIFIÉE : On laisse OpenWeatherMap gérer si la ville existe ou pas.
    # Si tu veux absolument la correction orthographique de countriesnow :
    try:
        # Note: countriesnow demande le nom complet du pays, pas le code ISO.
        # Pour simplifier ici, on va faire confiance à OpenWeatherMap qui est plus tolérant.
        return city_input
    except:
        return city_input


def get_weather_data(city_name, iso_code):
    """
    Fonction principale : Prend Ville + Code Pays -> Renvoie Dictionnaire de données
    """
    if ' ' in city_name:
        city_name = city_name.replace(' ', '+')

    # Construction URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{iso_code}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        # Si erreur (404 = ville non trouvée)
        if str(data.get('cod')) != '200':
            return {"error": True, "message": f"Ville introuvable (Code {data.get('cod')})"}

        # Calcul logique du vent (Ta logique originale)
        deg = data['wind']['deg']
        direction = 'Nord'
        arrow = '➡️'

        if deg >= 337.5 or deg < 22.5:
            direction, arrow = 'Nord', '⬇️'  # N
        elif 22.5 <= deg < 67.5:
            direction, arrow = 'Nord-Est', '↙️'  # NE
        elif 67.5 <= deg < 112.5:
            direction, arrow = 'Est', '⬅️'  # E
        elif 112.5 <= deg < 157.5:
            direction, arrow = 'Sud-Est', '↖️'  # SE
        elif 157.5 <= deg < 202.5:
            direction, arrow = 'Sud', '⬆️'  # S
        elif 202.5 <= deg < 247.5:
            direction, arrow = 'Sud-Ouest', '↗️'  # SO
        elif 247.5 <= deg < 292.5:
            direction, arrow = 'Ouest', '➡️'  # O
        else:
            direction, arrow = 'Nord-Ouest', '↘️'  # NO

        # Création du dictionnaire propre pour Tkinter
        result = {
            "error": False,
            "city_name": data['name'],
            "country": data['sys']['country'],
            "coords_lat": data['coord']['lat'],
            "coords_lon": data['coord']['lon'],
            "temp": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "temp_min": data['main']['temp_min'],
            "temp_max": data['main']['temp_max'],
            "pressure": data['main']['pressure'],
            "humidity": data['main']['humidity'],
            "visibility": data['visibility'],
            "wind_speed": round(data['wind']['speed'] * 3.6, 1),  # km/h
            "wind_direction": direction,
            "wind_icon": arrow,
            "clouds": data['clouds']['all'],

            # Gestion des précipitations (sécurité si pas de pluie)
            "rain_1h": data.get('rain', {}).get('1h', 0),
            "snow_1h": data.get('snow', {}).get('1h', 0),

            # Textes formatés depuis desc.py
            "desc_main": weathermain(data['weather'][0]['main']),
            "desc_detailed": description(data['weather'][0]['description']),
            "weather_icon": weatheremoji(data['weather'][0]['icon']),
            "map_url": f"https://www.openstreetmap.org/#map=13/{data['coord']['lat']}/{data['coord']['lon']}"
        }
        return result

    except Exception as e:
        return {"error": True, "message": f"Erreur technique : {str(e)}"}