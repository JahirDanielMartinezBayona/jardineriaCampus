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
        if("2009") in valorPedido.get("fecha_pedido") and valorPedido.get("estado") == ("Rechazado"):
            pedidosRechazados.append({
                    "codigo_pedido": valorPedido.get("codigo_pedido"),
                    "codigo_de_cliente": valorPedido.get("codigo_cliente"),
                    "fecha_pedido": valorPedido.get("fecha_pedido"),
                    "estado_pedido": valorPedido.get("estado")
                })
    return pedidosRechazados

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for valorPedido in cli.pedido:
        if valorPedido.get("estado") == "Entregado" and valorPedido.get("fecha_entrega") is None:
           valorPedido["fecha_entrega"] = valorPedido.get("fecha_esperada")
        if valorPedido.get("estado") == "Entregado":
            date_1 = "/".join(valorPedido.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(valorPedido.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidosEntregado.append({
                    "codigo_de_pedido": valorPedido.get("codigo_pedido"),
                    "codigo_de_cliente": valorPedido.get("codigo_cliente"),
                    "fecha_de_esperada": valorPedido.get("fecha_esperada"),
                    "fecha_de_entrega": valorPedido.get("fecha_entrega")
                })
    return pedidosEntregado

def getAllEnEnero():
    pedidosEnero= []
    for valorPedido in cli.pedido:
        fecha_entrega = valorPedido.get ("fecha_entrega")
        if fecha_entrega:
            date_1= "/".join(valorPedido.get("fecha_entrega").split("-")[::-1])
            start= datetime.strptime(date_1,"%d/%m/%Y")
            if start.month == 1 and valorPedido.get("estado")=="Entregado":
                pedidosEnero.append({
                    "codigo_pedido": valorPedido.get("codigo_pedido"),
                    "codigo_de_cliente": valorPedido.get("codigo_cliente"),
                    "fecha_de_entrega": valorPedido.get("fecha_entrega"),
                    "estado_pedido": valorPedido.get("estado")
                })
    return pedidosEnero