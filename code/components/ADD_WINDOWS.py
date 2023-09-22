from typing import Optional, Tuple, Union
import customtkinter as ctk
from code.config.style.colors import *
from code.config.style.font import *
from code.config.style.main import *
from code.other.modes_app.adding.add_prod import Add_Product
from code.other.modes_app.adding.add_client import Add_Client
from code.other.modes_app.adding.add_sell import Add_Sell
import code.database.produtos.Database as dbProdutos
from code.other.formulas.Get_Time.Get_Today import GET_TODAY

class Add_Window_Sell(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)  
        
        self.products_list = []
        for keys in dbProdutos.produtos.keys():
            self.products_list.append(keys)
        
        self.geometry('400x500')
        self.title('Adicionar')
        self.resizable(False, False)

        today = GET_TODAY()
        today = f'{today[0]}/{today[1]}/{today[2]}'
        
        self.data = ctk.StringVar(value=f'{today}')
        self.produto = ctk.StringVar(value='Produto')
        self.quantia = ctk.DoubleVar(value=0.0)
        self.nome = ctk.StringVar()
        self.categoria = ctk.StringVar(value='Dinheiro')
        self.notas = ctk.StringVar(value='Ex.: Leite')
    
        self.widgets()
    
    def update_data(self, _):
        self.data.set(self.data_input.get())
        self.produto.set(self.produto_input.get())
        self.quantia.set(self.quantia_input.get())
        self.nome.set(self.nome_input.get())
        self.categoria.set(self.categoria_input.get())
        if self.produto.get() == 'Investimento':
            if not hasattr(self, 'notas_input') or not isinstance(self.notas_input, ctk.CTkEntry):
                self.notas_input, self.title_notas_input = self.add_input(
                    self, self.update_data, self.notas, 'Escreva a finalidade do investimento:'
                )
            self.notas.set(self.notas_input.get())
        else:
            try:
                self.notas_input.destroy()
                try:
                    self.title_notas_input.destroy()
                except:
                    self.title_notas_input.destroy()                    
            except:
                pass
        
    def add_input(self, master, command, var, title):
        title = ctk.CTkLabel(
            self, text=f'{title}'
        )
        title.pack(side='top')
        input = ctk.CTkEntry(
            master, width=300, textvariable=var,
            corner_radius=10
        ) 
        input.pack(side='top', padx=10, pady=10)
        input.bind("<FocusOut>", command)
        return input, title
    
    def add_item(self):
        if self.produto.get() == 'Investimento':
            if self.notas.get() == '' or self.notas.get() == None:
                print('Escreva a finalidade do investimento')
            if self.notas.get() in self.products_list:
                estoque_quantia = ctk.CTkInputDialog(
                    text=f'Insira a quantidade do produto {self.notas.get()} a ser adicionado no estoque',
                    button_fg_color=RED, button_hover_color=DARKER_RED
                )
                estoque = estoque_quantia.get_input()
                if estoque == '' or float(estoque) <= 0:
                    print('Insira um nome valido')
                else:
                    Add_Sell(self.data.get(), self.produto.get(), self.quantia.get(), self.nome.get(), self.categoria.get(), self.notas.get(), float(estoque))
        else:
            if self.nome.get():
                Add_Sell(self.data.get(), self.produto.get(), self.quantia.get(), self.nome.get(), self.categoria.get(), self.notas.get(), 0)
            else:
                Add_Sell(self.data.get(), self.produto.get(), self.quantia.get(), None, self.categoria.get(), self.notas.get(), 0)

    def widgets(self):
        self.data_input, title = self.add_input(
            self, self.update_data, self.data, 'Data'
        )
        ctk.CTkLabel(
            self,
            text='Finalidade'
        ).pack(side='top')
        self.produto_input = ctk.CTkComboBox(
            self, width=300, corner_radius=10, variable=self.produto, values=self.products_list
        )
        self.produto_input.pack(side='top', padx=10, pady=10)
        self.quantia_input, title = self.add_input(
            self, self.update_data, self.quantia, 'Quantia'
        )
        self.nome_input, title = self.add_input(
            self, self.update_data, self.nome, 'Nome do Contribuente'
        )
        ctk.CTkLabel(
            self,
            text='Tipo de transação'
        ).pack(side='top')        
        self.categoria_input = ctk.CTkComboBox(
            self, width=300, corner_radius=10, variable=self.categoria, values=['Dinheiro', 'Fiado', 'PIX', 'Cartão', 'Outro']
        )
        self.categoria_input.pack(side='top', padx=10, pady=10)
        
        btn_send = ctk.CTkButton(
            self, 400, corner_radius=10, text='Adicionar', fg_color=RED, hover_color=DARKER_RED, text_color=WHITE, command=lambda : self.add_item()
        )
        btn_send.pack(side='top', fill='x', padx=15, pady=7) 


class Add_Product_Window(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        self.geometry('400x300')
        self.title('Adicionar')
        self.resizable(False, False)
        
        self.name = ctk.StringVar(value='Produto')
        self.price = ctk.DoubleVar()
        self.cart = ctk.StringVar()
    
        self.widgets()
    
    def update_data(self, _):
        self.name.set(self.name_input.get())
        self.price.set(self.price_input.get())
        self.cart.set(self.cart_input.get())
        
    def add_input(self, master, command, var, title):
        ctk.CTkLabel(
            self, text=f'{title}'
        ).pack(side='top')
        input = ctk.CTkEntry(
            master, width=300, textvariable=var,
            corner_radius=10
        ) 
        input.pack(side='top', padx=10, pady=10)
        input.bind("<FocusOut>", command)
        return input
    
    def add_item(self):
        Add_Product(self.name.get(), self.price.get(), self.cart.get())        
    
    def widgets(self):
        self.name_input = self.add_input(
            self, self.update_data, self.name, 'Produto'
        )
        self.price_input = self.add_input(
            self, self.update_data, self.price, 'Preço'
        )
        self.cart_input = self.add_input(
            self, self.update_data, self.cart, 'Cartegoria'
        )
        
        btn_send = ctk.CTkButton(
            self, 400, corner_radius=10, text='Adicionar', fg_color=RED, hover_color=DARKER_RED, text_color=WHITE, command=lambda : self.add_item()
        )
        btn_send.pack(side='top', fill='x', padx=15, pady=7) 