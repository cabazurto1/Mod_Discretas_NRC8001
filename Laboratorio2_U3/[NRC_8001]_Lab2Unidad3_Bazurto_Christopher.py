"""
Taller #4- 3P
Ejercicio #2
Descripción: Ejercicio de grafos busqueda general 

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
def buscadorRuta(inicio, meta, ruta1, ruta2):
    """
    Es un procedimiento que nos permite conocer las rutas y el costo de cada una
    Parametros:
    ------------
        Tiene 4 parámetros de entrada: inicio, meta, ruta1, ruta2
    
    Retorna:
    ------------
        Retorna dos parámetros: la primera ruta y su costo, y la segunda ruta y su costo.
    """
    # Inicializar el contador de costo para cada ruta
    cost1 = 0
    cost2 = 0
    # Verificar el costo de la primera ruta
    for i in range(len(ruta1)):
        # Sumar el costo de cada segmento de la ruta
        cost1 += ruta1[i][2] 
        # Verificar si llegamos a la meta
        if ruta1[i][1] == meta: 
          # De ser así, detener el cálculo del costo
          break 
    # Verificar el costo de la segunda ruta
    for i in range(len(ruta2)):
        # Sumar el costo de cada segmento de la ruta
        cost2 += ruta2[i][2] 
        # Verificar si llegamos a la meta
        if ruta2[i][1] == meta: 
          # De ser así, detener el cálculo del costo
          break 
    # Devolver las rutas y sus costos
    return (ruta1, cost1), (ruta2, cost2)

if __name__ == '__main__':
    #Rutas 
    ruta1 = [("ESPE", "U. Catolica", 1), ("U. Catolica", "Quicentro",2)]
    ruta2 = [("ESPE", "El Ejido", 1), ("El Ejido", "CCI", 2),
            ("CCI", "Quicentro", 3)]
    #inicio 
    inicio = "ESPE"
    #fin
    meta = "Quicentro" 
    # Llamada a la función
    rutasCosto = buscadorRuta(inicio, meta, ruta1, ruta2)
    # Mostrar las rutas y sus costos
    print("Rutas:")
    for i, ruta in enumerate(rutasCosto):
      print(f"Ruta {i + 1}: {ruta[0]} (costo: {ruta[1]})")