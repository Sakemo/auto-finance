import code.database.produtos.Database as dbProdutos

def delete_prod(id, widgets, parent, app_mode, geometry, destroy):
    for key, produto in dbProdutos.produtos.items():
        if produto['id'] == id:
            dbProdutos.produtos.pop(key)
            with open('code/database/produtos/Database.py', 'w', encoding='utf-8') as file:
                file.write(f'produtos = {dbProdutos.produtos}')
            widgets(parent, app_mode, geometry, destroy)
            break
        else:
            continue