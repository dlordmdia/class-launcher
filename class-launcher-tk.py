'''
Idea by @DlordMdia
UI Base code by @YarostheLaunchpadder
Edited by @#DlordMdia
'''

# MODULE IMPORTS!
import tkinter as tk  # Base tkinter module
import tkinter.ttk as ttk  # Fancy Widgets! :D
import webbrowser  # Open links
from functools import partial  # Module to call functions with arguments from buttons
import os
from PIL import ImageTk, Image  # Image-related module

# Window Initial Size Definition
window_width = 550
window_height = 300

window = tk.Tk()
window.title("Class Launcher")
window.configure(bg="white")

# Set Window Size from previously defined values
window.geometry(f"{window_width}x{window_height}")
window.minsize(550, 300)


# Read Settings

if not os.path.exists("config.txt"):  # Check if settings file exists
    # If not, then write default values
    f = open("config.txt", "w")
    f.write("0,Light")
    f.close()

configfile = open("config.txt", "r")
configcontents = configfile.read()  # Get contents of settings file

if (configcontents == ""):  # If file exists, but empty
    configfile.write("0,Light")  # Write default values

else:  # Else, read the values contained and split them into a list
    configlist = configcontents.split(",")

configfile.close()  # Close the file so it doesn't corrupt or get stuck in a locked state

# Variables Definitions
current_user = tk.StringVar(value=0)
current_theme = "Light"

# THEME DEFAULTS
frame_style = ttk.Style()
frame_style.configure("My.TFrame", background="white")

button_style = ttk.Style()
button_style.configure('my.TButton', font=('Segoe UI', 12))

label_style = ttk.Style()
label_style.configure("My.TLabel", background="white")

# This is the list for defining classes. It will be used to generate the grid of buttons accordingly
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


def show_timetable():  # Switch to Timetable Screen
    timetable.pack(fill='both', expand=1)
    launch.pack_forget()
    window.resizable(False, False)
    window.geometry("462x480")


def return_to_launch():  # Switch back to Launcher Screen
    launch.pack(fill='both', expand=1)
    timetable.pack_forget()
    window.resizable(True, True)


def switch_theme():  # Swap the current theme
    global current_theme
    global theme_button
    if current_theme == "Light":  # If currently the theme is light
        # Make it dark
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

    else:  # If it is dark
        # Then make it light
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

    # Write changes to config file
    writeconfig = open("config.txt", "w")
    writeconfig.write(f"{current_user.get()},{current_theme}")
    writeconfig.close()

# Apply a specified theme


def apply_theme(target_theme):
    if target_theme != current_theme:  # If the current theme isn't the wanted theme
        switch_theme()  # Swap them, so the targeted one becomes current


current_user.set(configlist[0])  # Load the current user ID from settings

apply_theme(configlist[1])


def open_classroom(class_id):
    webbrowser.open(
        f"https://classroom.google.com/u/{current_user.get()}/c/{class_id}")


def userid_changed():
    writeconfig = open("config.txt", "w")
    writeconfig.write(f"{current_user.get()},{current_theme}")
    writeconfig.close()


launch = ttk.Frame(window, style="My.TFrame")
timetable = ttk.Frame(window, style="My.TFrame")

# ----- MAIN LAUNCH WINDOW -----

frame = ttk.Frame(launch, height=1000, style="My.TFrame")  # Grid Layout

# Configure Grid Layout
for i in range(int((round(len(class_list))/4)+1)):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

# Temp Variables to generate list correctly
current_row = 0
current_col = 0

# Iterate through the classes
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

bottom_row = ttk.Frame(launch, style="My.TFrame")
bottom_row.rowconfigure(0, weight=1)

for i in range(5):
    bottom_row.columnconfigure(i, weight=1)

# BOTTOM ROW WIDGETS
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


# ----- TIMETABLE WINDOW -----
tt_image = ImageTk.PhotoImage(Image.open(
    "clases.png"))  # Open image of timetable
# Prepare the renderer for the image
tt_label = tk.Label(timetable, image=tt_image)
tt_label.image = tt_image  # Set the previously defined image to the Label space
tt_label.pack(pady=5)  # Add Label to layout

# Button to return to the Launcher Screen
ttk.Button(timetable, text="Volver", command=return_to_launch).pack(pady=5)

if __name__ == '__main__':  # If the program is running as main (not imported)
    return_to_launch()  # Switch to the main layout (Launch Screen)
    window.mainloop()  # Run Program, Render UI & Loop to listen changes
