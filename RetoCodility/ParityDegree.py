"""
Reto codility
Tema: Parity Degrre
Descripción: El usuario ingresa el numero de elementos de un arreglo y regresa el primer numero no repetitivo

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
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

def ingresoNum():
    """
    Es un procedimiento que nos permite ingresar un numero entero positivo 
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
        num = input("Ingrese el numero:  ")
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

def numDivision(num):
    """
    Es un procedimiento que nos determina el numero de divisiones de un entero
    Parametros:
    ------------
        Tiene  un parámetro de entrada (num)
    
    Retorna:
    ------------
        Retorna el numero de divisiones
    """
    #inicializamos contador en 0
    cont =0
    #inicio bucle
    while True:
        #si el modulo de num % 2 es 0 entonces
        if(num % 2 == 0):
            #num es igual a num div 2 
           num=num/2
           #aumenta cont + 1 
           cont += 1
        else:
            #termina bucle
            break
    #retorna contador
    return cont

if __name__ == '__main__':
    #entrada de datos
    num = ingresoNum()
    #calculo de las diviciones
    numDiv=numDivision(num)
    #imprimir resultados
    print("El numero de divisiones de "+str(num)+" es: "+str(numDiv))
    #crear sample depruebas
    num_sumple= lambda a:num
    #Calculo del tiempo de complejidad 
    beast, others = big_o.big_o(numDivision,num_sumple)     
    #imprime tiempo de complejidad
    print(beast)
 
    