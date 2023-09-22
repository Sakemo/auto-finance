from datetime import datetime
from code.other.formulas.Get_Time.Get_Date import GET_DATE

def SOMA_SES_DATA(database, data_procurada, chave_soma, exception = ''):
    soma = 0
    if GET_DATE(datetime.now(), data_procurada) is not None:
        for data in database.values():
            data_venda = datetime.strptime(data['data'], '%d/%m/%Y')
            if GET_DATE(data_venda, data_procurada):
                if data['produto'] != 'Despesa' and  data['produto'] != 'Investimento' and data['produto'] != exception:
                    soma += data[chave_soma]
                else:
                    continue
    else:
        for data in database.values():
            if data['produto'] != 'Despesa' and  data['produto'] != 'Investimento' and data['produto'] != exception:
                soma += data[chave_soma]
    return soma