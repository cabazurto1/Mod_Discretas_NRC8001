"""
Reto codility
Tema: Parking Bill
Descripción: El usuario ingresa las horas de llegada(HH:MM) y salida del parqueadro
calcula el pago.

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
import re
import big_o
def numerosEnStr(cadena):
    """
    Es un procedimiento que nos permite extraer numeros de una cadena
    Parametros:
    ------------
        Tiene un parámetro de entrada  cadena
    
    Retorna:
    ------------
        Retorna arreglo con los numeros extraidos
    """
    #asigna numStr los numeros de tipo entero de la cadena 
    numStr = [int(numStr) for numStr in re.findall(r'-?\d+\.?\d*', cadena)]
    #retorna cadena
    return numStr

def ingresoHora(tiempo):
    """
    Es un procedimiento que nos permite ingresar horas en forma de HH:MM
    Parametros:
    ------------
        Tiene un parámetro de entrada  tiempo
    
    Retorna:
    ------------
        Retorna arreglo con los HH y MM
    """
    #inicio de bucle
    while True:
        #Ingreso de HH:MM
        horaStr =  input("Ingrese la hora de "+tiempo+" :  ")
        #Si la longitud del arreglo ingresado es igual a HH:MM entonces
        if len(horaStr) == len("HH:MM"):
            #Crea arreglo con las HH y MM ingresadas
            numStr= numerosEnStr(horaStr)
            #si las horas HH  estan en [0 -24] y los minutos MM   estan en [0 -60]
            if (int(numStr[0]) >= 0) and  (int(numStr[0]) <= 24) and (int(numStr[1]) >= 0) and  (int(numStr[1]) <= 60):
                #retorna el arreglo  de HH y MM
                return numStr
            else:
                #imprimir error
               print("Ingrese Horas(H) [0-24] y Minutos(M) [0-60]")
        else:
            #imprimir error
            print("Ingrese la hora en el formato HH:MM donde H(horas) y M(minutos)")

def calMulta(numStrIngreso,numStrsalida):
    """
    Es un procedimiento que nos permite calcular el pago del parqueadero en funcion
    a las horas de entra y salida
    Parametros:
    ------------
        Tiene dos parámetros de entrada  (numStrIngreso,numStrsalida)
    
    Retorna:
    ------------
        Retorna el valor a pagar del parqueadero
    """
    #inicializamos pago en -1
    pago = -1
    #si la hora de salida es mayor o igual a la de llegada (posision de la horas) entonces
    if numStrIngreso[0] <= numStrsalida[0]:
        #si  las horas y minutos son iguales
        if(numStrIngreso[0]==numStrsalida[0]) and (numStrIngreso[1]==numStrsalida[1]):
            #imprimir que no ingresado al parqueadero
            print("Usted no ha ingresado al parqueadero el pago es: 0" )
            #retorna pago 
            return pago
        else:
            #si los minutos de salida son mayor a 15 entonces:
            if (numStrsalida[1] > 15):
                #agregue numsalida una hora de salida mas 
                numsalida = numStrsalida[0]+1
            else:
                #caso contrario asigne a numsalida las horas de salida
                numsalida=  numStrsalida[0]
            #si los minutos de entrada son mayor a 15 entonces:
            if (numStrIngreso[1] > 15):
                #agregue numingreso una hora  mas
                numingreso = numStrIngreso[0]+1
            else:
                #caso contrario asigne a numingresolas horas de salida
                numingreso=  numStrIngreso[0]
            #tiempo de uso es la diferencia entre las horas de salida y entrada
            tiempoUso = abs(numsalida-numingreso)
            #calculo del pago
            pago = 2 +  3 +((tiempoUso-1)*4)
            #imprimir resultados
            print("Usted ha ingresado al parqueadero por "+str(tiempoUso) +" horas el pago es: "+str(pago))
            #retorna pago
            return pago
    else:
        #imprimir que las horas ingresadas no son validas
        print("Porfavor ingrese una hora de salida valida")
        #retorna pago
        return pago
def calMultas(cadenaString):
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
def printComplexTiempo(pagoStr):
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
    longA= len(pagoStr)
    #inicio del bucle hasta la longitud de la cadena 
    for i in range(longA):
        pagoStr_sample= lambda a:str(pagoStr[i])
        #Calculo del tiempo de complejidad de las cadenas creadas
        beast, others = big_o.big_o(calMultas,pagoStr_sample)     
    #imprime tiempo de complejidad
    print(beast) 

if __name__ == '__main__':
    #ingreso de datos
    numStrIngreso = ingresoHora("Llegada")
    numStrsalida = ingresoHora("Salida")
    #calculo del pago
    pago = calMulta(numStrIngreso,numStrsalida)
    #tiempo de complejidad
    printComplexTiempo(str(pago))


