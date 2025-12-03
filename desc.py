def description(key):
    weather_description_fr = {
        # Group 2xx: Thunderstorm (Orage)
        "thunderstorm with light rain": "orage avec pluie faible",
        "thunderstorm with rain": "orage avec pluie",
        "thunderstorm with heavy rain": "orage avec fortes pluies",
        "light thunderstorm": "orage léger",
        "thunderstorm": "orage",
        "heavy thunderstorm": "violent orage",
        "ragged thunderstorm": "orage déchiqueté",
        "thunderstorm with light drizzle": "orage avec bruine légère",
        "thunderstorm with drizzle": "orage avec bruine",
        "thunderstorm with heavy drizzle": "orage avec forte bruine",

        # Group 3xx: Drizzle (Bruine)
        "light intensity drizzle": "bruine légère",
        "drizzle": "bruine",
        "heavy intensity drizzle": "forte bruine",
        "light intensity drizzle rain": "bruine et pluie légère",
        "drizzle rain": "bruine et pluie",
        "heavy intensity drizzle rain": "forte bruine et pluie",
        "shower rain and drizzle": "averse de pluie et bruine",
        "heavy shower rain and drizzle": "forte averse de pluie et bruine",
        "shower drizzle": "averse de bruine",

        # Group 5xx: Rain (Pluie)
        "light rain": "pluie faible",
        "moderate rain": "pluie modérée",
        "heavy intensity rain": "forte pluie",
        "very heavy rain": "très forte pluie",
        "extreme rain": "pluie extrême",
        "freezing rain": "pluie verglaçante",
        "light intensity shower rain": "averse de pluie faible",
        "shower rain": "averse de pluie",
        "heavy intensity shower rain": "forte averse de pluie",
        "ragged shower rain": "averse de pluie irrégulière",

        # Group 6xx: Snow (Neige)
        "light snow": "neige faible",
        "snow": "neige",
        "heavy snow": "forte neige",
        "sleet": "grésil",
        "light shower sleet": "averse de grésil faible",
        "shower sleet": "averse de grésil",
        "light rain and snow": "pluie et neige mêlées faibles",
        "rain and snow": "pluie et neige mêlées",
        "light shower snow": "averse de neige faible",
        "shower snow": "averse de neige",
        "heavy shower snow": "forte averse de neige",

        # Group 7xx: Atmosphere (Conditions atmosphériques)
        "mist": "brume",
        "smoke": "fumée",
        "haze": "brume sèche",
        "sand/dust whirls": "tourbillons de sable/poussière",
        "fog": "brouillard",
        "sand": "sable",
        "dust": "poussière",
        "volcanic ash": "cendres volcaniques",
        "squalls": "grains",
        "tornado": "tornade",

        # Group 800: Clear (Ciel clair)
        "clear sky": "ciel dégagé",

        # Group 80x: Clouds (Nuages)
        "few clouds": "quelques nuages",  # 11-25%
        "scattered clouds": "nuages épars",  # 25-50%
        "broken clouds": "nuages fragmentés",  # 51-84%
        "overcast clouds": "ciel couvert"  # 85-100%
    }
    return(weather_description_fr[key])

def weathermain(key):
    weather_main_fr = {
        "Thunderstorm": "Il y a de l'Orage",
        "Drizzle": "Il Bruine",
        "Rain": "Il pleue",
        "Snow": "Il Neige",
        "Mist": "Il y a de la Brume",
        "Smoke": "Il y a de la Fumée",
        "Haze": "Il y a de la Brume sèche",
        "Dust": "Il y a de la Poussière",
        "Fog": "Il y a du Brouillard",
        "Sand": "Il y a du Sable",
        "Ash": "Il y a des Cendres volcaniques",
        "Squall": "Il y a des Rafales",
        "Tornado": "Il y a une Tornade",
        "Clear": "Il y a un Ciel dégagé",
        "Clouds": "Il y a des Nuages"
    }
    return(weather_main_fr[key])

def weatheremoji(key):
    weather_emojis = {
        # Ciel clair
        "01d": "☀️",  # Soleil
        "01n": "🌙",  # Lune

        # Quelques nuages
        "02d": "b",  # Soleil caché
        "02n": "☁️",  # Nuage (la nuit)

        # Nuages épars / fragmentés
        "03d": "☁️",
        "03n": "☁️",
        "04d": "☁️",  # Souvent plus sombre
        "04n": "☁️",

        # Pluie (Averses)
        "09d": "🌧️",
        "09n": "🌧️",

        # Pluie (Soleil + Pluie vs Pluie nuit)
        "10d": "🌦️",
        "10n": "🌧️",

        # Orage
        "11d": "⛈️",
        "11n": "⛈️",

        # Neige
        "13d": "❄️",
        "13n": "❄️",

        # Brume / Brouillard
        "50d": "🌫️",
        "50n": "🌫️"
    }
    return(weather_emojis[key])