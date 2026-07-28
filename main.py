import customtkinter as ctk
import os
from PIL import Image, ImageTk

app = ctk.CTk()
app.title("Caesar Chiper")
app.geometry("1000x700")
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

BASE_DIR = os.path.dirname(__file__)
icon_path = os.path.join(BASE_DIR, "icon", "1240849307331198986.png")
icon = ImageTk.PhotoImage(Image.open(icon_path))

app.iconphoto(False, icon)

eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = eng_lower.upper()

ukr_lower = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
ukr_upper = ukr_lower.upper()

def caesar(char, alphabet, shift):
    pass
    

encodeb = ctk.CTkButton(master=app, text = "Encode the text", corner_radius=40, font=("Arial", 25, "bold"))
encodeb.place(relx=0.33, rely=0.48, anchor="center")

decodeb = ctk.CTkButton(master=app, text = "Decode the text", corner_radius=40, font=("Arial", 25, "bold"))
decodeb.place(relx=0.67, rely=0.48, anchor="center")


entry = ctk.CTkEntry(master=app, placeholder_text="Shift", corner_radius=20, font=("Arial", 25, "bold"), width=100, height=40)
entry.place(relx=0.5, rely=0.48, anchor="center")


inputbox = ctk.CTkTextbox(master=app, corner_radius=20, width=450, height=220, font=("Arial", 25, "bold"), border_color="#1B6AAE", border_width=3, wrap="word")
inputbox.place(relx=0.5, rely=0.22, anchor="center")

outputbox = ctk.CTkTextbox(master=app, corner_radius=20, width=450, height=220, font=("Arial", 25, "bold"), border_color="#1B6AAE", border_width=3, wrap="word")
outputbox.place(relx=0.5, rely=0.75, anchor="center")

app.mainloop()