import modules.getClientes as clientes
import modules.getEmpleados as empleados
import modules.getPedido as pedido
import modules.getPago as pago
import os
import time
import modules.getOficina as readOficina
import modules.getProducto as readProducto
import modules.updateProducto as updateProducto
import modules.deleteProducto as deleteProducto
from tabulate import tabulate
import modules.postProducto as createProducto
import modules.postGama as createGama
import modules.postOficina as createOficina
import modules.getGamas as readGamas

#print (tabulate(prod.defAllData(),headers="keys", tablefmt="github"))
if(__name__ == "__main__"):
    def menuPrincipal():
        while True:
            os.system("clear")
            print("""
                             ___      _            _             _ 
  /\/\   ___ _ __  _   _    / _ \_ __(_)_ __   ___(_)_ __   __ _| |
 /    \ / _ \ '_ \| | | |  / /_)/ '__| | '_ \ / __| | '_ \ / _` | |
/ /\/\ \  __/ | | | |_| | / ___/| |  | | | | | (__| | |_) | (_| | |
\/    \/\___|_| |_|\__,_| \/    |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                    |_|            
1. Cliente
2. Empleado
3. Pago
4. Pedido
5. Producto
0. Salir
        """)
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                clientes.menu()
            elif(opcion == 2):
                menuEmpleados()
            elif(opcion == 3):
                pago.menu()
            elif(opcion == 4):
                pedido.menu()
            elif(opcion == 5):
                menuProducto()
            elif(opcion == 0):
                break

def menuEmpleados():
    while True:
        os.system("clear")
        print("""
    ____                        __                   __                             __               __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                            /_/                                             
        1. Ver información de todas las oficinas
        2. Guardar Oficina
        3. Guardar Empleado
        4. Actualizar Oficina
        5. Actualizar Emplado      
        6. Eliminar empleado
        7. Eliminar empleado
        0. Regresar al menu principal
""")
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            readOficina.menu()
        elif(opcion == 2):
            createOficina.asistenteConsultas()
        elif(opcion == 3):
            createProducto.asistenteConsultas()
        elif(opcion == 4):
            createGama.asistenteConsultas()
        elif(opcion == 5):
            updateProducto.menu()
        elif(opcion == 6):
            deleteProducto.menu()
        elif(opcion == 0):
            break
        input("Seleccione una tecla para continuar......")

def menuProducto():
    while True:
        os.system("clear")
        print("""

                                      __                             __           __            
   ____ ___  ___  ____  __  __   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                           /_/                                                  

        1. Reportes de los productos
        2. Reporte del nombre de la gama
        3. Guardar producto
        4. Guardar gama
        5. Actualizar
        6. Eliminar productos
        0. Regresar al menu principal
        """)
        # print("""
        #       1. Reportes de los productos
        #       2. Guardar 
        #       3. Actualizar
        #       4. Eliminar productos
        #       0. Regresar al menu principal
        # """)
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            readProducto.menu()
        elif(opcion == 2):
            readGamas.menuImprimirAllNombre()
        elif(opcion == 3):
            createProducto.asistenteConsultas()
        elif(opcion == 4):
            createGama.asistenteConsultas()
        elif(opcion == 5):
            updateProducto.menu()
        elif(opcion == 6):
            deleteProducto.menu()
        elif(opcion == 0):
            break
        input("Seleccione una tecla para continuar......")



menuPrincipal()
# def exeProd():
#     producto = {
#     "codigo_producto":input("Ingrese el codigo_producto: "),
#     "nombre":  input("Ingrese el nombre: "),
#     "gama":  gG.getAllNombre()[int(input("Seleccione la gama{{}}"\t\n".join([f"{i}. {val}" for i, val in enumerate(gG.getAllNombre())])))],
#     "dimensiones":  input("Ingrese las dimensiones: "),
#     "proveedor":  input("Ingrese el proveedor: "),
#     "descripcion":  input("Ingrese la descripcion: "),
#     "cantidad_en_stock":  int(input("Ingrese la cantidad_en_stock: ")),
#     "precio_venta":  int(input("Ingrese el precio_venta: ")),
#     "precio_proveedor":  int(input("Ingrese el precio_proveedor: ")),
#     }
#     psProducto.postProducto(producto)
#     print("Producto Guardado")

# exeProd()