"""
Laboratorio #1 - 2P
Ejercicio #7
Descripción: Calcular el área del cilindro.
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

def ingresoRadio():
    """
    Es un procedimiento que nos permite ingresar  el radio de un cilindro
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
        radio = input("Ingrese el radio del cilindro (r):  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(radio) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if float(radio) > 0:
                #retorna el numero
                return radio
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def ingresoAltura():
    """
    Es un procedimiento que nos permite ingresar la altura de un cilindro
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
        altura = input("Ingrese la altura del cilindro (h):  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(altura) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y > 0
            if float(altura) > 0:
                #retorna el numero
                return altura
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def calculoAreaCilindro(altura,radio):
    areaCilindro =2 *math.pi*float(radio)*(float(altura) + float(radio))
    return areaCilindro


if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("      Calcular el área del cilindro A = 2*pi*r(r+h)         \n")
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    radio = ingresoRadio()
    altura = ingresoAltura()
    areaCilindro = calculoAreaCilindro(altura,radio)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("El area del cilindro es: " + str(areaCilindro))
    print("\n--------------------------------------------------------------\n")
 