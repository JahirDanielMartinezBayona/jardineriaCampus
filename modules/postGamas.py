import json
import requests
import os

def postGama():
    # json-server storage/gama_producto.json -b 5502
    gama = {
        "gama": input("Ingrese el nombre del gama: "),
        "descripcion_texto": input("Ingrese el descripcion en texto: "), 
        "descripcion_html": input("Ingrese el descripcion en html: "),
        "imagen": input("Ingrese la url de la imagen: ")
    }

    peticion = requests.post("http://10.0.2.15:5502", data=json.dumps(gama))
    res = peticion.json()
    res["Mensaje"] = "Gama Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              ______                     
  / ____/_  ______ __________/ /___ ______   / ____/___ _____ ___  ____ _
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / / __/ __ `/ __ `__ \/ __ `/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / /_/ / /_/ / / / / / / /_/ / 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/      \____/\__,_/_/ /_/ /_/\__,_/  
                                                                         
""")
        postGama()
        opcion = int(input("""
¿Deseas continuar guardando otro gama?
0. Regresar a la opción de gama
Presione cualquier otra número para seguir guardando gama...
"""))
        if(opcion == 0):
            break
        