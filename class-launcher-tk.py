'''
Idea by @DlordMdia
UI Base code by @YarostheLaunchpadder
Edited by @#DlordMdia
'''

import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk  # Fancy Widgets! :D
import webbrowser
from functools import partial
import os
from PIL import ImageTk, Image

# Window Initial Size Definition
window_width = 550
window_height = 300

window = Tk()
window.title("Class Launcher")
window.configure(bg="white")

# Set Window Size from previously defined values
window.geometry(f"{window_width}x{window_height}")
window.minsize(550, 300)
# Read Settings

if not os.path.exists("config.txt"):
    f = open("config.txt", "w")
    f.write("0,Light")
    f.close()

configfile = open("config.txt", "r")
configcontents = configfile.read()

if (configcontents == ""):
    configfile.write("0,Light")

else:
    configlist = configcontents.split(",")

configfile.close()

current_user = tk.StringVar(value=0)
current_theme = "Light"

frame_style = ttk.Style()
frame_style.configure("My.TFrame", background="white")
frame = ttk.Frame(window, height=1000, style="My.TFrame")  # Grid Layout

button_style = ttk.Style()
button_style.configure('my.TButton', font=('Segoe UI', 12))

label_style = ttk.Style()
label_style.configure("My.TLabel", background="white")


class_list = [
    {"name": "Català", "id": "NTQ2NzkyMzY3NDcy"},
    {"name": "Castellano", "id": "NTQ2OTAwOTYzNDkx"},
    {"name": "English", "id": "https://google.com"},  # LINK NOT DEFINED!
    {"name": "Mates", "id": "NTQ1ODQ1NjA3MTA3"},
    {"name": "TIC", "id": "NTQ2MjkyMDE4MDI5"},
    {"name": "Tecnologia", "id": "NTQ2OTY2NTc4OTAx"},
    {"name": "Economia", "id": "NTQ3MjUzNjgxNzIw"},
    {"name": "Educació Física", "id": "NTQ3MjE2MzkzOTA2"},
    {"name": "Geografia", "id": "NTQ3MDA3OTU4Owindowx"},
    {"name": "Tutoria", "id": "NTQ1NjczNjg1MDMz"},
    {"name": "Valors", "id": "NTQ1ODM0Njg1NzE0"},

]


def switch_theme():
    global current_theme
    global theme_button
    if current_theme == "Light":
        window.config(bg="#26242f")
        frame_style.configure("My.TFrame", background="#26242f")
        button_style.configure("My.TFrame", background="#26242f")
        label_style.configure(
            "My.TLabel", background="#26242f", foreground="#ffffff")
        current_theme = "Dark"
        try:
            theme_button.config(text="Light")

        except:
            pass

    else:
        window.config(bg="#ffffff")
        frame_style.configure("My.TFrame", background="#ffffff")
        button_style.configure("My.TFrame", background="#ffffff")
        label_style.configure(
            "My.TLabel", background="#ffffff", foreground="#000000")
        current_theme = "Light"
        try:
            theme_button.config(text="Dark")

        except:
            pass

        writeconfig = open("config.txt", "w")
        writeconfig.write(f"{current_user.get()},{current_theme}")
        writeconfig.close()


def apply_theme(target_theme):
    if target_theme != current_theme:
        switch_theme()


current_user.set(configlist[0])

apply_theme(configlist[1])


def open_classroom(class_id):
    webbrowser.open(
        f"https://classroom.google.com/u/{current_user.get()}/c/{class_id}")


def show_timetable():
    tt_window = Toplevel(window)
    tt_window.title("Horario")
    tt_window.configure(bg="white")
    tt_window.geometry("462x433")
    tt_window.resizable(False, False)
    tt_image = ImageTk.PhotoImage(Image.open("clases.png"))
    label1 = tk.Label(tt_window, image=tt_image)
    label1.image = tt_image

    # Position image
    label1.pack()


def userid_changed():
    writeconfig = open("config.txt", "w")
    writeconfig.write(f"{current_user.get()},{current_theme}")
    writeconfig.close()


# Configure Grid Layout
for i in range(int((round(len(class_list))/4)+1)):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

current_row = 0
current_col = 0
for lesson in class_list:
    # Generate Function for Button
    action = partial(open_classroom, lesson["id"])
    ttk.Button(frame, text=lesson["name"], style="my.TButton", command=action).grid(
        row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")

    # Change Current Row & Column being rendered
    if current_col == 3:
        current_col = 0
        current_row += 1

    else:
        current_col += 1

# Render Properties of Grid
frame.pack(pady=10, padx=10, fill="both", expand=True, side="top")

bottom_row = ttk.Frame(window, style="My.TFrame")

bottom_row.rowconfigure(0, weight=1)

for i in range(5):
    bottom_row.columnconfigure(i, weight=1)

ttk.Label(bottom_row, text="User ID:", font=("Arial", 12), style="My.TLabel",
          ).grid(column=0, row=0, padx=5, pady=5)
ttk.Spinbox(
    bottom_row,
    from_=0,
    to=10,
    textvariable=current_user,
    width=10,
    font=("Arial", 12),
    command=userid_changed).grid(column=1, row=0, padx=5, pady=5)

ttk.Label(bottom_row, text="Theme:", font=("Arial", 12), style="My.TLabel",
          ).grid(column=2, row=0, padx=5, pady=5)

theme_button = ttk.Button(bottom_row, text="Dark",
                          style="my.TButton", command=switch_theme)
theme_button.grid(
    row=0, column=3, padx=5, pady=5)

ttk.Button(bottom_row, text="Horario",
           style="my.TButton", command=show_timetable).grid(
    row=0, column=4, padx=30, pady=5, sticky=tk.E)

# Fix Theme Button Text
if current_theme == "Light":
    theme_button.config(text="Dark")

else:
    theme_button.config(text="Light")

bottom_row.pack(pady=10, padx=10, side="left")


window.mainloop()  # Run Program, Render UI & Loop to listen changes
