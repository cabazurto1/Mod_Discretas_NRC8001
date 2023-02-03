"""
Proyecto II - P2
Tema: Inventario del Restaurante
Descripción: Sistema de inverntario del restaurante de comida rapida "Los Mega Apanados de la ESPE"


Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.3.0.1
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
    """
    Valida que se ingres una palabra sin caracters especiales
    Parametros:
    ------------
        Tiene un  parámetro de entrada  palabra
    
    Retorna:
    ------------
        Retorna verdadero o falso en caso de error
    """
    # Verifica si la entrada es una cadena
    if isinstance(palabra, str):
        # divide la cadena en una lista utilizando los espacios en blanco
        listaPalabra = palabra.split()
        # Itera sobre cada elemento de la lista
        for letra in listaPalabra:
            # Verifica si el elemento es alfabético
            if not letra.isalpha():
                # Si el elemento no es alfabético, devuelve False
                return False
        # Si todos los elementos son alfabéticos, devuelve True
        return True
    # Si la entrada no es una cadena, devuelve False
    return False

def validarFecha(fecha):
    """
    Si la fecha no se encuentra en el formato correcto, la función devolverá False. 
    Parametros:
    ------------
        Tiene un  parámetro de entrada  fecha
    
    Retorna:
    ------------
        Retorna verdadero o falso en caso de error
    """
    # intenta realizar la operación dentro del bloque try
    try:
        # utilizando el formato '%d-%m-%Y' para convertir fecha en un objeto de tipo date
        date = datetime.strptime(fecha, '%d-%m-%Y')
        # si la conversión es exitosa, devuelve True
        return True
    # si ocurre un error de tipo ValueError
    except ValueError:
        #devuelve False
        return False

def validarFechaActual(fecha):
    """
    Se compara la fecha convertida con la fecha actual, si la fecha convertida es 
    menor a la fecha actual devuelve True, si no devuelve False. 
    Parametros:
    ------------
        Tiene un  parámetro de entrada  fecha
    
    Retorna:
    ------------
        Retorna verdadero o falso en caso de error
    """
    # intenta realizar la operación dentro del bloque try
    try:
        # utilizando el formato '%d-%m-%Y' para convertir fecha en un objeto de tipo date
        date = datetime.strptime(fecha, '%d-%m-%Y')
        # si la fecha es menor a la fecha actual
        if date < datetime.now():
            # devuelve True
            return True
        else:
            #devuelve False
            return False
    # si ocurre un error de tipo ValueError
    except ValueError:
        #devuelve False
        return False
def validarCodProductoExist(codProduc):
    """
    Valida que el codigo de un producto existe en la base de datos
    Parametros:
    ------------
        Tiene un  parámetro de entrada  codProduc
    
    Retorna:
    ------------
        Retorna verdadero o falso 
    """
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'find_one()' de la colección para buscar un documento (producto) específico con el código especificado en el argumento codProduc
    product = collection.find_one({"codProduc":codProduc})
    # Si el producto es encontrado
    if product is not None:
        # retorna True
        return True
    else:
        # retorna False
        return False

def validarnombreProducExist(nombreProduc):
    """
    Valida que el nombre de un producto existe en la base de datos
    Parametros:
    ------------
        Tiene un  parámetro de entrada  nombreProduc
    
    Retorna:
    ------------
        Retorna verdadero o falso 
    """
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'find_one()' de la colección para buscar un documento (producto) específico con el código especificado en el argumento codProduc
    product = collection.find_one({"nombreProduc":nombreProduc})
    # Si el producto es encontrado
    if product is None:
        print(f"El nombre de producto {nombreProduc} no se encuentra en la base de datos, se puede ingresar.")
        # retorna True
        return True
    else:
        print(f"El nombre de producto {nombreProduc} ya se encuentra en la base de datos, no se puede ingresar.")
        # retorna False
        return False

def ValidarProducto(product):
    """
    verifica si el producto ingreso es correcto
    Parametros:
    ------------
        Tiene un  parámetro de entrada  product
    
    Retorna:
    ------------
        Retorna verdadero o falso en caso de error
    """
    # intenta realizar la operación dentro del bloque try
    try:
        # crea una lista con las claves esperadas en el diccionario
        datosProducto = ["codProduc", "nombreProduc", "fechaCad", "cantProduc"]
        # verifica si todas las claves están en el diccionario
        if all(dato in product for dato in datosProducto):
            # convierte fechaCad en un objeto de tipo date
            date = datetime.strptime(product["fechaCad"], '%d-%m-%Y')
            # si la fecha de caducidad es mayor a la fecha actual y cantProduc es mayor a 0
            if date > datetime.now() and product["cantProduc"] > 0:
                #devuelve True
                return True
    # si ocurre un error de tipo ValueError
    except ValueError:
        #devuelve False
        return False
    # si no se cumplen las condiciones
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
        if  validadorEnteros(Cantidad) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if int(Cantidad) >= 0:
                #retorna el numero
                return int(Cantidad)
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero >= 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 


def ingresoNombreProduc():
    """
    La función pide al usuario que ingrese el nombre del producto utilizando la función input().
    Utiliza un ciclo while para asegurar que se ingresa un nombre válido.
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna nombre del producto
    """
    # mientras sea verdadero
    while True:
        # pide al usuario ingresar el nombre del producto
        nombreProduc = input("Ingrese el nombre del producto:  ")
        # si el nombre ingresado es válido
        if validarPalabras(nombreProduc) == True and len(nombreProduc) <= 20:
            # convierte el nombre en minúsculas
            nombreProduc = nombreProduc.lower()
            if validarnombreProducExist(nombreProduc) == True:
                # devuelve el nombre
                return nombreProduc
        else:
            # si el nombre ingresado no es válido, imprime un mensaje de error
            print("No ingreso un nombre válido, intente de nuevo")

def ingresoFecha():
    """
    Ingreso de la fecha, si la fecha ingresada no es válida, se imprime un mensaje de error indicando que se debe ingresar 
    una fecha en el formato correcto y se vuelve a pedir la fecha de caducidad.
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna fecha 
    """
    # mientras sea verdadero
    while True:
        # pide al usuario ingresar la fecha de caducidad
        fechCad = input("Ingrese la Fecha de caducidad en dd-mm-yyyy:  ")
        # verifica si la fecha ingresada es válida
        if validarFecha(fechCad) == True:
            # verifica si la fecha ingresada es mayor a la fecha actual
            if validarFechaActual(fechCad) == False:
                # si se cumplen las condiciones, devuelve la fecha ingresada
                return fechCad
            else:
                # si la fecha ingresada es menor o igual a la fecha actual, imprime un mensaje de error
                print("La fecha del producto ingresado esta cadaducada o caduca el dia de hoy")
        # si la fecha ingresada no es válida
        elif validarFecha(fechCad) == False:
            # imprime un mensaje de error y vuelve a pedir la fecha de caducidad
            print("Ingrese una Fecha de caducidad en formato coreecto, intente de nuevo")

def ingresoCodProduc():
    while True:
        # Solicita al usuario que ingrese el código del producto a buscar
        codProduc = input("Ingrese el codigo del producto(ID): ")
        # Utiliza la función "findMong" para buscar el producto con el código especificado en la base de datos
        if validarCodProductoExist(codProduc) == True:
            #imprime Producto Encontrado
            print("\n--Producto Encontrado--\n")
            #retorna el codigo del producto validado
            return codProduc
        else:
            #imprime Producto No Encontrado
            print("\n--Producto No Encontrado--\n")
            #Imprime mensaje de Revisar de nuevo la tabla
            print("Revise de nuevo la tabla")
            #Imprime tabla de inventario
            opc5()

def ingresoProduc():
    """
    Ingreso datos del producto, genera ID del producto y crea una lista producto
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna producto
    """
    # crea una lista vacía para almacenar los datos del producto
    producto = list()
    # obtiene el nombre del producto mediante la función ingresoNombreProduc()
    nombreProduc = ingresoNombreProduc()
    # obtiene la fecha de caducidad mediante la función ingresoFecha()
    fechaCad = ingresoFecha()
    # obtiene la cantidad del producto mediante la función ingresoCantidad()
    cantProduc =  ingresoCantidad()
    # toma el tiempo actual
    tiempoInicio = time.time()
    # genera un código (ID) para el producto mediante la función generarID()
    codProduc = generarID()
    # toma el tiempo final
    tiempoFin = time.time()
    # imprime el tiempo de ejecución para generar el código (ID) del producto
    print("Tiempo[2] de ejecución para generar codigo(ID) del producto: ",round(tiempoFin - tiempoInicio,4))

    # agrega los datos
    producto = [codProduc,nombreProduc,fechaCad,cantProduc]
    #retorna datos
    return producto

#################################################################################
#MongoDB conexion
#################################################################################
def collectionMongoDB():
    """
    Conexion a la base de datos mongoDB
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna colleccion
    """
    try:
        # Dirección URL de la base de datos MongoDB
        mongoUri = "mongodb+srv://usBazurto:contrasenia99@cluster0.js9z1jh.mongodb.net/test"
        # Conecta al cliente de MongoDB utilizando la dirección URL
        cliente = MongoClient(mongoUri)
        # Selecciona la base de datos 'Inventario'
        db = cliente['Inventario']
        # Selecciona la colección 'Producto' dentro de la base de datos 'Inventario'
        collection = db['Producto']
        # Devuelve la colección 'Producto'
        return collection
    except:
        #En caso de no cenectarse imprimer error y cierra el programa
        print("Error en la conexión a la base de datos.")
        salir()

def retornTodosProductosMongoDB():
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'find()' de la colección para obtener todos los documentos (productos)
    productos = collection.find()
    # Devuelve todos los productos encontrados
    return productos
#################################################################################
#EXTRA
#################################################################################

def continuarEjecucion():
    
    """
    La función continuarEjecucion() se utiliza para dar una pausa en la ejecución 
    del programa y esperar a que el usuario presione la tecla Enter antes de continuar. 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        No Retorna 
    """
    # Pide al usuario que presione Enter para continuar
    input("Presione Enter para continuar...")

#################################################################################
#Procesos
#################################################################################
#Indicar que debe mostrar en consola el uso de memoria para funcion generarID()
@profile(precision=2)
def generarID():
    """
    La función generarID() se utiliza para generar un código único (ID) para un producto. 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna el ID 
    """
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Genera un código aleatorio de 5 caracteres alfanuméricos
    codProduc = ''.join(random.choice(string.ascii_letters + string.digits) for __ in range(5))
    # Busca en la colección si ya existe un producto con el mismo código generado
    producto = collection.find_one({"codProduc": codProduc})
    # Si el producto no existe en la colección
    if producto is None:
        #imprime mensaje de id valido
        print("El codigo generado (ID) es valido")
        #retorna ID
        return codProduc
    else:
        #imprime mensaje de id no valido
        print("El codigo generado (ID) ya existe, se generara uno nuevo")
        #Retorna generarID() para crear otro id valido, usa recursividad
        return generarID()

#Indicar que debe mostrar en consola el uso de memoria para funcion imputMongo(producto)
@profile(precision=4)
def imputMongo(producto):
    """
    La función imputMongo() se utiliza para agregar un nuevo producto a la base de datos MongoDB. 
    Parametros:
    ------------
        Tiene  parámetro de entrada producto 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'insert_one()' de la colección para agregar un nuevo documento (producto) con los valores del argumento producto
    collection.insert_one({"codProduc":producto[0],"nombreProduc":producto[1],"fechaCad":producto[2],"cantProduc":producto[3]})

#Indicar que debe mostrar en consola el uso de memoria para funcion findMong(codProduc)
@profile(precision=4)
def findMong(codProduc):
    """
    Busca y muestra un producto específico en la base de datos MongoD
    Parametros:
    ------------
        Tiene  parámetro de entrada codProduct
    
    Retorna:
    ------------
        No Retorna  
    """
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'find_one()' de la colección para buscar un documento (producto) específico con el código especificado en el argumento codProduc
    product = collection.find_one({"codProduc":codProduc})
    # Imprime los detalles del producto encontrado
    print(product)
    # guarda los valores del producto en variables
    codProduc = product["codProduc"]
    nombreProduc = product["nombreProduc"]
    fechaCad =  product["fechaCad"]
    cantProduc= product["cantProduc"]
    #crea una lista con los datos del producto y un valor fijo 3
    listaDatosProductoCad=[product,"3"]
    #llama a una función llamada productoProximoCaducar pasando como parametro la lista
    productoProximoCaducar(listaDatosProductoCad)
    #crea una función lambda que recibe como parametro la lista y la guarda en una variable
    listaDatosProductoCad_samples= lambda a:listaDatosProductoCad
    #Calculo del tiempo de complejidad de las cadenas creadas
    best, others = big_o.big_o(productoProximoCaducar,listaDatosProductoCad_samples)
    #imprime tiempo de complejidad para productoProximoCaducar
    print(best)
    #LLama a 'notificarStock(cantProduc)' para saber si hay que reponer producto
    notificarStock(cantProduc)
    #crea una función lambda que recibe como parametro la lista y la guarda en una variable
    cantProduc_samples= lambda a:cantProduc
    #Calculo del tiempo de complejidad de las cadenas creadas
    best2, others = big_o.big_o(notificarStock,cantProduc_samples)
    #imprime tiempo de complejidad para notificarStock
    print(best2)
    #imprime datos del producto
    print("Producto encontrado con codigo(ID) "+ codProduc +" sus datos son: \n")
    print("Nombre del producto: "+  nombreProduc)
    print("Fecha de caducidad: "+ fechaCad)
    print("Cantindad del Producto: "+ cantProduc)
  
#Indicar que debe mostrar en consola el uso de memoria para funcion updataCantidadProducto(codProduc)
@profile(precision=4)
def updataCantidadProducto(codProduc):
    """
    se utiliza para actualizar la cantidad de un producto específico en la base de datos MongoDB. 
    Parametros:
    ------------
        Tiene  parámetro de entrada codProduct
    
    Retorna:
    ------------
        No Retorna  
    """
    # Establecer conexión con la base de datos y seleccionar colección de productos
    collection = collectionMongoDB()
    # Obtener la nueva cantidad del producto a actualizar
    cantProduc =  ingresoCantidad()
    # Actualizar la cantidad del producto con el código especificado en el argumento 'codProduc'
    productActua = collection.update_one({"codProduc":codProduc},{"$set":{"cantProduc":cantProduc}})
    # Comprobar si el producto fue actualizado correctamente
    if productActua.matched_count > 0:
        #imprime Cantidad actualizada para el producto con ID
        print(f"Cantidad actualizada para el producto con ID {codProduc}")
    else:
        #imprime "No se encontró el producto especificado"
        print("No se encontró el producto especificado")

#Indicar que debe mostrar en consola el uso de memoria para funcion deleteMong(codProduc)
@profile(precision=4)
def deleteMong(codProduc):
    """
    se utiliza para eliminar un producto específico de la base de datos MongoDB.
    Parametros:
    ------------
        Tiene  parámetro de entrada codProduct
    
    Retorna:
    ------------
        No Retorna  
    """
    #Establecemos conexión con la base de datos y seleccionamos la colección de productos
    collection = collectionMongoDB()
    # Utilizamos el método delete_one() para eliminar el producto especificado
    productElimado = collection.delete_one({"codProduc":codProduc})
    # Verificamos si el producto fue eliminado correctamente
    if productElimado.deleted_count > 0:
        print("Producto eliminado exitosamente")
    else:
        print("No se encontró el producto especificado")



#Indicar que debe mostrar en consola el uso de memoria para funcion printTablaProductos(productos)
@profile(precision=4)
def printTablaProductos(productos):
    """
    La función se utiliza para imprimir en consola una tabla con los datos de los productos. 
    Parametros:
    ------------
        Tiene  parámetro de entrada Productos
    
    Retorna:
    ------------
        No Retorna  
    """
    # Creamos una tabla
    table = PrettyTable()
    # Creamos  las columnas correspondientes
    table.field_names = ["Codigo del producto", "Nombre del producto", "Fecha de caducidad", "Cantidad del producto"]
    # Recorremos cada producto en la lista de productos
    
    for product in productos:
        #Añadimos cada producto a la tabla con los valores correspondientes "codProduc":codProduc
        table.add_row([product["codProduc"], product["nombreProduc"], product["fechaCad"], product["cantProduc"]])
    # Imprimimos la tabla en consola
    print(table)


#Indicar que debe mostrar en consola el uso de memoria para funcion printTablaProductos(productos)
@profile(precision=4)
def productoProximoCaducar(listaDatosProductoCad):
    """
    La función notifica que un producto esta por caducar o caduco 
    Parametros:
    ------------
        Tiene  parámetro de entrada listaDatosProductoCad
    
    Retorna:
    ------------
        No Retorna  
    """
    #asigno a producto los productos de la lista
    producto = listaDatosProductoCad[0]
    #asigno a diasRestantes del producto para notificar
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
        #impresion de proximo a cadicar
        print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")
        print(f"El producto con código {producto['codProduc']} está próximo a caducar. La fecha de caducidad es {fechaCaducidad.strftime('%d/%m/%Y')}")
        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
    else:
        #impresion de que no caduca aun
        print("\n--------------------------------------------------------------------------\n")
        print(f"El producto con código {producto['codProduc']} aun no esta proximo a caducar.")
        print("--------------------------------------------------------------------------\n")
@profile(precision=4)
def notificarStock(cantidad):
    """
    La función notifica que un producto esta por agotarse 
    Parametros:
    ------------
        Tiene  parámetro de entrada cantidad del producto
    
    Retorna:
    ------------
        No Retorna  
    """
    #convirete a entero el valor de la cantodad
    cantidad = int(cantidad)
    #si la cantidad es 0 
    if cantidad == 0:
        #Imprime mensaje de producto agotado
        print("El producto se ha agotado")
    #si la cantidad es <=10 
    elif cantidad <= 10:
        #Imprime mensaje de producto por agotarse
        print("El producto esta por agotarse")
    else:
        #Imprime mensaje de producto sin agotarse
        print("El producto tiene suficiente stock")

################################################################################
#Menu
################################################################################
def imprimirMenu(opciones):
    """
    La función imprime el menu princial
    Parametros:
    ------------
        tiene un parámetro opciones
    
    Retorna:
    ------------
        No Retorna  
    """
    #inicio del bucle
    for i in range(len(opciones)):
        #imprime opciones
        print(opciones[i])
   
def menuPrincipal():
    """
    La función crea el menu principal
    Parametros:
    ------------
        tiene un parámetro opciones
    
    Retorna:
    ------------
        No Retorna  
    """
    #Lista de occiones
    opciones = ["1. Ingreso de productos","2. Buscar Producto","3. Actualizar Producto","4. Eliminar Producto","5. Ver Inventario","6. Salir"]
    #inicio del bucle para el menu
    while True:
        print("-------------------------------\n")
        print("  Servicion de inventario\n")
        print("Los Mega Apanados de la ESPE\n")
        print("-------------------------------\n")
        #mostrar menu
        imprimirMenu(opciones)
        #ingresar opc
        opc=ingresoOpc()
        #si opc es 1
        if (opc == 1):
            #Llamar funcion opc1 Ingresar producto
            opc1()
        #si opc es 2
        elif(opc == 2):
            #Llamar funcion opc2 Buscar producto
            opc2()
        #si opc es 3
        elif(opc == 3):
            #Llamar funcion opc3 Actualizar producto
            opc3()
        #si opc es 4
        elif(opc == 4):
            #Llamar funcion opc4 Eliminar producto
            opc4()
        #si opc es 5
        elif(opc == 5):
            #Llamar funcion opc5 Ver Inventario
            opc5()
        #si opc es 6
        elif(opc == 6):
            #Llamar funcion salir 
            salir()
            break
        else:
            #Imprimir que la opcion no existe
            print("Opcion ingresa no existe, intente de nuevo")

def opc1():
    
    """
    La función opc1 es para ingresar un producto del inventario 
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Mide el tiempo de ejecución al inicio de la función
    tiempoInicio = time.time()
    # Imprime una línea de separación y el título de la opción
    print("\n---------------------------------\n")
    print("Ingreso de productos al inventario")
    print("---------------------------------\n")
    # Utiliza la función "ingresoProduc" para obtener los datos del producto a ingresar
    producto = ingresoProduc()
    # Utiliza la función "imputMongo" para ingresar el producto a la base de datos
    imputMongo(producto)
    # Utiliza la función "ValidarProducto" para validar los datos del producto ingresado
    ValidarProducto(producto)
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    # Imprime el tiempo de ejecución en segundos para ingresar el producto
    print("Tiempo[s] de ejecución para el ingreso del producto: ",round(tiempoFin - tiempoInicio,4))
    # Utiliza la función "continuarEjecucion" para permitir al usuario continuar con la ejecución del programa
    continuarEjecucion()


def opc2():
    """
    La función opc2 es para buscar un producto del inventario especificando el código del producto 
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Mide el tiempo de ejecución al inicio de la función
    tiempoInicio = time.time()
    # Imprime una línea de separación y el título de la opción
    print("\n---------------------------------\n")
    print('Buscar producto del inventario')
    print("---------------------------------\n")
    # Solicita al usuario que ingrese el código del producto a buscar
    codProduc = ingresoCodProduc()
    #realiza la busqueda del producto y sus datos
    findMong(codProduc)
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    # Imprime el tiempo de ejecución en segundos para buscar el producto
    print("Tiempo[s] de ejecución para la busqueda del producto: ",round(tiempoFin - tiempoInicio,4))
    # Utiliza la función "continuarEjecucion" para permitir al usuario continuar con la ejecución del programa
    continuarEjecucion()


def opc3():
    """
    La función opc3 es para actualizar la cantidad de un producto especificando el código del producto
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Mide el tiempo de ejecución al inicio de la función
    tiempoInicio = time.time()
    # Imprime una línea de separación y el título de la opción
    print("\n---------------------------------\n")
    print('Actualizar cantidad de un producto')
    print("---------------------------------\n")
    # Solicita al usuario que ingrese el código del producto a actualizar
    codProduc = ingresoCodProduc()
    # Utiliza la función "updataCantidadProducto" para actualizar la cantidad del producto con el código especificado en la base de datos
    updataCantidadProducto(codProduc)
    # Obtiene la colección 'Producto' mediante la función collectionMongoDB()
    collection = collectionMongoDB()
    # Utiliza el método 'find_one()' de la colección para buscar un documento (producto) específico con el código especificado en el argumento codProduc
    product = collection.find_one({"codProduc":codProduc})
    #asigna a cantProduc la cantidad del producto de la coleccion buscada
    cantProduc= product["cantProduc"]
    #LLama a 'notificarStock(cantProduc)' para saber si hay que reponer producto
    notificarStock(cantProduc)
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    # Imprime el tiempo de ejecución en segundos para actualizar la cantidad del producto
    print("Tiempo[s] de ejecución para Actualizar cantidad del producto: ",round(tiempoFin - tiempoInicio,4))
    # Utiliza la función "continuarEjecucion" para permitir al usuario continuar con la ejecución del programa
    continuarEjecucion()


def opc4():
    """
    La función opc4 es para eliminar un producto del inventario especificando el código del producto 
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Mide el tiempo de ejecución al inicio de la función
    tiempoInicio = time.time()
    # Imprime una línea de separación y el título de la opción
    print("\n---------------------------------\n")
    print('Eliminar  producto del inventario')
    print("---------------------------------\n")
    # Solicita al usuario que ingrese el código del producto a eliminar
    codProduc = input("Ingrese el codigo del producto: ")
    # Utiliza la función "deleteMong" para eliminar el producto con el código especificado de la base de datos
    deleteMong(codProduc)
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    # Imprime el tiempo de ejecución en segundos para eliminar el producto
    print("Tiempo[s] de ejecución para Eliminar producto: ",round(tiempoFin - tiempoInicio,4))
    # Utiliza la función "continuarEjecucion" para permitir al usuario continuar con la ejecución del programa
    continuarEjecucion()

def opc5():
    """
    La función opc5 es para imprimir el inventario de productos de "Los Mega Apanados de la ESPE"
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Mide el tiempo de ejecución al inicio de la función
    tiempoInicio = time.time()
    # Imprime una línea de separación y el título del inventario
    print("             -----------------------------------------------\n")
    print('              Inventario de "Los Mega Apanados de la ESPE"')
    print("             -----------------------------------------------\n")
    # Obtiene una lista de productos utilizando la función "retornTodosProductosMongoDB"
    productos = retornTodosProductosMongoDB()
    # Utiliza la función "printTablaProductos" para imprimir la lista de productos en formato de tabla
    printTablaProductos(productos)
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    # Imprime el tiempo de ejecución en segundos para la impresión de la tabla
    print("Tiempo[s] de ejecución para la impresion de la tabla: ",round(tiempoFin - tiempoInicio,4))
    # Utiliza la función "continuarEjecucion" para permitir al usuario continuar con la ejecución del programa
    continuarEjecucion()



def salir():
    """
    Este código define una función llamada "salir" que imprime una cuenta regresiva de 5 segundos antes de imprimir un mensaje de despedida.
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Utiliza un bucle "for" con la función "range" para contar desde 5 hasta 1 con un intervalo de decremento de 1 en cada iteración
    for i in range(5, 0, -1):
        # Imprime un mensaje con el tiempo restante antes de salir del inventario
        print(f"\rSaliendo del inventario en {i} segundos...", end="")
        # Utiliza la función "flush" de "sys.stdout" para vaciar la salida antes de que transcurra el tiempo especificado en "time.sleep"
        # para que el contador sea visible en tiempo real
        sys.stdout.flush()
        # Utiliza la función "sleep" de "time" para detener la ejecución durante 1 segundo antes de continuar con la siguiente iteración
        time.sleep(1)
    # Imprime un mensaje de despedida al finalizar la cuenta regresiva
    print("\n\n¡Regresa Pronto! :3\n")


################################################################################
#Main
################################################################################

if __name__ == '__main__':
    # Mide el tiempo de ejecución al final de la función
    tiempoInicio = time.time()
    #llama menu principal
    menuPrincipal()
    # Mide el tiempo de ejecución al final de la función
    tiempoFin = time.time()
    #imprime tiempo de ejecucion
    print("Tiempo[s] de ejecución del programa: ",round(tiempoFin - tiempoInicio,4))