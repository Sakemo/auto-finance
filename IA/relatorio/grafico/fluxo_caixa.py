import matplotlib.pyplot as plt
from code.config.style.font import *

fontdict={'family' : FONT_NAME}

def Fluxo_Caixa_Graph(dados):
    # Extrair os rótulos e os valores dos dados do fluxo de caixa
    rotulos = ['Positivo', 'Negativo', 'Caixa']
    valores = [dados[2]['Fluxo Positivo'], dados[2]['Fluxo Negativo'], dados[2]['Fluxo de Caixa']]

    # Criar o gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(rotulos, valores, color=['green', 'red', 'blue'])
    plt.xlabel('Tipo de Fluxo', fontdict=fontdict)
    plt.ylabel('Valor', fontdict=fontdict)
    plt.title('Fluxo de Caixa', fontdict=fontdict)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Salvar o gráfico no diretório 'images/relatorios'
    plt.savefig('images/relatorios/fluxo_de_caixa.png')