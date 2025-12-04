from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

from customtkinter import CTkButton

root = CTk()
root.title("Weather's Call")
root.geometry("1000x600")
root.resizable(False, False)
root.config(bg="#252530")

menu = CTkFrame(root, border_color='#202029', )
menu.place(relx=0.01, rely=0.02, relwidth=0.30, relheight=0.96)
menu.grid_rowconfigure(0, weight=1)

label = CTkLabel(menu, text="WeatherDATA", padx=5, pady=5, font=("Monserrat", 30, 'bold'), text_color='white')
label.place(relx=0.15, rely=0.055, relwidth=0.7, relheight=0.05)

search_field = CTkEntry(menu, placeholder_text="Pays ...")
search_field.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.05)
search_button = CTkButton(menu, text='Search')


root.mainloop()

