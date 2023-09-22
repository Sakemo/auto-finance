from datetime import datetime
from code.other.formulas.Get_Time.Get_Date import GET_DATE
from code.other.formulas.Get_Time.Get_Today import GET_TODAY

def CONT_SES(vendas, condicao, data):
    contador = 0
    for venda in vendas.values():
        data_venda = datetime.strptime(venda['data'], '%d/%m/%Y')
        if data == (0, 0, 0) or condicao(data_venda, data):
            if venda['produto'] != 'Despesa' and  venda['produto'] != 'Investimento' and venda['produto'] != 'Pagamento':
                contador += 1
    return contador

def CONT(vendas):
    data_obj = GET_TODAY()
    vendas_mes = CONT_SES(
        vendas,
        GET_DATE,
        (0,data_obj[1],data_obj[2])
    )
    vendas_dia = CONT_SES(
        vendas,
        GET_DATE,
        (data_obj[0], data_obj[1], data_obj[2])
    )
    vendas_total = CONT_SES(
        vendas,
        GET_DATE,
        (0,0,0)
    )
    return vendas_dia, vendas_mes, vendas_total