from typing import Tuple
import customtkinter as ctk
from IA.relatorio.main import Relatorio_Financeiro
from IA.analise.main import Analise
from code.config.style.colors import *
from code.config.style.font import *
from code.config.style.main import *
from code.config.ultilities.Load_Image import Load_Image
from code.components.ADD_WINDOWS import Add_Product_Window, Add_Window_Sell
# Importations Settins
Tuple = Tuple

# Paths to Images Variables
Path_Img = {
    'RELATORIO_IMG_PATH': 'images/wand-magic-sparkles-solid.png',
    'ANALISE_IMG_PATH': 'images/wand-sparkles-solid.png',
    'ADD_IMG_PATH' : 'images/plus-solid.png'
}

# Image Loadings and Resizes
Images_Ctk = {}
for key, value in Path_Img.items():
    img_loaded = Load_Image(value, ICON_SIZE)
    new_key = key.replace('IMG_PATH', 'OBJ')
    Images_Ctk[new_key] = ctk.CTkImage(light_image=img_loaded, dark_image=img_loaded, size=ICON_SIZE)

button_data = [
('relatorio_button', Images_Ctk['RELATORIO_OBJ'], RED, DARKER_RED,'Gerar Relatorio', Relatorio_Financeiro),
('analise_button', Images_Ctk['ANALISE_OBJ'], RED, DARKER_RED, 'Gerar Analise', Analise),
('add_btn', Images_Ctk['ADD_OBJ'], RED, DARKER_RED, '', '')
]