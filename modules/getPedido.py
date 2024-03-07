import storage.pedido as cli
from datetime import datetime

def getAllPedidoEstados():
    pedidoLista = set()
    for val in cli.pedido:
        estado = val.get("estado")
        pedidoLista.add(estado)
    return pedidoLista

def getAllPedidosEntregadosFueraTiempo():
    pedidosEntregado= []
    for valorPedido in cli.pedido:
        if valorPedido.get("estado") == "Entregado" and valorPedido.get("fecha_entrega") is None:
            valorPedido["fecha_entrega"] = valorPedido.get("fecha_esperada")
        if valorPedido.get("estado") == "Entregado":
            fechaNumero1= "/".join(valorPedido.get("fecha_entrega").split("-")[::-1])
            fechaNumero2= "/".join(valorPedido.get("fecha_esperada").split("-")[::-1])
            star= datetime.strptime(fechaNumero1,"%d/%m/%Y" )
            end= datetime.strptime(fechaNumero2,"%d/%m/%Y")
            diff= end.date( ) - star.date()
            if(diff.days < 0):
                pedidosEntregado.append({ 
                "codigoPedido": valorPedido.get("codigo_pedido"),
                "codigoCliente": valorPedido.get ("codigo_cliente"),
                "fechaEsperada": valorPedido.get("fecha_esperada"),
                "fechaEntrega": valorPedido.get("fecha_entrega")
            })
    return pedidosEntregado