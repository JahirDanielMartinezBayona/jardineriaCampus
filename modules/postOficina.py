import json
import requests
import os
def postOficina():
    # json-server storage/oficina.json -b 5503
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese el nombre de la ciudad: "),
        "pais": input("Ingrese el nombre del país: "),
        "region": input("Ingrese el nombre de la región: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "telefono": input("Ingrese el teléfono: "),
        "linea_direccion1": input("Ingrese la primera línea de dirección: "),
        "linea_direccion2": input("Ingrese la segunda línea de dirección: ")
    }
    peticion = requests.post("http://10.0.2.15:5503", data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              ____  _____      _            
  / ____/_  ______ __________/ /___ ______   / __ \/ __(_)____(_)___  ____ _
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / / / / /_/ / ___/ / __ \/ __ `/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / /_/ / __/ / /__/ / / / / /_/ / 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/      \____/_/ /_/\___/_/_/ /_/\__,_/  
                                                                            
""")
        postOficina()
        opcion = int(input("""
¿Deseas continuar guardando otro producto?
0. Regresar a la opción de Producto
Presione cualquier otra número para seguir guardando productos...
"""))
        if(opcion == 0):
            break