import modules.getClientes as clientes
import modules.getEmpleados as empleados
import modules.getPedido as pedido
import modules.getPago as pago
from tabulate import tabulate

print (tabulate(pago.getAllClientesPagosNombreRepresentantesVentas(),headers="keys", tablefmt="github"))