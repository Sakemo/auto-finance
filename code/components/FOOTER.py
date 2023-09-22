from typing import Optional, Tuple, Union
from code.config.settings_footer import *
import customtkinter as ctk
from IA.relatorio.resultados import Receita_Total

class Footer_Widgets(ctk.CTkFrame):
    def __init__(self, app_mode, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    
        self.widgets(app_mode)
    
    def widgets(self, app_mode):
        buttons_frame = ctk.CTkFrame(
            self
        )
        buttons_frame.pack(pady=6)
        
        for button_name, image, fg_color, hover_color, type_name, function_command in button_data:
            if type_name != '':
                command = function_command
                button = ctk.CTkButton(
                    buttons_frame, fg_color=fg_color, hover_color=hover_color,width=200, height=50, text=f'{type_name}', image=image, font = ctk.CTkFont(FONT_NAME, FONT_SIZE), command=lambda : command()
                ).pack(padx=5, pady=3, side='left', fill='both')
            else:
                if app_mode == 'produtos' or app_mode == 'produtos_exp':
                    button = ctk.CTkButton(
                        buttons_frame, fg_color=fg_color, command=Add_Product_Window, hover_color=hover_color, text=f'{type_name}', image=image, width=200, height=50, font = ctk.CTkFont(FONT_NAME, FONT_SIZE)
                    ).pack(padx=5, pady=3, side='left', fill='both')
                elif app_mode == 'vendas' or app_mode == 'vendas_exp':
                    button = ctk.CTkButton(
                        buttons_frame, fg_color=fg_color, command=Add_Window_Sell, hover_color=hover_color, text=f'{type_name}', image=image, width=200, height=50, font = ctk.CTkFont(FONT_NAME, FONT_SIZE)
                    ).pack(padx=5, pady=3, side='left', fill='both')