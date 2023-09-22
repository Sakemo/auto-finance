import code.database.clientes.Database as dbClientes

def delete_client(id, widgets, parent, app_mode, geometry, destroy):
    for key, cliente in dbClientes.clientes.items():
        if key == id:
            dbClientes.clientes.pop(key)
            with open('code/database/clientes/Database.py', 'w', encoding='utf-8') as file:
                file.write(f'clientes = {dbClientes.clientes}')
            widgets(parent, app_mode, geometry, destroy)
            break
        else:
            continue