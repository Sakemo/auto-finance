def analise_basic(relatorio):
    resultado = []
    
    for item in relatorio:
        if isinstance(item, dict):
            for chave, valor in item.items():
                if isinstance(valor, (int, float)):
                    resultado.append(f"{chave}: R${valor:.2f}")
                elif isinstance(valor, list):
                    resultado.append(f"{chave}:")
                    for subitem in valor:
                        if isinstance(subitem, dict):
                            for subchave, subvalor in subitem.items():
                                resultado.append(f"  {subchave}: R${subvalor:.2f}")
                        elif isinstance(subitem, tuple):
                            produto, *dados = subitem 
                            resultado.append(f"  Produto: {produto}")
                            for i, subvalor in enumerate(dados):
                                if i == 0:
                                    resultado.append(f"    Estoque: {subvalor}")
                                elif i == 1:
                                    resultado.append(f"    Diferença Lucro-Estoque: {subvalor}")
                elif isinstance(valor, dict):
                    resultado.append(f"{chave}:")
                    for subchave, subvalor in valor.items():
                        if isinstance(subvalor, (int, float)):
                            resultado.append(f"  {subchave}: R${subvalor:.2f}")
                        elif isinstance(subvalor, list):
                            resultado.append(f"  {subchave}:")
                            for subsubitem in subvalor:
                                if isinstance(subsubitem, tuple):
                                    produto, *dados = subsubitem 
                                    resultado.append(f"    Produto: {produto}")
                                    for i, subsubvalor in enumerate(dados):
                                        if i == 0:
                                            resultado.append(f"      Estoque: {subsubvalor}")
                                        elif i == 1:
                                            resultado.append(f"      Diferença Lucro-Estoque: {subsubvalor}")
                else:
                    resultado.append(f"{chave}: {valor:.2f}")
        else:
            resultado.append(f"Outro valor: {item:.2f}")
    
    return '\n'.join(resultado)