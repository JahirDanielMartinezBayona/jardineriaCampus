import json
import requests
import os
import modules.getGamas as gG

def postEmpleado():
    # json-server storage/empleado.json -b 5504
    empleado = {
        "codigo_empleado":int(input("Ingrese el código del empleado: ")),
        "nombre":input("Ingrese el nombre: "),
        "apellido1":input("Ingrese el apellido 1: "),
        "apellido2":input("Ingrese el apellido 2: "),
        "extension":input("Ingrese la extensión: "),
        "email":input("Ingrese el email: "),
        "codigo_oficina":input("Ingrese el código de oficina: "),
        "codigo_jefe":int(input("Ingrese el código del jefe: ")),
        "puesto":input("Ingrese el puesto: ")
    }
    
    peticion = requests.post("http://10.0.2.15:5504", data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              ______                __               __          
  / ____/_  ______ __________/ /___ ______   / ____/___ ___  ____  / /__  ____ _____/ /___  _____
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/     /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                         /_/                                                                                                                                                                         
""")
        postEmpleado()
        opcion = int(input("""
¿Deseas continuar guardando otro empleado?
0. Regresar a la opción de Empleado
Presione cualquier otra número para seguir guardando empleado...
"""))
        if(opcion == 0):
            break