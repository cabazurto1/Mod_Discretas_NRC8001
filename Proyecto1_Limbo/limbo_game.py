"""
Descripción:
Se adapto el juego tradicional limbo, donde originalmente al ritmo de la música el jugador
debe cruzar una barra que según el nivel baja, la modificación que se realizo fue que el 
usuario responda tres preguntas matemáticas básicas si son correctas pasara el nivel de la 
barra, y si falla una pierde el juego.

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""

def finDeJuego():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al perder el juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||         FIN DEL JUEGO       ||\n")
    print("||           PERDISTE          ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||             :C              ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("*************************************\n")
    print("\n")


def nivelUno():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al primer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||=============================||\n")
    print("||                 __          ||\n")
    print("||                |  |         ||\n")
    print("||                |__|         ||\n")
    print("||               /             ||\n")
    print("||        |_____/              ||\n")
    print("||        _____/               ||\n")
    print("||       |    |                ||\n")
    print("||       |    |                ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelDos():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al segundo nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||                 __ ___      ||\n")
    print("||         |______/  |___|     ||\n")
    print("||          _____/             ||\n")
    print("||         /    /              ||\n")
    print("||        /    /               ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelTres():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al tercer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||           \___________      ||\n")
    print("||        ______|   |____|     ||\n")
    print("||     __|   __|               ||\n")
    print("*************************************\n")
    print("\n")

def reglas():
    """
    Es un procedimiento que nos muestra una impresión correspondiente a las reglas del juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("_______________________________________________________________\n")
    print("Este juego contara de 3 preguntas, referenciando a 3 niveles,\n")
    print("si respones una pregunta bien podras pasar la barra del limbo\n")
    print("en caso de que falles una perderas.\n")
    print("_______________________________________________________________\n")


def perteneceFibonacci(num1):
    """
    Es un procedimiento que nos permite determinar si un numero pertenece a la serie de Fibonacci
    Parametros:
    ------------
        Tiene parametros de entrada, num1 (Es numero que se quiere saber si pertenece a la serie de Fibonacci)
    
    Retorna:
    ------------
        si retorna un valor, esFibonacci (Si el numero pertenece es True, caso contrario False)
    """
    #Inicializa valores, a = 0 y b =1, para iniciar la serie de Fibonacci
    a, b = 0,1
    #Inicializa la variable n = 100, representando el limite de la serie
    n=100
    #Inicializa la variable  esFibonacci=False
    esFibonacci=False
    #Inicio del bucle, serie de Fibonacci
    while a < n:
        #Asigna valores de a = b y b=a+b
        a, b = b, a+b
        #Si a es igual al numero ingresado (num1) entoces
        if a == num1:
            #Se asigana a esFibonacci=True, el numero ingresa si pertenece a la serie
            esFibonacci=True
            #Retorna el valor de esFibonacci
            return esFibonacci
    #Retorna el valor de esFibonacci
    return esFibonacci
#Inicializa variables paso de nivel correspondiente al nivel, todas en False
pasoPrimernivel = False
pasoSegundonivel = False
pasoTercernivel = False
#Imprime inicio del juego
print("------------------------------------------\n")
print("                  BIENVENIDO              \n")
print("                JUEGO DEL LIMBO           \n")
print("------------------------------------------\n")
#Imprime las reglas del juego
reglas()
#Imprime mensaje de ingreso de nombre del jugador y asigna el nombre a nombreJugador
nombreJugador = input("Por favor ingrese su nombre: ")
#Imprime mensaje del primer nivel del limbo
print("Nivel 1: Ingrese 2 numeros pares diferentes\n")
#Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
primerNumero = int(input("Por favor ingrese el primer numero: "))
#Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
segundoNumero = int(input("Por favor ingrese el segundo numero: "))
#Si los dos numeros ingresados son pares y no se repiten entonces
if (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
    #Imprime que se paso el nivel uno
    nivelUno()
    #Asigna pase de nivel 1 a verdero
    pasoPrimernivel = True
else:
    #Imprime el fin del juego
    finDeJuego()
#Si paso el primer nivel entonces
if(pasoPrimernivel == True):
    #Imprime mensaje del segundo nivel del limbo
    print("Nivel 2: Ingrese 2 numeros de la serie de fibonacci diferentes\n")
    #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
    primerNumero = int(input("Por favor ingrese el primer numero: "))
    #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
    segundoNumero = int(input("Por favor ingrese el segundo numero: "))
    #si los dos nuemeros son diferentes y pertencen a la serie entonces
    if (pasoPrimernivel == True) and (perteneceFibonacci(primerNumero)==True)and (perteneceFibonacci(segundoNumero)==True) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel dos
        nivelDos()
        #Asigna pase de nivel 2 a verdero
        pasoSegundonivel = True
    else:
        #Imprime el fin del juego
        finDeJuego()
#si paso el segundo nivel entonces
if(pasoSegundonivel == True):
    #Imprime mensaje del tercer nivel del limbo
    print("Nivel 3: Ingrese 2 numeros de la serie de fibonacci que sean pares y diferentes\n")
    #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
    primerNumero = int(input("Por favor ingrese el primer numero: "))
    #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
    segundoNumero = int(input("Por favor ingrese el segundo numero: "))
    #si los dos numeros ingresados son diferentes y pares y pertencen a la serie de fibonacci entonces
    if(pasoSegundonivel == True) and (perteneceFibonacci(primerNumero)==True) and (perteneceFibonacci(segundoNumero)==True) and (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel tres
        nivelTres()
        #Asigna pase de nivel 3 a verdero
        pasoTercernivel = True
        #Imprime mensaje de ganar el juego
        print("------------------------------------------\n")
        print("                  FELICIDADES             \n")
        print("          GANASTE " + nombreJugador +" \n")
        print("             EL JUEGO DEL LIMBO           \n")
        print("------------------------------------------\n")
    else:
        #Imprime el fin del juego
        finDeJuego()  
    
 

    


    
     

    

 



