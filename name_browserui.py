#!/usr/bin/python3

# Made by Nicole Sausville
# Due Date: 8/16/24
# Description: A GUI interface for interacting with
#              the Names database.

import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk
from ShowGenders import ShowGenders

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Name_Browser.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class Name_BrowserUI:
    def __init__(self, master=None):
        self.start_ui(master)
        self.setup_gender_entry()

    def start_ui(self, master):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        self.main_window: ttk.Frame = self.builder.get_object("top_level1", master)
        self.builder.connect_callbacks(self)

        self.gender_combo = self.builder.get_object('gender_combo', master)

    def setup_gender_entry(self):
        genders = ShowGenders.fetch_genders()
        self.gender_combo['values'] = [ShowGenders.ALL_GENDERS] + [gender.get_gender() for gender in genders]

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Name Popularity per Year")
    app = Name_BrowserUI(root)
    app.run()
