from code.other.modes_app.adding.add_client import Handle_Client
import code.database.vendas.Database as dbVendas
import code.database.produtos.Database as dbProdutos

                        
def Add_Sell(data, finalidade, quantia, nome, categoria, notas, estoque):
    novo_id = max(dbVendas.vendas.keys(), default=0) + 1
    
    for key, produto in dbProdutos.produtos.items():
        if produto['nome'] == finalidade:
            dado_preco = float(produto['preco'])
            dado_quantia = float(quantia)
            
            tipo_produto = str(produto['tipo'])
            id_produto = int(produto['id'])
            
            if id_produto != 0 and tipo_produto != 'Kg':
                preco_venda = round(float(dado_preco*(dado_quantia)), 2)
            elif tipo_produto == 'Kg':
                if dado_quantia >= 100:
                    preco_venda = round(float(dado_preco*(dado_quantia)), 2)
                else:
                    preco_venda = round(float(dado_preco*(dado_quantia)), 2)
            if id_produto == 0:
                preco_venda = round(float(dado_preco*(dado_quantia)), 2)
            break
        
    else:
        print('Produto Inexistente')
    
    if categoria == '' or categoria == None:
        categoria = 'Dinheiro'
    elif (categoria == '' or categoria == None) and (nome != '' or nome != None):
        categoria = 'Fiado'
    elif categoria == 'Fiado' and (nome == '' or nome == None):
        print('Não é possivel vender fiado sem o nome do cliente')
    
    if produto == 'Pagamento' and (nome == '' or nome == None):
        print('Insira o nome do cliente.')
    
    if produto == 'Pagamento' and (categoria == 'Fiado' or categoria == '' or categoria == None):
        categoria == 'Dinheiro'
        
    for key, produto in dbProdutos.produtos.items():
        vendas_produto = int(produto['vendas'])
        custo_produto = float(produto['custo'])
        lucro_produto = float(produto['lucro'])
        estoque_produto = float(produto['estoque'])
        tipo_produto = str(produto['tipo'])
        id_produto = int(produto['id'])
        if key == finalidade and key != 'Investimento':
            vendas_produto += 1
            lucro_produto += preco_venda
            estoque_produto -= quantia
        if (notas == produto['nome'] or notas == produto['categoria']):
            if finalidade == 'Investimento':
                custo_produto += preco_venda
                estoque_produto += float(estoque)   
        lucro_produto = (lucro_produto - custo_produto)
        produto['vendas'] = vendas_produto
        produto['custo'] = custo_produto
        produto['lucro'] = lucro_produto
        produto['estoque'] = estoque_produto
    
    if (nome != '' and nome != None):
        Handle_Client(nome=nome, produto=finalidade, preco=preco_venda, categoria=categoria, data=data)
    
    if finalidade != 'Investimento':
        new_sell = {
            'data': data, 'categoria': categoria, 'produto': finalidade, 'quantia': quantia, 'preco': preco_venda, 'nome': nome, 'tipo' : tipo_produto
        }
    else:
        new_sell = {
            'data': data, 'categoria': categoria, 'produto': finalidade, 'quantia': estoque, 'preco': preco_venda, 'nome': nome, 'investido':notas
        }
    
    dbVendas.vendas[novo_id] = new_sell
    
    with open('code/database/produtos/Database.py', 'w', encoding='utf-8') as file:
        file.write(f'produtos = {dbProdutos.produtos}')
    
    with open('code/database/vendas/Database.py', 'w', encoding='utf-8') as file:
        file.write(f'vendas = {dbVendas.vendas}')