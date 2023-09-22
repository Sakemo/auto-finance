from typing import Literal, Tuple
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from code.components.Card.CARD import Card
from code.config.settings_card import *
from code.config.style.colors import *
from code.config.style.font import *
from code.config.style.main import *
from code.other.modes_app.delete.delete_sell import delete_sell

def Creation_of_Cards(database: list, Frame_Card, app_mode):
    card = Card(data_list=database, master=Frame_Card, app_mode=app_mode)
    
    if app_mode == 'produtos' or app_mode == 'produtos_exp':
        id_item = database[0]['id']
        if id_item != 0:
            card.pack(padx=10, pady=10, fill='both')
    else:
        card.pack(padx=10, pady=10, fill='both')

    if app_mode != 'dashboard' and app_mode != 'dashboard_exp' and '_exp' in app_mode:
        btn_del = ctk.CTkLabel(card, width=50, height=50, fg_color=WHITE, image=Images_Ctk['DELETE_OBJ'], text='', cursor='hand2')
        btn_del.place(relx=0.87, rely=0.02)
        return btn_del