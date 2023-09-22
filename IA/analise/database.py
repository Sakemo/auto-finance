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
 