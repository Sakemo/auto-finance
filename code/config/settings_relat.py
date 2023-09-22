from code.config.ultilities.Load_Image import Load_Image
import customtkinter as ctk

# Icon Size
IMAGE_SIZE = (600,600)
ICON_SIZE = (20,20)
# Paths to Images Variables
Path_Img = {
    'FLUXO_IMG_PATH': 'images/relatorios/fluxo_de_caixa.png',
    'LUCRATIVIDADE_IMG_PATH' : 'images/relatorios/lucratividade_por_produto.png',
    'LUCRO_IMG_PATH' : 'images/relatorios/lucro_real.png',
    'RECEITA_IMG_PATH' : 'images/relatorios/media_receita_lucro.png',
    'PATRIMONIO_IMG_PATH' : 'images/relatorios/patrimonio.png',
    'DOWNLOAD_IMG_PATH' : 'images/download-solid .png'
}

# Image Loadings and Resizes
Images_Ctk = {}
for key, value in Path_Img.items():
    img_loaded = Load_Image(value, IMAGE_SIZE)
    new_key = key.replace('IMG_PATH', 'OBJ')
    if 'DOWNLOAD' not in key:
        Images_Ctk[new_key] = ctk.CTkImage(light_image=img_loaded, dark_image=img_loaded, size=IMAGE_SIZE)
    else:
        Images_Ctk[new_key] = ctk.CTkImage(light_image=img_loaded, dark_image=img_loaded, size=ICON_SIZE)
