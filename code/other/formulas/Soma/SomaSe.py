from code.other.formulas.Get_Time.Get_Date import GET_DATE
from code.other.formulas.Soma.SomaSeData import SOMA_SES_DATA

def SOMA_SES(database, chave_soma, chave_verificar, valor_verificar):
    total = 0
    if isinstance(database, list):
        if chave_verificar == 'data':
            return SOMA_SES_DATA(database, GET_DATE, valor_verificar, chave_soma)
        for item in database:
            if item[str(chave_verificar)] == str(valor_verificar):
                total += float(item[str(chave_soma)])
    elif isinstance(database, dict):
        for item in database.values():
            if item[str(chave_verificar)] == str(valor_verificar):
                total += float(item[str(chave_soma)])
    else:
        print('ERRO. OS DADOS DEVEM SER UMA LISTA OU DICIONARIO.')

    return total