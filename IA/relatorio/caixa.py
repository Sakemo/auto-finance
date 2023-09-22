from code.database.clientes.Database import clientes
from code.database.produtos.Database import produtos
from code.database.vendas.Database import vendas

def Fluxo_Caixa_Operacional():
    fluxo = 0
    fluxo_negativo = 0
    fluxo_investimento = 0
    for id_, venda in vendas.items():
        if venda['categoria'] == 'Dinheiro':
            if venda['produto'] != 'Despesa' and venda['produto'] != 'Investimento':
                fluxo += venda['preco']
            elif venda['produto'] == 'Despesa':
                fluxo_negativo += venda['preco']
            elif venda['produto'] == 'Investimento':
                fluxo_investimento += venda['preco']
    if fluxo >= fluxo_negativo:
        fluxo_operacional = fluxo - (fluxo_negativo + fluxo_investimento)
    else:
        fluxo_operacional = 0
        
    return (fluxo, fluxo_negativo, fluxo_investimento, fluxo_operacional)