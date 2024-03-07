import modules.getClientes as clientes
import modules.getEmpleados as empleados
import modules.getPedido as pedido
import modules.getPago as pago
from tabulate import tabulate

#print (tabulate(empleados.getJefeEmpresaInformacion()))
# print (tabulate(clientes.getAllClientTelefono()))
#print(clientes.getAllClientTelefono())
print(tabulate(pago.getAllCodigosPagosAnio()))