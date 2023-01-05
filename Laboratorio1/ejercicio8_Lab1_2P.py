"""
Laboratorio #1 - 2P
Ejercicio #15
Descripción: Resuélvala siguiente ecuación ((-1) k + 1) / (2 * k -1) ((- 1) ^ {k + 1}) / (2 * k-1)
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
def ingresoNumK():
    """
    Es un procedimiento que nos permite ingresar  un numero K 
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
        numK = input("Ingrese el numero K:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(numK) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            if float(numK) != (1/2):
                #retorna el numero
                return numK
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("   El dato ingresado debe ser diferente a 1/2, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def calculoEc(numK):
    """
    Es un procedimiento que nos permite ingresar  un numero K 
    Parametros:
    ------------
        Tiene un parámetro de entrada 
    
    Retorna:
    ------------
        Retorna resultado de la Ec.
    """
    numK = float(numK)
    resultadoEc = pow(-1,numK + 1)*(1-numK)/pow(2*numK-1,2)
    return resultadoEc

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("      Calcular ((-1) k + 1) / (2 * k -1) ((- 1) ^ {k + 1}) / (2 * k-1)       \n")
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    numK = ingresoNumK()
    resultadoEc = calculoEc(numK)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("El resultado de la ecuacion es: " + str(resultadoEc))
    print("--------------------------------------------------------------\n")