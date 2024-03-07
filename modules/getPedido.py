import storage.pedido as cli

def getAllPedidoEstados():
    pedidoLista = set()
    for val in cli.pedido:
        estado = val.get("estado")
        pedidoLista.add(estado)
    return pedidoLista
