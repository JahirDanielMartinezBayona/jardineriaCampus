import storage.pedido as cli
from datetime import datetime

def getAllPedidoEstados():
    pedidoLista = set()
    for valorPedido in cli.pedido:
        estado = valorPedido.get("estado")
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

def getAllPedidosRechazados():
    pedidosRechazados = []
    for valorPedido in cli.pedido:
        if("2009") in valorPedido.get("fecha_pedido") and valorPedido.get("estado") is ("Rechazado"):
            pedidosRechazados.append({
                    "codigo_pedido": valorPedido.get("codigo_pedido"),
                    "codigo_de_cliente": valorPedido.get("codigo_cliente"),
                    "fecha_pedido": valorPedido.get("fecha_pedido"),
                    "estado_pedido": valorPedido.get("estado")
                })
    return pedidosRechazados