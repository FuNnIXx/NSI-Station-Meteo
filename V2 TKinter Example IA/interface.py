import tkinter as tk
from tkinter import messagebox
import webbrowser  # Pour ouvrir le lien de la carte
from iso_manager import get_iso_code
from weather_engine import get_weather_data


def ouvrir_carte():
    """Ouvre le lien OpenStreetMap dans le navigateur si disponible"""
    url = current_map_url.get()
    if url:
        webbrowser.open(url)


def lancer_recherche(event=None):
    """Fonction principale déclenchée par le bouton ou la touche Entrée"""
    # 1. Récupération des entrées
    pays_txt = entry_pays.get().strip()
    ville_txt = entry_ville.get().strip()

    if not pays_txt or not ville_txt:
        messagebox.showwarning("Attention", "Veuillez remplir les champs Pays et Ville.")
        return

    # 2. Recherche du code Pays (ISO)
    iso = get_iso_code(pays_txt)
    if not iso:
        messagebox.showerror("Erreur", f"Le pays '{pays_txt}' est introuvable.")
        return

    # 3. Appel au moteur Météo (API)
    # On change le curseur pour montrer que ça charge
    root.config(cursor="watch")
    root.update()

    data = get_weather_data(ville_txt, iso)

    # On remet le curseur normal
    root.config(cursor="")

    # 4. Traitement du résultat
    if data.get("error"):
        messagebox.showerror("Erreur API", data["message"])
        return

    # 5. Affichage des données (Mise à jour des variables Tkinter)
    # Titre Ville / Pays
    var_titre.set(f"{data['city_name']} ({data['country']})")

    # Températures
    var_temp.set(f"{data['temp']}°C")
    var_ressenti.set(f"Ressenti : {data['feels_like']}°C")
    var_min_max.set(f"Min: {data['temp_min']}°C  |  Max: {data['temp_max']}°C")

    # Météo (Icone + Desc)
    var_desc.set(f"{data['weather_icon']} {data['desc_detailed'].capitalize()}")
    var_main_desc.set(data['desc_main'])

    # Vent et conditions
    infos_vent = f"{data['wind_icon']} Vent : {data['wind_speed']} km/h ({data['wind_direction']})"
    infos_supp = f"💧 Humidité : {data['humidity']}%\n☁️ Nuages : {data['clouds']}%"

    # Gestion Pluie/Neige (Afficher seulement si > 0)
    if data['rain_1h'] > 0:
        infos_supp += f"\n☔ Pluie (1h) : {data['rain_1h']} mm"
    if data['snow_1h'] > 0:
        infos_supp += f"\n❄️ Neige (1h) : {data['snow_1h']} mm"

    var_details.set(f"{infos_vent}\n{infos_supp}")

    # Lien Carte
    current_map_url.set(data['map_url'])
    btn_map.pack(pady=5)  # On affiche le bouton carte seulement maintenant

    # On affiche le cadre de résultat s'il était caché
    frame_resultats.pack(fill="both", expand=True, padx=10, pady=10)


# --- CRÉATION DE LA FENÊTRE ---
root = tk.Tk()
root.title("Weather's Call")
root.geometry("400x550")
root.resizable(False, False)

# Couleurs et Fonts
BG_COLOR = "#f0f0f0"
root.config(bg=BG_COLOR)
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_TEMP = ("Helvetica", 28, "bold")
FONT_NORMAL = ("Helvetica", 11)

# Variable globale pour stocker l'URL de la carte
current_map_url = tk.StringVar()

# --- HEADER (TITRE) ---
lbl_main_title = tk.Label(root, text="☁️ Weather's Call ☀️", font=("Verdana", 20, "bold"), bg=BG_COLOR, fg="#333")
lbl_main_title.pack(pady=15)

# --- ZONE DE RECHERCHE (FRAME) ---
frame_input = tk.Frame(root, bg=BG_COLOR)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Pays :", bg=BG_COLOR).grid(row=0, column=0, padx=5, sticky="e")
entry_pays = tk.Entry(frame_input, width=20)
entry_pays.grid(row=0, column=1, padx=5)
entry_pays.insert(0, "France")  # Valeur par défaut

tk.Label(frame_input, text="Ville :", bg=BG_COLOR).grid(row=1, column=0, padx=5, sticky="e")
entry_ville = tk.Entry(frame_input, width=20)
entry_ville.grid(row=1, column=1, padx=5)

# Bouton Rechercher
btn_search = tk.Button(root, text="🔍 Rechercher", command=lancer_recherche, bg="#007bff", fg="white",
                       font=("Arial", 10, "bold"))
btn_search.pack(pady=10)

# Lier la touche "Entrée" à la recherche
root.bind('<Return>', lancer_recherche)

# --- ZONE RÉSULTATS (FRAME) ---
# On crée un cadre avec une bordure pour faire joli
frame_resultats = tk.Frame(root, bg="white", bd=2, relief="groove")
# Note : on ne le .pack() pas tout de suite, on attend la première recherche

# Variables Tkinter pour mise à jour dynamique
var_titre = tk.StringVar()
var_temp = tk.StringVar()
var_ressenti = tk.StringVar()
var_min_max = tk.StringVar()
var_desc = tk.StringVar()
var_main_desc = tk.StringVar()
var_details = tk.StringVar()

# Widgets d'affichage
lbl_ville = tk.Label(frame_resultats, textvariable=var_titre, font=FONT_TITLE, bg="white", fg="#007bff")
lbl_ville.pack(pady=(10, 5))

lbl_desc = tk.Label(frame_resultats, textvariable=var_desc, font=("Arial", 14), bg="white")
lbl_desc.pack()

lbl_temp = tk.Label(frame_resultats, textvariable=var_temp, font=FONT_TEMP, bg="white", fg="#333")
lbl_temp.pack(pady=5)

lbl_ressenti = tk.Label(frame_resultats, textvariable=var_ressenti, font=("Arial", 10, "italic"), bg="white", fg="gray")
lbl_ressenti.pack()

lbl_min_max = tk.Label(frame_resultats, textvariable=var_min_max, font=("Arial", 9), bg="white", fg="gray")
lbl_min_max.pack(pady=(0, 10))

# Séparateur
tk.Frame(frame_resultats, height=2, bd=1, relief="sunken").pack(fill="x", padx=20, pady=5)

lbl_details = tk.Label(frame_resultats, textvariable=var_details, font=FONT_NORMAL, bg="white", justify="left")
lbl_details.pack(pady=10)

# Bouton Carte (caché au début)
btn_map = tk.Button(frame_resultats, text="🗺️ Voir sur la carte", command=ouvrir_carte, bg="#28a745", fg="white")
# Sera affiché dans la fonction

# --- BOUCLE PRINCIPALE ---
root.mainloop()