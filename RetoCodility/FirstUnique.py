"""
Reto codility
Tema: First Unique
Descripción: El usuario ingresa el numero de elementos de un arreglo y regresa el primer numero no repetitivo

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
import random
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

def ingresoNumA():
    """
    Es un procedimiento que nos permite ingresar el numero de elementos de arreglo A
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
        print("\n--------------------------------------------------------------\n")
        numA = input("Ingrese el numero de elementos de arreglo A:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validadorEnteros(numA) == False:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero entero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            if int(numA) > 0:
                return int(numA)
            else:
                #Imprime mensaje de error en ingreso de datos
                print("-------------------------------------------------------------------------\n")
                print("                              ERROR                                      \n")
                print("Ingrese un numero mayor a 0, intente de nuevo    \n")
                print("------------------------------------------------------------------------\n")

def crearListaA(numA):
    """
    Es un procedimiento que nos permite crear un arreglo de N elemntos enteros de forma aleatoria
    Parametros:
    ------------
        Tiene  parámetro de entrada  numA
    
    Retorna:
    ------------
        Retorna un arreglo de enteros aleatorios
    """
    #inicializo el arreglo en 0
    A = [ ]
    #inicio del bucle hasta el numA
    for i in range (numA):
        #Agregue un entero random a A desde 0 hasta numA
        A.append(random.randint(0,numA))
    #retorno del arreglo
    return A


def solution(A):
    """
    Es un procedimiento que nos permite encontrar el primer caracter sin repetir
    Parametros:
    ------------
        Tiene un parámetr de entrada  cadena
    
    Retorna:
    ------------
        Retorna caracter sin repetir
    """
    #asigno longitud de la cadena a longA
    longA= len(A)
    #inicializo contador y numSinRep
    numSinRep=-1
    cont = 0
    #inicio del bucle hasta la longitud de la cadena 
    for i in range(longA):
        #inicio del segundo bucle hasta la longitud de la cadena 
        for j in range(longA):
            #si el caracter en la posición i es diferente a la j entonces 
            if A[i] != A[j]:
                #contador aumenta 1
                cont += 1
                #si el contador es igual a la longitud de la cadena en -1 entonces
                if cont == longA-1 :
                    #asigna ese caracter en caracterRe
                    numSinRep = A[i]      
    #retorna el caracter no repetido
    return numSinRep

if __name__ == '__main__':
    #Ingreso del numero de datos
    numA=ingresoNumA()
    #Generar el arreglo
    A = crearListaA(numA)
    #Solucion del arreglo 
    numSinRep = solution(A)
    #Mostrar resultados
    print("El arreglo generado: " + str(A))
    print("El primer numero sin repetir: " + str(numSinRep))
    #test prueba
    A_samples= lambda a:A
    #Calculo del tiempo de complejidad de las cadenas creadas
    beast, others = big_o.big_o(solution,A_samples) 
    #imprimir tiempo de solucion
    print(beast)



