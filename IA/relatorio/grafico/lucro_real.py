import matplotlib.pyplot as plt

def Lucro_Real_Graph(dados):
    # Extrair os valores relevantes
    receita_total = dados[0]['Receita Total']
    custos_totais = dados[0]['Custos Totais']
    lucro_bruto = dados[0]['Lucro Bruto']
    lucro_liquido = dados[0]['Lucro Liquido']

    # Nomes das categorias
    categorias = ['Receita Total', 'Custos Totais', 'Lucro Bruto', 'Lucro Líquido']

    # Valores correspondentes
    valores = [receita_total, custos_totais, lucro_bruto, lucro_liquido]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, valores, color=['blue', 'red', 'green', 'purple'])
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    plt.title('Lucro Real')

    # Salvar a imagem no diretório 'images/relatorios'
    plt.savefig('images/relatorios/lucro_real.png')