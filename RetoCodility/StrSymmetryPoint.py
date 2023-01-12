"""
Reto codility
Tema: StrSymmetryPoint

Descripción: El usuario ingresa una cadena 

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
import big_o
def invertirStr(cadena):
    """
    Es un procedimiento que invirte un cadena de caracteres 
    Parametros:
    ------------
        Tiene  un parámetro de entrada (cadena)
    
    Retorna:
    ------------
        Retorna la cade invertida
    """
    #asigna a  StrInve la cadena invertida
    StrInver= ''.join(reversed(cadena))
    #retorna  StrInver
    return StrInver

def ingresoCadena():
    """
    Es un procedimiento que permite ingresar una cadena por teclado
    Parametros:
    ------------
        Tiene  un parámetro de entrada (cadena)
    
    Retorna:
    ------------
        Retorna la cade invertida
    """
    #ingreso de la cadena
    cadena = input("Ingrese una cadena:  ")
    #retorna cadena
    return cadena

def sinRepeticion(cadenaString):
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

def StrpuntoSimetria(cadena,StrInver):
    """
    Es un procedimiento que permite sabe el punto de simteria de una cadena 
    Parametros:
    ------------
        Tiene  dos parámetros de entrada (cadena,StrInver)
    
    Retorna:
    ------------
        Retorna el punto de simetria y -1 en caso de no tener
    """
    puntoSimetria=-1;
    if(cadena==StrInver):
        puntoSimetria=int((len(cadena)-1)/2)
        print("La simetria en la palabra " + cadena +" esta en la posicion: "+str(puntoSimetria)+" [" +cadena[puntoSimetria]+"]")
        print("Debido a que: "+cadena[:puntoSimetria]+" = "+StrInver[:puntoSimetria])        
    else:
        print("La simetria en la palabra " + cadena)
        print("No tiene simetria")
    return puntoSimetria
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
        cadena_sample= lambda a:str(cadena[i])
        #Calculo del tiempo de complejidad de las cadenas creadas
        beast, others = big_o.big_o(sinRepeticion,cadena_sample)     
    #imprime tiempo de complejidad
    print(beast)


if __name__ == '__main__':
    #decalracion de variable de entrada
    cadena = ingresoCadena()
    #invertir cadena
    StrInver = invertirStr(cadena)
    #punto de simetria
    
    puntoSimetria = StrpuntoSimetria(cadena,StrInver)
    printComplexTiempo(cadena)
    
