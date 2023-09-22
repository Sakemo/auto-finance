import matplotlib.pyplot as plt

def Patrimonio_Graph(dados):
    # Extrair os valores de "Total a Receber" e "Total de Dívidas"
    total_a_receber = 0.0
    total_de_dividas = 0.0

    for item in dados:
        if isinstance(item, dict) and 'Ativos' in item and 'Passivos' in item:
            total_a_receber = item['Ativos']['Total a Receber']
            total_de_dividas = item['Passivos']['Total de Dívidas']

    # Cores personalizadas para as fatias do gráfico
    cores = ['#2216B2', '#B21616']

    # Explodir a fatia "Total a Receber" para enfatizá-la
    explode = (0, 0)

    # Criar o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie([total_a_receber, total_de_dividas], labels=['Ativo', 'Passivo'], autopct='%1.1f%%',
           startangle=90, colors=cores, explode=explode)


    # Salvar a imagem no diretório 'images/relatorios'
    plt.savefig('images/relatorios/patrimonio.png', bbox_inches='tight', dpi=300)