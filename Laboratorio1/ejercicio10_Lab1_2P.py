"""
Laboratorio #1 - 2P
Ejercicio #
Descripción: Hallar la potencia de cualquier número x^y
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
def ingresoValorY():
    """
    Es un procedimiento que nos permite ingresar  un numero entero 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna numero flota
    """
    #Bucle del ingreso de datos
    while True:
        #Ingreso del dato 
        print("\n--------------------------------------------------------------\n")
        numZ = input("Ingrese el valor del exponente y:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validarFloat(numZ) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #retorna el numero
            return numZ
def ingresoValorX():
    """
    Es un procedimiento que nos permite ingresar  un numero entero 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna numero flota
    """
    #Bucle del ingreso de datos 
    while True:
        #Ingreso del dato 
        print("\n--------------------------------------------------------------\n")
        numX = input("Ingrese el valor de x:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validarFloat(numX) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #retorna el numero
            return numX

def calculoExpo(numX,numY):
    """
    Es un procedimiento que nos permite calcular la ec. y = x^2/2
    Parametros:
    ------------
        Tiene dos parámetros de entrada de tipo flotante
    
    Retorna:
    ------------
        Retorna el valor calculado del Ec. y = x^2/2
    """
    #Calculo de x^y
    calcExpo = pow(float(numX),float(numY))
    #retorno del valor
    return calcExpo

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("      Calcular la Ec. x^y      \n")
    print("--------------------------------------------------------------\n")
    #Inicializo variables x y z
    numX = ingresoValorX()
    numY = ingresoValorY()
    calcExpo=calculoExpo(numX,numY)
    #imprimo resultado de y = x^y
    print("Ec. (x^y) es : " + str(calcExpo))