#!/usr/bin/python3

# Made by Nicole Sausville
# Due Date: 8/16/24
# Description: A GUI interface for interacting with the Names database.
# Tutoring

import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk
from ShowGenders import ShowGenders, Show

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Name_Browser.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class Name_BrowserUI:
    def __init__(self, master=None):
        self.init_ui(master)
        self.setup_tree()
        self.setup_gender_entry()
        # self.setup_type_combo()
        self.fetch_names()

    def init_ui(self, master):
        self.__builder = pygubu.Builder()
        self.__builder.add_resource_paths(RESOURCE_PATHS)
        self.__builder.add_from_file(PROJECT_UI)
        self.main_window: ttk.Frame = self.__builder.get_object("top_level1", master)
        self.__builder.connect_callbacks(self)

        self.__gender_combo = self.__builder.get_object('gender_combo', master)
        self.__name_entry = self.__builder.get_object('name_entry', master)
        self.__tree = self.__builder.get_object('show_tree', master)

    def setup_tree(self):
        tree = self.__tree

        tree.configure(columns=(0, 1, 2, 3, 4), displaycolumns=(0, 1, 2, 3, 4))

        tree.heading(0, text="Name", anchor=tk.W)
        tree.heading(1, text="Gender")
        tree.heading(2, text="Year")
        tree.heading(3, text="NameCount")
        tree.heading(4, text="Total")

        tree.column(0, width=50)
        tree.column(1, width=50, anchor=tk.CENTER)
        tree.column(2, width=50, anchor=tk.CENTER)
        tree.column(3, width=80, anchor=tk.CENTER)
        tree.column(4, width=80, anchor=tk.CENTER)

    def setup_gender_entry(self):
        genders = ShowGenders.fetch_genders()
        self.__gender_combo['values'] = [ShowGenders.ALL_GENDERS] + [gender.get_gender() for gender in genders]
        self.__gender_combo.current(0)

    def gender_changed(self, event):
        print("Gender Changed:", self.__gender_combo.get())
        self.fetch_names()

    def names_changed(self, event):
        print("Names Changed:", self.__name_entry.get())
        self.fetch_names()

    @staticmethod
    def names_to_tuple(show):
        return(
            show.get_name(),
            show.get_gender(),
            show.get_year(),
            show.get_count(),
            show.get_total()
        )

    # Receives info from Show Class
    def fetch_names(self):
        name_entry = self.__name_entry.get().capitalize()
        shows = Show.fetch_names(self.__gender_combo.get(), name_entry)

        # Resets the tree when new input is given
        for i in self.__tree.get_children():
            self.__tree.delete(i)

        # Displays the tree
        for i in range(len(shows)):
            self.__tree.insert("","end", values=Name_BrowserUI.names_to_tuple(shows[i]))

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Name Popularity per Year and Gender")
    app = Name_BrowserUI(root)
    app.run()
