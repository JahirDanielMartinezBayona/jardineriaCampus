import json
import requests

def postProducto(producto):
    peticion = requests.post("http://192.168.246.128:5501", data=json.dumps(producto))
    res = peticion.json()
    return res