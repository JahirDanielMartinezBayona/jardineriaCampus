import json
import requests
import os
import modules.getGamas as gG

def postPedido():
    # json-server storage/pedido.json -b 5507
    pedido = {
        "codigo_pedido": int(input("Ingrese el código del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese el fecha del esperada: "),
        "fecha_entrega": input("Ingrese el fecha de entrega: "),
        "estado": input("Ingrese el estado: "),
        "comentario": input("Ingrese el comentario: "),
        "codigo_cliente": int(input("Ingrese el código del cliente: "))
    }
    
    peticion = requests.post("http://10.0.2.15:5507", data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              ____           ___     __          
  / ____/_  ______ __________/ /___ ______   / __ \___  ____/ (_)___/ /___  _____
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / /_/ / _ \/ __  / / __  / __ \/ ___/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/     /_/    \___/\__,_/_/\__,_/\____/____/  
                                                                                                                                                                                                                       
""")
        postPedido()
        opcion = int(input("""
¿Deseas continuar guardando otro pedido?
0. Regresar a la opción de Pedido
Presione cualquier otra número para seguir guardando pedido...
"""))
        if(opcion == 0):
            break