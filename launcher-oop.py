'''
Idea by @DlordMdia
Base code by @YarostheLaunchpadder
Edited by @DlordMdia

OOP Version - Advanced
'''

# MODULE IMPORTS!
import tkinter as tk  # Base tkinter module
import tkinter.ttk as ttk  # Fancy Tkinter Widgets
import webbrowser  # Open links
import os
import customtkinter as ctk
#from screens.launch import ClassScreen
from functools import partial  # Module to call functions with arguments from buttons
from PIL import ImageTk, Image  # Image-related module

window_width = 600
window_height = 300

# This is the list for defining classes. It will be used to generate the grid of buttons accordingly
class_list = [
    {"name": "Català", "id": "NTQ2NzkyMzY3NDcy"},
    {"name": "Castellano", "id": "NTQ2OTAwOTYzNDkx"},
    {"name": "English", "id": "NTI3MTU2NzY4Mjg4"},
    {"name": "Mates", "id": "NTQ1ODQ1NjA3MTA3"},
    {"name": "TIC", "id": "NTQ2MjkyMDE4MDI5"},
    {"name": "Tecnologia", "id": "NTQ2OTY2NTc4OTAx"},
    {"name": "Economia", "id": "NTQ3MjUzNjgxNzIw"},
    {"name": "Educació Física", "id": "NTQ3MjE2MzkzOTA2"},
    {"name": "Geografia", "id": "NTQ3MDA3OTU4OTkx"},
    {"name": "Tutoria", "id": "NTQ1NjczNjg1MDMz"},
    {"name": "Valors", "id": "NTQ1ODM0Njg1NzE0"},

]


class LauncherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.class_list = class_list
        self.title('Dlord Launcher')
        self.geometry(f"{window_width}x{window_height}")
        self.minsize(550, 300)

        # Read Settings
        if not os.path.exists("config.txt"):  # Check if settings file exists
            # If not, then write default values
            f = open("config.txt", "w")
            f.write("0,Light")
            f.close()

        self.configfile = open("config.txt", "r")
        self.configcontents = self.configfile.read()  # Get contents of settings file

        if (self.configcontents == ""):  # If file exists, but empty
            self.configfile.write("0,Light")  # Write default values

        else:  # Else, read the values contained and split them into a list
            self.configlist = self.configcontents.split(",")

        # Close the file so it doesn't corrupt or get stuck in a locked state
        self.configfile.close()

        # Variables Definitions
        self.current_user = tk.StringVar(value=0)
        self.current_theme = "Light"

        # THEME DEFAULTS

        self.button_style = ttk.Style()
        self.button_style.configure('my.TButton', font=('Segoe UI', 12))
        # Load the current user ID from settings
        self.current_user.set(self.configlist[0])
        self.apply_theme(self.configlist[1])

        launch_grid = ctk.CTkFrame(self, height=1000)  # Grid Layout

        # Configure Grid Layout
        for i in range(int((round(len(self.class_list))/4)+1)):
            launch_grid.rowconfigure(i, weight=1)

        for i in range(4):
            launch_grid.columnconfigure(i, weight=1)

        # Temp Variables to generate list correctly
        current_row = 0
        current_col = 0

        # Iterate through the classes
        for lesson in self.class_list:
            # Generate Function for Button
            action = partial(self.open_classroom, lesson["id"])
            ctk.CTkButton(launch_grid, text=lesson["name"], command=action).grid(
                row=current_row, column=current_col, padx=5, pady=5, sticky="nsew")

            # Change Current Row & Column being rendered
            if current_col == 3:
                current_col = 0
                current_row += 1

            else:
                current_col += 1

        # Render Properties of Grid
        launch_grid.pack(pady=10, padx=10, fill="both",
                         expand=True, side="top")

        bottom_row = ctk.CTkFrame(self)
        bottom_row.rowconfigure(0, weight=1)

        for i in range(5):
            bottom_row.columnconfigure(i, weight=1)

        # BOTTOM ROW WIDGETS
        ctk.CTkLabel(bottom_row, text="User ID:",
                     ).grid(column=0, row=0, padx=5, pady=5)

        ctk.CTkComboBox(bottom_row,
                        values=["0", "1", "2",  "3", "4", "5"],
                        command=self.userid_changed,
                        variable=self.current_user).grid(column=1, row=0, padx=5, pady=5)

        ctk.CTkLabel(bottom_row, text="Theme:",
                     ).grid(column=2, row=0, padx=5, pady=5)

        self.theme_button = ctk.CTkButton(
            bottom_row, text="Dark", command=self.switch_theme)

        self.theme_button.grid(
            row=0, column=3, padx=5, pady=5)

        ctk.CTkButton(bottom_row, text="Horario", command=self.show_timetable).grid(
            row=0, column=4, padx=30, pady=5, sticky=tk.E)

        bottom_row.pack(pady=10, padx=10, side="left")

        # Fix Theme Button Text
        if self.current_theme == "Light":
            self.theme_button.configure(text="Dark")

        else:
            self.theme_button.configure(text="Light")

    def switch_theme(self):  # Swap the current them

        if self.current_theme == "Light":
            ctk.set_appearance_mode("Dark")
            self.current_theme = "Dark"
            try:
                self.theme_button.configure(text="Light")

            except:
                pass

        else:
            ctk.set_appearance_mode("Light")
            self.current_theme = "Light"
            try:
                self.theme_button.configure(text="Dark")

            except:
                pass

        # Write changes to config file
        writeconfig = open("config.txt", "w")
        writeconfig.write(f"{self.current_user.get()},{self.current_theme}")
        writeconfig.close()

    # Apply a specified theme
    def apply_theme(self, target_theme):
        if target_theme != self.current_theme:  # If the current theme isn't the wanted theme
            self.switch_theme()  # Swap them, so the targeted one becomes current

    def userid_changed(self, choice):
        writeconfig = open("config.txt", "w")
        writeconfig.write(f"{choice},{self.current_theme}")
        writeconfig.close()

    def open_classroom(self, class_id):
        webbrowser.open(
            f"https://classroom.google.com/u/{self.current_user.get()}/c/{class_id}")

    def show_timetable(self):
        tt_window = ctk.CTkToplevel(self)
        tt_window.geometry("400x430")
        tt_window.title("Horario")

        def close_window():
            tt_window.destroy()
            tt_window.update()

        image1 = Image.open("clases.png")
        image1 = image1.resize((700, 650), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)

        label1 = ctk.CTkLabel(tt_window, image=test)
        label1.image = test
        label1.pack(fill="both", expand="yes")

        # Button to return to the Launcher Screen
        ctk.CTkButton(tt_window, text="Cerrar",
                      command=close_window).pack(pady=5)


if __name__ == "__main__":
    LauncherApp().mainloop()
