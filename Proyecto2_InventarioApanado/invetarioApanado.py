"""
Proyecto II - P2
Tema: Inventario del Restaurante
Descripción: Sistema de inverntario del restaurante de comida rapida "Los Mega Apanados de la ESPE"


Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.1
"""
from datetime import datetime
from pymongo import MongoClient
from prettytable import PrettyTable
import random
import string
import big_o
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

def validate_words(words):
    if isinstance(words, str):
        word_list = words.split()
        for word in word_list:
            if not word.isalpha():
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
def generarID():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

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
            if float(Cantidad) > 0:
                #retorna el numero
                return Cantidad
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 


def ingresoNombreProduc():
    while True:
        nombreProduc = input("Ingrese el nombre del producto:  ")
        if validate_words(nombreProduc) == True:
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
    codProduc = generarID()
    cantProduc =  ingresoCantidad()
    producto = [codProduc,nombreProduc,fechaCad,cantProduc]
    return producto

def imputMongo(producto):
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    while True:
        if collection.find_one({"codProduc":producto[0]}) == True:
            producto[0]= generarID()
        else:
            break
    collection.insert_one({"codProduc":producto[0],"nombreProduc":producto[1],"fechaCad":producto[2],"cantProduc":producto[3]})

def findMong(codProduc):
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    product = collection.find_one({"codProduc":codProduc})
    print(product)
    codProduc = product["codProduc"]
    nombreProduc = product["nombreProduc"]
    fechaCad =  product["fechaCad"]
    cantProduc= product["cantProduc"]
    print("Producto encontrado con codigo "+ codProduc +" sus datos son: \n")
    print("Nombre del producto: "+  nombreProduc)
    print("Fecha de caducidad: "+ fechaCad)
    print("Cantindad del Producto: "+ cantProduc)

def updataCantidadProducto(codProduc):
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    cantProduc =  ingresoCantidad()
    productActua = collection.update_one({"codProduc":codProduc},{"$set":{"cantProduc":cantProduc}})
    if productActua.matched_count > 0:
        print(f"Cantidad actualizada para el producto con ID {codProduc}")
    else:
        print("No se encontró el producto especificado")

def deleteMong(codProduc):
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    
    productElimado = collection.delete_one({"codProduc":codProduc})
    if productElimado.deleted_count > 0:
        print("Producto eliminado exitosamente")
    else:
        print("No se encontró el producto especificado")

def printTablaProductos():
    mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
    cliente = MongoClient(mongoUri)
    #Database
    db = cliente['Inventario']
    collection = db['Producto']
    table = PrettyTable()
    products = collection.find()
    table.field_names = ["Codigo del producto", "Nombre del producto", "Fecha de caducidad", "Cantidad del producto"]

    # Añadimos cada producto a la tabla
    for product in products:
        table.add_row([product["codProduc"], product["nombreProduc"], product["fechaCad"], product["cantProduc"]])

    # Imprimimos la tabla
    print(table)
    





def validate_product(product):
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

def opc1():
    print("Ingreso de productos al inventario")
    producto = ingresoProduc()
    imputMongo(producto)
    validate_product(producto)
    for i in range(len(producto)):
        #impresion de las cadenas y el caracter sin repetir
        cadenaPrueba= lambda a:producto[i]
        #Calculo del tiempo de complejidad de las cadenas creadas
        best, others = big_o.big_o(validate_product,cadenaPrueba)
    print(best)

def opc2():
    print('Buscar producto del inventario')
    codProduc = input("Ingrese el codigo del producto: ")
    findMong(codProduc)


def opc3():
    print('Actualizar productos')
    codProduc = input("Ingrese el codigo del producto: ")
    updataCantidadProducto(codProduc)


def opc4():
    print('Eliminar  producto del inventario')
    codProduc = input("Ingrese el codigo del producto: ")
    deleteMong(codProduc)

def opc5():
    print('Has elegido la opción 5')
    printTablaProductos()


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menuPrincipal()