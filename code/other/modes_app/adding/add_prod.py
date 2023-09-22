import code.database.produtos.Database as dbProdutos

def Add_Product(nome, preco, cart = '', tipo = 'U'):
    max_id = -1
    
    for produto, info in dbProdutos.produtos.items():
        if info['id'] > max_id and info['id'] not in (0,0):
            max_id = info['id']
            max_key = produto
            
    if max_id != -1:
        if nome == '' or nome == 'Produto' or nome == None:
            print('Nome do produto não inserido')
            return False
        if preco == 0.0 or preco == None or preco == '':
            print('Insira um preço valido')
            return False
        
        new_id = max_id + 1
        
        new_product = {
            'id' : new_id,
            'nome' : f'{nome}',
            'preco' : f'{preco}',
            'categoria' : cart,
            'estoque' : 0,
            'data compra' : '',
            'custo' : 0.0,
            'lucro' : 0.0,
            'vendas' : 0,
            'tipo' : f'{tipo}'
        }
        
        dbProdutos.produtos[f'{nome}'] = new_product
        with open('code/database/produtos/Database.py', 'w', encoding='utf-8') as file:
            file.write(f'produtos = {dbProdutos.produtos}')