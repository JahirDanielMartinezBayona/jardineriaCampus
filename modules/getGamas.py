#import json
import requests
from tabulate import tabulate

def getAllGama():
    # json-server storage/gama_producto.json -b 5502
    peticion = requests.get("http://192.168.246.128:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre

def menuImprimirAllNombre():
    print(tabulate(getAllNombre(), headers="keys", tablefmt="github"))

