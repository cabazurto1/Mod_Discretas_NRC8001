"""
Laboratorio #1 - 2P
Ejercicio #13
Descripción: Preguntar al usuario su nombre y lo salude con su nombre.
Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
def ingresonombre():
    """
    Es un procedimiento que nos permite ingresar el nombre de una persona
    Parametros:
    ------------
        No tiene  parámetro de entrada 
    
    Retorna:
    ------------
        Retorna el nombre validado
    """
    #Bucle del ingreso de 
    while True:
        #Ingreso del dato 
        print("\n--------------------------------------------------------------\n")
        nombre = input("Ingrese El nombre:  ")
        print("\n--------------------------------------------------------------\n")
        #si el dato ingresado es un espacio
        if nombre == "":
             #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("        No hay dato ingresado, intente de nuevo   \n")
            print("--------------------------------------------------------------\n") 
        else:
            return nombre

def saludo(nombre):
    """
    Es un procedimiento que nos permite realizar un saludo con el nombre ingresado
    Parametros:
    ------------
        Tiene un parámetro de entrada nombre 
    
    Retorna:
    ------------
        No retorna nada
    """
    #imprime saludo
    print("Hola " + nombre +" ten un buen dia y toma mucha agua. Adios")

if __name__ == '__main__':
    print("--------------------------------------------------------------\n")
    print("                     Saludo con nombre       \n")
    print("--------------------------------------------------------------\n")
    #inicializo variables 
    nombre = ingresonombre()
    #imprimo saludo
    saludo(nombre)
   
