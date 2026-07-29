import customtkinter as ctk
import os
from PIL import Image, ImageTk

app = ctk.CTk()
app.title("Caesar Chipher")
app.geometry("1000x700")
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

BASE_DIR = os.path.dirname(__file__)
icon_path = os.path.join(BASE_DIR, "icon", "1240849307331198986.png")
icon = ImageTk.PhotoImage(Image.open(icon_path))

app.iconphoto(False, icon)
app.resizable(False, False)

def caesar(text, shift):
    eng_lower = "abcdefghijklmnopqrstuvwxyz"
    eng_upper = eng_lower.upper()

    ukr_lower = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    ukr_upper = ukr_lower.upper()

    result = ""

    for char in text:
        if char in eng_lower:
            indx = (eng_lower.index(char) + shift) % len(eng_lower)
            result += eng_lower[indx]
    
        elif char in eng_upper:
            indx = (eng_upper.index(char) + shift) % len(eng_upper)
            result += eng_upper[indx]

        elif char in ukr_lower:
            indx = (ukr_lower.index(char) + shift) % len(ukr_lower)
            result += ukr_lower[indx]

        elif char in ukr_upper:
            indx = (ukr_upper.index(char) + shift) % len(ukr_upper)
            result += ukr_upper[indx]
        else:
            result += char
    return result    


def getting_shift():
    try:
        return int(entry.get().strip())
    except ValueError:
        return 3

def encodebtn():
    text = inputbox.get("1.0", "end-1c")
    shift = getting_shift()
    result = caesar(text, shift)
    outputbox.delete("1.0", "end")
    outputbox.insert("1.0", result)

def decodebtn():
    text = inputbox.get("1.0", "end-1c")
    shift = getting_shift()
    result = caesar(text, -shift)
    outputbox.delete("1.0", "end")
    outputbox.insert("1.0", result)

def copytext():
    output_text = outputbox.get("1.0", "end-1c")
    if output_text.strip():
        app.focus()
        app.clipboard_clear()
        app.clipboard_append(output_text)
        app.update()

        copybutton.configure(text = "Copied")
        app.after(2000, lambda: copybutton.configure(text = "Copy"))

encodeb = ctk.CTkButton(master=app, text = "Encode the text", corner_radius=40, font=("Arial", 25, "bold"), command=encodebtn)
encodeb.place(relx=0.32, rely=0.48, anchor="center")

decodeb = ctk.CTkButton(master=app, text = "Decode the text", corner_radius=40, font=("Arial", 25, "bold"), command=decodebtn)
decodeb.place(relx=0.68, rely=0.48, anchor="center")


entry = ctk.CTkEntry(master=app, placeholder_text="Shift", corner_radius=20, font=("Arial", 25, "bold"), width=100, height=40, border_width=3)
entry.place(relx=0.5, rely=0.48, anchor="center")


inputbox = ctk.CTkTextbox(master=app, corner_radius=20, width=450, height=220, font=("Arial", 25, "bold"), border_color="#1B6AAE", border_width=3, wrap="word")
inputbox.place(relx=0.5, rely=0.22, anchor="center")

outputbox = ctk.CTkTextbox(master=app, corner_radius=20, width=450, height=220, font=("Arial", 25, "bold"), border_color="#1B6AAE", border_width=3, wrap="word")
outputbox.place(relx=0.5, rely=0.75, anchor="center")

copybutton = ctk.CTkButton(master=app, text = "Copy", corner_radius=5, font=("Arial", 18, "bold"), width=60, height=35, command=copytext)
copybutton.place(relx=0.77, rely=0.87, anchor="center")

app.mainloop()