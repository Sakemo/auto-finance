import matplotlib.pyplot as plt
import os

def Lucratividade_Produto_Graph(dados):
    lucratividade_por_produto = dados[1]['Ativos']['Lucratividade por Produto']
    produtos = [produto[0] for produto in lucratividade_por_produto]
    lucratividade = [produto[1] for produto in lucratividade_por_produto]
    plt.figure(figsize=(12, 6))
    plt.barh(produtos, lucratividade, color=['green' if lucro >= 0 else 'red' for lucro in lucratividade])
    plt.xlabel('Lucratividade')
    plt.title('Lucratividade por Produto')
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    output_dir = 'images/relatorios'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, 'lucratividade_por_produto.png'))
    plt.close()