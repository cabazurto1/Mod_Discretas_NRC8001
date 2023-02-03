"""
Laboratorio 1 - 3P

Descripción: Programar Agente Sistema de automatización de tráfico

Autor:
Christopher Amek Bazurto Mora

Verisión:
VER.1.0.0
"""
import big_o
def SistemaAutomatizacionTrafico(vias):
    """
    Es un procedimiento que nos determina el costo de las vias, para controlar el trafico
    Parametros:
    ------------
        Tiene  un parámetro de entrada vias
    
    Retorna:
    ------------
        Retorna un parámetro costo
    """
    # Inicializa un contador para el costo
    costo = 0
      # Recorre cada par de clave-valor en el diccionario "vias"
    for via, estado in vias.items():
        # Si la vía está cerrada (estado igual a 1)
        if estado == 1:
            # Aumenta el costo en 1
            costo += 1
    return costo

def imprimirEstadoVias(vias):
    """
    Es un procedimiento nos permite imprimir el estado de las vias
    Parametros:
    ------------
        Tiene  un parámetro de entrada vias
    
    Retorna:
    ------------
        No retorna un parámetro 
    """
      # Recorre cada par de clave-valor en el diccionario "vias"
    for via, estado in vias.items():
        # Si la vía está cerrada (estado igual a 1)
        if estado == 1:
            #impireme la via si esta cerrada
            print(via +" cerrada aumenta costo +1")
            


def ingresoViasEstado():
    """
    Es un procedimiento que nos permite ingresar el estado de una via
    Parametros:
    ------------
        No tiene  un parámetro de entrada 
    
    Retorna:
    ------------
        Retorna un parámetro vias(diccionario)
    """
    # Inicializa el diccionario de vías
    vias = {  'Quito': 0,  'Esmeraldas': 0,  'Guayaquil': 0,  'Machala': 0}
    # Crea una lista de las claves de las vías
    keys = list(vias.keys())
    # Inicializa un índice para recorrer las claves
    index = 0
    # Repite hasta que se hayan actualizado todas las vías
    while index < len(keys):
        # Obtiene la clave de la vía en el índice actual
        key = keys[index]
        # Pide al usuario el estado de la vía
        val = input(f"Introduzca el estado de la vía '{key}' (1 para cerrada y 0 para abierta): ")
        # Valida la entrada
        while val != "1" and val != "0":
            print("Entrada inválida. Introduzca 1 para cerrada y 0 para abierta.")
            val = input(f"Introduzca el estado de la vía '{key}' (1 para cerrada y 0 para abierta): ")
        # Actualiza el estado de la vía
        vias[key] = int(val)
        # Avanza al siguiente índice
        index += 1
    # Devuelve el diccionario actualizado
    return vias



if __name__ =='__main__':
    #imprimir titulo
    print("--------------------------------------\n")
    print("Sistema de automatización de tráfico\n")
    print("--------------------------------------\n")
    #ingreso de estdos de las vias
    vias = ingresoViasEstado()
    #calculo de los costos
    costo = SistemaAutomatizacionTrafico(vias)
    #imprimir estado de vias
    imprimirEstadoVias(vias)
    #imprimir costo total
    print("El costo total: "+ str(costo))
    #crea una función lambda que recibe como parametro la lista y la guarda en una variable
    vias_samples= lambda a:vias
    #Calculo del tiempo de complejidad de las cadenas creadas
    best, others = big_o.big_o(SistemaAutomatizacionTrafico,vias_samples)
    print(best)