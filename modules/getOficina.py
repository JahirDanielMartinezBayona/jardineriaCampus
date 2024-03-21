import requests
import os
from tabulate import tabulate

def getAllData():
    #json-server storage/oficina.json -b 5503
    peticion = requests.get("http://10.0.2.15:5503")
    data = peticion.json()
    return data

def menu():
    while True:
        os.system("clear")
        print("""
    ____                        __                   __        ____  _____      _            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
          /_/                                                                                
            1. Ver toda la información de oficinas
            0. Regresar al menu de oficina
    """)
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllData(), headers="keys", tablefmt="github"))                         
        elif(opcion == 0):
            break
        input("Seleccione una tecla para continuar......")