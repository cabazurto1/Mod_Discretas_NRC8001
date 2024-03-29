
def medirDesempeno(lapiz):
    """
    Es un procedimiento para medir Desempeño del Lapiz.
    Parametros:
    ------------
       Tiene  un parámetro de entrada lapiz
    Retorna:
    ------------
        Devuelve Desempeño lapiz
    """
    # Inicializa un contador para la precisión en la detección de la posición y la traducción a texto digital
    precision = 0
    # Inicializa un contador para la velocidad de reconocimiento de escritura y transcripción
    velocidad = 0
    # Inicializa un contador para el nivel de integración con otros dispositivos
    integracion = 0
    # Inicializa un contador para la duración de la batería y tiempo de carga
    bateria = 0
    # Inicializa un contador para la calidad de la escritura y la sensibilidad a la presión
    calidad = 0
    # Inicializa un contador para la funcionalidad adicional
    funcionalidad = 0
    # Inicializa un contador para la facilidad de uso y configuración
    facilidad = 0
    # Inicializa un contador para el precio y valor
    precio = 0
    
    # Verifica la precisión en la detección de la posición y la traducción a texto digital
    if lapiz['precision'] >= 0.9:
        precision += 1
    # Verifica la velocidad de reconocimiento de escritura y transcripción
    if lapiz['velocidad'] >= 100:
        velocidad += 1
    # Verifica el nivel de integración con otros dispositivos
    if lapiz['integracion'] >= 0.8:
        integracion += 1
    # Verifica la duración de la batería y tiempo de carga
    if lapiz['bateria'] >= 5:
        bateria += 1
    # Verifica la calidad de la escritura y la sensibilidad a la presión
    if lapiz['calidad'] >= 0.8:
        calidad += 1
    # Verifica la funcionalidad adicional
    if lapiz['funcionalidad'] == True:
        funcionalidad += 1
    # Verifica la facilidad de uso y configuración
    if lapiz['facilidad'] >= 0.8:
        facilidad += 1
    # Verifica el precio y valor
    if lapiz['precio'] <= 50:
        precio += 1
        
    # Calcula la puntuación total del desempeño
    puntuacionDesempe = precision + velocidad + integracion + bateria + calidad + funcionalidad + facilidad + precio
    return puntuacionDesempe

def validarPrecision(precision):
    """
    Es un procedimiento para validar Precision
    Parametros:
    ------------
       Tiene un parámetro de entrada Precision
    Retorna:
    ------------
        Devuelve Precision entero 
    """
    try:
        precision = float(precision)
        if 0 <= precision <= 1:
            return True
        else:
            print("Error: la precisión debe ser un número entre 0 y 1.")
            return False
    except ValueError:
        print("Error: la precisión debe ser un número.")
        return False

def validarVelocidad(velocidad):
    """
    Es un procedimiento para validar velocidad.
    Parametros:
    ------------
       Tiene un parámetro de entrada velocidad
    Retorna:
    ------------
        Devuelve velocidad entero 
    """
    try:
        velocidad = int(velocidad)
        if velocidad > 0:
            return True
        else:
            print("Error: la velocidad debe ser un número entero positivo.")
            return False
    except ValueError:
        print("Error: la velocidad debe ser un número entero.")
        return False

# Función que valida el parámetro de integración
def validarIntegracion(integracion):
    """
    Es un procedimiento para validar Integracion.
    Parametros:
    ------------
       Tiene un parámetro de entrada Integracion
    Retorna:
    ------------
        Devuelve Integracion entero 
    """
    while True:
        try:
            integracion = int(integracion)
            # Si integracion no está en el rango de 1 a 5, se genera un error
            if integracion < 1 or integracion > 5:
                raise ValueError
            return integracion
        except ValueError:
            # Si se genera un error, se pide al usuario que ingrese el valor de integración nuevamente
            integracion = input("Error: el valor de integración debe ser un número entero entre 1 y 5. Inténtelo de nuevo: ")

# Función que valida el parámetro de batería
def validarBateria(bateria):
    """
    Es un procedimiento para validar Bateria.
    Parametros:
    ------------
       Tiene un parámetro de entrada Bateria
    Retorna:
    ------------
        Devuelve Bateria entero 
    """
    while True:
        try:
            bateria = int(bateria)
            return bateria
        except ValueError:
            # Si se genera un error, se pide al usuario que ingrese el valor de batería nuevamente
            bateria = input("Error: el valor de batería debe ser un número entero. Inténtelo de nuevo: ")

# Función que valida el parámetro de calidad
def validarCalidad(calidad):
    """
    Es un procedimiento para validar Calidad.
    Parametros:
    ------------
       Tiene un parámetro de entrada Calidad
    Retorna:
    ------------
        Devuelve Calidad entero 
    """
    while True:
        try:
            calidad = int(calidad)
            # Si calidad no está en el rango de 1 a 10, se genera un error
            if calidad < 1 or calidad > 10:
                raise ValueError
            return calidad
        except ValueError:
            # Si se genera un error, se pide al usuario que ingrese el valor de calidad nuevamente
            calidad = input("Error: el valor de calidad debe ser un número entero entre 1 y 10. Inténtelo de nuevo: ")

# Función que valida el parámetro de funcionalidad
def validarFuncionalidad(funcionalidad):
    """
    Es un procedimiento para validar Funcionalidad.
    Parametros:
    ------------
       Tiene un parámetro de entrada Funcionalidad
    Retorna:
    ------------
        Devuelve Funcionalidad 
    """
    while True:
        # Se convierte funcionalidad a minúsculas para permitir 'Sí' y 'sí' como entrada válida
        funcionalidad = funcionalidad.lower()
        if funcionalidad == "si" or funcionalidad == "no":
            # Si funcionalidad es 'sí', se retorna True, de lo contrario, False
            return funcionalidad == "si"
        else:
            # Si se genera un error, se pide al usuario que ingrese el valor de funcionalidad nuevamente
            funcionalidad = input("Error: por favor ingrese 'Sí' o 'No'. Inténtelo de nuevo: ")

def validarFacilidad(facilidad):
    """
    Es un procedimiento para validar facilidad.
    Parametros:
    ------------
       Tiene un parámetro de entradafacilidad
    Retorna:
    ------------
        Devuelve facilidad fotante
    """
    while True:
        try:
            facilidad = int(facilidad)
            if facilidad < 1 or facilidad > 10:
                raise ValueError
            return facilidad
        except ValueError:
            facilidad = input("Error: el valor de facilidad debe ser un número entero entre 1 y 10. Inténtelo de nuevo: ")

def validarPrecio(precio):
    """
    Es un procedimiento para validar el Precio.
    Parametros:
    ------------
       Tiene un parámetro de entrada precio
    Retorna:
    ------------
        Devuelve precio fotante
    """
    # In
    while True:
        try:
            precio = float(precio)
            return precio
        except ValueError:
            precio = input("Error: el valor de precio debe ser un número decimal. Inténtelo de nuevo: ")



def ingresarParametrosLapiz():
    """
    Es un procedimiento para ingresar Parametros Lapiz.
    Parametros:
    ------------
       No Tiene  parámetros de entrada
    Retorna:
    ------------
        Devuelve un diccionario lapiz
    """
    # Inicializa el diccionario de parámetros del lápiz inteligente
    lapiz = {'precision': 0, 'velocidad': 0, 'integracion': 0, 'bateria': 0, 'calidad': 0, 'funcionalidad': False, 'facilidad': 0, 'precio': 0}
    # Pide al usuario que ingrese los parámetros del lápiz
    lapiz['precision'] = validarPrecision(input("Ingrese la precisión en la detección de la posición en la hoja y en la traducción a texto digital (un número entre 0 y 1): "))
    lapiz['velocidad'] = validarVelocidad(input("Ingrese la velocidad de reconocimiento de escritura y transcripción (en palabras por minuto): "))
    lapiz['integracion'] = validarIntegracion(input("Ingrese el nivel de integración con otros dispositivos y aplicaciones (un número entre 1 y 5): "))
    lapiz['bateria'] = validarBateria(input("Ingrese la duración de la batería (en horas): "))
    lapiz['calidad'] = validarCalidad(input("Ingrese la calidad de los materiales y la construcción del lápiz (un número entre 1 y 10): "))
    lapiz['funcionalidad'] = validarFuncionalidad(input("¿El lápiz tiene funcionalidades adicionales? (Si o No): ").lower()) == 'si'
    if lapiz['funcionalidad']:
        lapiz['facilidad'] = validarFacilidad(input("Ingrese la facilidad de uso de las funcionalidades adicionales (un número entre 1 y 10): "))
        lapiz['precio'] = validarPrecio(input("Ingrese el precio del lápiz en dólares: "))
    return lapiz

def calcularPuntuacionLapiz(lapiz):
    """
    Es un procedimiento para calcular Puntuacion del Lapiz.
    Parametros:
    ------------
        Tiene un parámetro de entrada lapiz
    
    Retorna:
    ------------
        Devuelve puntuacion
    """
    # Inicializa la puntuación en cero
    puntuacion = 0
    # Precision
    if lapiz['precision'] >= 0.8:
        puntuacion += 3
    elif lapiz['precision'] >= 0.6:
        puntuacion += 2
    elif lapiz['precision'] >= 0.4:
        puntuacion += 1
    # Velocidad
    if lapiz['velocidad'] >= 80:
        puntuacion += 3
    elif lapiz['velocidad'] >= 60:
        puntuacion += 2
    elif lapiz['velocidad'] >= 40:
        puntuacion += 1
    # Integración
    if lapiz['integracion'] >= 4:
        puntuacion += 3
    elif lapiz['integracion'] >= 3:
        puntuacion += 2
    elif lapiz['integracion'] >= 2:
        puntuacion += 1
    # Batería
    if lapiz['bateria'] >= 8:
        puntuacion += 3
    elif lapiz['bateria'] >= 6:
        puntuacion += 2
    elif lapiz['bateria'] >= 4:
        puntuacion += 1
    # Calidad
    if lapiz['calidad'] >= 8:
        puntuacion += 3
    elif lapiz['calidad'] >= 6:
        puntuacion += 2
    elif lapiz['calidad'] >= 4:
        puntuacion += 1
    # Funcionalidad
    if lapiz['funcionalidad']:
        if lapiz['facilidad'] >= 8:
            puntuacion += 3
        elif lapiz['facilidad'] >= 6:
            puntuacion += 2
        elif lapiz['facilidad'] >= 4:
            puntuacion += 1
    # Precio
    if lapiz['precio'] <= 50:
        puntuacion += 3
    elif lapiz['precio'] <= 100:
        puntuacion += 2
    elif lapiz['precio'] <= 150:
        puntuacion += 1
    return puntuacion

def calcularCalidad(lapiz):
    """
    Es un procedimiento para calcular la caliodad del Lapiz.
    Parametros:
    ------------
        Tiene un parámetro de entrada lapiz
    
    Retorna:
    ------------
        Devuelve calidad
    """
    # Calcula la calidad del lápiz según los parámetros ingresados
    calidad = 1.0
    # Se reducen puntos por baja precisión
    if lapiz['precision'] < 0.8:
        calidad -= 0.2
    elif lapiz['precision'] < 0.9:
        calidad -= 0.1
    # Se reducen puntos por baja velocidad
    if lapiz['velocidad'] < 60:
        calidad -= 0.2
    elif lapiz['velocidad'] < 80:
        calidad -= 0.1
    # Se reducen puntos por falta de integración
    if lapiz['integracion'] == 0:
        calidad -= 0.3
    elif lapiz['integracion'] == 1:
        calidad -= 0.1
    # Se reducen puntos por baja duración de la batería
    if lapiz['bateria'] < 6:
        calidad -= 0.2
    elif lapiz['bateria'] < 10:
        calidad -= 0.1
    # Se reducen puntos por mala calidad
    if lapiz['calidad'] < 8:
        calidad -= 0.2
    elif lapiz['calidad'] < 9:
        calidad -= 0.1
    # Se reducen puntos por falta de facilidad de uso
    if lapiz['facilidad'] < 8:
        calidad -= 0.2
    elif lapiz['facilidad'] < 9:
        calidad -= 0.1
    # Se reducen puntos por alto precio
    if lapiz['precio'] > 150:
        calidad -= 0.2
    elif lapiz['precio'] > 100:
        calidad -= 0.1
    # Si el lápiz es incompatible con el sistema operativo, se reduce la calidad en un 20%
    if not lapiz['funcionalidad']:
        calidad *= 0.8
    # La calidad no puede ser menor a 0
    calidad = max(calidad, 0)
    return calidad

def crearGrafo(nodos, aristas):
    """
    Es un procedimiento  crea Grafos.
    Parametros:
    ------------
        Tiene dos parámetros de entrada (nodos, aristas)
    
    Retorna:
    ------------
        Devuelve grafo
    """
    # Creamos el diccionario de nombres de los nodos
    nombres_nodos = {i+1: nodo for i, nodo in enumerate(nodos)}

    # Creamos el grafo utilizando un diccionario de listas de adyacencia
    grafo = {nodo: [] for nodo in nodos}
    # Creamos las aristas del grafo
    for arista in aristas:
        # Agregamos las aristas en una dirección
        grafo[arista[0]].append(arista[1])
        grafo[arista[1]].append(arista[0])
    return grafo


def menu():
    """
    Crea un grafo a partir de una lista de nodos y una lista de aristas.

    Args:
        nodos (list): Lista de nombres de los nodos del grafo.
        aristas (list): Lista de pares de nombres de nodos que indican las aristas del grafo.

    Returns:
        dict: Un diccionario que representa el grafo, donde las llaves son los nombres de los nodos y los valores son
        listas de los nombres de los nodos adyacentes.

    """
    while True:
        print("---Proyecto U3---")
        print("1. Agente inteligente")
        print("2. Grafo")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            # Acción para la opción "Agente inteligente"
            #ingreso de parámetros del lápiz
            lapiz = ingresarParametrosLapiz()
            #calcular calidad del lápiz
            calidad = calcularCalidad(lapiz)
            puntuacionDesempe = medirDesempeno(lapiz)
            costos = calcularPuntuacionLapiz(lapiz)
            #imprimir resultado
            print("La calidad del lápiz es: "+ str(calidad))
            print("La desempeño del lápiz es: "+ str(puntuacionDesempe))
            print("La costos del lápiz es: "+ str(costos))
        elif opcion == "2":
            # Acción para la opción "Grafo"
            #Crear nodos
            nodos = ["Lápiz inteligente", "Sensores", "Información de escritura", "Procesamiento de lenguaje natural", "Análisis morfológico",
                        "Análisis sintáctico", "Modelos de lenguaje", "Detección de errores ortográficos", "Comparación con diccionario",
                        "Palabras correctamente escritas", "Palabras mal escritas", "Notificación de error", "Usuario",
                        "Interfaz de usuario", "Base de datos de palabras", "Algoritmos de detección de errores", "Preprocesamiento de datos",
                        "Filtros de datos", "Aprendizaje automático", "Entrenamiento del modelo"]
            #Crear aristas
            aristas = [("Lápiz inteligente", "Sensores"), ("Lápiz inteligente", "Información de escritura"),
                        ("Lápiz inteligente", "Procesamiento de lenguaje natural"), ("Sensores", "Información de escritura"),
                        ("Información de escritura", "Procesamiento de lenguaje natural"), ("Procesamiento de lenguaje natural", "Análisis morfológico"),
                        ("Procesamiento de lenguaje natural", "Análisis sintáctico"), ("Procesamiento de lenguaje natural", "Modelos de lenguaje"),
                        ("Procesamiento de lenguaje natural", "Detección de errores ortográficos"), ("Procesamiento de lenguaje natural", "Comparación con diccionario"),
                        ("Análisis morfológico", "Procesamiento de lenguaje natural"), ("Análisis sintáctico", "Procesamiento de lenguaje natural"),
                        ("Modelos de lenguaje", "Procesamiento de lenguaje natural"), ("Detección de errores ortográficos", "Procesamiento de lenguaje natural"),
                        ("Detección de errores ortográficos", "Comparación con diccionario"), ("Detección de errores ortográficos", "Notificación de error"),
                        ("Comparación con diccionario", "Procesamiento de lenguaje natural"), ("Comparación con diccionario","Palabras correctamente escritas"), ("Comparación con diccionario", "Palabras mal escritas"),
                        ("Palabras correctamente escritas", "Comparación con diccionario"), ("Palabras mal escritas", "Comparación con diccionario"),
                        ("Palabras mal escritas", "Notificación de error"), ("Notificación de error", "Detección de errores ortográficos"),
                        ("Notificación de error", "Palabras mal escritas"), ("Notificación de error", "Usuario"),
                        ("Notificación de error", "Interfaz de usuario"), ("Usuario", "Notificación de error"),
                        ("Interfaz de usuario", "Notificación de error"), ("Base de datos de palabras", "Palabras correctamente escritas"),
                        ("Base de datos de palabras", "Palabras mal escritas"), ("Algoritmos de detección de errores", "Detección de errores ortográficos"),
                        ("Algoritmos de detección de errores", "Preprocesamiento de datos"), ("Algoritmos de detección de errores", "Filtros de datos"),
                        ("Algoritmos de detección de errores", "Aprendizaje automático"), ("Preprocesamiento de datos", "Algoritmos de detección de errores"),
                        ("Filtros de datos", "Algoritmos de detección de errores"), ("Aprendizaje automático", "Algoritmos de detección de errores")]
            #Crea grafo
            grafo = crearGrafo(nodos, aristas)
            print("Grafo:")
            #imprimir grafo
            for key, value in grafo.items():
                print(key, ":", value)
           
        elif opcion == "3":
            # Acción para la opción "Salir"
            print("Saliendo")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ =='__main__':
    #llama la funcion menu 
    menu()

    
    

