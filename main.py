import modules.getClientes as clientes
import modules.getEmpleados as empleados
import modules.getPedido as pedido
import modules.getPago as pago
import os
import time
import modules.getOficina as oficina
import modules.getProducto as readProducto
import modules.updateProducto as updateProducto
import modules.deleteProducto as deleteProducto
from tabulate import tabulate
import modules.postProducto as createProducto
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
                oficina.menu()
            elif(opcion == 3):
                empleados.menu()
            elif(opcion == 4):
                pedido.menu()
            elif(opcion == 5):
                menuProducto()
            elif(opcion == 0):
                break


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
        3. Guardar 
        4. Actualizar
        5. Eliminar productos
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
            #time.sleep(10)
        elif(opcion == 2):
            readGamas.menuImprimirAllNombre()
            #time.sleep(10)
        elif(opcion == 3):
            createProducto.menu()
        elif(opcion == 4):
            updateProducto.menu()
        elif(opcion == 5):
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