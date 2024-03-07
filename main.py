import modules.getClientes as clientes
import modules.getEmpleados as empleados
from tabulate import tabulate

#print (tabulate(empleados.getJefeEmpresaInformacion()))
# print (tabulate(clientes.getAllClientTelefono()))
#print(clientes.getAllClientTelefono())
print(tabulate(empleados.getEmpleadosNoRepresantesVentasInformacion()))