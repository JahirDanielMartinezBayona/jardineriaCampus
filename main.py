import modules.getClient as clientes
from tabulate import tabulate
print(tabulate(clientes.getAllClientPaisRegionCiudad("USA")))