# Abre um arquivo em modo de escrita (modo 'w')
with open('arquivo.txt', 'w') as arquivo:
    # Escreve no arquivo
    arquivo.write('Este é um exemplo de escrita em um arquivo de texto.\n')
    arquivo.write('Você pode adicionar mais linhas conforme necessário.\n')

# O arquivo é automaticamente fechado quando saímos do bloco 'with'

# Agora, você pode ler o conteúdo do arquivo se desejar
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
