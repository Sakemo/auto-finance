from code.other.formulas.Count.ContaSeData import CONT_SES, CONT
from code.other.formulas.Get_Time.Get_Today import GET_TODAY
from code.other.formulas.Get_Time.Get_Date import GET_DATE
from code.database.vendas.Database import vendas
from code.other.formulas.Soma.SomaSe import SOMA_SES
from code.other.formulas.Soma.SomaSeData import SOMA_SES_DATA
from datetime import datetime

database = []
def APPEND(titulo, dado):
    database.append({'titulo' : titulo,'data' : dado})
    return database

def Dashboard_Number(venda, resume):
    database.clear()
    
    venda_dia, venda_mes, venda_total = CONT(vendas)
    APPEND('Vendas do Dia', f'{venda_dia}')
    
    if resume == False:
        APPEND('Vendas do Mês', f'{venda_mes}')
        APPEND('Vendas no Ano', f'{venda_total}')
    
    return database
 
def Dashboard_Total(venda, resume):
    database.clear()
    data_obj = GET_TODAY()
    Total_Dia = SOMA_SES_DATA(
        vendas, (data_obj[0],data_obj[1], data_obj[2]), 'preco'
    )
    T_mes = SOMA_SES_DATA(
        vendas, (0,data_obj[1], data_obj[2]), 'preco'
    )
    T_ano = SOMA_SES_DATA(
        vendas, (0,0, data_obj[2]), 'preco'
    )
        
    APPEND('Total de Hoje', f'${round(float(Total_Dia),2)}')
    
    if resume == False:
        APPEND('Total do Mês', f'${round(float(T_mes))}')
        APPEND('Total do Ano', f'${round(float(T_ano))}')

    return database
 
def Dashboard_Lucro(venda, resume):
    database.clear()
    data_obj = GET_TODAY()
    
    new_vendas_dia = {}
    if GET_DATE(datetime.now(), (data_obj[0], data_obj[1], data_obj[2])) is not None:
        for id_, venda in vendas.items():
            data_venda = datetime.strptime(venda['data'], '%d/%m/%Y')
            if GET_DATE(data_venda, (data_obj[0], data_obj[1], data_obj[2])):
                new_vendas_dia[id_] = venda    
                
    Dinheiro_Dia = SOMA_SES(new_vendas_dia, 'preco', 'categoria', 'Dinheiro')
    PIX_dia = SOMA_SES(new_vendas_dia, 'preco', 'categoria', 'PIX')    
    cartao_dia = SOMA_SES(new_vendas_dia, 'preco', 'categoria', 'Cartão')    
    despesas_dia = SOMA_SES(new_vendas_dia, 'preco', 'produto', 'Despesa')
    investir_dia = SOMA_SES(new_vendas_dia, 'preco', 'produto', 'Investimento')
    
    lucro_dia = round(float(Dinheiro_Dia + PIX_dia + cartao_dia - (despesas_dia + investir_dia)),2)
    Apurado_dia = round(float(Dinheiro_Dia - despesas_dia), 2)
    
    APPEND('Rendimento', f'{lucro_dia}')
    APPEND('Capital de Giro', f'{Apurado_dia}')
    
    if resume == False:
        new_vendas_mes = {}
        if GET_DATE(datetime.now(), (data_obj[0], data_obj[1], data_obj[2])) is not None:
            for id_, venda in vendas.items():
                data_venda = datetime.strptime(venda['data'], '%d/%m/%Y')
                if GET_DATE(data_venda, (0, data_obj[1], data_obj[2])):
                    new_vendas_mes[id_] = venda    
                    
        Dinheiro_mes = SOMA_SES(new_vendas_mes, 'preco', 'categoria', 'Dinheiro')
        PIX_mes = SOMA_SES(new_vendas_mes, 'preco', 'categoria', 'PIX')    
        cartao_mes = SOMA_SES(new_vendas_mes, 'preco', 'categoria', 'Cartão')    
        despesas_mes = SOMA_SES(new_vendas_mes, 'preco', 'produto', 'Despesa')
        investir_mes = SOMA_SES(new_vendas_mes, 'preco', 'produto', 'Investimento')
        Fiado_dia = SOMA_SES(new_vendas_dia, 'preco', 'categoria', 'Fiado')
        Fiado_mes = SOMA_SES(new_vendas_mes, 'preco', 'categoria', 'Fiado')

        lucro_mes = round(float(Dinheiro_mes + PIX_mes + cartao_mes - (despesas_mes + investir_mes)),2)
        Apurado_mes = round(float(Dinheiro_mes - despesas_mes), 2)
        
        APPEND('Rendimento Mensal', f'{lucro_mes}')
        APPEND('Capital Acumulado Mensal', f'{Apurado_mes}')
        APPEND('Fiado do Dia', f'${Fiado_dia}')
        APPEND('Fiado do Mês', f'${Fiado_mes}')

    
    return database

def Database_Vendas(venda, resume = False):
    database.clear()
    data = venda['data']
    produto = venda['produto']
    preco = venda['preco']
    
    APPEND('Finalidade', produto)
    APPEND('Data da Transação', data)
    APPEND('Valor', f'${preco}')
    
    if resume == False:
        quantia = venda['quantia']
        categoria = venda['categoria']
        nome_cliente = venda['nome']
        if produto != 'Investimento':
            tipo_quantia = venda['tipo']
        
        APPEND('Meio de Pagamento', categoria)
        if produto != 'Pagamento' and produto != 'Despesa' and produto != 'Investimento':
            APPEND('Quantia', f'{quantia}/{tipo_quantia}')
        if nome_cliente != '':
            APPEND('Nome do Contribuente', nome_cliente)

    return database

def Database_Clients(cliente, resume=False):
    database.clear()
    nome = cliente['nome']
    fiado = cliente['fiado']
    APPEND('Nome', nome)
    APPEND('Total de Fiado', f'${fiado}')
    
    if resume == False:
        compras = cliente['compras']
        contato = cliente['contato']
        APPEND('Contato', contato)
        APPEND('Total de Compras', f'${compras}')

    data_compra = cliente['data_de_compra']
    continuar = cliente['continuar']
    return database

def Database_Produtos(produto, resume=False):
    database.clear()
    id_ = produto['id']
    nome = produto['nome']
    preco = produto['preco']
    vendas = produto['vendas'] 
    database.append({'id': id_})

    if nome != 'Pagamento' and nome != 'Despesa' and nome != 'Investimento':
        APPEND('Produto', nome)
        APPEND('Preço', f'R${preco}')
        APPEND('Vendas', f'{vendas}')
        if resume == False:
            cartegoria = produto['categoria']
            estoque = produto['estoque']
            custo = produto['custo']
            lucro = produto['lucro']
            APPEND('Cartegoria', cartegoria)
            APPEND('Quantidade em Estoque', estoque)
            APPEND('Investimento', custo)
            APPEND('Lucro', f'R${lucro}')
    return database