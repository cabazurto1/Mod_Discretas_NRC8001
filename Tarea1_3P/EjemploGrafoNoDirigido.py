"""
Tarea #1 - 3P
Ejemplo #1
Descripción: 
Ejemplo de aplicación de un grafo no dirigido en una red social(Twitter).

Autor: 
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""

def seguimientos(aristas):
    """
    Es un procedimiento imprimer los seguimientos de una red social(Twitter).
    Parametros:
    ------------
        Tiene un parámetro de entrada (aristas)
    
    Retorna:
    ------------
        No Retorna nada 
    """
    # Recorremos cada usuario en el diccionario "aristas"
    for usuario, seguidos in aristas.items():
        # Imprimimos el nombre del usuario y a quienes sigue
        print(f"{usuario} sigue a {seguidos}")

if __name__ == '__main__':
    print("Ejemplo de aplicación de un grafo no dirigido")
    # Definimos el conjunto de vértices (usuarios)
    vertices = ['Pablo', 'Pedro', 'Maria', 'Juan', 'Ana']
    # Definimos el conjunto de aristas (seguimientos)
    aristas = {
    'Pablo': ['Pedro', 'Maria'],
    'Pedro': ['Maria', 'Juan'],
    'Maria': ['Juan'],
    'Juan': ['Ana'],
    'Ana': ['Pablo']
    }
    # Llamamos a la función "seguimientos" y le pasamos el diccionario "aristas"
    seguimientos(aristas)
