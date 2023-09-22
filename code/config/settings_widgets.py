import code.database.clientes.Database as dbClientes
import code.database.vendas.Database as dbVendas
import code.database.produtos.Database as dbProdutos
from code.components.Card.data.DATABASE import Database_Vendas, Database_Clients, Database_Produtos, Dashboard_Number, Dashboard_Total, Dashboard_Lucro

app_mode_to_db = {
    'clientes': (dbClientes.clientes, Database_Clients),
    'vendas': (dbVendas.vendas, Database_Vendas),
    'produtos': (dbProdutos.produtos, Database_Produtos),
    'clientes_exp': (dbClientes.clientes, Database_Clients),
    'vendas_exp': (dbVendas.vendas, Database_Vendas),
    'produtos_exp': (dbProdutos.produtos, Database_Produtos)
}