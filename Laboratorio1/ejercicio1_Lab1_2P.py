"""
Laboratorio #1 - 2P
Ejercicio #1
Descripción: Preguntar al usuario por el número de horas trabajadas y el coste por hora. 

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""


def validadorEnteros(num):
    """
    Es un procedimiento que nos determina si un dato ingresado(numero) es un digito
    si lo es retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    Parametros:
    ------------
        Tiene  un parámetro de entrada (num)
    
    Retorna:
    ------------
        Retorna  el número entero o false en caso de no ser entero
    """
    #inicializa validador de numero en falso
    numeroValido = False
    # si el numero ingresado es un digito entonces
    if num.isdigit():
        #validador en verdadero (True)
        numeroValido = True
        #retorna el numero 
        return int(num)
    else:
        #retorna validador en False
        return numeroValido

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

def ingresoHorasTrabajadas():
    """
    Es un procedimiento que nos permite ingresar  las horas trabajadas 
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna numero flotante
    """
    #Bucle del ingreso de datos 
    while True:
        #Ingreso del dato 
        print("\n--------------------------------------------------------------\n")
        horasTrabajadas = input("Ingrese horas trabajadas:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un entero entonces
        if validadorEnteros(horasTrabajadas) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero entero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            return horasTrabajadas

def ingresoCosteXHora():
    """
    Es un procedimiento que nos permite ingresar  el costo de las horas trabajdas
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
        costeXHora = input("Ingrese el coste por hora:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un flotante entonces
        if validarFloat(costeXHora) == False:
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        El dato ingresado no es un numero, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            #si el numero es flotante y > 0
            if float(costeXHora) >= 0:
                #retorna el numero
                return costeXHora
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("    El dato ingresado no es un numero >= 0, intente de nuevo   \n")
                print("--------------------------------------------------------------\n") 

def calculaHorasPagadas(horasTrabajadas,costeXHora):
    """
    Es un procedimiento que nos permite calcular las ganancias por las trabajadas
    Parametros:
    ------------
        Tiene  dos parametros de entrada horasTrabajadas, costeXHora
    
    Retorna:
    ------------
        Retorna el número ganacias generadas
    """
    horasPagadas = float(horasTrabajadas)*float(costeXHora)
    return float(horasPagadas)

if __name__ == '__main__':
    #Asignación de las horas trabajadas ingresadas
    horasTrabajadas= ingresoHorasTrabajadas()
    #Asignación del ingreso de costo por hora a coste por hora 
    costeXHora =  ingresoCosteXHora()
    # asignacion de las horas calculadas a horas pagadas
    horasPagadas = calculaHorasPagadas(horasTrabajadas,costeXHora)
    #impresion de los datos ingresados
    print("--------------------------------------------------------------\n")
    print("Las horas trabajadas son " + str(horasTrabajadas) + " y el coste por hora "+ str(costeXHora) +" genera una ganancia de: " + str(horasPagadas) + "$")
    print("--------------------------------------------------------------\n")
