"""
Laboratorio #1 - 2P
Ejercicio #19
Descripción: Ingresar la longitud y el ancho de un rectángulo y encontrar su perímetro.
Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""

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
def ingresoLongitud():
    """
    Es un procedimiento que nos permite ingresar la longitud de un rectangulo
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
        longitud = input("Ingrese la longitud del rectangulo:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(longitud) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if float(longitud) > 0:
                #retorna el numero
                return longitud
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def ingresoAncho():
    """
    Es un procedimiento que nos permite ingresar la longitud de un rectangulo
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
        ancho = input("Ingrese el ancho del rectangulo:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(ancho) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if float(ancho) > 0:
                #retorna el numero
                return ancho
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 


def calcPeriRect(longitud,ancho):
    """
    Es un procedimiento que nos permite realizar el calculo del perimetro de un rectangulo con dos lados
    Parametros:
    ------------
       Tiene dos parámetros entrada
    
    Retorna:
    ------------
        Retorna perimetro del rectangulo
    """
    #calculo del perimetro del rectangulo
    perRec = float(longitud)*2 + float(ancho)*2
    #retorna el perimetro
    return  perRec

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("Calculo del perimetro de un rectangulo              \n" )
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    ancho =  ingresoAncho()
    longitud = ingresoLongitud()
    perRec =  calcPeriRect(longitud,ancho)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("El perimetro del rectangulo es: " + str( perRec))
    print("--------------------------------------------------------------\n")

