import code.database.clientes.Database as dbClientes
from customtkinter import CTkInputDialog
from code.config.style.colors import RED, DARKER_RED

def Add_Client(nome, contato, data):
    new_id = max(dbClientes.clientes.keys(), default=1) + 1
    new_client = {
        'nome' : f'{nome}',
        'fiado' : 0,
        'contato' : f'{contato}',
        'compras' : 0,
        'data_de_compra' : f'{data}',
        'continuar' : True
    }
    dbClientes.clientes[new_id] = new_client
    with open('code/database/clientes/Database.py', 'w', encoding='utf-8') as file:
        file.write(f'clientes = {dbClientes.clientes}')

def Handle_Client(nome, produto, preco, categoria, data):
    found_client = False
    for key, cliente in dbClientes.clientes.items():
        if cliente['nome'] == nome:
            found_client = True
            cliente['data_de_compra'] = f'{data}'
            if produto == 'Pagamento':
                total_fiado = float(cliente['fiado'])
                total_fiado = round(float(total_fiado - preco), 2)
                cliente['fiado'] = total_fiado
                with open('code/database/clientes/Database.py', 'w', encoding='utf-8') as file:
                    file.write(f'clientes = {dbClientes.clientes}')
            else:
                if categoria == 'Fiado':
                    if cliente['continuar'] == True:
                        total_fiado = float(cliente['fiado'])
                        total_fiado = round(float(total_fiado + preco), 2)
                        cliente['fiado'] = total_fiado
                        total_compras = float(cliente['compras'])
                        total_compras = round(float(total_compras + preco))
                        cliente['compras'] = total_compras
                        with open('code/database/clientes/Database.py', 'w', encoding='utf-8') as file:
                            file.write(f'clientes = {dbClientes.clientes}')
                    else:
                        print('venda não autorizada')
                        break
    if not found_client:
        print('Nome não encontrado')
        contact_inputbox = CTkInputDialog(
            text=f'Insira o Número de Telefone para contato com {nome}',
            button_fg_color=RED,
            button_hover_color=DARKER_RED
        )
        Add_Client(nome=nome, contato=contact_inputbox.get_input(), data=data)
        Handle_Client(nome, produto, preco, categoria, data)