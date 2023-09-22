from code.database.clientes.Database import clientes
from code.database.produtos.Database import produtos
from code.database.vendas.Database import vendas

def Pessoas_Atendidas():
    nomes_clientes = set()
    for id_, venda in vendas.items():
        nome_cliente = venda.get('nome', '')
        if nome_cliente:
            nomes_clientes.add(nome_cliente)
    
    for id_, venda in vendas.items():
        if not venda.get('nome', ''):
            nomes_clientes.add('Cliente Desconhecido')
    
    return len(nomes_clientes)

def Receita_Total():
    receita_total = 0
    for id_, venda in vendas.items():
        if venda['produto'] != 'Despesa' and venda['produto'] != 'Investimento':
            receita_total += venda['preco']
    return receita_total

def Despesas_Operacionais():
    despesas_operacionais = 0
    despesas_dispensavel = 0
    for id_, venda in vendas.items():
        if venda['produto'] == 'Despesa':
            despesas_dispensavel += venda['preco']
        elif venda['produto'] == 'Investimento':
            despesas_operacionais += venda['preco']
    depesas_totais = despesas_operacionais + despesas_dispensavel            
    return despesas_operacionais, despesas_dispensavel, depesas_totais

def Lucro_Bruto():
    d, d, despesas_totais = Despesas_Operacionais()
    receita_total = Receita_Total()
    lucro_bruto = receita_total - despesas_totais
    return lucro_bruto

def Lucro_Liquido():
    despesas_operacionais, despesas_dispensaveis, d = Despesas_Operacionais()
    receita_total = Receita_Total()
    lucro_liquido = receita_total - (despesas_dispensaveis)
    return lucro_liquido, despesas_operacionais