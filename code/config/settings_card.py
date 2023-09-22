from code.config.ultilities.Load_Image import Load_Image
import customtkinter as ctk


# Icon Size
ICON_SIZE = (20,20)

# Paths to Images Variables
Path_Img = {
    'DELETE_IMG_PATH': 'images/trash-solid.png'
}

# Image Loadings and Resizes
Images_Ctk = {}
for key, value in Path_Img.items():
    img_loaded = Load_Image(value, ICON_SIZE)
    new_key = key.replace('IMG_PATH', 'OBJ')
    Images_Ctk[new_key] = ctk.CTkImage(light_image=img_loaded, dark_image=img_loaded, size=ICON_SIZE)