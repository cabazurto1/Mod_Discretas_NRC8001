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
        if collection.find({"codProduc":producto[0]}) == True:
            producto[0]= generarID()
        else:
            break
    collection.insert_one({"codProduc":producto[0],"nombreProduc":producto[1],"fechaCad":producto[2],"cantProduc":producto[3]})

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
    print(validate_product(producto))
    for i in range(len(producto)):
        #impresion de las cadenas y el caracter sin repetir
        cadenaPrueba= lambda a:producto[i]
        #Calculo del tiempo de complejidad de las cadenas creadas
        best, others = big_o.big_o(validate_product,cadenaPrueba)
    print(best)
    print(*producto)

def opc2():
    print('Has elegido la opción 2')


def opc3():
    print('Has elegido la opción 3')

def opc4():
    print('Has elegido la opción 4')

def opc5():
    print('Has elegido la opción 5')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menuPrincipal()