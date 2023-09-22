from code.other.modes_app.adding.add_client import Handle_Client
import code.database.vendas.Database as dbVendas
import code.database.produtos.Database as dbProdutos

def delete_sell(id, widgets, parent, app_mode, geometry, destroy):
    for key, venda in dbVendas.vendas.items():
        if key == id:
            dbVendas.vendas.pop(key)
            with open('code/database/vendas/Database.py', 'w', encoding='utf-8') as file:
                file.write(f'vendas = {dbVendas.vendas}')
            widgets(parent, app_mode, geometry, destroy)
            break
        else:
            continue