from iso_manager import get_iso_code
from weather_engine import get_weather_data

# Simulation de ce que fera l'interface graphique (Tkinter)

print("--- TEST DU MOTEUR METEO ---")
pays_input = "France"  # Simule ce qui est tapé dans la case Pays
ville_input = "Paris"  # Simule ce qui est tapé dans la case Ville

print(f"1. Recherche du code ISO pour : {pays_input}")
iso = get_iso_code(pays_input)

if iso:
    print(f"   -> Code trouvé : {iso}")

    print(f"2. Appel API Météo pour {ville_input}, {iso}...")
    data = get_weather_data(ville_input, iso)

    if data.get("error"):
        print(f"   -> ERREUR : {data['message']}")
    else:
        print("\n--- SUCCÈS ! VOICI LES DONNÉES RECUES (Format Dictionnaire) ---")
        # On affiche le dictionnaire brut pour vérifier
        print(data)

        print("\n--- EXEMPLE D'AFFICHAGE ---")
        print(f"Ville : {data['city_name']} ({data['country']})")
        print(f"Météo : {data['weather_icon']} {data['desc_detailed']}")
        print(f"Température : {data['temp']}°C (Ressenti {data['feels_like']}°C)")
        print(f"Vent : {data['wind_icon']} {data['wind_speed']} km/h ({data['wind_direction']})")
        print(f"Lien carte : {data['map_url']}")

else:
    print("   -> Pays inconnu.")