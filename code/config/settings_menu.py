from typing import Tuple
import customtkinter as ctk
from code.config.style.colors import *
from code.config.style.font import *
from code.config.style.main import *
from code.config.ultilities.Load_Image import Load_Image
import code.database.clientes.Database as dbClientes
import code.database.vendas.Database as dbVendas
import code.database.produtos.Database as dbProdutos
# Importations Settins
Tuple = Tuple

# Paths to Images Variables
Path_Img = {
    'EXPAND_IMG_PATH': 'images/square-caret-down-solid.png',
    'DASHBOARD_IMG_PATH': 'images/chart-line-solid.png',
    'CLIENTS_IMG_PATH': 'images/address-book-solid.png',
    'BUSINESS_IMG_PATH': 'images/money-bills-solid.png',
    'PRODUCTS_IMG_PATH': 'images/box-archive-solid.png',
    'FILTER_IMG_PATH' : 'images/filter-solid.png',
    'SEARCH_IMG_PATH' : 'images/magnifying-glass-solid.png'
}

# Image Loadings and Resizes
Images_Ctk = {}
for key, value in Path_Img.items():
    img_loaded = Load_Image(value, ICON_SIZE)
    new_key = key.replace('IMG_PATH', 'OBJ')
    Images_Ctk[new_key] = ctk.CTkImage(light_image=img_loaded, dark_image=img_loaded, size=ICON_SIZE)
    
# Layout Settings
COLUMN_MAIN = 5
ROW_MAIN = 2

button_data = [
('dashboard_button', Images_Ctk['DASHBOARD_OBJ'], RED, DARKER_RED,'dashboard'),
('business_button', Images_Ctk['BUSINESS_OBJ'], RED, DARKER_RED, 'vendas'),
('products_button', Images_Ctk['PRODUCTS_OBJ'], RED, DARKER_RED, 'produtos'),
('clients_button', Images_Ctk['CLIENTS_OBJ'], RED, DARKER_RED, 'clientes'),
('expand_button', Images_Ctk['EXPAND_OBJ'], WHITE, LIGHT_GRAY, '_exp')
]

search_data = [
    ('clientes', dbClientes.clientes),
    ('vendas', dbVendas.vendas),
    ('produtos', dbProdutos.produtos)
]