import json
import requests
import os
import modules.getGamas as gG

def postPago():
    # json-server storage/pago.json -b 5506
    pago = {
    "codigo_cliente":int(input("Ingrese el código del cliente: ")),
    "forma_pago":input("Ingrese la forma de pago: "),
    "id_transaccion":input("Ingrese el id de la transacción: "),
    "fecha_pago":input("Ingrese la fecha de pago: "),
    "total":int(input("Ingrese el total: "))
}
    
    peticion = requests.post("http://10.0.2.15:5506", data=json.dumps(pago))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              ____                        
  / ____/_  ______ __________/ /___ ______   / __ \____ _____ _____  _____
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / /_/ / __ `/ __ `/ __ \/ ___/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / ____/ /_/ / /_/ / /_/ (__  ) 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/     /_/    \__,_/\__, /\____/____/  
                                                      /____/              
""")
        postPago()
        opcion = int(input("""
¿Deseas continuar guardando otro pago?
0. Regresar a la opción de Pago
Presione cualquier otra número para seguir guardando pago...
"""))
        if(opcion == 0):
            break