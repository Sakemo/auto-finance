from code.database.clientes.Database import clientes
from code.database.produtos.Database import produtos
from code.database.vendas.Database import vendas

def Ticket_Medio():
    ticket_total = 0
    ticket_quantia = 0
    for id_, venda in vendas.items():
        if venda['produto'] != 'Despesa' and venda['produto'] != 'Investimento' and venda['produto'] != 'Pagamento':
            ticket_quantia += 1
            ticket_total += venda['preco']
    
    return (ticket_total/ticket_quantia)