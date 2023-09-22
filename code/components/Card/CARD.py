from typing import Optional, Tuple, Union
import customtkinter as ctk
from code.config.style.colors import *
from code.config.style.font import *
from code.config.style.main import *
from code.config.settings_card import *

class Card(ctk.CTkFrame):
    def __init__(self, app_mode, data_list : list, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        if data_list != None:
            for data_dict in data_list:
                for key, value in data_dict.items():
                    if key == 'titulo':
                        title_label = ctk.CTkLabel(self, text=value, text_color=BLACK, font=ctk.CTkFont(FONT_NAME, FONT_SIZE))
                        title_label.grid(sticky='w', padx=12, pady=1)
                    elif key == 'data':
                        data_label = ctk.CTkLabel(self, text=value, text_color=BLACK, font=ctk.CTkFont(FONT_NAME, BIGGER_FONT_SIZE, weight='bold'))
                        data_label.grid(sticky='w', padx=12, pady=1)
        
        self.configure(
            fg_color=WHITE
        )