from PIL.ImageOps import expand
from customtkinter import *  #     pip install customtkinter
from CTkListbox import * #     pip install CTkListbox
import messagebox
import webbrowser
from PIL import Image
import datetime
from dict import *
import requests

'''VARIABLES DE DEFINITIONS'''

color_bg = '#292933'
color_frame = '#202029'

data = False

city_name = False
ctr_name = False

temp_unit = '°C' #defaut = °C a modif vers °F
speed_unit = 'km/h' #defaut = km/h modif vers mph

condition_desc_code = 'N/A'
condition_img = '01n'
temp = '---'
temp_min = '---'
temp_max = '---'
fells_like = '---'
pressure = '---'
wind = '---'
visibility = '---'
cloud = '---'
humidity = '---'
lon = '---'
lat = '---'


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
    global temp_unit, speed_unit
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
    global cloud
    if wind == '---':
        return '0'
    elif wind  >= 337.5 or wind < 22.5:
        return 'n'
    elif 22.5 <= wind < 67.5:
        return 'ne'
    elif 67.5 <= wind < 112.5:
        return "e"
    elif 112.5 <= wind < 157.5:
        return 'se'
    elif 157.5 <= wind < 202.5:
        return 's'
    elif 202.5 <= wind < 247.5:
        return 'sw'
    elif 247.5 <= wind < 292.5:
        return "w"
    else:
        return 'nw'

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

def get_weather_data():
    global city_name, ctr_name, data, condition_desc_code, condition_img, temp, temp_min, temp_max, fells_like, pressure, wind, visibility, cloud, humidity, lon, lat

    if not ctr_name:
        messagebox.showerror('Error', 'Veuillez selectionner un pays')
        return()

    if not city_name:
        messagebox.showerror('Error', 'Veuillez selectionner une ville')
        return()

    url = 'https://api.openweathermap.org/data/2.5/weather?q=###,++&appid=7585221fbcead099c4e4c4bb6fd3b68f&units=metric'
    url = url.replace('###', city_name)
    url = url.replace('++', ctr_name)

    response =  requests.get(url)
    response = response.json()

    if response['cod'] == '404':
        messagebox.showerror('Error', 'Ville introuvable')
        return()
    else:
        data = response
        condition_desc_code = description()[data['weather'][0]['description']]
        condition_img = data['weather'][0]['icon']
        temp = round(data['main']['temp'])
        temp_min = 0
        return None


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

space2 = CTkFrame(right_side, fg_color=color_bg, corner_radius=0, height=15) # A DEFAUT DE PADY, UNE FRAME TRANSPARENTE
space2.pack(side=TOP, fill=BOTH)

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

openstreetmap_button = CTkButton(title_frame, text='OpenStreetMap', font=('Monserrat', 15), text_color='#59608C', corner_radius=10, fg_color='white', hover_color='#B6B6B6', command=open_map, width=50)
openstreetmap_button.pack(pady=10, padx=5, side=RIGHT)

validate_button = CTkButton(title_frame, text='RECHERCHER', font=('Monserrat', 15, 'bold'), text_color='#59608C', corner_radius=10, fg_color='white', hover_color='#B6B6B6', width=50)
validate_button.pack(pady=10, padx=5, side=RIGHT)

# MERNU FRAME

app_title = CTkLabel(menu, text='WeatherDATA', font=('Monserrat', 30, 'bold'), width=300, text_color='white')
app_title.pack(pady=30, padx=0, side=TOP, fill=BOTH)

# RECHERCHE DU PAYS

ctr_search_frame = CTkFrame(menu, fg_color=color_frame)
ctr_search_frame.pack(side=TOP, fill=BOTH, pady=7.5, padx=15)

ctr_entry = CTkEntry(ctr_search_frame, placeholder_text='Pays ...', corner_radius=10, width=175, height=35, fg_color='white', text_color='#59608C')
ctr_entry.pack(fill=BOTH, pady=0, padx=0, side=LEFT)

ctr_button = CTkButton(ctr_search_frame, text='VALIDER', corner_radius=10, font=('Monserrat', 15, 'bold'), hover_color='#B6B6B6', text_color='#59608C', fg_color='white', width=80) # BOUTON VALIDER PAYS
ctr_button.pack(fill=BOTH, pady=0, padx=0, side=RIGHT)

ctr_list = CTkListbox(menu, width=2)
ctr_list.pack(side=TOP, fill=BOTH, expand=YES,pady=7.5, padx=15)

# RECHERCHE DE LA VILLE

city_search_frame = CTkFrame(menu, fg_color=color_frame)
city_search_frame.pack(side=TOP, fill=BOTH, pady=7.5, padx=15)

city_entry = CTkEntry(city_search_frame, placeholder_text='Ville ...', corner_radius=10, width=175, height=35, fg_color='white', text_color='#59608C')
city_entry.pack(fill=BOTH, pady=0, padx=0, side=LEFT)

city_button = CTkButton(city_search_frame, text='VALIDER', corner_radius=10, font=('Monserrat', 15, 'bold'), hover_color='#B6B6B6', text_color='#59608C', fg_color='white', width=80) # BOUTON VALIDER PAYS
city_button.pack(fill=BOTH, pady=0, padx=0, side=RIGHT)

city_list = CTkListbox(menu, width=2)
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

temp_display = CTkLabel(frame_temp, text=temp, font=("Monserrat", 50, "bold"), anchor='center')
temp_display.pack(side=LEFT, fill=BOTH, padx=(50, 0), pady=(15, 0))

temp_unit_label = CTkLabel(frame_temp, text=temp_unit, font=("Monserrat", 15, "bold"), text_color='white')
temp_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

temp_min_displayed = CTkLabel(frame_general_1, text=f'MIN : {temp_min}{temp_unit} \nMAX : {temp_max}{temp_unit} \nRessenti : {fells_like}{temp_unit}', font=("Monserrat", 15), text_color='grey', compound=RIGHT, anchor='n')
temp_min_displayed.pack(fill=BOTH, expand=Y)

# PRESSURE

frame_general_2 = CTkFrame(general_info, fg_color=color_frame, corner_radius=10)
frame_general_2.pack(side=LEFT, fill=BOTH, pady=5, padx=5, expand=YES)

pessure_display = CTkLabel(frame_general_2, text=pressure, font=("Monserrat", 50, "bold"), anchor='center')
pessure_display.pack(side=LEFT, fill=BOTH, padx=(50, 0))

pressure_unit_label = CTkLabel(frame_general_2, text='hpa', font=("Monserrat", 15, "bold"))
pressure_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

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
wind_frame.pack(side=LEFT, fill=BOTH, pady=5, padx=5)

visibility_frame = CTkFrame(precisions_info, fg_color=color_frame)
visibility_frame.pack(side=LEFT, fill=BOTH, pady=5, padx=5)

cloud_frame = CTkFrame(precisions_info, fg_color=color_frame)
cloud_frame.pack(side=LEFT, fill=BOTH, pady=5, padx=5)

humidity_frame = CTkFrame(precisions_info, fg_color=color_frame)
humidity_frame.pack(side=LEFT, fill=BOTH, pady=5, padx=5)

# WIND

wind_display_img = CTkImage(light_image=Image.open(f'img/icons_wind/0.png'), dark_image=Image.open(f'img/icons_wind/0.png'), size=(165, 165))
wind_display = CTkLabel(wind_frame, image=wind_display_img, text='')
wind_display.pack(fill=BOTH, pady=(35, 0))

text_wind_frame = CTkFrame(wind_frame, fg_color=color_frame)
text_wind_frame.pack(fill=BOTH, pady=5, padx=5)

wind_value = CTkLabel(text_wind_frame, text=wind, font=("Monserrat", 58, 'bold'), text_color='white')
wind_value.pack(side=LEFT, fill=BOTH, padx=(35, 0))

wind_unit_label = CTkLabel(text_wind_frame, text=speed_unit, font=("Monserrat", 20, 'bold'), anchor=SW)
wind_unit_label.pack(side=LEFT, fill=BOTH, expand=YES)

# VISIBILITY

visibility_display_img = CTkImage(light_image=Image.open(f'img/icons_vis/00.png'), dark_image=Image.open(f'img/icons_vis/00.png'), size=(165, 165))
visibility_display = CTkLabel(visibility_frame, image=visibility_display_img, text='')
visibility_display.pack(fill=BOTH, pady=(35, 0))

# CLOUDS

cloud_display_img = CTkImage(light_image=Image.open(f'img/icons_clouds/0.png'), dark_image=Image.open(f'img/icons_clouds/0.png'), size=(165, 165))
cloud_display = CTkLabel(cloud_frame, image=cloud_display_img, text='')
cloud_display.pack(fill=BOTH, pady=(35, 0))

# HUMIDITY

humidity_display_img = CTkImage(light_image=Image.open(f'img/icons_hum/00.png'), dark_image=Image.open(f'img/icons_hum/00.png'), size=(165, 165))
humidity_display = CTkLabel(humidity_frame, image=humidity_display_img, text='')
humidity_display.pack(fill=BOTH, pady=(35, 0))


# PRECISION FRAME NAME

canvas_title_precision = CTkCanvas(title_info_2_frame, highlightthickness=0)
canvas_title_precision.pack(pady=10, padx=1, expand=YES)
canvas_title_precision.create_text(12, 133, text="PRECISIONS", font=("Monserrat", 15, "bold"), fill="#000000", angle=90)

# METRIC TO IMPERIAL / DATE

date = CTkLabel(right_side, text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), font=('Monserrat', 12), text_color='white')
date.pack(side=LEFT)

m_i_switch = CTkSwitch(right_side, text=f'Actuel : {temp_unit} : METRIC / IMPERIAL', font=('Monserrat', 12, 'bold'), text_color='white', command=toggle_metric_imperial)
m_i_switch.pack(side=RIGHT)

root.mainloop()