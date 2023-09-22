from ast import Tuple
from ctypes import Union
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from code.config.settings_relat import *
from code.config.style.colors import *
from code.config.style.font import *

class Relatorio_Window(ctk.CTkToplevel):
    window_open = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if Relatorio_Window.window_open:
            self.destroy()
            return

        Relatorio_Window.window_open = True

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1), weight=1)

        self.title('Relatorio Financeiro')
        self.create_widgets()

    def on_close(self):
        Relatorio_Window.window_open = False
        self.destroy()

    def download_image(self, image_path: str):
        directory = filedialog.askdirectory(title="Selecione uma pasta para baixar a imagem")
        if directory:
            import shutil
            image_name = image_path.split("/")[-1]
            destination_path = f"{directory}/{image_name}"
            shutil.copy(image_path, destination_path)

    def create_widgets(self):
        image_labels = []
        for i, (key, img_path) in enumerate(Path_Img.items()):
            img_label = ctk.CTkLabel(self, corner_radius=20, image=Images_Ctk[key.replace('_IMG_PATH', '_OBJ')], text='')
            img_label.grid(column=i % 3, row=i // 3, sticky='nswe', padx=2, pady=2)
            image_labels.append(img_label)

            # Adicione o botão de download abaixo de cada imagem
            download_btn = ctk.CTkButton(self, 50, 50, corner_radius=10, fg_color=WHITE, hover_color=LIGHT_GRAY, image=Images_Ctk['DOWNLOAD_OBJ'], text='', bg_color='transparent', command=lambda : self.download_image(img_path))
            download_btn.place(in_=img_label, anchor='se', bordermode='outside', relx=0.95, rely=0.95)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.grid_rowconfigure(i, weight=1)

        txt_frame = ctk.CTkScrollableFrame(self, width=600, height=600, fg_color=WHITE)
        txt_label = ctk.CTkLabel(txt_frame, width=600, font=ctk.CTkFont(FONT_NAME, 16), height=600,text_color=BLACK, text='Legenda e Informações \n\n- Fluxo de caixa: Registro das entradas e saídas de dinheiro.\n\n- Lucratividade por produto: Avaliação dos lucros gerados por cada item vendido.\n\n- Receita total: Soma de todas as vendas realizadas.\n\n- Custo total: Soma de todos os gastos operacionais.\n\n- Lucro bruto: Diferença entre a receita total e o custo total.\n\n- Lucro líquido: Lucro bruto menos despesas adicionais e impostos.\n\n- Ativos da empresa: Bens e recursos possuídos pela empresa.\n\n- Passivos da empresa: Obrigações e dívidas a serem pagas.', compound='left', anchor='w')
        txt_label.pack()
        txt_frame.grid(column=2, row=1, sticky='nswe')