import os
import requests
from tabulate import tabulate

def getAllData():
    #json-server storage/empleado.json -b 5504
    peticion = requests.get("http://10.0.2.15:5504")
    data = peticion.json()
    return data
def getAllEmpleadosInformacion():
    empleadoObjecto = list()
    for val in getAllData():
        obtenerEmpleado = {
        "codigo_empleado": val.get("codigo_empleado"),
        "nombre": val.get("nombre"),
        "apellido1": val.get("apellido1"),
        "apellido2": val.get("apellido2"),
        "extension": val.get("extension"),
        "email": val.get("email"),
        "codigo_oficina": val.get("codigo_oficina"),
        "codigo_jefe": val.get("codigo_jefe"),
        "puesto": val.get("puesto")
        }
        empleadoObjecto.append(obtenerEmpleado)
    return empleadoObjecto

def getJefeEmpresaInformacion():
    empleadoObjeto = list()
    for val in getAllData():
        if val.get("codigo_jefe")==None:
            obtenerEmpleado = {
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellido1": val.get("apellido1"),
                "apellido2": val.get("apellido2"),
                "email": val.get("email")
            }
            empleadoObjeto.append(obtenerEmpleado)
    return empleadoObjeto

def getEmpleadosNoRepresantesVentasInformacion():
    empleadoObjeto = list()
    for val in getAllData():
        if val.get("puesto") != "Representante Ventas":
            obtenerEmpleado = {
                "nombre": val.get("nombre"),
                "apellido1": val.get("apellido1"),
                "apellido2": val.get("apellido2"),
                "puesto": val.get("puesto"),
            }
            empleadoObjeto.append(obtenerEmpleado)
    return empleadoObjeto
# def getEmpleadoEspanioles():
#     empleadoObjecto = list()
#     for val in getAllData():
#         obtenerEmpleado = {
#         "codigo_empleado": val.get("codigo_empleado"),
#         "nombre": val.get("nombre"),
#         "apellido1": val.get("apellido1"),
#         "apellido2": val.get("apellido2"),
#         "extension": val.get("extension"),
#         "email": val.get("email"),
#         "codigo_oficina": val.get("codigo_oficina"),
#         "codigo_jefe": val.get("codigo_jefe"),
#         "puesto": val.get("puesto")
#         }
#         empleadoObjecto.append(obtenerEmpleado)
def menu():
    while True:
        os.system("clear")
        print("""
    ____                        __              __                             __               __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                       /_/                                     
            1. Ver la información de todos los empleados
            2. Ver el listado con el nombre, apellido y puesto de aquellos empleados que no sean representantes de ventas.
            3. Ver el nombre del puesto, nombre, apellidos y email del jefe de la empresa.
            0. Regresar al menu de empleados
              """)
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllEmpleadosInformacion(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            print(tabulate(getEmpleadosNoRepresantesVentasInformacion(), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            print(tabulate(getJefeEmpresaInformacion(), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break
        input("Seleccione una tecla para continuar......")