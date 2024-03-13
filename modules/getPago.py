import storage.pago as pa
import storage.cliente as cli
import storage.empleado as empl
def getAllCodigosPagosAnio():
    codigosAnio = []
    codigosMostrarSinRepetir = set()
    for valorPago in pa.pago:
        if "2008" in valorPago.get("fecha_pago"):
            codigoCliente = valorPago.get("codigo_cliente")
            if codigoCliente not in codigosMostrarSinRepetir:
                codigosAnio.append(
                    {
                        "codigo_cliente": valorPago.get("codigo_cliente"),
                        "fecha": valorPago.get("fecha_pago"),
                        "total": valorPago.get("total")
                    }
                )
                codigosMostrarSinRepetir.add(codigoCliente)
    return codigosAnio

def getAllPagosFecha():
    pagosFecha = []
    for valorPago in pa.pago:
        if("2008") in valorPago.get("fecha_pago") and valorPago.get("forma_pago") == ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": valorPago.get("codigo_cliente"),
                    "fecha_pago": valorPago.get("fecha_pago"),
                    "forma_pago": valorPago.get("forma_pago"),
                    "total": valorPago.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)
    return pagosFecha

def getAllFormasDePago():
    tipoPago = set()
    for valorPago in pa.pago:
        formaPago = valorPago.get("forma_pago")
        if formaPago not in tipoPago:
            tipoPago.add(formaPago)
    return tipoPago

def getAllClientesPagosNombreRepresentantesVentas():
    clientesPagosRepresentanteVentas = list()
    for valorPago in pa.pago:
        for valorCliente in cli.cliente:
            if valorPago.get("codigo_cliente") == valorCliente.get("codigo_cliente"):
                for valorEmpleado in empl.empleado:
                    if valorCliente.get("codigo_empleado_rep_ventas") == valorEmpleado.get("codigo_empleado"):
                        clientesPagosRepresentanteVentasObjeto = {
                            "nombre_cliente":valorCliente.get("nombre_cliente"),
                            "nombre_representante":valorEmpleado.get("nombre")
                        }
                        clientesPagosRepresentanteVentas.append(clientesPagosRepresentanteVentasObjeto)
    return clientesPagosRepresentanteVentas

def getAllClientesNoPagosNombreRepresentantesVentas():
    clientesPagosRepresentanteVentas = list()
    for valorPago in pa.pago:
        for valorCliente in cli.cliente:
            if valorPago.get("codigo_cliente") == valorCliente.get("codigo_cliente"):
                for valorEmpleado in empl.empleado:
                    if not(valorCliente.get("codigo_empleado_rep_ventas") == valorEmpleado.get("codigo_empleado")):
                        clientesPagosRepresentanteVentasObjeto = {
                            "nombre_cliente":valorCliente.get("nombre_cliente"),
                            "nombre_representante":valorEmpleado.get("nombre")
                        }
                        clientesPagosRepresentanteVentas.append(clientesPagosRepresentanteVentasObjeto)
    return clientesPagosRepresentanteVentas