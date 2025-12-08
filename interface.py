from PIL.ImageOps import expand
from customtkinter import *  #     pip install customtkinter
from CTkListbox import * #     pip install CTkListbox
import messagebox
import webbrowser
from PIL import Image
from dict import *

'''VARIABLES DE DEFINITIONS'''

color_bg = '#292933'
color_frame = '#202029'

data = False

city_name = False
ctr_name = False

temp_unit = '°C' #defaut = °C a modif vers °F

condition_desc_code = 'ciel dégagé'
condition_img = '01d'
temp = 0
temp_min = 0
temp_max = 0
fells_like = 0
pressure = 1024
wind = 0
visibility = 0
cloud = 0
humidity = 0
lon = 0
lat = 0


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

openstreetmap_button = CTkButton(title_frame, text='OpenStreetMap', font=('Monserrat', 15), text_color='#59608C', corner_radius=10, fg_color='white', hover_color='#B6B6B6', command=open_map)
openstreetmap_button.pack(pady=10, padx=15, side=RIGHT)

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

# PRECISION FRAME NAME

canvas_title_precision = CTkCanvas(title_info_2_frame, highlightthickness=0)
canvas_title_precision.pack(pady=10, padx=1, expand=YES)
canvas_title_precision.create_text(12, 132, text="PRECISIONS", font=("Monserrat", 15, "bold"), fill="#000000", angle=90)

root.mainloop()