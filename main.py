import modules.getClientes as clientes
from tabulate import tabulate
print (tabulate(clientes.getAllClienteEspanioles()))
# print (tabulate(clientes.getAllClientTelefono()))
# print(clientes.getAllClientTelefono())