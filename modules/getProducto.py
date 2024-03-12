import storage.producto as prod

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio.

def getAllStocksPriceGama(gama,stock):
    condiciones = []
    for val in prod.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)
    def precio(val):
        return val.get("precio_venta")
    condiciones.sort(key=precio)
    for i,val in enumerate(condiciones):
        
        if(val.get("gama")=="Ornamentales"):
            return val.get("precio_venta")
    filtro = prod.producto.sort(key=precio)
    return filtro
        