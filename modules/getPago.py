import storage.pago as cli
def getAllCodigosPagosAño():
    CodigosAño = []
    codigos_vistos = set()
    for val in cli.pago:
        if "2008" in val.get("fecha_pago"):
            codigo_cliente = val.get("codigo_cliente")
            if codigo_cliente not in codigos_vistos:
                CodigosAño.append(
                    {
                        "codigo_cliente": val.get("codigo_cliente"),
                        "fecha": val.get("fecha_pago"),
                        "total": val.get("total")
                    }
                )
                codigos_vistos.add(codigo_cliente)
    return CodigosAño