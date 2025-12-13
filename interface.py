from difflib import get_close_matches #      pip install cdifflib
from PIL.ImageOps import expand
from customtkinter import *  #     pip install customtkinter
from tkinter import messagebox
from CTkListbox import * #     pip install CTkListbox
'''import messagebox #     pip install messagebox'''
import webbrowser
from PIL import Image #     pip install Pillow
import datetime

from dict import *
import requests #     pip install requests

'''VARIABLES DE DEFINITIONS'''

color_bg = '#292933'
color_frame = '#202029'

data = False

city_checked = True
ctr_checked = True
city_name = False
ctr_name = False
ctr_iso = False

temp_unit = '°C' # defaut = °C a modif vers °F
speed_unit = 'km/h' # defaut = km/h modif vers mph
vis_unit = 'm' # defaut = m modif vers miles

condition_desc_code = 'N/A'
condition_img = '01n'
temp = '---'
temp_min = '---'
temp_max = '---'
fells_like = '---'
pressure = '---'
wind = '---'
wind_deg = '---'
visibility = '---'
cloud = '---'
humidity = '---'
lon = '---'
lat = '---'
rain = 'NO DATA'
snow = 'NO DATA'
sunrise = 0000
sunset = 0000

'''FONCTIONS'''

# OpenSteetMap Button

def open_map():
    if not city_name or not ctr_name or not data:
        messagebox.showerror('Error', "Effectuez une recherche avant d'ouvrir la carte")
        return()
    openstreetmap = 'https://www.openstreetmap.org/#map=13/###/+++'
    openstreetmap = openstreetmap.replace('###', f'{lat}')
    openstreetmap = openstreetmap.replace('+++', f'{lon}')
    if openstreetmap:
        webbrowser.open(openstreetmap)
    return None


def toggle_metric_imperial():
    global temp_unit, speed_unit, vis_unit
    if temp_unit == '°C':
        temp_unit = '°F'
        m_i_switch.configure(text=f'Actuel : IMP : METRIC / IMPERIAL')

    else:
        temp_unit = '°C'
        m_i_switch.configure(text=f'Actuel : MET : METRIC / IMPERIAL')

    if speed_unit == 'km/h':
        speed_unit = 'mph'

    else:
        speed_unit = 'km/h'

    return None



def get_clouds_img():
    global cloud
    if cloud == 0 or cloud == '---':
        return '0'
    elif 25 >= cloud > 0:
        return '25'
    elif 50 >= cloud > 25:
        return '50'
    elif 75 >= cloud > 50:
        return '75'
    else:
        return '100'

def get_wind_img():
    global wind_deg
    if wind_deg == '---':
        # return '0'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/0.png'), dark_image=Image.open(f'img/icons_wind/0.png'))
    elif wind_deg >= 337 or wind_deg < 22:
        # return 'n'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/n.png'), dark_image=Image.open(f'img/icons_wind/n.png'))
    elif 22 <= wind_deg < 67:
        # return 'ne'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/ne.png'), dark_image=Image.open(f'img/icons_wind/ne.png'))
    elif 67 <= wind_deg < 112:
        # return "e"
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/e.png'), dark_image=Image.open(f'img/icons_wind/e.png'))
    elif 112 <= wind_deg < 157:
        # return 'se'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/se.png'), dark_image=Image.open(f'img/icons_wind/se.png'))
    elif 157 <= wind_deg < 202:
        # return 's'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/s.png'), dark_image=Image.open(f'img/icons_wind/s.png'))
    elif 202 <= wind_deg < 247:
        # return 'sw'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/sw.png'), dark_image=Image.open(f'img/icons_wind/sw.png'))
    elif 247 <= wind_deg < 292:
        # return "w"
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/w.png'), dark_image=Image.open(f'img/icons_wind/w.png'))
    else:
        # return 'nw'
        wind_display_img.configure(light_image=Image.open(f'img/icons_wind/nw.png'), dark_image=Image.open(f'img/icons_wind/nw.png'))

def get_visibility_img():
    global visibility
    if visibility == '---':
        return '00'
    elif visibility == 0:
        return '0'
    elif 250 >= visibility > 0:
        return '250'
    elif 500 >= visibility > 250:
        return '500'
    elif 750 >= visibility > 500:
        return '750'
    elif 1000 >= visibility > 750:
        return '1000'
    elif 1500 >= visibility > 1000:
        return '1500'
    elif 3000 >= visibility > 1500:
        return '3000'
    elif 6000 >= visibility > 3000:
        return '6000'
    elif 10000 >= visibility > 6000:
        return '10000'
    return None


def get_humidity_img():
    global humidity
    if humidity == '---':
        return '00'
    elif humidity == 0:
        return '0'
    elif 25 >= humidity > 0:
        return '25'
    elif 50 >= humidity > 25:
        return '50'
    elif 75 >= humidity > 50:
        return '75'
    else:
        return '100'

def ctr_city_check():
    global ctr_name, city_name, city_checked, ctr_checked

    if not city_name or not ctr_name or city_name == '' or ctr_name == '' :
        messagebox.showerror('Error', 'Veuillez sélectionner une ville et un pays dans les listes avant de lancer la recherche')
        return(False)

    return(True)

def call_api():
    global city_name, ctr_name, data, condition_desc_code, condition_img, temp, temp_min, temp_max, fells_like, pressure, wind, visibility, cloud, humidity, lon, lat, wind_deg, snow, rain, sunrise, sunset

    if not ctr_city_check():
        return

    if not ctr_name:
        return()

    if not city_name:
        return()

    url = 'https://api.openweathermap.org/data/2.5/weather?q=###,++&appid=7585221fbcead099c4e4c4bb6fd3b68f&units=metric'
    url = url.replace('###', city_name)
    url = url.replace('++', ctr_iso)

    if temp_unit == '°F':
        url = url.replace('metric', 'imperial')

    response =  requests.get(url)
    response = response.json()

    if response['cod'] == '404':
        messagebox.showerror('Error', 'Ville introuvable')
        return()
    else:
        data = response
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        condition_desc_code = data['weather'][0]['id']
        condition_img = data['weather'][0]['icon']
        temp = round(data['main']['temp'])
        fells_like = round(data['main']['feels_like'])
        temp_min = round(data['main']['temp_min']) 
        temp_max = round(data['main']['temp_max'])
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        visibility = data['visibility']
        wind = round(data['wind']['speed'])
        if temp_unit == '°F':
            wind = round(data['wind']['speed'])
        elif temp_unit == '°C':
            wind = round(data['wind']['speed'] * 3.6)
        wind_deg = data['wind']['deg']
        cloud = data['clouds']['all']
        if 'rain' in data:
            rain = f'{data['rain']['1h']}mm'
        else:
            rain = 'Pas de pluie cette heure-ci'
        if 'snow' in data:
            snow = f'{data['snow']['1h']}mm'
        else:
            snow = 'Pas de neige cette heure-ci'
        sunrise = data['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M')
        sunset = data['sys']['sunset']
        sunset = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M')

        refresh_ui()

        # print(data)
        return None

def refresh_ui():
    global city_name, ctr_name, data, condition_desc_code, condition_img, temp, temp_min, temp_max, fells_like, pressure, wind, visibility, cloud, humidity, lon, lat, wind_deg, snow, rain, sunrise, sunset

    header.configure(text=f'Données météo à {city_name} ')
    conditions_display_img.configure(light_image=Image.open(f'img/icons/{condition_img}@2x.png'), dark_image=Image.open(f'img/icons/{condition_img}@2x.png'))
    conditions_display.configure(text=f'\n\n\n\n\n\n{description()[data['weather'][0]['description']]}')
    temp_display.configure(text=temp)
    temp_unit_label.configure(text=temp_unit)
    temp_other_displayed.configure(text=f'MIN : {temp_min}{temp_unit} \nMAX : {temp_max}{temp_unit} \nRessenti : {fells_like}{temp_unit}')
    pessure_display.configure(text=pressure)
    get_wind_img()
    wind_value.configure(text=wind)
    wind_unit_label.configure(text=speed_unit)
    visibility_display_img.configure(light_image=Image.open(f'img/icons_vis/{get_visibility_img()}.png'), dark_image=Image.open(f'img/icons_vis/{get_visibility_img()}.png'))
    vis_value.configure(text=visibility)
    cloud_display_img.configure(light_image=Image.open(f'img/icons_clouds/{get_clouds_img()}.png'), dark_image=Image.open(f'img/icons_clouds/{get_clouds_img()}.png'))
    cloud_value.configure(text=cloud)
    humidity_display_img.configure(light_image=Image.open(f'img/icons_hum/{get_humidity_img()}.png'), dark_image=Image.open(f'img/icons_hum/{get_humidity_img()}.png'))
    humidity_value.configure(text=humidity)
    date.configure(text=f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}     Sunrise / Sunset : {sunrise} / {sunset}')
    temp_unit_label.configure(text=temp_unit)
    wind_unit_label.configure(text=speed_unit)
    temp_other_displayed.configure(text=f'MIN : {temp_min}{temp_unit} \nMAX : {temp_max}{temp_unit} \nRessenti : {fells_like}{temp_unit}')
    space_rain_snow.configure(text=f'Précipitations (mm) : {rain}   /   Neige (mm) : {snow}')

def city_search_get():
    global city_name, ctr_name
    if not ctr_name:
        messagebox.showerror('Error', 'Sélectionnez un pays avant de chercher une ville')
        return
    city_list.delete(0, END) # Clear previous results
    search_term = city_entry.get()
    if search_term:
        url = "https://countriesnow.space/api/v0.1/countries/cities"
        payload = payload = {"country" : f"{ctr_name}"}
        response = requests.post(url, json=payload)
        cities = response.json()
        cities = cities['data']
        matches = get_close_matches(search_term, cities, n=15, cutoff=0.5)
        for match in matches:
            city_list.insert(END, match)
    else:
        city_list.delete(0, END)

def city_listbox_select(selected_item):
    global city_name, city_checked

    city_name = selected_item
    city_checked = True

def ctr_search_get():
    ctr_list.delete(0, END) # Clear previous results
    search_term = ctr_entry.get()
    if search_term:
        country_names = ctr_to_iso()
        country_names = country_names.keys()
        matches = get_close_matches(search_term, country_names, n=15, cutoff=0.1)
        for match in matches:
            # Capitalize the first letter of each word for display
            ctr_list.insert(END, match.title())

    else:
        ctr_list.delete(0, END)

def ctr_listbox_select(selected_item):
    global ctr_name, ctr_checked, ctr_iso

    ctr_name = selected_item
    ctr_checked = True
    ctr_iso = ctr_to_iso()[ctr_name]
    # print(ctr_iso)

'''INTERFACE UI'''

# ROOT

root = CTk()

root.title("WeatherDATA")
root.geometry("1100x700")
root.resizable(False, False)
root.config(bg=color_bg)
root.iconbitmap('logo.ico')

# FRAMING

frame = CTkFrame(root, fg_color=color_bg, corner_radius=0)
frame.pack(side=TOP, fill=BOTH, expand=True, pady=7.5, padx=7.5)

menu = CTkFrame(frame, fg_color=color_frame, width=300, corner_radius=10)
menu.pack(side=LEFT, fill=BOTH, pady=7.5, padx=7.5)

right_side = CTkFrame(frame, fg_color=color_bg, corner_radius=0)
right_side.pack(side=RIGHT, fill=BOTH, expand=True, pady=7.5, padx=7.5)

title_frame = CTkFrame(right_side, fg_color=color_frame, height=70, corner_radius=10) # TOP FRAME CITY TITLE + OPENSTREETMAP BUTTON
title_frame.pack(side=TOP, fill=BOTH)

space1 = CTkFrame(right_side, fg_color=color_bg, corner_radius=0, height=15) # A DEFAUT DE PADY, UNE FRAME TRANSPARENTE
space1.pack(side=TOP, fill=BOTH)

general_info = CTkFrame(right_side, fg_color=color_frame, corner_radius=10, height=180) # MID FRAME INFO MERE
general_info.pack(side=TOP, fill=BOTH)

'''# Space RAIN / SNOW INFO'''

space_rain_snow = CTkLabel(right_side, fg_color=color_frame, corner_radius=10, text_color='white', text=f'Précipitations (mm) : {rain}   /   Neige (mm) : {snow}', font=('Monserrat', 15, 'bold'), anchor=W)
space_rain_snow.pack(expand=YES, fill=BOTH, pady=10, padx=0)

'''# Space RAIN / SNOW INFO'''

precisions_info = CTkFrame(right_side, fg_color=color_frame, corner_radius=10)
precisions_info.pack(side=TOP, fill=BOTH, expand=YES)

# Cadres titres verticaux General et Precision

title_info_1_frame = CTkFrame(general_info, fg_color='white', corner_radius=100, width=25) # Cadre titre general
title_info_1_frame.pack(side=LEFT, fill=BOTH, pady=10, padx=12)
title_info_1_frame.pack_propagate(False)

title_info_2_frame = CTkFrame(precisions_info, fg_color='white', corner_radius=100, width=25) # Cadre titre precisions
title_info_2_frame.pack(side=LEFT, fill=BOTH, pady=10, padx=12)
title_info_2_frame.pack_propagate(False)

# TITLE FRAME

header = CTkLabel(title_frame, text=f'Données météo à {city_name} ', font=('Monserrat', 30, 'bold'), text_color='white', bg_color='transparent')
header.pack(pady=10, padx=15, side=LEFT)

validate_button = CTkButton(title_frame, text='RECHERCHER', font=('Monserrat', 15, 'bold'), text_color='#59608C', corner_radius=10, fg_color='white', hover_color='#B6B6B6', width=50, command=call_api)
validate_button.pack(pady=10, padx=5, side=RIGHT)

# MERNU FRAME

app_title = CTkLabel(menu, text='WeatherDATA', font=('Monserrat', 30, 'bold'), width=300, text_color='white')
app_title.pack(pady=30, padx=0, side=TOP, fill=BOTH)

# RECHERCHE DU PAYS

ctr_search_frame = CTkFrame(menu, fg_color=color_frame)
ctr_search_frame.pack(side=TOP, fill=BOTH, pady=7.5, padx=15)

ctr_entry = CTkEntry(ctr_search_frame, placeholder_text='Pays ...', corner_radius=10, width=175, height=35, fg_color='white', text_color='#59608C')
ctr_entry.pack(fill=BOTH, pady=0, padx=0, side=LEFT)

ctr_button = CTkButton(ctr_search_frame, text='VALIDER', corner_radius=10, font=('Monserrat', 15, 'bold'), hover_color='#B6B6B6', text_color='#59608C', fg_color='white', width=80, command=ctr_search_get) # BOUTON VALIDER PAYS
ctr_button.pack(fill=BOTH, pady=0, padx=0, side=RIGHT)

ctr_list = CTkListbox(menu, width=2, text_color='white', command=ctr_listbox_select)
ctr_list.pack(side=TOP, fill=BOTH, expand=YES,pady=7.5, padx=15)

# RECHERCHE DE LA VILLE

city_search_frame = CTkFrame(menu, fg_color=color_frame)
city_search_frame.pack(side=TOP, fill=BOTH, pady=7.5, padx=15)

city_entry = CTkEntry(city_search_frame, placeholder_text='Ville ...', corner_radius=10, width=175, height=35, fg_color='white', text_color='#59608C')
city_entry.pack(fill=BOTH, pady=0, padx=0, side=LEFT)

city_button = CTkButton(city_search_frame, text='VALIDER', corner_radius=10, font=('Monserrat', 15, 'bold'), hover_color='#B6B6B6', text_color='#59608C', fg_color='white', width=80, command=city_search_get) # BOUTON VALIDER CITY
city_button.pack(fill=BOTH, pady=0, padx=0, side=RIGHT)

city_list = CTkListbox(menu, width=2, command=city_listbox_select, text_color='white')
city_list.pack(side=TOP, fill=BOTH, expand=YES,pady=7.5, padx=15)

space3 = CTkFrame(menu, fg_color=color_frame, corner_radius=0, height=7.5)
space3.pack()

# GENERAL INFO FRAME

general_info.pack_propagate(False)

# TEMP

frame_general_1 = CTkFrame(general_info, fg_color=color_frame, corner_radius=10)
frame_general_1.pack(side=LEFT, fill=BOTH, pady=5, padx=5, expand=YES)

frame_temp = CTkFrame(frame_general_1, fg_color=color_frame, corner_radius=10)
frame_temp.pack(fill=BOTH, pady=20, padx=20)

temp_display = CTkLabel(frame_temp, text=temp, font=("Monserrat", 50, "bold"), anchor='center', text_color='white')
temp_display.pack(side=LEFT, fill=BOTH, padx=(50, 0), pady=(15, 0))

temp_unit_label = CTkLabel(frame_temp, text=temp_unit, font=("Monserrat", 15, "bold"), text_color='white', anchor=SW)
temp_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

temp_other_displayed = CTkLabel(frame_general_1, text=f'MIN : {temp_min}{temp_unit} \nMAX : {temp_max}{temp_unit} \nRessenti : {fells_like}{temp_unit}', font=("Monserrat", 15), text_color='grey', compound=RIGHT, anchor='n')
temp_other_displayed.pack(fill=BOTH, expand=Y)

# PRESSURE

frame_general_2 = CTkFrame(general_info, fg_color=color_frame, corner_radius=10)
frame_general_2.pack(side=LEFT, fill=BOTH, pady=5, padx=5, expand=YES)

pessure_display = CTkLabel(frame_general_2, text=pressure, font=("Monserrat", 50, "bold"), anchor='center', text_color='white')
pessure_display.pack(side=LEFT, fill=BOTH, padx=(50, 0))

pressure_unit_label = CTkLabel(frame_general_2, text='hpa', font=("Monserrat", 15, "bold"), text_color='white', anchor=SW)
pressure_unit_label.pack(side=LEFT, fill=BOTH, expand=YES, pady=(0, 80))

# CONDITIONS

frame_general_3 = CTkFrame(general_info, fg_color=color_frame, corner_radius=10)
frame_general_3.pack(side=LEFT, fill=BOTH, pady=5, padx=(0, 5), expand=YES)

conditions_display_img = CTkImage(light_image=Image.open(f'img/icons/{condition_img}@2x.png'), dark_image=Image.open(f'img/icons/{condition_img}@2x.png'), size=(190, 190))
conditions_display = CTkLabel(frame_general_3, image=conditions_display_img, text=f'\n\n\n\n\n\n{condition_desc_code}', font=("Monserrat", 20), text_color='grey', anchor='n')
conditions_display.pack(fill=BOTH, padx=(0, 0))


# GENERAL FRAME NAME

canvas_title_general = CTkCanvas(title_info_1_frame, highlightthickness=0)
canvas_title_general.pack(pady=10, padx=1, expand=YES)
canvas_title_general.create_text(12, 90, text="GENERAL", font=("Monserrat", 15, "bold"), fill="#000000", angle=90)

# PRECISION INFO FRAME

# FRAMING

wind_frame = CTkFrame(precisions_info, fg_color=color_frame)
wind_frame.pack(side=LEFT, fill=BOTH, pady=0, padx=5)

visibility_frame = CTkFrame(precisions_info, fg_color=color_frame)
visibility_frame.pack(side=LEFT, fill=BOTH, pady=0, padx=5)

cloud_frame = CTkFrame(precisions_info, fg_color=color_frame)
cloud_frame.pack(side=LEFT, fill=BOTH, pady=0, padx=5)

humidity_frame = CTkFrame(precisions_info, fg_color=color_frame)
humidity_frame.pack(side=LEFT, fill=BOTH, pady=0, padx=5)

# WIND

wind_display_img = CTkImage(light_image=Image.open(f'img/icons_wind/0.png'), dark_image=Image.open(f'img/icons_wind/0.png'), size=(165, 165))
wind_display = CTkLabel(wind_frame, image=wind_display_img, text='')
wind_display.pack(fill=BOTH, pady=(20, 0))

text_wind_frame = CTkFrame(wind_frame, fg_color=color_frame)
text_wind_frame.pack(fill=BOTH, pady=5, padx=5)

wind_value = CTkLabel(text_wind_frame, text=wind, font=("Monserrat", 58, 'bold'), text_color='white')
wind_value.pack(side=LEFT, fill=BOTH, padx=(35, 0))

wind_unit_label = CTkLabel(text_wind_frame, text=speed_unit, font=("Monserrat", 20, 'bold'), anchor=SW, text_color='white')
wind_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

wind_text_desc = CTkLabel(wind_frame, text='VENT', text_color='grey', font=("Monserrat", 20))
wind_text_desc.pack()

# VISIBILITY

visibility_display_img = CTkImage(light_image=Image.open(f'img/icons_vis/00.png'), dark_image=Image.open(f'img/icons_vis/00.png'), size=(165, 165))
visibility_display = CTkLabel(visibility_frame, image=visibility_display_img, text='')
visibility_display.pack(fill=BOTH, pady=(20, 0))

text_vis_frame = CTkFrame(visibility_frame, fg_color=color_frame)
text_vis_frame.pack(fill=BOTH, pady=10, padx=5)

vis_grid = CTkFrame(text_vis_frame, fg_color=color_frame)
vis_grid.pack()

vis_value = CTkLabel(vis_grid, text=visibility, font=("Monserrat", 50, 'bold'), text_color='white')
vis_value.grid(row=0, column=0, sticky='e')

vis_unit_label = CTkLabel(vis_grid, text=vis_unit, font=("Monserrat", 20, 'bold'), anchor=SW, text_color='white')
vis_unit_label.grid(row=0, column=1, sticky='w')

vis_text_desc = CTkLabel(visibility_frame, text='VISIBILITE', text_color='grey', font=("Monserrat", 20))
vis_text_desc.pack()

# CLOUDS

cloud_display_img = CTkImage(light_image=Image.open(f'img/icons_clouds/0.png'), dark_image=Image.open(f'img/icons_clouds/0.png'), size=(165, 165))
cloud_display = CTkLabel(cloud_frame, image=cloud_display_img, text='')
cloud_display.pack(fill=BOTH, pady=(20, 0))

text_cloud_frame = CTkFrame(cloud_frame, fg_color=color_frame)
text_cloud_frame.pack(fill=BOTH, pady=5, padx=5)

cloud_value = CTkLabel(text_cloud_frame, text=cloud, font=("Monserrat", 58, 'bold'), text_color='white')
cloud_value.pack(side=LEFT, fill=BOTH, padx=(35, 0))

cloud_unit_label = CTkLabel(text_cloud_frame, text='%', font=("Monserrat", 20, 'bold'), anchor=SW, text_color='white')
cloud_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

cloud_text_desc = CTkLabel(cloud_frame, text='COUVERTURE', text_color='grey', font=("Monserrat", 20))
cloud_text_desc.pack()

# HUMIDITY

humidity_display_img = CTkImage(light_image=Image.open(f'img/icons_hum/00.png'), dark_image=Image.open(f'img/icons_hum/00.png'), size=(165, 165))
humidity_display = CTkLabel(humidity_frame, image=humidity_display_img, text='')
humidity_display.pack(fill=BOTH, pady=(20, 0))

text_humidity_frame = CTkFrame(humidity_frame, fg_color=color_frame)
text_humidity_frame.pack(fill=BOTH, pady=5, padx=5)

humidity_value = CTkLabel(text_humidity_frame, text=humidity, font=("Monserrat", 58, 'bold'), text_color='white')
humidity_value.pack(side=LEFT, fill=BOTH, padx=(35, 0))

humidity_unit_label = CTkLabel(text_humidity_frame, text='%', font=("Monserrat", 20, 'bold'), anchor=SW, text_color='white')
humidity_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

humidity_text_desc = CTkLabel(humidity_frame, text='HUMIDITE', text_color='grey', font=("Monserrat", 20))
humidity_text_desc.pack()

# PRECISION FRAME NAME

canvas_title_precision = CTkCanvas(title_info_2_frame, highlightthickness=0)
canvas_title_precision.pack(pady=10, padx=1, expand=YES)
canvas_title_precision.create_text(12, 133, text="PRECISIONS", font=("Monserrat", 15, "bold"), fill="#000000", angle=90)

# METRIC TO IMPERIAL / DATE

date = CTkLabel(right_side, text=f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}     Sunrise / Sunset : {sunrise} / {sunset} (UTC+1)', font=('Monserrat', 12), text_color='white')
date.pack(side=LEFT)

openstreetmap_button = CTkButton(right_side, text='OpenStreetMap', font=('Monserrat', 15, 'bold'), text_color='#59608C', corner_radius=10, fg_color='white', hover_color='#B6B6B6', command=open_map, width=50)
openstreetmap_button.pack(pady=10, padx=5, side=RIGHT)

m_i_switch = CTkSwitch(right_side, text=f'Actuel : MET : METRIC / IMPERIAL', font=('Monserrat', 12, 'bold'), text_color='white', command=toggle_metric_imperial)
m_i_switch.pack(side=RIGHT)

root.mainloop()