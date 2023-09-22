from IA.analise.friendly import analise_basic
from IA.relatorio.main import Relatorio_Financeiro
from code.components.ANALISE import Analise_Window

def Analise():
    relatorio = Relatorio_Financeiro()
    analise = analise_basic(relatorio)
    Analise_Window(relatorio)
    return analise