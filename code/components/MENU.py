from code.config.settings_menu import *
from code.other.modes_app.toogle_mode import toogle_mode
import customtkinter as ctk
from code.config.ultilities.Search import search, filter_dict


class Menu_Widgets(ctk.CTkFrame):
    def __init__(self, parent, destroy: bool, geometry : tuple , name : str, widgets, app_mode : str, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        for col in range(COLUMN_MAIN):
            self.columnconfigure(col, weight=1)
        for row in range(ROW_MAIN):
            self.rowconfigure(row, weight=1)

        self.buttons = self.create_widgets(parent, destroy, geometry, name, widgets, app_mode)
        self.layout()

    def create_widgets(self, parent, destroy: bool, geometry : tuple , name : str, widgets, app_mode : str):
        self.buttons = {}
        for button_name, image, fg_color, hover_color, type_name in button_data:
            if type_name != '_exp':
                button = ctk.CTkButton(
                    self, fg_color=fg_color, hover_color=hover_color, text='', image=image,
                    command=lambda type_name=type_name: toogle_mode(parent, destroy, geometry, type_name, widgets, app_mode)
                )
                self.buttons[button_name] = button
            else:
                if type_name not in app_mode:
                    button = ctk.CTkButton(
                        self, fg_color=fg_color, hover_color=hover_color, text='', image=image,
                        command=lambda type_name=type_name: toogle_mode(parent, destroy, geometry, f'{app_mode}{type_name}', widgets, app_mode)
                    )
                    self.buttons[button_name] = button  
                else:
                    new_type = app_mode.replace(f'{type_name}', '')
                    button = ctk.CTkButton(
                        self, fg_color=fg_color, hover_color=hover_color, text='', image=image,
                        command=lambda type_name=type_name: toogle_mode(parent, destroy, geometry, f'{new_type}', widgets, app_mode)
                    )
                    self.buttons[button_name] = button 
        
        for app, database in search_data:
            if app_mode == app:
                def search_create():
                    search_var = ctk.StringVar()
                    search_input = ctk.CTkEntry(self, fg_color=WHITE, corner_radius=10, text_color=BLACK, font=ctk.CTkFont(FONT_NAME, FONT_SIZE), textvariable=search_var)
                    search_button = ctk.CTkButton(self, fg_color=WHITE, hover_color=LIGHT_GRAY, corner_radius=10, text='', image=Images_Ctk['SEARCH_OBJ'], 
                                                command=lambda : search(search_var.get(), database, widgets, parent, app_mode, geometry, destroy))
                    search_input.bind('<Return>', lambda _: search(search_var.get(), database, widgets, parent, app_mode, geometry, destroy))
                    search_input.grid(column=0, row=(ROW_MAIN-1), columnspan=(COLUMN_MAIN - 2), sticky='nswe', pady=2, padx=2)
                    search_button.grid(column=(COLUMN_MAIN-2), row=(ROW_MAIN-1), padx=2)

                search_create()
                filter_var = ctk.StringVar(value='Reoganizar')
                filter_button = ctk.CTkOptionMenu(self, fg_color=WHITE, text_color=BLACK, button_color=WHITE, dropdown_fg_color=BLACK, dropdown_hover_color='#444', button_hover_color=LIGHT_GRAY, values=['Mais Antigo', 'Novo', 'Maior Valor', 'Menor Valor', 'A-Z'], variable=filter_var, command=lambda _ : filter_dict(filter_var.get(), database, widgets, parent, app_mode, geometry, destroy))
                filter_button.grid(column=(COLUMN_MAIN-1), row=(ROW_MAIN - 1), padx=2)
                break
        
        return self.buttons
    def layout(self):
        for i, (button_name, button) in enumerate(self.buttons.items()):
                button.grid(column=i, row=0, padx=2)
