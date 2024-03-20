import json
import requests
import modules.getGamas as gG

def postProducto():
    # json-server storage/producto.json -b 5501
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrese la dimensiones del producto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrese el cantidad en stock: ")),
        "precio_venta": int(input("Ingrese el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
    
    peticion = requests.post("http://10.0.2.15:5501", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def asistenteConsultas():
    while True:
        print("""
   ______                     __              ____                 __           __           ______                _                      
  / ____/_  ______ __________/ /___ ______   / __ \_________  ____/ /_  _______/ /_____     / ____/___  ____ ___  (_)__  ____  ____ ____ _
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \   / /   / __ \/ __ `__ \/ / _ \/ __ \/_  // __ `/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ /  / /___/ /_/ / / / / / / /  __/ / / / / // /_/ / 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/     /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/   \____/\____/_/ /_/ /_/_/\___/_/ /_/ /___|__,_/  
                                                                                                                                          
""")
        postProducto()
        