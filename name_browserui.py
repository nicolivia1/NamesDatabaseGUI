#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk
from ShowNames import ShowNames

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Name_Browser.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class Name_BrowserUI:
    def __init__(self, master=None):
        self.start_ui(master)
        self.setup_name_entry()
    def start_ui(self, master):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        self.main_window: ttk.Frame = self.builder.get_object(
            "top_level1", master)
        self.builder.connect_callbacks(self)

        self.name_entry = self.builder.get_object('name_entry', master)
        self.gender_combo = self.builder.get_object('gender_combo', master)

    def setup_name_entry(self):
        names = ShowNames.fetch_names()
    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Name Popularity per Year")
    app = Name_BrowserUI(root)
    app.run()
