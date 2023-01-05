"""
Laboratorio #1 - 2P
Ejercicio #9
Descripción: Calcular el teorema de Pitágoras
Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
import math
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
        #Retorna verdadero
		return True
	except:
        #En caso de excepción retorna false
		return False

def ingresoNumA():
    """
    Es un procedimiento que nos permite ingresar  un numero A 
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
        numA = input("Ingrese el numero A:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(numA) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #retorna el numero
            return numA

def ingresoNumB():
    """
    Es un procedimiento que nos permite ingresar  un numero B
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
        numB = input("Ingrese el numero B:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(numB) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #retorna el numero
            return numB

def calculoPitagoras(numA,numB):
    """
    Es un procedimiento mos permite calcular el teorema de Pitágoras c^2=a^2+b^2
    Parametros:
    ------------
        Tiene  dos parámetros de entrada (numA,numB)
    
    Retorna:
    ------------
        Retorna  el valor del teorema de Pitágoras c^2
    """
    numPitagoras= pow(float(numA),2)+pow(float(numB),2)
    return numPitagoras

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("      Calcular el teorema de Pitágoras c^2=a^2+b^2         \n")
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    numA = ingresoNumA()
    numB = ingresoNumB()
    numPitagoras = calculoPitagoras(numA,numB)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("El teorema de Pitágoras c^2=a^2+b^2 donde c^2 es: " + str(numPitagoras))
    print("--------------------------------------------------------------\n")