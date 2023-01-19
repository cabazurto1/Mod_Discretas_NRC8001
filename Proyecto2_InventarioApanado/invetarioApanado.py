"""
Proyecto II - P2
Tema: Inventario del Restaurante
Descripción: Sistema de inverntario del restaurante de comida rapida "Los Mega Apanados de la ESPE"


Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.1
"""
#######################################################################################
# Librerias
#######################################################################################
from datetime import datetime
from pymongo import MongoClient
from prettytable import PrettyTable
import random
import string
import big_o
import time
from memory_profiler import profile
import sys

#######################################################################################
#Validacion de datos
######################################################################################
def validadorEnteros(num):
    """
    Es un procedimiento que nos determina si un dato ingresado(numero) es un digito
    si lo es retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    Parametros:
    ------------
        Tiene  un parámetro de entrada (num)
    
    Retorna:
    ------------
        Retorna el valor de True si es el dato ingresado es un digito y false si no lo es
    """
    #inicializa validador de numero en falso
    numeroValido = False
    # si el numero ingresado es un digito entonces
    if num.isdigit():
        #retorna validador en verdadero (True)
        numeroValido = True
        return numeroValido
    else:
        #retorna validador en False
        return numeroValido

def validarFloat(numFloat):
    #"""
    #Es un procedimiento que nos determina si un dato ingresado(numero) es un flotante
    #si lo es retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    #Parametros:
    #------------
    #    Tiene  un parámetro de entrada (numFloat)
    #Retorna:
    #------------
    #    Retorna el valor de True si es el dato ingresado es un floatante y false si no lo es
    #"""
    #Si el numero es flotante
	try:
		float(numFloat)
        #retorna true 
		return True
	except:
        #En caso de excepción retorna false
		return False

def validarPalabras(palabra):
    if isinstance(palabra, str):
        listaPalabra = palabra.split()
        for letra in listaPalabra:
            if not letra.isalpha():
                return False
        return True
    return False

def validFecha(fecha):
    try:
        date = datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def validFechaActual(fecha):
    try:
        date = datetime.strptime(fecha, '%d-%m-%Y')
        if date < datetime.now():
            
            return True
        else:
            return False
    except ValueError:
        return False
def ValidarProducto(product):
    try:
        keys = ["codProduc", "nombreProduc", "fechaCad", "cantProduc"]
        if all(key in product for key in keys):
            date = datetime.strptime(product["fechaCad"], '%d-%m-%Y')
            if date > datetime.now():
                if product["cantProduc"] > 0:
                    return True
    except ValueError:
        return False
    return False
######################################################################################
#Ingreso de Datos
######################################################################################
def ingresoOpc():
    """
    Es un procedimiento que nos permite ingresar un numero entero positivo 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna numero entero
    """
    #Bucle del ingreso de datos
    while True:
        #Ingreso del dato 
        print("\n------------------------------\n")
        num = input("Ingrese la Opcion:  ")
        print("\n------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validadorEnteros(num) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero entero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            if int(num) > 0:
                return int(num)
            else:
                #Imprime mensaje de error en ingreso de datos
                print("-------------------------------------------------------------------------\n")
                print("                              ERROR                                      \n")
                print("Ingrese un numero mayor a 0, intente de nuevo    \n")
                print("------------------------------------------------------------------------\n")

def ingresoCantidad():
    """
    Es un procedimiento que nos permite ingresar la Cantidad de un rectangulo
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna numero flotante
    """
    #Bucle del ingreso de 
    while True:
        #Ingreso del dato 
        print("\n--------------------------------------------------------------\n")
        Cantidad = input("Ingrese la Cantidad del producto:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(Cantidad) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if float(Cantidad) >= 0:
                #retorna el numero
                return Cantidad
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero >= 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 


def ingresoNombreProduc():
    while True:
        nombreProduc = input("Ingrese el nombre del producto:  ")
        if validarPalabras(nombreProduc) == True:
            nombreProduc = nombreProduc.lower()
            return nombreProduc
        else:
            print("No ingreso un nombre, intente de nuevo")

def ingresoFecha():
    while True:
        fechCad = input("Ingrese la Fecha de caducidad en dd-mm-yyyy:  ")
        if validFecha(fechCad) == True:
            if validFechaActual(fechCad) == False:
                return fechCad
            else:
                print("La fecha del producto ingresado esta cadaducada o caduca el dia de hoy")
        elif validFecha(fechCad) == False:
            print("Ingrese una Fecha de caducidad en formato coreecto, intente de nuevo")


def ingresoProduc():
    producto = list()
    nombreProduc = ingresoNombreProduc()
    fechaCad = ingresoFecha()
    tiempoInicio = time.time()
    cantProduc =  ingresoCantidad()
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para generar codigo(ID) del producto: ",round(tiempoFin - tiempoInicio,4))

    codProduc = generarID()
    producto = [codProduc,nombreProduc,fechaCad,cantProduc]
    return producto




#################################################################################
#MongoDB conexion
#################################################################################
def collectionMongoDB():
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    return collection

def retornTodosProductosMongoDB():
    collection = collectionMongoDB()
    productos = collection.find()
    return productos
#################################################################################
#EXTRA
#################################################################################

def continuarEjecucion():
    input("Presione Enter para continuar...")

#################################################################################
#Procesos
#################################################################################

@profile(precision=4)
def generarID():
    collection = collectionMongoDB()
    # Generamos un código aleatorio de 8 caracteres alfanuméricos
    codProduc = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    producto = collection.find_one({"codProduc": codProduc})
    # buscamos el código en la colección
    # si el producto no existe en la colección
    if producto is None:
        print("El codigo generado (ID) es valido")
        return codProduc
    else:
        print("El codigo generado (ID) ya existe, se generara uno nuevo")
        return generarID()


@profile(precision=4)
def imputMongo(producto):
    collection = collectionMongoDB()
    collection.insert_one({"codProduc":producto[0],"nombreProduc":producto[1],"fechaCad":producto[2],"cantProduc":producto[3]})

@profile(precision=4)
def findMong(codProduc):
    collection = collectionMongoDB()
    product = collection.find_one({"codProduc":codProduc})
    print(product)
    codProduc = product["codProduc"]
    nombreProduc = product["nombreProduc"]
    fechaCad =  product["fechaCad"]
    cantProduc= product["cantProduc"]
    listaDatosProductoCad=[product,"3"]
    productoProximoCaducar(listaDatosProductoCad)
    listaDatosProductoCad_samples= lambda a:listaDatosProductoCad
    #Calculo del tiempo de complejidad de las cadenas creadas
    best, others = big_o.big_o(productoProximoCaducar,listaDatosProductoCad_samples)
    print(best)
    notificarStock(cantProduc)
    cantProduc_samples= lambda a:cantProduc
    #Calculo del tiempo de complejidad de las cadenas creadas
    best2, others = big_o.big_o(notificarStock,cantProduc_samples)
    print(best2)

    print("Producto encontrado con codigo(ID) "+ codProduc +" sus datos son: \n")
    print("Nombre del producto: "+  nombreProduc)
    print("Fecha de caducidad: "+ fechaCad)
    print("Cantindad del Producto: "+ cantProduc)
  

@profile(precision=4)
def updataCantidadProducto(codProduc):
    collection = collectionMongoDB()
    cantProduc =  ingresoCantidad()
    productActua = collection.update_one({"codProduc":codProduc},{"$set":{"cantProduc":cantProduc}})
    if productActua.matched_count > 0:
        print(f"Cantidad actualizada para el producto con ID {codProduc}")
    else:
        print("No se encontró el producto especificado")
@profile(precision=4)
def deleteMong(codProduc):
    collection = collectionMongoDB()
    
    productElimado = collection.delete_one({"codProduc":codProduc})
    if productElimado.deleted_count > 0:
        print("Producto eliminado exitosamente")
    else:
        print("No se encontró el producto especificado")



@profile(precision=4)
def printTablaProductos(productos):
    table = PrettyTable()
    table.field_names = ["Codigo del producto", "Nombre del producto", "Fecha de caducidad", "Cantidad del producto"]
    # Añadimos cada producto a la tabla
    for product in productos:
        table.add_row([product["codProduc"], product["nombreProduc"], product["fechaCad"], product["cantProduc"]])
    # Imprimimos la tabla
    print(table)
    



@profile(precision=4)
def productoProximoCaducar(listaDatosProductoCad):
    producto = listaDatosProductoCad[0]
    diasRestantes = int(listaDatosProductoCad[1])
    # Obtenemos la fecha de caducidad del producto

    fechaCaducidad = producto["fechaCad"]
    
    # Convertimos la fecha de caducidad a un objeto datetime
    fechaCaducidad = datetime.strptime(producto["fechaCad"], '%d-%m-%Y')
    
    # Obtenemos la fecha actual
    fecha_actual = datetime.now()
    
    # Calculamos la diferencia entre la fecha actual y la fecha de caducidad
    diferencia = fechaCaducidad - fecha_actual
     # Verificamos si la diferencia en días es menor o igual a los días restantes especificados
    if diferencia.days <= diasRestantes:
        print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")
        print(f"El producto con código {producto['codProduc']} está próximo a caducar. La fecha de caducidad es {fechaCaducidad.strftime('%d/%m/%Y')}")
        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
    else:
        print("\n--------------------------------------------------------------------------\n")
        print(f"El producto con código {producto['codProduc']} aun no esta proximo a caducar.")
        print("--------------------------------------------------------------------------\n")
@profile(precision=4)
def notificarStock(cantidad):
    cantidad = int(cantidad)
    if cantidad == 0:
        print("El producto se ha agotado")
    elif cantidad <= 10:
        print("El producto esta por agotarse")
    else:
        print("El producto tiene suficiente stock")

################################################################################
#Menu
################################################################################
def imprimirMenu(opciones):
    for i in range(len(opciones)):
        print(opciones[i])
   
def menuPrincipal():
    opciones = ["1. Ingreso de productos","2. Buscar Producto","3. Actualizar Producto","4. Eliminar Producto","5. Ver Inventario","6. Salir"]
    while True:
        print("-------------------------------\n")
        print("  Servicion de inventario\n")
        print("Los Mega Apanados de la ESPE\n")
        print("-------------------------------\n")
        imprimirMenu(opciones)
        opc=ingresoOpc()
        if (opc == 1):
            opc1()
        elif(opc == 2):
            opc2()
        elif(opc == 3):
            opc3()
        elif(opc == 4):
            opc4()
        elif(opc == 5):
            opc5()
        elif(opc == 6):
            salir()
            break
        else:
            print("Opcion ingresa no existe, intente de nuevo")


def opc1():
    tiempoInicio = time.time()
    print("\n---------------------------------\n")
    print("Ingreso de productos al inventario")
    print("---------------------------------\n")
    producto = ingresoProduc()
    imputMongo(producto)
    ValidarProducto(producto)
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para el ingreso del producto: ",round(tiempoFin - tiempoInicio,4))
    continuarEjecucion()
 

def opc2():
    tiempoInicio = time.time()
    print("\n---------------------------------\n")
    print('Buscar producto del inventario')
    print("---------------------------------\n")
    codProduc = input("Ingrese el codigo del producto(ID): ")
    findMong(codProduc)
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para la busqueda del producto: ",round(tiempoFin - tiempoInicio,4))
    continuarEjecucion()


def opc3():
    tiempoInicio = time.time()
    print("\n---------------------------------\n")
    print('Actualizar cantidad de un producto')
    print("---------------------------------\n")
    codProduc = input("Ingrese el codigo del producto: ")
    updataCantidadProducto(codProduc)
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para Actualizar cantidad del producto: ",round(tiempoFin - tiempoInicio,4))
    continuarEjecucion()


def opc4():
    tiempoInicio = time.time()
    print("\n---------------------------------\n")
    print('Eliminar  producto del inventario')
    print("---------------------------------\n")
    codProduc = input("Ingrese el codigo del producto: ")
    deleteMong(codProduc)
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para Eliminar producto: ",round(tiempoFin - tiempoInicio,4))
    continuarEjecucion()

def opc5():
    # Mide el tiempo de ejecución
    tiempoInicio = time.time()
    print("             -----------------------------------------------\n")
    print('              Inventario de "Los Mega Apanados de la ESPE"')
    print("             -----------------------------------------------\n")
    productos = retornTodosProductosMongoDB()
    printTablaProductos(productos)
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución para la impresion de la tabla: ",round(tiempoFin - tiempoInicio,4))
    continuarEjecucion()



def salir():
    for i in range(5, 0, -1):
        print(f"\rSaliendo del inventario en {i} segundos...", end="")
        sys.stdout.flush()
        time.sleep(1)
    print("\n\n¡Regresa Pronto! :3\n")


################################################################################
#Main
################################################################################

if __name__ == '__main__':
    tiempoInicio = time.time()
    menuPrincipal()
    tiempoFin = time.time()
    print("Tiempo[s] de ejecución del programa: ",round(tiempoFin - tiempoInicio,4))