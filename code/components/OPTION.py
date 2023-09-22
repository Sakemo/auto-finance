from ast import Tuple
from ctypes import Union
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from code.config.settings_relat import *
from code.config.style.colors import *
from code.config.style.font import *
import tkinter as tk
from tkinter import ttk

class Analise_Window(ctk.CTkToplevel):
    window_open = False

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if Analise_Window.window_open:
            self.destroy()
            return

        Analise_Window.window_open = True

        for i in range(len(data)):
            self.columnconfigure((i), weight=1)
        self.rowconfigure((0, 1), weight=1)

        self.title('Relatorio e Ánalise')
        self.create_widgets(data)

    def create_widgets(self, data):
        pass