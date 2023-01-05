"""
Laboratorio #1 - 2P
Ejercicio #3
Descripción:Dadas dos longitudes ingresadas por el usuario que corresponden a los lados de un rectángulo,
calcular el perímetro y el área del mismo

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

def ingresoladorectangulo():
    """
    Es un procedimiento que nos permite ingresar  dos lados de un rectangulo
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna lista de lados del rectangulo
    """
    #inicializo un contador 
    cont = 0
    #Inicializamos un arreglo vacio llamado  listaLados
    listaLados = []
    #Bucle del ingreso de datos
    while True:
        #Ingreso del dato a sumar
        print("\n--------------------------------------------------------------\n")
        num = input("Ingrese el lado del rectangulo:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validarFloat(num) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero ingresado es un flotante > 0 entonces
            if float(num) > 0:
                #añade num ingresado de tipo flotante a la lista de numeros
                listaLados.append(num)
                cont += 1        
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero > 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 
        if cont == 2:
            #fin del bucle
            break
    return listaLados

def calculaPerimetroRectangulo(listaLados):
    """
    Es un procedimiento que nos permite realizar el calculo del perimetro de un rectangulo con dos lados
    Parametros:
    ------------
       Tiene  parámetro de entrada, tipo lista 
    
    Retorna:
    ------------
        Retorna perimetro del rectangulo
    """
    #inicializamos la sumatoria en 0
    perimetroRec=0
    #Bucle para recorrer cada una de las posiciones de la lista 
    for i in range(len(listaLados)):
        #calculo del perimetro del rectangulo
         perimetroRec += float(listaLados[i])*2
        #Retorna perimetro
    return  perimetroRec
def calculaArearoRectangulo(listaLados):
    """
    Es un procedimiento que nos permite realizar el calculo del area de un rectangulo con dos lados
    Parametros:
    ------------
       Tiene  parámetro de entrada, tipo lista 
    
    Retorna:
    ------------
        Retorna area del rectangulo
    """
    #Caculo del area del rectangulo
    areaRec= float(listaLados[0]) *  float(listaLados[1])
    return  areaRec

if __name__ == '__main__':
    #inicializo variables 
    listaLados = ingresoladorectangulo()
    perimetroRec = calculaPerimetroRectangulo(listaLados)
    areaRec = calculaArearoRectangulo(listaLados)
    #imprimo resultados
    print("--------------------------------------------------------------\n")
    print("El area del rectangulo es: " + str(areaRec))
    print("--------------------------------------------------------------\n")
    print("--------------------------------------------------------------\n")
    print("El perimetro del rectangulo es: " + str( perimetroRec))
    print("--------------------------------------------------------------\n")

