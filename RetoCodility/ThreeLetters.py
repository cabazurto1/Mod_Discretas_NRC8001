"""
Reto codility
Tema: Tree Letters
Descripción: El usuario ingresa el numero de letra a y b para generar una cadena
sin repetir aaa o bbb

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

def ingresoNum(A):
    """
    Es un procedimiento que nos permite ingresar el numero de cadenas 
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
        num = input("Ingrese el numero "+A+" :")
        print("\n--------------------------------------------------------------\n")
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



def randomStr(numA,numB) :
    """
    Es un procedimiento que nos permite generar una cadena de caracters formados por el numero de letras ingresados
    con solo letras 'a', 'b'
    Parametros:
    ------------
        Tiene dos parámetros de entrada  numA, numB
    
    Retorna:
    ------------
        Retorna Str random de letras 'a','b'
    """
    #inicializo cadena de respuesta en ""
    resStr = ""
    #inicio del bucle (hacer mientras numA o numB )>0
    while numA > 0 or numB > 0:
        #si la longitud de la cadena nueva es >= 2 y las dos posiciones anteriores son iguales entonces 
        if len(resStr) >= 2 and resStr[-1] == resStr[-2]:
            #si la posicion anterior -1 de la cadena es igual a 'a' enotnces 
            if resStr[-1] == 'a':
                #si tambien el numB>0
                if numB > 0:
                    #agregue 'b' a la cadena
                    resStr += 'b'
                    #disminuya en -1 al numB
                    numB -= 1
                #en caso de que numB <= 0 entonces pregunte si numA >0
                elif numA > 0:
                    #agregue 'a' a la cadena
                    resStr += 'a'
                    #disminuya en -1 al numA
                    numA -= 1
            #si la posicion anterior -1 de la cadena es igual a 'b' enotnces 
            elif resStr[-1] == 'b':
                #si tambien el numA>0
                if numA > 0:
                    #agregue 'a' a la cadena
                    resStr += 'a'
                    #disminuya en -1 al numA
                    numA -= 1
                #si tambien el numB>0
                elif numB > 0:
                    #agregue 'b' a la cadena
                    resStr += 'b'
                    #disminuya en -1 al numB
                    numB -= 1
        elif numA > numB:
            #agregue 'a' a la cadena
            resStr += 'a'
            #disminuya en -1 al numA
            numA -= 1
        else:
            #agregue 'b' a la cadena
            resStr += 'b'
            #disminuya en -1 al numB
            numB -= 1
    #retorna la cadena
    return resStr
def randomStr1(cadenaString):
    """
    Es un procedimiento que nos permite ingresar calcular el tiempo de complejidad
    Parametros:
    ------------
        Tiene  parámetro de entrada  cadenaString
    
    Retorna:
    ------------
        Retorna numero entero, el tiempo de complejidad
    """
    #Crea como lista cada cadena ingresada
    CadenaStringList = list(cadenaString)
    #Calculo del tiempo de complejidad
    caractSinRepe = next((ele for ele in CadenaStringList if CadenaStringList.count(ele)==1),None)
    #Retorna el tiempo de complejidad
    return caractSinRepe
def printComplexTiempo(cadena):
    """
    Es un procedimiento que nos permite imprimer el tiempo de complejidad
    Parametros:
    ------------
        Tiene un parámetr de entrada  cadena
    
    Retorna:
    ------------
        no retorna nada
    """
    #asigno longitud de la cadena a longA
    longA= len(cadena)
    #inicio del bucle hasta la longitud de la cadena 
    for i in range(longA):
        cadenaAux= lambda a:str(cadena[i])
        #Calculo del tiempo de complejidad de las cadenas creadas
        complexTiempo, others = big_o.big_o(randomStr1,cadenaAux)     
    #imprime tiempo de complejidad
    print(complexTiempo)
            

if __name__ == '__main__':
    #ingreso de datos
    numA = ingresoNum("A")
    numB = ingresoNum("B")
    #Generar la cadena de letras 'a', 'b' de longitud A+B
    cadena = randomStr(numA,numB)
    #Imprimir resultados:
    print("La cadena con A: "+str(numA)+" y B: "+str(numB)+" es: " +cadena)
    printComplexTiempo(cadena)


  
