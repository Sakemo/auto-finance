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
from code.components.Card.CARD import Card

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

        self.title('Analise de Relatorio Financeiro')
        self.create_widgets(data)

    def database(self, data, index):
        database = []
        for key, value in data[index].items():
            if key == 'Ativos':
                database.append({'titulo': '', 'data' : 'Ativos da Empresa'})
                for chave, valor in value.items():
                    if chave != 'Lucratividade por Produto':
                        database.append({'titulo' : chave, 'data' : valor})
            elif key == 'Passivos':
                database.append({'titulo': '', 'data' : 'Passivos da Empresa'})
                for chave, valor in value.items():
                    database.append({'titulo' : chave, 'data' : valor})
            else:
                database.append({'titulo' : key, 'data' : value})

        return database

    def on_close(self):
        Analise_Window.window_open = False
        self.destroy()

    def create_widgets(self, data):
        frame = ctk.CTkScrollableFrame(self, width=600, height=800)
        frame.pack()
        for i in range(len(data)):
            database = self.database(data, i)
            card = Card('app', database, frame)
            card.pack(padx=5, pady=10, fill='both')