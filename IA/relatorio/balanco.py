from code.database.clientes.Database import clientes
from code.database.produtos.Database import produtos
from code.database.vendas.Database import vendas
from datetime import datetime, timedelta

def Ativos():
    data_atual = datetime.now()
    
    fiado_a_receber = 0
    fiado_atrasado = 0
    valor_estoque = 0
    lucratividade = []
    
    for id_, cliente in clientes.items():
        fiado_a_receber += cliente['fiado']
        data_compra = cliente['data_de_compra']
        for id_, venda in vendas.items():
            if venda['data'] == data_compra and venda['produto'] != 'Pagamento' and venda['nome'] == cliente['nome']:
                data_compra_obj = datetime.strptime(data_compra, '%d/%m/%Y')
                restante_data = data_atual - data_compra_obj
                mes = timedelta(days=30)
                if restante_data >= mes:
                    fiado_atrasado += cliente['fiado']    
    for id_, produto in produtos.items():
        valor_a_receber = (produto['estoque']*produto['preco'])
        if produto['lucro'] <= 0:
            diferenca = valor_a_receber + produto['lucro']
        else:
            diferenca = valor_a_receber - produto['lucro']
        produto_investi = (produto['nome'], valor_a_receber, diferenca)
        lucratividade.append(produto_investi)
        
        valor_estoque += valor_a_receber    
        
    return {
        'Contas a Receber' : fiado_a_receber,
        'Contas Atrasadas' : fiado_atrasado,
        'Lucratividade de Estoque' : valor_estoque,
        'Lucratividade por Produto' : lucratividade,
        'Total a Receber' : fiado_a_receber + valor_estoque
    }

def Passivos():
    contas_a_pagar = 0
    dividas = 0
    for id_, venda in vendas.items():
        if venda['produto'] == 'Despesa' and venda['categoria'] == 'Fiado':
            contas_a_pagar += venda['preco']
        elif venda['produto'] == 'Investimento' and venda['categoria'] == 'Fiado':
            dividas += venda['preco']
    devendo = contas_a_pagar + dividas
    
    return {
        'Despesas a Pagar' : contas_a_pagar,
        'Investimento a Pagar' : dividas, 
        'Total de Dívidas': devendo
    }
    
def Patrimonio_Liquido():
    ativos = Ativos()
    passivos = Passivos()
    return (ativos['Total a Receber'] - passivos['Total de Dívidas'])