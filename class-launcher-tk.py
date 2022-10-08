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

# Window Initial Size Definition
window_width = 500
window_height = 300

window = Tk()
window.title("Class Launcher")

# Set Window Size from previously defined values
window.geometry(f"{window_width}x{window_height}")


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


# TODO: Implement Function
def open_classroom(class_name):
    print(f"Opening {class_name}")
    # webbrowser.open(clasroom_links[class_name])


frame = tk.Frame(window)  # Grid Layout
# Render Properties of Grid
frame.pack(pady=10, padx=10, fill="both", expand=True)

style = ttk.Style().configure('my.TButton', font=('Segoe UI', 12))

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

window.mainloop()  # Run Program, Render UI & Loop to listen changes
