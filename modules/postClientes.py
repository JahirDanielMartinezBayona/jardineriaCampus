import json
import requests
import os
import modules.getGamas as gG

def postCliente():
    # json-server storage/cliente.json -b 5501
    cliente = {
        "codigo_cliente":int(input("Ingrese el código del cliente: ")),
        "nombre_cliente":input("Ingrese el nombre del cliente: "),
        "nombre_contacto":input("Ingrese el nombre del contacto: "),
        "apellido_contacto":input("Ingrese el apellido del contacto: "),
        "telefono":input("Ingrese "),
        "fax":input("Ingrese el fax"),
        "linea_direccion1":input("Ingrese la línea de dirección 1:"),
        "linea_direccion2":input("Ingrese la línea de dirección 2:"),
        "ciudad":input("Ingrese el nombre de la ciudad: "),
        "region":input("Ingrese el nombre de la región: "),
        "pais":input("Ingrese el nombre del país: "),
        "codigo_postal":input("Ingrese el código postal: "),
        "codigo_empleado_rep_ventas":int(input("Ingrese el código de empleado en representante de ventas: ")),
        "limite_credito":float(input("Ingrese el límite de crédito: "))
    }

    
    
    peticion = requests.post("http://10.0.2.15:5505", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def asistenteConsultas():
    while True:
        os.system("clear")
        print("""
   ______                     __              _________            __           
  / ____/_  ______ __________/ /___ ______   / ____/ (_)__  ____  / /____  _____
 / / __/ / / / __ `/ ___/ __  / __ `/ ___/  / /   / / / _ \/ __ \/ __/ _ \/ ___/
/ /_/ / /_/ / /_/ / /  / /_/ / /_/ / /     / /___/ / /  __/ / / / /_/  __(__  ) 
\____/\__,_/\__,_/_/   \__,_/\__,_/_/      \____/_/_/\___/_/ /_/\__/\___/____/  
                                                                                 
""")
        postCliente()
        opcion = int(input("""
¿Deseas continuar guardando otro cliente?
0. Regresar a la opción de Cliente
Presione cualquier otra número para seguir guardando clientes...
"""))
        if(opcion == 0):
            break