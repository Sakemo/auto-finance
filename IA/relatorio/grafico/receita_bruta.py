import os
import ast
import matplotlib.pyplot as plt
from collections import defaultdict

def Receita_Bruta_Graph():
    diretorio = 'relatorios/'
    medias_por_mes = defaultdict(lambda: {'Receita Total': 0, 'Lucro Liquido': 0, 'Lucro Bruto': 0})
    contagem_por_mes = defaultdict(int)
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            with open(os.path.join(diretorio, arquivo), 'r') as f:
                conteudo = f.read()
                data = ast.literal_eval(conteudo)
                receita_total = data[0]['Receita Total']
                lucro_liquido = data[0]['Lucro Liquido']
                lucro_bruto = data[0]['Lucro Bruto']
                partes = arquivo.split('.')[0].split('-')
                mes_ano = f'{partes[1]}-{partes[2]}'
                medias_por_mes[mes_ano]['Receita Total'] += receita_total
                medias_por_mes[mes_ano]['Lucro Liquido'] += lucro_liquido
                medias_por_mes[mes_ano]['Lucro Bruto'] += lucro_bruto
                contagem_por_mes[mes_ano] += 1
    for mes_ano in medias_por_mes:
        num_arquivos = contagem_por_mes[mes_ano]
        medias_por_mes[mes_ano]['Receita Total'] /= num_arquivos
        medias_por_mes[mes_ano]['Lucro Liquido'] /= num_arquivos
        medias_por_mes[mes_ano]['Lucro Bruto'] /= num_arquivos
    meses = list(medias_por_mes.keys())
    media_receita_total = [valores['Receita Total'] for valores in medias_por_mes.values()]
    media_lucro_liquido = [valores['Lucro Liquido'] for valores in medias_por_mes.values()]
    media_lucro_bruto = [valores['Lucro Bruto'] for valores in medias_por_mes.values()]
    plt.figure(figsize=(12, 6))
    plt.plot(meses, media_receita_total, marker='o', label='Média Receita Total', color='blue')
    plt.plot(meses, media_lucro_liquido, marker='o', label='Média Lucro Liquido', color='green')
    plt.plot(meses, media_lucro_bruto, marker='o', label='Média Lucro Bruto', color='yellow')
    plt.xlabel('Mês e Ano')
    plt.ylabel('Valor Médio')
    plt.title('Média Mensal de Receita Total, Lucro Líquido e Lucro Bruto')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Salvar a imagem no diretório 'images/relatorios' com um nome específico
    nome_arquivo = 'media_receita_lucro.png'
    caminho_arquivo = os.path.join('images', 'relatorios', nome_arquivo)
    plt.savefig(caminho_arquivo)
    plt.close()