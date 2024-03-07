import modules.getClientes as clientes
import modules.getEmpleados as empleados
import modules.getPedido as pedido
from tabulate import tabulate

#print (tabulate(empleados.getJefeEmpresaInformacion()))
# print (tabulate(clientes.getAllClientTelefono()))
#print(clientes.getAllClientTelefono())
print(tabulate(pedido.getAllPedidoEstados()))