import storage.empleado as cli

def getAllEmpleadosInformacion():
    clienteObjecto = list()
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
        clienteObjecto.append(obtenerEmpleado)
    return clienteObjecto
