
import time
import sys

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
def ingresoOpc():
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
        print("\n------------------------------\n")
        num = input("Ingrese la Opcion:  ")
        print("\n------------------------------\n")
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


################################################################################
#Menu
################################################################################
def menu():
    print("----Menu de progrmas----")
    print("1. Inventario versión (Cliente)")
    print("2. Inventario versión (Test)")
    print("3. Salir")
    opcion = int(ingresoOpc())
    if opcion == 1:
        exec(open('invetarioApanadoClient.py').read())
    elif opcion == 2:
        exec(open('invetarioApanado.py').read())
    elif opcion == 3:
        salir()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu()

def salir():
    """
    Este código define una función llamada "salir" que imprime una cuenta regresiva de 5 segundos antes de imprimir un mensaje de despedida.
    Parametros:
    ------------
        No tiene parámetro 
    
    Retorna:
    ------------
        No Retorna  
    """
    # Utiliza un bucle "for" con la función "range" para contar desde 5 hasta 1 con un intervalo de decremento de 1 en cada iteración
    for i in range(5, 0, -1):
        # Imprime un mensaje con el tiempo restante antes de salir del inventario
        print(f"\rSaliendo del Menu en {i} segundos...", end="")
        # Utiliza la función "flush" de "sys.stdout" para vaciar la salida antes de que transcurra el tiempo especificado en "time.sleep"
        # para que el contador sea visible en tiempo real
        sys.stdout.flush()
        # Utiliza la función "sleep" de "time" para detener la ejecución durante 1 segundo antes de continuar con la siguiente iteración
        time.sleep(1)
    # Imprime un mensaje de despedida al finalizar la cuenta regresiva
    print("\n\n¡Regresa Pronto! :3\n")

if __name__ == '__main__':
    menu()