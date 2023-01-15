"""
Proyecto II - P2
Tema: Inventario del Restaurante
Descripción: Sistema de inverntario del restaurante de comida rapida "Los Mega Apanados de la ESPE"


Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
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


def opc1():
    print('Has elegido la opción 1')


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