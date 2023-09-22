cache_before_search = []

def search(var, data_container, function, parent, app_mode, geometry, destroy):
    data = data_container
    cache_before_search.append(data.copy())
    
    if var == '' or var is None:
        data.clear()
        data.update(cache_before_search[0]) 
        function(parent, app_mode, geometry, destroy)
        return
    
    filtered_data = {}
    
    for product_name, product_info in data.items():
        found = False
        for key, value in product_info.items():
            if str(var) in str(value):
                found = True
                break
        if found:
            filtered_data[product_name] = product_info
    
    data.clear()
    data.update(filtered_data)
    
    function(parent, app_mode, geometry, destroy)

def filter_dict(var, data_container, function, parent, app_mode, geometry, destroy):
    data = data_container
    
    if var == 'A-Z':
        if 'vendas' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['produto']))
        else:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['nome']))
    elif var == 'Novo':
        if 'vendas' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['data'], reverse=True))
        elif 'produtos' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['id'], reverse=True))
        else:
            data_ordenado = dict(sorted(data.items(), reverse=True))
    elif var == 'Mais Antigo':
        if 'vendas' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['data']))
        elif 'produtos' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['id']))
        else:
            data_ordenado = dict(sorted(data.items()))
    elif var == 'Maior Valor':
        if 'clientes' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['fiado'], reverse=True))
        else:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['preco'], reverse=True))
    elif var == 'Menor Valor':
        if 'clientes' in app_mode:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['fiado']))
        else:
            data_ordenado = dict(sorted(data.items(), key=lambda x: x[1]['preco']))
            
            
    data.clear()
    data.update(data_ordenado)
    function(parent, app_mode, geometry, destroy)            