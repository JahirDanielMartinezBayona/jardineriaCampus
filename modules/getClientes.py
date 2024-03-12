import storage.cliente as cli 
def getAllClientesName():
    clienteName = list()
    for valorCliente in cli.cliente:
        codigoName = dict({
        "codigo_cliente": valorCliente.get("codigo_cliente"),
        "nombre_cliente": valorCliente.get("nombre_cliente")
        })
        clienteName.append(codigoName)
    return clienteName
def getOneClientCodigo(codigo):
    for valorCliente in cli.cliente:
        if(valorCliente.get("codigo_cliente") == codigo):
            return{
        "codigo_cliente": valorCliente.get("codigo_cliente"),
        "nombre_cliente": valorCliente.get("cliente_cliente")   
            } 
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for valorCliente in cli.cliente:
        if(valorCliente.get("limite_credito") >= limiteCredit and valorCliente.get("ciudad") == ciudad):
            clienteCredic.append(valorCliente)
            return clienteCredic
def getAllClientPaisRegionCiudad(pais, region = None, ciudad = None):
    clientZone = list()
    for valorCliente in cli.cliente:
        if(
        valorCliente.get("pais")== pais and 
        (valorCliente.get("region") == region or valorCliente.get("region") == None) or
        (valorCliente.get("ciudad") == ciudad or valorCliente.get("ciudad") == None)
        ):
            clientZone.append(valorCliente)
    return clientZone
def getAllClientCodigoPostal():
    clientCodigoPostal= list()
    for valorCliente in cli.cliente:
        codigoPostal=dict({
        "codigo_cliente": valorCliente.get("codigo_cliente"),
        "nombre_cliente": valorCliente.get("nombre_cliente"),
        "codigo_postal": valorCliente.get("codigo_postal")
        })
        clientCodigoPostal.append(codigoPostal)
    return(clientCodigoPostal)
def getAllClientCiudad(ciudad):
    clientCity = list()
    for valorCliente in cli.cliente:
        if(
        (valorCliente.get("ciudad") == ciudad)
        ):
            clientCity.append(valorCliente)
    return clientCity
def getAllClientDireccion():
    clientDireccion=list()
    for valorCliente in cli.cliente:
        direccion=dict({
        "codigo_cliente": valorCliente.get("codigo_cliente"),
        "nombre_cliente": valorCliente.get("nombre_cliente"),
        "linea_direccion1": valorCliente.get("linea_direccion1")
        })
        clientDireccion.append(direccion)
    return(clientDireccion)
def getAllClientCreditEntre():
    clientCredit=list()
    for valorCliente in cli.cliente:
        if(valorCliente.get("limite_credito")>=5000 and valorCliente.get("limite_credito")<=10000):
            clientCredit.append(valorCliente)
    return clientCredit
def getAllClientTelefono():
    clientTelefono= list()
    for valorCliente in cli.cliente:
        telefono=dict({
        "codigo_cliente": valorCliente.get("codigo_cliente"),
        "nombre_cliente": valorCliente.get("nombre_cliente"),
        "telefono": valorCliente.get("telefono")
        })
        clientTelefono.append(telefono)
    return(clientTelefono)

def getAllClienteEspanioles():
    clienteEspaniolLista = list()
    for valorCliente in cli.cliente:
        if(valorCliente.get("pais") == "Spain"):
            clienteEspaniolObjeto = {
                "nombre_cliente": valorCliente.get('nombre_cliente')
            }
            clienteEspaniolLista.append(clienteEspaniolObjeto)
    return clienteEspaniolLista

def getAllClientesMadrid11O30():
    clientesMadridLista = list()
    for valorCliente in cli.cliente:
        if valorCliente.get("ciudad") == "Madrid" and (valorCliente.get("codigo_empleado_rep_ventas") == 11 or valorCliente.get("codigo_empleado_rep_ventas") == 30):
            clienteMadridObjeto = {
                "codigo_cliente": valorCliente.get("codigo_cliente"),
                "nombre_cliente": valorCliente.get("nombre_cliente"),
                "nombre_contacto": valorCliente.get("nombre_contacto"),
                "apellido_contacto": valorCliente.get("apellido_contacto"),
                "telefono": valorCliente.get("telefono"),
                "fax": valorCliente.get("fax"),
                "linea_direccion1": valorCliente.get("linea_direccion1"),
                "linea_direccion2": valorCliente.get("linea_direccion2"),
                "ciudad": valorCliente.get("ciudad"),
                "region": valorCliente.get("region"),
                "pais": valorCliente.get("pais"),
                "codigo_postal": valorCliente.get("codigo_postal"),
                "codigo_empleado_rep_ventas": valorCliente.get("codigo_empleado_rep_ventas"),
                "limite_credito": valorCliente.get("limite_credito")
            }
            clientesMadridLista.append(clienteMadridObjeto)
    return clientesMadridLista
# def menu():
#     print("""
#             Reportes de los clientes
#                 1. Obtener todos los clientes (código y nombre)
#                 2. Obtener un cliente por el código (código y nombre)
#                 3. Obtener toda la información de un cliente según su límite de crédito y ciudad que pertenece
        
#         """)
#     #opcion = int("\")
# menu()

def menu():
    print("""
    Menu de opciones de Cliente:
    1) Recibe el código y el nombre de todos los clientes
    2) Obtener información de un cliente por código
    3) Pedidos
    4) Pagos
            """)