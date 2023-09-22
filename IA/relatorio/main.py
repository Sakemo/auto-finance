from code.database.clientes.Database import clientes
from code.database.produtos.Database import produtos
from code.database.vendas.Database import vendas

from code.components.RELATORIO import Relatorio_Window

import IA.relatorio.balanco as BalançoPatrimonial
import IA.relatorio.caixa as FluxoDeCaixa
import IA.relatorio.resultados as DemonstrarResultado
import IA.relatorio.ticket as Ticket
from IA.relatorio.grafico.fluxo_caixa import *
from IA.relatorio.grafico.lucratividade_produto import *
from IA.relatorio.grafico.lucro_real import *
from IA.relatorio.grafico.patrimonio import *
from IA.relatorio.grafico.receita_bruta import *

from datetime import datetime

def Relatorio_Financeiro():
    # Demonstração de Resultados do Relatorio
    receita_total = DemonstrarResultado.Receita_Total()
    despesas_operacionais, despesas_dispensavel, depesas_totais = DemonstrarResultado.Despesas_Operacionais()
    lucro_bruto = DemonstrarResultado.Lucro_Bruto()
    lucro_liquido, despesas_operacionais = DemonstrarResultado.Lucro_Liquido()
    pessoas_atendidas = DemonstrarResultado.Pessoas_Atendidas()
    Demonstracao_Resultado = {
        'Receita Total' : receita_total,
        'Custos Totais' : depesas_totais,
        'Despesas Operacionais' : despesas_operacionais,
        'Outros Gastos' : despesas_dispensavel,
        'Lucro Bruto' : lucro_bruto,
        'Lucro Liquido' : lucro_liquido,
        'Pessoas Atendidas' : pessoas_atendidas
    }
    
    # Balanço Patrimonial do Relatorio
    ativos = BalançoPatrimonial.Ativos()
    passivos = BalançoPatrimonial.Passivos()
    patrimonio = BalançoPatrimonial.Patrimonio_Liquido()
    Balanço_Patrimonial = {
        'Ativos' : ativos,
        'Passivos' : passivos,
        'Patrimônio Liquido' : patrimonio
    }
    
    # Fluxo de Caixa do Relatorio
    fluxo = FluxoDeCaixa.Fluxo_Caixa_Operacional()
    Fluxo_de_Caixa = {
        'Fluxo de Caixa' : fluxo[3],
        'Fluxo Positivo' : fluxo[0],
        'Fluxo Negativo' : fluxo[1],
        'Fluxo Investido' : fluxo[2]
    }
    
    # Ticket Medio
    ticket_medio = Ticket.Ticket_Medio()

    # Tranformar em Relatorio Amigavel
    content = [Demonstracao_Resultado, Balanço_Patrimonial, Fluxo_de_Caixa, {'Ticket Médio' : ticket_medio}]
    data_atual = datetime.now()
    data_formatada = str(data_atual.strftime("%d-%m-%Y"))
    with open(f'relatorios/{data_formatada}.txt', 'w', encoding= 'utf-8') as file:
        file.write(f'{content}')
    Fluxo_Caixa_Graph(content)
    Lucratividade_Produto_Graph(content)
    Lucro_Real_Graph(content)
    Patrimonio_Graph(content)
    Receita_Bruta_Graph()
    
    Relatorio_Window()
    return content