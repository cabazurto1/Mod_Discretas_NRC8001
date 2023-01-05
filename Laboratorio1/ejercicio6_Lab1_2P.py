"""
Laboratorio #1 - 2P
Ejercicio #11
Descripción: Ingresar un valor en libras y transformarlo a kilos y gramos
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

def ingresoLibras():
    """
    Es un procedimiento que nos permite ingresar la cantidad de libras
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
        numLb = input("Ingrese las libras(lb):  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(numLb) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y >0
            if float(numLb) >= 0:
                #retorna el numero
                return numLb
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero >= 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def converKg(numLb):
    """
    Es un procedimiento que nos permite convertir de Lb a Kg 
    Parametros:
    ------------
        Tiene un parámetro de entrada numLb 
    
    Retorna:
    ------------
        Retorna numero flotante
    """
    #Ec. para convertir de Lb a Kg
    numKg = float(numLb)/2.2046
    #retorna numKg
    return numKg

def converGr(numLb):
    """
    Es un procedimiento que nos permite convertir de Lb a g 
    Parametros:
    ------------
        Tiene un parámetro de entrada numLb 
    
    Retorna:
    ------------
        Retorna numero flotante
    """
    #Ec. para convertir de Lb a g
    numGr = float(converKg(numLb))*1000
    #retorna numG
    return numGr

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("      Convertidor de Libras a Kilogramos y Gramos      \n")
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    numLb = ingresoLibras()
    numKg =  converKg(numLb)
    numGr =  converGr(numLb)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("De Lb: " + str(numLb)+"[lb]"+ " a Kg: " + str(numKg)+"[kg]")
    print("\n--------------------------------------------------------------\n")
    print("--------------------------------------------------------------\n")
    print("De Lb: " + str(numLb)+"[lb]"+ " a g: " + str(numGr)+"[g]")
    print("\n--------------------------------------------------------------\n")