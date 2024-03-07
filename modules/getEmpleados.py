import storage.empleado as cli

def getAllEmpleadosInformacion():
    empleadoObjecto = list()
    for val in cli.empleado:
        obtenerEmpleado = {
        "codigo_empleado": val.get("codigo_empleado"),
        "nombre": val.get("nombre"),
        "apellido1": val.get("apellido1"),
        "apellido2": val.get("apellido2"),
        "extension": val.get("extension"),
        "email": val.get("email"),
        "codigo_oficina": val.get("codigo_oficina"),
        "codigo_jefe": val.get("codigo_jefe"),
        "puesto": val.get("puesto")
        }
        empleadoObjecto.append(obtenerEmpleado)
    return empleadoObjecto

def getJefeEmpresaInformacion():
    empleadoObjeto = list()
    for val in cli.empleado:
        if val.get("codigo_jefe")==None:
            obtenerEmpleado = {
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellido1": val.get("apellido1"),
                "apellido2": val.get("apellido2"),
                "email": val.get("email")
            }
            empleadoObjeto.append(obtenerEmpleado)
    return empleadoObjeto

def getEmpleadosNoRepresantesVentasInformacion():
    empleadoObjeto = list()
    for val in cli.empleado:
        if val.get("puesto") != "Representante Ventas":
            obtenerEmpleado = {
                "nombre": val.get("nombre"),
                "apellido1": val.get("apellido1"),
                "apellido2": val.get("apellido2"),
                "puesto": val.get("puesto"),
            }
            empleadoObjeto.append(obtenerEmpleado)
    return empleadoObjeto
# def getEmpleadoEspanioles():
#     empleadoObjecto = list()
#     for val in cli.empleado:
#         obtenerEmpleado = {
#         "codigo_empleado": val.get("codigo_empleado"),
#         "nombre": val.get("nombre"),
#         "apellido1": val.get("apellido1"),
#         "apellido2": val.get("apellido2"),
#         "extension": val.get("extension"),
#         "email": val.get("email"),
#         "codigo_oficina": val.get("codigo_oficina"),
#         "codigo_jefe": val.get("codigo_jefe"),
#         "puesto": val.get("puesto")
#         }
#         empleadoObjecto.append(obtenerEmpleado)