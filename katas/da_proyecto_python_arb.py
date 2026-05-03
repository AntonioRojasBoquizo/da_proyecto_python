# ===================================
# ===================================
# DATA & ANALYTICS V3  
# MÓDULO 6 | 🐍 Python
# DataProject | Lógica. Katas Python
# Autor | Antonio Rojas Boquizo
# ===================================
# ===================================




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 01
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena.  
# Los espacios no deben ser considerados.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función frecuencia_letras.
def frecuencia_letras(texto):
    """
    Función que recibe una cadena de texto y devuelve un diccionario con las frecuencias de cada letra en la cadena.
    Los espacios no son tenidos en cuenta.
    Se ignoran las diferencias entre mayúsculas y minúsculas.

    Args:
        - texto (str): Cadena de texto a analizar.

    Returns:
        - dict: Diccionario cuyas claves son las letras de la cadena de texto y los valores su frecuencia de aparición. 
    """


                    # Se crea un diccionario vacío para almacenar las letras de la cadena de texto y su frecuencia de aparición.
    diccionario_letras_frecuencias = {}
                    # Se hace uso del método lower() para convertir todos los caracteres de la cadena de texto original a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.
    texto_minus = texto.lower()


                    # Se utiliza un bucle for para recorrer cada carácter de la cadena de texto (en minúsculas).
    for caracter in texto_minus:


                    # Se emplea un condicional if para evaluar si el carácter actual de la cadena de texto es un espacio.
        if caracter == " ":
                    # En caso afirmativo, se pasa a la siguiente iteración (siguiente carácter de la cadena de texto) sin hacer nada.     
            continue
                    # Se emplea un condicional elif para evaluar si el carácter actual, cuando no cumple la primera condición (el carácter actual no es un espacio),
                    # ya existe como clave dentro del diccionario.
        elif caracter in diccionario_letras_frecuencias:
                    # En caso afirmativo, se incrementa en 1 el valor asociado a dicha clave (se aumenta en una unidad la frecuencia de aparición del carácter actual).
            diccionario_letras_frecuencias [caracter] += 1
                    # Si el carácter actual no cumple las dos condiciones previas (el carácter actual no es un espacio ni existe aún como clave dentro del diccionario),
        else:
                    # Se añade el carácter actual como una clave del diccionario y se le asigna el valor 1.
            diccionario_letras_frecuencias [caracter] = 1


                    # Por último, la función devuelve el diccionario cuyas claves son las letras de la cadena de texto y los valores su frecuencia de aparición. 
    return diccionario_letras_frecuencias


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean dos cadenas de texto (str).
texto1 = "en un lugar de la mancha"
texto2 = "En un lugar de la Mancha"


                    # Se llama a la función con las cadenas de texto como argumentos y se muestra el resultado.
print("")
print("")
print("====================================================================================================")
print("KATA 01")
print("====================================================================================================")                                                    
print("==========")
print(f"Cadena de texto original ----------> {texto1}")
print(f"Diccionario obtenido --------------> {frecuencia_letras(texto1)}")
print("==========")
print(f"Cadena de texto original ----------> {texto2}")
print(f"Diccionario obtenido --------------> {frecuencia_letras(texto2)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 01
# ====================================================================================================
# Cadena de texto original ----------> en un lugar de la mancha
# Diccionario obtenido --------------> {'e': 2, 'n': 3, 'u': 2, 'l': 2, 'g': 1, 'a': 4, 'r': 1, 'd': 1, 'm': 1, 'c': 1, 'h': 1}
# ==========
# Cadena de texto original ----------> En un lugar de la Mancha
# Diccionario obtenido --------------> {'e': 2, 'n': 3, 'u': 2, 'l': 2, 'g': 1, 'a': 4, 'r': 1, 'd': 1, 'm': 1, 'c': 1, 'h': 1}
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 02
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.  
# Usa la función map()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# PROGRAMA 
# ====================================================================================================

                    # Se crea la lista (list) de números (int, float) dada.
lista_numeros1 = [1, 2, 3.3, 4.4]
                    # Se define una función lambda que recibe un número (int, float) y devuelve su doble (int, float).
                    # Se hace uso de la función map() para aplicar la función lambda a cada elemento de la lista de números original.
                    # La función map() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list(). 
lista_dobles = list(map(lambda numero: 2*numero, lista_numeros1))


# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA
# ====================================================================================================

                    # Se ejecuta el programa y se muestra el resultado.
print("====================================================================================================")
print("KATA 02")
print("====================================================================================================")
print("==========")
print(f"Lista de números original ----------------> {lista_numeros1}")
print(f"Nueva lista de números obtenida ----------> {lista_dobles}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 02
# ====================================================================================================
# ==========
# Lista de números original ----------------> [1, 2, 3.3, 4.4]
# Nueva lista de números obtenida ----------> [2, 4, 6.6, 8.8]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 03
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.  
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función palabra_en_lista.
def palabra_en_lista(lista_palabras, palabra_objetivo):
    """
    Función que recibe una lista de palabras y una palabra objetivo, y devuelve una lista con todas las palabras de la lista original
    que contienen la palabra objetivo.

    Args:
        - lista_palabras (list): Lista de palabras (str) en las que va a buscarse la palabra objetivo.
        - palabra_objetivo (str): Palabra que va a buscarse en las palabras de la lista original.

    Returns:
        - list: Lista de palabras (str) con todas las palabras de la lista de palabras original que contienen la palabra objetivo. 
    """


                    # Se crea una lista vacía para almacenar las palabras de la lista original que contienen la palabra objetivo.
    lista_con_palabra = []


                    # Se utiliza un bucle for para recorrer cada palabra de la lista de palabras original.
    for palabra in lista_palabras:      


                    # Se emplea un condicional if para evaluar si la palabra objetivo está contenida en la palabra actual de la lista de palabras.
        if palabra_objetivo in palabra:
                    # En caso afirmativo, se hace uso del método append() para añadir la palabra actual a la lista de palabras que contienen la palabra objetivo.
            lista_con_palabra.append(palabra)

            
                    # Por último, la función devuelve la lista con todas las palabras de la lista original que contienen la palabra objetivo.
    return lista_con_palabra


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de palabras (str) y varias palabras objetivo (str).
lista_palabras1 = ["marinero", "remar", "amargo", "dulce", "marea", "amarillo", "martillo", "azul", "clavo", "submarino"]
palabra1 = "mar"
palabra2 = "amar"
palabra3 = "verde"


                    # Se llama a la función con la lista de palabras y las palabras objetivo como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 03")
print("====================================================================================================") 
print("==========")
print("Lista de palabras original")
print(lista_palabras1)
print("==========")
print(f"Lista de palabras que contienen la palabra {palabra1}")
print(palabra_en_lista(lista_palabras1, palabra1))
print("==========")
print(f"Lista de palabras que contienen la palabra {palabra2}")
print(palabra_en_lista(lista_palabras1, palabra2))
print("==========")
print(f"Lista de palabras que contienen la palabra {palabra3}")
print(palabra_en_lista(lista_palabras1, palabra3))
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 03
# ====================================================================================================
# ==========
# Lista de palabras original
# ['marinero', 'remar', 'amargo', 'dulce', 'marea', 'amarillo', 'martillo', 'azul', 'clavo', 'submarino']
# ==========
# Lista de palabras que contienen la palabra mar
# ['marinero', 'remar', 'amargo', 'marea', 'amarillo', 'martillo', 'submarino']
# ==========
# Lista de palabras que contienen la palabra amar
# ['amargo', 'amarillo']
# ==========
# Lista de palabras que contienen la palabra verde
# []
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 04
# Genera una función que calcule la diferencia entre los valores de dos listas.  
# Usa la función map()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función restar_listas.
def restar_listas(lista1, lista2):
    """
    Función que recibe dos listas de números, calcula la diferencia entre los valores de dichas listas y devuelve el resultado en forma de lista de números. 

    Args:
        - lista1 (list): Lista de números (int, float) a cuyos elementos le van a ser restados los elementos de lista de números lista2.
        - lista2 (list): Lista de números (int, float) cuyos elementos van a ser restados a los elementos de la lista de números lista1.
    
    Returns:
        - list: Lista de números (int, float) cuyos elementos se obtienen restando a cada elemento de la lista1 el elemento correspondiente de la lista2.
    """


                    # Se define una función lambda que recibe dos números y devuelve su resta.
                    # Se hace uso de la función map() para aplicar la función lambda a cada elemento de la lista1 y de la lista2. 
                    # Las dos lista se recorren en paralelo, es decir, se resta el primer elemento de la lista1 y el primero de la lista2,
                    # el segundo elemento de la lista1 y el segundo de la lista 2, y así sucesivamente.
                    # La función map() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve la lista de números con la diferencia entre los valores de las dos listas originales.
    return list(map(lambda numero1,numero2: numero1-numero2, lista1, lista2))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean dos listas (list) de números (int, float).
lista_numeros1 = [40, 10, 30.3, 6.6]
lista_numeros2 = [10, 20, 4.4, 50.5]


                    # Se llama a la función con las listas de números como argumentos y se muestra el resultado.
print("")
print("====================================================================================================")
print("KATA 04")
print("====================================================================================================") 
print("==========")
print(f"Primera lista de números original ----------> {lista_numeros1}")
print(f"Segunda lista de números original ----------> {lista_numeros2}")
print(f"Nueva lista de números obtenida ------------> {restar_listas(lista_numeros1, lista_numeros2)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 04
# ====================================================================================================
# ==========
# Primera lista de números original ----------> [40, 10, 30.3, 6.6]
# Segunda lista de números original ----------> [10, 20, 4.4, 50.5]
# Nueva lista de números obtenida ------------> [30, -10, 25.9, -43.9]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 05
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5.  
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado.  
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función evaluar_media.
def evaluar_media(lista_numeros, nota_aprobado = 5):   
    """
    Función que recibe una lista de números y un valor opcional nota_aprobado, que por defecto es 5,
    y devuelve una tupla con la media de los números de la lista y un estado, 
    que será "aprobado" si la media iguala o supera el valor nota_aprobado o "suspenso" en caso contario.

    Args:
        - lista_numeros (list): Lista de números (int, float) con los valores cuya media va a calcularse.      
        - nota_aprobado (int, float): Valor de referencia para comparar la media de la lista de números.
                                      Si la media iguala o supera este valor el estado será "aprobado", en caso contrario el estado será "suspenso".
                                      Su valor por defecto es 5. 
                                 
    Returns:
        - tuple: Tupla que contiene la media de los números de la lista original (int, float) y el estado (str), que puede ser "aprobado" o "suspenso".
    """


                    # Se utiliza la función sum() para sumar todos los elementos de la lista de números.
                    # Se usa la función len() para contar la cantidad de elementos de la lista de números.
                    # Se calcula la media de los números de la lista original como el cociente de la suma de todos los números de la lista entre la longitud de dicha lista.
    media = sum(lista_numeros) / len(lista_numeros)


                    # Se emplea un condicional if para evaluar si la media iguala o supera el valor de referencia para el aprobado.
    if media >= nota_aprobado:
                    # En caso afirmativo, se crea la variable estado y se le asigna el valor "aprobado" (str).
        estado = "aprobado"
                    # Si la media no cumple la condición previa (media inferior al valor de referencia para el aprobado), 
    else:       
                    # Se crea la variable estado y se le asigna el valor "suspenso" (str).
        estado = "suspenso"


                    # Por último, la función devuelve una tupla que contiene la media de los números de la lista original (int, float) y el estado (str).
    return (media, estado)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias listas (list) de números (int, float).
lista_numeros1 = [2, 5, 4.5, 3.6]
lista_numeros2 = [5, 6.2, 7, 7.3]
lista_numeros3 = [8, 9, 7, 10, 8]


                    # Se llama a la función con las listas de números como argumentos, sin especificar ningún valor de nota de aprobado, y se muestra el resultado. 
                    # En este caso, al no indicarse un valor en la nota de aprobado, se hace uso del valor por defecto (5).
print("====================================================================================================")
print("KATA 05")
print("====================================================================================================") 
print("==========")
print(f"Nota de aprobado: 5")
print(f"Lista de notas: {lista_numeros1} ----------> Resultados: {evaluar_media(lista_numeros1)}")
print(f"Lista de notas: {lista_numeros2} ----------> Resultados: {evaluar_media(lista_numeros2)}")
print(f"Lista de notas: {lista_numeros3} ----------> Resultados: {evaluar_media(lista_numeros3)}")


                    # Se llama a la función con las listas de números como argumentos, especificando un valor de nota de aprobado de 6.5, y se muestra el resultado.
print("==========")
print(f"Nota de aprobado: 6.5")
print(f"Lista de notas: {lista_numeros1} ----------> Resultados: {evaluar_media(lista_numeros1,6.5)}")
print(f"Lista de notas: {lista_numeros2} ----------> Resultados: {evaluar_media(lista_numeros2,6.5)}")
print(f"Lista de notas: {lista_numeros3} ----------> Resultados: {evaluar_media(lista_numeros3,6.5)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 05
# ====================================================================================================
# ==========
# Nota de aprobado: 5
# Lista de notas: [2, 5, 4.5, 3.6] ----------> Resultados: (3.775, 'suspenso')
# Lista de notas: [5, 6.2, 7, 7.3] ----------> Resultados: (6.375, 'aprobado')
# Lista de notas: [8, 9, 7, 10, 8] ----------> Resultados: (8.4, 'aprobado')
# ==========
# Nota de aprobado: 6.5
# Lista de notas: [2, 5, 4.5, 3.6] ----------> Resultados: (3.775, 'suspenso')
# Lista de notas: [5, 6.2, 7, 7.3] ----------> Resultados: (6.375, 'suspenso')
# Lista de notas: [8, 9, 7, 10, 8] ----------> Resultados: (8.4, 'aprobado')
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 06
# Escribe una función que calcule el factorial de un número de manera recursiva.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función factorial.
def factorial(numero):
    """
    Función que recibe un número entero no negativo y devuelve su factorial.

    Args:
        - numero (int): Número entero mayor o igual a cero cuyo factorial se busca obtener. 

    Returns:
        - int: Factorial del número dado como parámetro de la función.
    """


                    # Caso base:
                    # Se emplea un condicional if para evaluar si el número actual es 0 o 1.
    if numero == 0 or numero == 1:
                    # En caso afirmativo, el resultado es 1.
        resultado = 1


                    # Caso recursivo:
                    # Si el número actual no cumple la condición previa (número mayor que 1),
    else:
                    # el resultado se obtiene multiplicando el número actual por el factorial del número anterior.
                    # Para ello, es necesario volver a llamar a la función factorial dentro de su ejecución (función recursiva).
        resultado = numero * factorial(numero - 1)


                    # Por último, la función devuelve el factorial del número original.
    return resultado


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varios números enteros no negativos (int). 
numero1 = 0
numero2 = 1
numero3 = 2 
numero4 = 3
numero5 = 4
numero6 = 5


                    # Se llama a la función con los números como argumentos y se muestran los resultados.
print("====================================================================================================")
print("KATA 06")
print("====================================================================================================")  
print("==========")
print(f'El factorial del número {numero1} es {factorial(numero1)}')
print(f'El factorial del número {numero2} es {factorial(numero2)}')
print(f'El factorial del número {numero3} es {factorial(numero3)}')
print(f'El factorial del número {numero4} es {factorial(numero4)}')
print(f'El factorial del número {numero5} es {factorial(numero5)}')
print(f'El factorial del número {numero6} es {factorial(numero6)}')
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 06
# ====================================================================================================
# ==========
# El factorial del número 0 es 1
# El factorial del número 1 es 1
# El factorial del número 2 es 2
# El factorial del número 3 es 6
# El factorial del número 4 es 24
# El factorial del número 5 es 120
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 07
# Genera una función que convierta una lista de tuplas a una lista de strings.  
# Usa la función map()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función tuplas_a_strings.
def tuplas_a_strings(lista_tuplas):
    """
    Función que convierte una lista de tuplas a una lista de strings.

    Args:
        - lista_tuplas (list): Lista de tuplas (tuple) que se busca convertir a una lista de strings.

    Returns:
        - list: Lista de strings (str) obtenida a partir de la lista de tuplas original. 
    """


                    # Se utiliza la función str() para convertir una tupla (tuple) a una cadena de texto (str).
                    # Se hace uso de la función map() para aplicar la función str() a cada elemento de la lista de tuplas original.
                    # La función map() devuelve un objeto iterable, para convertirlo en una lista se hace uso de la función list().
                    # Por último, la función devuelve la lista de strings obtenida a partir de la lista de tuplas original.
    return list(map(str, lista_tuplas))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de tuplas (tuple).
lista_tuplas1 = [(1, 2, 3.3, 4.4), (5.6, "sancho"), ("quijote", "dulcinea", True)]


                    # Se llama a la función con la lista de tuplas como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 07")
print("====================================================================================================")  
print("==========")
print(f"Lista de tuplas original -----------> {lista_tuplas1}")
print(f"Lista de strings obtenida ----------> {tuplas_a_strings(lista_tuplas1)}")
print("==========")
print(f"La lista de tuplas original es de tipo {type(lista_tuplas1)} y sus elementos son de tipo {type(lista_tuplas1[0])}")
print(f"La lista de strings obtenida es de tipo {type(tuplas_a_strings(lista_tuplas1))} y sus elementos son de tipo {type(tuplas_a_strings(lista_tuplas1)[0])}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 07
# ====================================================================================================
# ==========
# Lista de tuplas original -----------> [(1, 2, 3.3, 4.4), (5.6, 'sancho'), ('quijote', 'dulcinea', True)]
# Lista de strings obtenida ----------> ['(1, 2, 3.3, 4.4)', "(5.6, 'sancho')", "('quijote', 'dulcinea', True)"]
# ==========
# La lista de tuplas original es de tipo <class 'list'> y sus elementos son de tipo <class 'tuple'>
# La lista de strings obtenida es de tipo <class 'list'> y sus elementos son de tipo <class 'str'>
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 08
# Escribe un programa que pida al usuario dos números e intente dividirlos.  
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.  
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# PROGRAMA
# ====================================================================================================

                    # Se define un bloque try para contener el código que puede generar errores.
try:
                    # Se utiliza la función input() para pedir al usuario que introduzca el primer número (dividendo de la división).
                    # La función input() devuelve un string (str), para convertirlo a un número decimal se emplea la función float().
    numero1 = float(input("Por favor, introduzca el primer número (dividendo de la división):"))
                    # Se utiliza la función input() para pedir al usuario que introduzca el segundo número (divisor de la división).
                    # La función input() devuelve un string (str), para convertirlo en un número decimal se emplea la función float().
    numero2 = float(input("Por favor, introduzca el segundo número (divisor de la división):"))
                    # Se realiza la división del primer número entre el segundo y se almacena la solución en la variable resultado.
    resultado = numero1 / numero2


                    # Se define un bloque except para capturar el error en caso de que el usuario ingrese un valor no numérico.
except ValueError:
                    # Se muestra un mensaje que informa al usuario del motivo que impide realizar la división.
    print("====================================================================================================")
    print("KATA 08")
    print("====================================================================================================") 
    print("==========")
    print("La división no ha podido realizarse con éxito")
    print("Deben introducirse valores numéricos (int, float)")
    print("==========")
    print("")
    print("")


                    # Se define un bloque except para capturar el error en caso de que el usuario intente dividir entre cero.
except ZeroDivisionError:
                    # Se muestra un mensaje que informa al usuario del motivo que impide realizar la división.
    print("====================================================================================================")
    print("KATA 08")
    print("====================================================================================================") 
    print("==========")
    print("La división no ha podido realizarse con éxito")
    print("No se puede dividir entre cero")
    print("==========")
    print("")
    print("")


                    # Se define un bloque else cuyo código se ejecuta si no se produce ninguna excepción en el bloque try.
else:
                    # Se muestra un mensaje que informa al usuario del éxito de la división y de su resultado.
                    # Se emplea la funcion round() para redondear el resultado de la división (a dos decimales).
    print("====================================================================================================")
    print("KATA 08")
    print("====================================================================================================") 
    print("==========")
    print("División realizada con éxito")
    print(f"El resultado de dividir {numero1} entre {numero2} es {round(resultado,2)}")
    print("==========")
    print("")
    print("")


# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA 
# ====================================================================================================

                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Introducir 60 como primer número y 6.3 como segundo número.
# Output esperado:
# ====================================================================================================
# KATA 08
# ====================================================================================================
# ==========
# División realizada con éxito
# El resultado de dividir 60.0 entre 6.3 es 9.52
# ==========


                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Introducir la palabra libro como primer número.
# Output esperado:
# ====================================================================================================
# KATA 08
# ====================================================================================================
# ==========
# La división no ha podido realizarse con éxito
# Deben introducirse valores numéricos (int, float)
# ==========


                    # ==========
                    # Ejemplo 3
                    # ==========
                    # Introducir 60 como primer número y 0 como segundo número.
# Output esperado:
# ====================================================================================================
# KATA 08
# ====================================================================================================
# ==========
# La división no ha podido realizarse con éxito
# No se puede dividir entre cero
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 09
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.  
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].  
# Usa la función filter()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función excluir_mascotas.
def excluir_mascotas(lista_mascotas):
    """
    Función que recibe una lista de mascotas y devuelve una nueva lista excluyendo ciertas mascotas prohibidas en España.

    Args:
        - lista_mascotas (list): Lista de nombres de mascotas (str) a analizar.

    Returns:
        - list: Lista de nombres de mascotas (str) que incluye todas las mascotas de la lista original excepto aquellas que están prohibidas en España.
    """


                    # Se crea la lista (list) de mascotas prohibidas en España (str).
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


                    # Se define una función lambda que devuelve True si una mascota no está en la lista de mascotas prohibidas, y False en caso contrario.
                    # Se hace uso de la función filter() para aplicar la funcion lambda a cada elemento de la lista de mascotas original
                    # y conservar aquellas mascotas que cumplen la condición (True).
                    # La funcion filter() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve la nueva lista con todas las mascotas de la lista original excepto las incluidas en la lista de mascotas prohibidas.
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de mascotas (str).
lista_mascotas1 = ["Perro", "Gato", "Cocodrilo", "Rana", "Tigre"]


                    # Se llama a la función con la lista de mascotas como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 09")
print("====================================================================================================") 
print("==========")
print(f"Lista de mascotas prohibidas --------------> ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']")
print("==========")
print(f"Lista de mascotas original ----------------> {lista_mascotas1}")
print(f"Nueva lista de mascotas obtenida ----------> {excluir_mascotas(lista_mascotas1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 09
# ====================================================================================================
# ==========
# Lista de mascotas prohibidas --------------> ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']
# ==========
# Lista de mascotas original ----------------> ['Perro', 'Gato', 'Cocodrilo', 'Rana', 'Tigre']
# Nueva lista de mascotas obtenida ----------> ['Perro', 'Gato', 'Rana']
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 10
# Escribe una función que reciba una lista de números y calcule su promedio.  
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función promedio_lista.
def promedio_lista(lista_numeros):
    """
    Función que recibe una lista de números y devuelve su promedio.
    Si la lista está vacía, se lanza una excepción personalizada.

    Args:
        - lista_numeros (list): Lista de números (int, float) cuyo promedio se quiere calcular.

    Returns:
        - float: Promedio de los valores de la lista de números original.
    """


                    # Se usa la función len() para contar la cantidad de elementos de la lista de números.
                    # Se emplea un condicional if para evaluar si la la longitud de la lista de números es cero (lista vacía).
    if len(lista_numeros) == 0:
                    # En caso afirmativo, se lanza una excepción personalizada y se muestra un mensaje que informa al usuario del motivo que impide calcular el promedio.
        raise Exception ("La lista está vacía, no es posible calcular el promedio")
                    
                    
                    # Si la lista no cumple la condición previa (lista no vacía). 
    else:
                    # Se utiliza la función sum() para sumar todos los elementos de la lista de números.
                    # Se usa la función len() para contar la cantidad de elementos de la lista de números.
                    # Se calcula el promedio de los números de la lista original como el cociente de la suma de todos los números de la lista entre la longitud de dicha lista.
                    # Por último, la función devuelve el promedio obtenido.
        return sum(lista_numeros) / len(lista_numeros)
    
               
# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN Y MANEJO DEL ERROR 
# ====================================================================================================

                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Se crea una lista (list) de números (int, float) y se muestra en pantalla.
lista_numeros1 = [10, 20, 30.3, 40.44]
print("====================================================================================================")
print("KATA 10")
print("====================================================================================================") 
print("==========")
print(f"Lista de números original ----------> {lista_numeros1}")

                    # Se define un bloque try para contener el código que puede generar errores.
try:
                    # Se llama a la función con la lista de números como argumento y se muestra el resultado.
    print(f"Promedio ---------------------------> {promedio_lista(lista_numeros1)}")
    print("==========")

                    # Se define un bloque except para capturar la excepción (introducir una lista vacía).
except Exception as excepcion1:
                    # Se muestra un mensaje que informa al usuario del motivo que impide calcular el promedio.
    print(f"ERROR: {excepcion1}")
    print("==========")


# Output esperado:
# ====================================================================================================
# KATA 10
# ====================================================================================================
# ==========
# Lista de números original ----------> [10, 20, 30.3, 40.44]
# Promedio ---------------------------> 25.185
# ==========


                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Se crea una lista (list) de números (int, float) vacía.
lista_numeros2 = []
print("==========")
print(f"Lista de números original ----------> {lista_numeros2}")

                    # Se define un bloque try para contener el código que puede generar errores.
try:
                    # Se llama a la función con la lista de números como argumento y se muestra el resultado.
    print(f"Promedio ---------------------------> {promedio_lista(lista_numeros2)}")
    print("==========")

                    # Se define un bloque except para capturar la excepción (introducir una lista vacía).
except Exception as excepcion1:
                    # Se muestra un mensaje que informa al usuario del motivo que impide calcular el promedio.
    print(f"ERROR: {excepcion1}")
    print("==========")
    print("")
    print("")


# Output esperado:
# ==========
# Lista de números original ----------> []
# ERROR: La lista está vacía, no es posible calcular el promedio
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 11
# Escribe un programa que pida al usuario que introduzca su edad.  
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# PROGRAMA
# ====================================================================================================

                    # Se define un bloque try para contener el código que puede generar errores.
try:
                    # Se utiliza la función input() para pedir al usuario que introduzca su edad.
                    # La función input() devuelve un string (str), para convertirlo en un número entero se emplea la función int().
    edad_usuario = int(input("Por favor, introduzca su edad en años (Ejemplo: 30):"))
 

                    # Se emplea un condicional if para evaluar si el número introducido está fuera del rango esperado (menor que 0 o mayor que 120).
    if edad_usuario < 0 or edad_usuario > 120:
                    # En caso afirmativo, se muestra un mensaje que informa al usuario que el valor introducido está fuera del rango esperado.
        print("====================================================================================================")
        print("KATA 11")
        print("====================================================================================================") 
        print("==========")
        print(f"{edad_usuario} años es una edad fuera del rango esperado")
        print("==========")
        print("")
        print("")
                    # Si el número introducido no cumple la condición previa (número dentro del rango esperado).
    else:
                    # Se muestra un mensaje que recuerda la edad introducida.
        print("====================================================================================================")
        print("KATA 11")
        print("====================================================================================================")    
        print("==========")
        print(f"Su edad es {edad_usuario} años")
        print("==========")
        print("")
        print("")


                    # Se define un bloque except para capturar el error en caso de que el usuario ingrese un valor no numérico
except ValueError:
                    # Se muestra un mensaje que informa al usuario que el valor introducido no es válido
    print("====================================================================================================")
    print("KATA 11")
    print("====================================================================================================") 
    print("==========")
    print(f"El valor introducido no es válido")
    print("==========")
    print("")
    print("")
                



# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA 
# ====================================================================================================
 
                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Introducir 50.
# Output esperado:
# ====================================================================================================
# KATA 11
# ====================================================================================================
# ==========
# Su edad es 50 años
# ==========        


                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Introducir 150.
# Output esperado:
# ====================================================================================================
# KATA 11
# ====================================================================================================
# ==========
# 150 años es una edad fuera del rango esperado
# ==========


                    # ==========
                    # Ejemplo 3
                    # ==========
                    # Introducir la palabra 'libro'.
# Output esperado:
# ====================================================================================================
# KATA 11
# ====================================================================================================
# ==========
# El valor introducido no es válido
# ========== 




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 12
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.  
# Usa la función map()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función longitud_palabras.
def longitud_palabras(frase):
    """
    Función que recibe una frase, la separa en palabras y devuelve una lista con la longitud de cada palabra.

    Args:
        - frase (str): Frase a analizar. 

    Returns:
        - list: Lista de números (int) donde cada elemento es la longitud de una palabra de la frase dada.
    """


                    # Se hace uso del método split() para dividir la frase original (str) en palabras (str) y devolverlas en forma de lista (list).
                    # En este caso, no es necesario indicar ningún argumento dentro de split(), 
                    # ya que este método divide por defecto usando los espacios en blanco como separadores.
                              
                    # Se utiliza la función len() para contar el número de caracteres (la longitud) de una palabra.
                    # Se hace uso de la función map() para aplicar la función len() a cada elemento de la lista (list) de palabras (str) (a cada palabra de la frase).
                    # La función map() devuelve un objeto iterable, para convertirlo en una lista se hace uso de la función list().
                    # Por último, la función devuelve una lista con la longitud de cada palabra de la frase original.
    return list(map(len, frase.split()))




# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una frase (str).
frase1 = "Era la primera vez que viajaba sola"


                    # Se llama a la función con la frase como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 12")
print("====================================================================================================")                    
print("==========")
print(f"Frase original ---------------------------------> {frase1}")
print(f"Lista con la longitud de cada palabra ----------> {longitud_palabras(frase1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 12
# ====================================================================================================
# ==========
# Frase original ---------------------------------> Era la primera vez que viajaba sola
# Lista con la longitud de cada palabra ----------> [3, 2, 7, 3, 3, 7, 4]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 13
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.  
# Usa la función map()
#
# Nota: El término 'conjunto de caracteres' del enunciado se ha interpretado como un grupo de caracteres, no como un set en el sentido estricto de Python.  
# En cualquier caso, uno de los pasos iniciales de la solución propuesta consiste en convertir el conjunto de caracteres original en un set.**
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función tuplas_may_min.
def tuplas_may_min(caracteres):
    """
    Función que recibe un conjunto de caracteres (str) y devuelve una lista (list) de tuplas (tuple) con cada letra en mayúscula y en minúscula.
    Las letras repetidas aparecen en la lista de tuplas una única vez.

    Args:
        - caracteres (str): Conjunto de caracteres a analizar. 

    Returns:
        - list: Lista de tuplas (tuple) con cada letra del string en mayúscula y en minúscula. No se repiten caracteres en caso de que aparezcan más de una vez. 
    """


                    # Se emplea la función set() para convertir el conjunto de caracteres original en un set. 
                    # De este modo se consiguen eliminar las letras repetidas, pues los sets no pueden contener elementos duplicados.
    caracteres_unicos = set(caracteres)


                    # Se define una función lambda que recibe un carácter y devuelve una tupla con el carácter en maýuscula y en minúscula.
                    # Para cambiar un caracter a mayúsculas se utiliza el método upper() y para cambiarlo a minúsculas el método lower(). 
                    # Se hace uso de la función map() para aplicar la función lambda a cada caracter del set obtenido a partir del conjunto original.
                    # La función map() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve una lista de tuplas con cada letra del string en maýuscula y en minúscula, excluyendo caracteres repetidos.
    return list(map(lambda caracter: (caracter.upper(), caracter.lower()), caracteres_unicos))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea un conjunto de caracteres (str).
texto1 = "lazarillo"


                    # Se llama a la función con el conjunto de caracteres como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 13")
print("====================================================================================================") 
print("==========")
print(f"Conjunto de caracteres original ----------> {texto1}")
print(f"Lista de tuplas obtenida -----------------> {tuplas_may_min(texto1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 13
# ====================================================================================================
# ==========
# Conjunto de caracteres original ----------> lazarillo
# Lista de tuplas obtenida -----------------> [('L', 'l'), ('O', 'o'), ('R', 'r'), ('Z', 'z'), ('A', 'a'), ('I', 'i')]
# ==========


                    # Nota: Es importante tener en cuenta que en un set sus elementos están desordenados,
                    # por tanto, al haber trabajado con un set para no considerar elementos duplicados, 
                    # el orden de las tuplas en la lista de tuplas obtenida puede variar en cada ejecución.




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 14
# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.  
# Usa la función filter()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función palabras_comienzo
def palabras_comienzo(lista_palabras, letra):
    """
    Función que recibe una lista de palabras y una letra, y devuelve una lista con aquellas palabras de la lista original que comienzan por la letra dada.

    Args:
        - lista_palabras (list): Lista de palabras (str) a analizar.
        - letra (str): Letra inicial que se usará como filtro.

    Returns:
        - list: Lista de palabras (str) de la lista original que comienzan por la letra inicial dada.
    """


                    # Se emplea el método lower() para convertir en minúsculas tanto la primera letra de una palabra como la letra inicial dada,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.
                
                    # Se define una función lambda que devuelve True si la primera letra de una palabra coincide con la letra inicial dada, y False en caso contrario.
                    # Se hace uso de la función filter() para aplicar la funcion lambda a cada elemento de la lista de palabras original
                    # y conservar aquellas palabras que cumplen la condición (True).
                    # La funcion filter() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve la nueva lista que incluye solo las palabras de la lista original que comienzan por la letra inicial dada.
    return list(filter(lambda palabra: palabra[0].lower() == letra.lower(), lista_palabras))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de palabras (str) y varias letra iniciales de referencia (str).
lista_palabras1 = ["caballero", "Macondo", "Cervantes", "alba", "magia", "mariposa", "Adela", "Castilla"]
letra1 = "a"
letra2 = "C"
letra3 = "m"
letra4 = "z" 


                    # Se llama a la función con la lista de palabras y las letras iniciales como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 14")
print("====================================================================================================") 
print("==========")
print(f"Lista de palabras original -----------------------------> {lista_palabras1}")
print("==========")
print(f"Lista de palabras que empiezan por la letra {letra1} ----------> {palabras_comienzo(lista_palabras1, letra1)}")
print(f"Lista de palabras que empiezan por la letra {letra2} ----------> {palabras_comienzo(lista_palabras1, letra2)}")
print(f"Lista de palabras que empiezan por la letra {letra3} ----------> {palabras_comienzo(lista_palabras1, letra3)}")
print(f"Lista de palabras que empiezan por la letra {letra4} ----------> {palabras_comienzo(lista_palabras1, letra4)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 14
# ====================================================================================================
# ==========
# Lista de palabras original -----------------------------> ['caballero', 'Macondo', 'Cervantes', 'alba', 'magia', 'mariposa', 'Adela', 'Castilla']
# ==========
# Lista de palabras que empiezan por la letra a ----------> ['alba', 'Adela']
# Lista de palabras que empiezan por la letra C ----------> ['caballero', 'Cervantes', 'Castilla']
# Lista de palabras que empiezan por la letra m ----------> ['Macondo', 'magia', 'mariposa']
# Lista de palabras que empiezan por la letra z ----------> []
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 15
# Crea una función lambda que sume 3 a cada número de una lista dada.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define una función lambda llamada suma3 que recibe una lista (list) de números (int, float), suma 3 a cada elemento de dicha lista 
                    # y devuelve el resultado en forma de lista (list) de números (int, float).
                    # La nueva lista ha sido creada usando una list comprehension.
suma3 = lambda lista: [elemento + 3 for elemento in lista]


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de números (int, float).
lista_numeros1 = [1, 2, 3.3, 4.4]


                    # Se llama a la función con la lista de números como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 15")
print("====================================================================================================")       
print("==========")
print(f"Lista de números original ----------------> {lista_numeros1}")
print(f"Nueva lista de números obtenida ----------> {suma3(lista_numeros1)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 15
# ====================================================================================================
# ==========
# Lista de números original ----------------> [1, 2, 3.3, 4.4]
# Nueva lista de números obtenida ----------> [4, 5, 6.3, 7.4]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n.  
# Usa la función filter()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función palabras_long.
def palabras_long(texto, numero):
    """
    Función que recibe una cadena de texto y un número entero n, y devuelve una lista de todas las palabras de la cadena de texto formadas por más de n caracteres.

    Args:
        - texto (str): Cadena de texto con las palabras que van a ser filtradas en base a su número de caracteres.
        - numero (int): Número entero utilizado como referencia para filtrar las palabras de la cadena de texto original.     

    Returns:
        - list: Lista de palabras (str) de la cadena de texto original cuyo número de caracteres supera al número entero dado.
    """


                    # Se hace uso del método split() para dividir la cadena de texto original (str) en palabras (str) y devolverlas en forma de lista (list).
                    # En este caso, no es necesario indicar ningún argumento dentro de split(), 
                    # ya que este método divide por defecto usando los espacios en blanco como separadores. 
    lista_palabras = texto.split()


                    # Se utiliza la función len() para contar el número de caracteres (la longitud) de una palabra.
                    # Se define una funcion lambda que devuelve True si una palabra tiene un número de caracteres superior al número entero dado, y False en caso contrario.
                    # Se hace uso de la función filter() para aplicar la funcion lambda a cada elemento de la lista de palabras
                    # y conservar aquellas palabras que cumplen la condición (True).
                    # La funcion filter() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve la nueva lista con todas las palabras de la cadena de texto original cuyo número de caracteres supera al número entero dado.
    return list(filter(lambda palabra: len(palabra) > numero, lista_palabras))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean una cadena de texto (str) y varios números enteros (int).
cadena_texto1 = "En un lugar de la Mancha"
numero1 = 1
numero2 = 4
numero3 = 5
numero4 = 8


                    # Se llama a la función con la cadena de texto y los números enteros como argumentos y se muestra el resultado. 
print("====================================================================================================")
print("KATA 16")
print("====================================================================================================")      
print("==========")
print(f"Cadena de texto original ----------------------------> {cadena_texto1}")
print("==========")
print(f"Lista de palabras de longitud superior a {numero1} ----------> {palabras_long(cadena_texto1, numero1)}")
print(f"Lista de palabras de longitud superior a {numero2} ----------> {palabras_long(cadena_texto1, numero2)}")
print(f"Lista de palabras de longitud superior a {numero3} ----------> {palabras_long(cadena_texto1, numero3)}")
print(f"Lista de palabras de longitud superior a {numero4} ----------> {palabras_long(cadena_texto1, numero4)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 16
# ====================================================================================================
# ==========
# Cadena de texto original ----------------------------> En un lugar de la Mancha
# ==========
# Lista de palabras de longitud superior a 1 ----------> ['En', 'un', 'lugar', 'de', 'la', 'Mancha']
# Lista de palabras de longitud superior a 4 ----------> ['lugar', 'Mancha']
# Lista de palabras de longitud superior a 5 ----------> ['Mancha']
# Lista de palabras de longitud superior a 8 ----------> []
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 17
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572).  
# Usa la función reduce()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se importa la función reduce del módulo functools.
from functools import reduce


                    # Se define la función unir_digitos.
def unir_digitos(lista_digitos):
    """
    Función que recibe una lista de dígitos y devuelve el número correspondiente (Ejemplo: [5,7,2] -----> 572)

    Args:
        - lista_digitos (list): Lista de números enteros (int) entre 0 y 9 que representan los dígitos de un número.

    Returns:
        - int: Número entero obtenido al interpretar la lista de dígitos original.
    """


                    # Se define una función lambda que recibe dos números, multiplica el primero de ellos por 10 (es decir, lo desplaza una posición a la izquierda)
                    # y le suma el segundo número.
                    # Se hace uso de la función reduce() para aplicar la función lambda de forma acumulativa: primero entre los dos primeros elementos de la lista de dígitos,
                    # luego entre el resultado obtenido y el siguiente elemento, y así sucesivamente hasta recorrer toda la lista.
                    # Por último, la función devuelve el número asociado a los dígitos de la lista original.
    return reduce(lambda num1, num2: num1*10 + num2, lista_digitos)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de dígitos (int).
lista_digitos1 = [1, 6, 0, 5]


                    # Se llama a la función con la lista de dígitos como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 17")
print("====================================================================================================")      
print("==========")
print(f"Lista de dígitos original ----------> {lista_digitos1}")
print(f"Número obtenido --------------------> {unir_digitos(lista_digitos1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 17
# ====================================================================================================
# ==========
# Lista de dígitos original ----------> [1, 6, 0, 5]
# Número obtenido --------------------> 1605
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 18
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)  
# y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.  
# Usa la función filter()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# PROGRAMA 
# ====================================================================================================

                    # Se crea una lista (list) de diccionarios (dict) con información de estudiantes (nombre, edad, calificación).
lista_estudiantes = [
    {"nombre":"Emilia Castellanos", "edad":28, "calificacion":78},
    {"nombre":"Mario Lorca", "edad":27, "calificacion":91},
    {"nombre":"Isabel Vargas", "edad":30, "calificacion":96},
    {"nombre":"Federico Allende", "edad":20, "calificacion":89},
    {"nombre":"Rosario Pardo", "edad":23, "calificacion":90}]


                    # Se define una función lambda que devuelve True si un estudiante tiene una calificación igual o superior a 90, y False en caso contrario.
                    # Se hace uso de la función filter() para aplicar la función lambda a cada elemento de la lista de diccionarios (a cada estudiante)
                    # y conservar aquellos estudiantes que cumplen la condición (True).
                    # La función filter() devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve una lista de diccionarios con los estudiantes cuya calificación es igual o superior a 90.
estudiantes_cal90 = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))


# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA
# ====================================================================================================

                    # Se ejecuta el programa y se muestra el resultado.
print("====================================================================================================")
print("KATA 18")
print("====================================================================================================")                    
print("==========")
print("Estudiantes con una calificación mayor o igual a 90")
print("==========")


                    # Para mostrar los resultados en pantalla de forma clara, se utiliza un bucle for que recorre e imprime todos los elementos de la lista estudiantes_cal90,
                    # es decir, muestra en pantalla todos los estudiantes cuya calificación es igual o superior a 90. 
for estudiante in estudiantes_cal90:
    print(estudiante)
                    # Si desea mostrarse únicamente el nombre de los estudiantes basta sustituir 'print(estudiante)' por 'print(estudiante["nombre"])'.
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 18
# ====================================================================================================
# ==========
# Estudiantes con una calificación mayor o igual a 90
# ==========
# {'nombre': 'Mario Lorca', 'edad': 27, 'calificacion': 91}
# {'nombre': 'Isabel Vargas', 'edad': 30, 'calificacion': 96}
# {'nombre': 'Rosario Pardo', 'edad': 23, 'calificacion': 90}
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 19
# Crea una función lambda que filtre los números impares de una lista dada.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define una función lambda llamada filtrar_impares que recibe una lista (list) de números enteros (int),
                    # recorre cada elemento de la lista, comprueba si al dividirlo entre 2 el resto de la división es distinto de cero (es decir, comprueba si es impar),
                    # y devuelve una lista (list) de números enteros (int) donde solo aparecen los números impares de la lista original.
                    # La nueva lista ha sido creada usando una list comprehension.
filtrar_impares = lambda lista: [elemento for elemento in lista if elemento %2 !=0]


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de números enteros (int).
lista_enteros1 = [1, 2, 3, 4, 11, 22, 33, 44]
                    
                    
                    # Se llama a la función con la lista de números enteros como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 19")
print("====================================================================================================")    
print("==========")
print(f"Lista de números original ------------------> {lista_enteros1}")
print(f"Lista de números impares obtenida ----------> {filtrar_impares(lista_enteros1)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 19
# ====================================================================================================
# ==========
# Lista de números original ------------------> [1, 2, 3, 4, 11, 22, 33, 44]
# Lista de números impares obtenida ----------> [1, 3, 11, 33]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 20
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.  
# Usa la función filter()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función filtrar_int.
def filtrar_int(lista):
    """
    Función que recibe una lista con elementos tipo integer y string, y devuelve una nueva lista solo con los valores integer de la lista original.

    Args:
        - lista (list): Lista con elementos tipo integer (int) y string (str).

    Returns:
        - list: Lista con los elementos tipo integer (int) de la lista original.
    """


                    # Se utiliza la función type() para conocer el tipo de dato de cada elemento de la lista original (int o str en este caso).
                    # Se define la función lambda que devuelve True si un elemento de la lista original es de tipo int, y False en caso contrario.
                    # Se hace uso de la función filter() para aplicar la función lambda a cada elemento de la lista original
                    # y conservar aquellos elementos que cumplen la condición (True).
                    # La función filter devuelve un objeto iterable, para convertirlo en una lista se emplea la función list().
                    # Por último, la función devuelve una lista con los elementos tipo int de la lista original.
    return list(filter(lambda elemento: type(elemento) == int, lista))


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) con elementos tipo integer (int) y string (str).
lista1= ["soledad", 1967, 1945, "casa", "colmena", 1951]


                    # Se llama a la función con la lista como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 20")
print("====================================================================================================")
print("==========")
print(f"Lista original con elementos tipo integer y string ----------> {lista1}")
print(f"Nueva lista con elementos tipo integer ----------------------> {filtrar_int(lista1)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 20
# ====================================================================================================
# ==========
# Lista original con elementos tipo integer y string ----------> ['soledad', 1967, 1945, 'casa', 'colmena', 1951]
# Nueva lista con elementos tipo integer ----------------------> [1967, 1945, 1951]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 21
# Crea una función que calcule el cubo de un número dado mediante una función lambda.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define una función lambda llamada cubo que recibe un número (int, float) y devuelve su cubo (int, float).
cubo = lambda x: x**3


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varios números (int, float).
numero1 = 1
numero2 = 2
numero3 = -3
numero4 = 4.5


                    # Se llama a la función con los números como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 21")
print("====================================================================================================")
print("==========")
print(f"El cubo de {numero1} vale {cubo(numero1)}")
print(f"El cubo de {numero2} vale {cubo(numero2)}")
print(f"El cubo de {numero3} vale {cubo(numero3)}")
print(f"El cubo de {numero4} vale {cubo(numero4)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 21
# ====================================================================================================
# ==========
# El cubo de 1 vale 1
# El cubo de 2 vale 8
# El cubo de -3 vale -27
# El cubo de 4.5 vale 91.125
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 22
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.  
# Usa la función reduce()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se importa la función reduce del módulo functools.
from functools import reduce


                    # Se define la función multiplicar_lista.
def multiplicar_lista(lista_numeros):
    """
    Función que recibe una lista numérica y devuelve el producto total de los valores de dicha lista.

    Args:
        - lista_numeros (list): Lista de números (int, float) cuyo producto se quiere obtener.

    Returns:
        - int, float: Producto total (int, float) de los valores de la lista numérica original.
    """


                    # Se define una función lambda que recibe dos números y los multiplica.
                    # Se hace uso de la función reduce() para aplicar la función lambda de forma acumulativa: primero entre los dos primeros elementos de la lista de números,
                    # luego entre el resultado obtenido y el siguiente elemento, y así sucesivamente hasta recorrer toda la lista.
                    # Por último, la función devuelve el producto total de los valores de la lista numérica original.
    return reduce(lambda num1, num2: num1*num2, lista_numeros)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de números (int, float).
lista_numeros1 = [1, 2, 3, 4, 5.7]


                    # Se llama a la función con la lista de números como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 22")
print("====================================================================================================")
print("==========")
print(f"Lista de números original ----------> {lista_numeros1}")
print(f"Resultado obtenido -----------------> {multiplicar_lista(lista_numeros1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 22
# ====================================================================================================
# ==========
# Lista de números original ----------> [1, 2, 3, 4, 5.7]
# Resultado obtenido -----------------> 136.8
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 23
# Concatena una lista de palabras.  
# Usa la función reduce()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se importa la función reduce del módulo functools.
from functools import reduce


                    # Se define la función concatenar_palabras.
def concatenar_palabras(lista_palabras):
    """
    Función que recibe una lista de palabras y devuelve una cadena de texto con todas las palabras concatenadas y separadas por un espacio.

    Args:
        - lista_palabras (list): Lista de palabras (str) que se buscan concatenar.

    Returns:
        - str: Cadena de texto con todas las palabras de la lista original concatenadas y separadas por un espacio.
    """


                    # Se define una función lambda que recibe dos palabras y las concatena dejando un espacio entre ellas.
                    # Se hace uso de la función reduce() para aplicar la función lambda de forma acumulativa: primero entre los dos primeros elementos de la lista de palabras,
                    # luego entre el resultado obtenido y el siguiente elemento, y así sucesivamente hasta recorrer toda la lista de palabras.
                    # Por último, la función devuelve una cadena de texto con todas las palabras de la lista original concatenadas y separadas por un espacio. 
    return reduce(lambda pal1, pal2: pal1 + " " + pal2, lista_palabras)




# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crea una lista (list) de palabras (str).
lista_palabras1 = ["con", "cien", "cañones", "por", "banda"]


                    # Se llama a la función con la lista de palabras como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 23")
print("====================================================================================================")
print("==========")
print(f"Lista de palabras original ----------> {lista_palabras1}")
print(f"Resultado obtenido ------------------> {concatenar_palabras(lista_palabras1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 23
# ====================================================================================================
# ==========
# Lista de palabras original ----------> ['con', 'cien', 'cañones', 'por', 'banda']
# Resultado obtenido ------------------> con cien cañones por banda
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 24
# Calcula la diferencia total en los valores de una lista.  
# Usa la función reduce()
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se importa la función reduce del módulo functools.
from functools import reduce


                    # Se define la función diferencia_total.
def diferencia_total(lista_numeros):
    """
    Función que recibe una lista de números y devuelve la diferencia total de los valores de dicha lista.

    Args:
        - lista_numeros (list): Lista de números (int, float) cuya diferencia total se quiere obtener.

    Returns:
        - int, float: Diferencia total (int, float) de los valores de la lista numérica original.
    """


                    # Se define una función lambda que recibe dos números y calcula su diferencia.
                    # Se hace uso de la función reduce() para aplicar la función lambda de forma acumulativa: primero entre los dos primeros elementos de la lista de números,
                    # luego entre el resultado obtenido y el siguiente elemento, y así sucesivamente hasta recorrer toda la lista de números.
                    # Por último, la función devuelve la diferencia total de los valores de la lista numérica original.
    return reduce(lambda num1, num2: num1 - num2, lista_numeros)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias listas (list) de números (int, float).
lista_numeros1 = [100, 1, 2, 3, 4.6]
lista_numeros2 = [2, 4, 0, 23]


                    # Se llama a la función con las listas de números como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 24")
print("====================================================================================================")
print("==========")
print(f"Lista de números original ----------> {lista_numeros1}")
print(f"Resultado obtenido -----------------> {diferencia_total(lista_numeros1)}")
print("==========")
print(f"Lista de números original ----------> {lista_numeros2}")
print(f"Resultado obtenido -----------------> {diferencia_total(lista_numeros2)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 24
# ====================================================================================================
# ==========
# Lista de números original ----------> [100, 1, 2, 3, 4.6]
# Resultado obtenido -----------------> 89.4
# ==========
# Lista de números original ----------> [2, 4, 0, 23]
# Resultado obtenido -----------------> -25
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 25
# Crea una función que cuente el número de caracteres en una cadena de texto dada. 
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función contar_caracteres.
def contar_caracteres(texto):
    """
    Función que recibe una cadena de texto (str) y devuelve la cantidad de caracteres que contiene.

    Args:
        texto (str): Cadena de texto cuyos caracteres se quieren contar. 

    Returns:
        - int: Número de caracteres de la cadena de texto original.
    """


                    # Se emplea la función len() para determinar la longitud de la cadena de texto, es decir, el número de caracteres que contiene.
                    # Por último, la función devuelve el número de caracteres de la cadena de texto original.
    return len(texto)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias cadenas de texto (str).
texto1 = "casa"
texto2 = "En esta"
texto3 = "En esta casa no se vuelve a llorar"


                    # Se llama a la función con las cadenas de texto como argumentos y se muestra el resultado.        
print("====================================================================================================")
print("KATA 25")
print("====================================================================================================")
print("==========")
print(f"Cadena de texto original ----------------------------> {texto1}")
print(f"Número de caracteres de la cadena de texto ----------> {contar_caracteres(texto1)}")
print("==========")
print(f"Cadena de texto original ----------------------------> {texto2}")
print(f"Número de caracteres de la cadena de texto ----------> {contar_caracteres(texto2)}")
print("==========")
print(f"Cadena de texto original ----------------------------> {texto3}")
print(f"Número de caracteres de la cadena de texto ----------> {contar_caracteres(texto3)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 25
# ====================================================================================================
# ==========
# Cadena de texto original ----------------------------> casa
# Número de caracteres de la cadena de texto ----------> 4
# ==========
# Cadena de texto original ----------------------------> En esta
# Número de caracteres de la cadena de texto ----------> 7
# ==========
# Cadena de texto original ----------------------------> En esta casa no se vuelve a llorar
# Número de caracteres de la cadena de texto ----------> 34
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 26
# Crea una función lambda que calcule el resto de la división entre dos números dados.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define una función lambda llamada resto_division que recibe dos números enteros (int) y devuelve el resto de su división (int).
resto_division = lambda num1, num2: num1 % num2


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varios números enteros (int).
numero1 = 10
numero2 = 2
numero3 = 3


                    # Se llama a la función con los números como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 26")
print("====================================================================================================")                   
print("==========")
print(f"Ejemplo de división exacta")
print(f"El resto de la división de {numero1} entre {numero2} es {resto_division(numero1,numero2)}")
print("==========")    
print(f"Ejemplo de división no exacta")
print(f"El resto de la división de {numero1} entre {numero3} es {resto_division(numero1,numero3)}")
print("==========") 
print("")
print("")  


# Output esperado: 
# ====================================================================================================
# KATA 26
# ====================================================================================================
# ==========
# Ejemplo de división exacta
# El resto de la división de 10 entre 2 es 0
# ==========
# Ejemplo de división no exacta
# El resto de la división de 10 entre 3 es 1
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 27
# Crea una función que calcule el promedio de una lista de números.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función calcular_promedio.
def calcular_promedio(lista_numeros):
    """
    Función que recibe una lista de números y devuelve su promedio.

    Args:
        - lista_numeros (list): Lista de números (int, float) cuyo promedio se quiere calcular.

    Returns:
        - float: Promedio de los valores de la lista de números original.
    """


                    # Se utiliza la función sum() para sumar todos los elementos de la lista de números.
                    # Se usa la función len() para contar la cantidad de elementos de la lista de números.
                    # Se calcula el promedio de los números de la lista original como el cociente de la suma de todos los números de la lista entre la longitud de dicha lista.
                    # Por último, la función devuelve el promedio obtenido.
    return sum(lista_numeros) / len(lista_numeros)


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN  
# ====================================================================================================
               
                    # Se crean varias listas (list) de números (int, float). 
lista_numeros1 = [10, 20, 30, 40]
lista_numeros2 = [1.1, 2.2, 3.3, 4.4]


                    # Se llama a la función con las listas de números como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 27")
print("====================================================================================================")                    
print("==========")
print(f"Lista de números original ----------> {lista_numeros1}")
print(f"Promedio ---------------------------> {calcular_promedio(lista_numeros1)}")
print("==========")
print(f"Lista de números original ----------> {lista_numeros2}")
print(f"Promedio ---------------------------> {calcular_promedio(lista_numeros2)}")
print("==========")
print("")
print("")


# Output esperado: 
# ====================================================================================================
# KATA 27
# ====================================================================================================
# ==========
# Lista de números original ----------> [10, 20, 30, 40]
# Promedio ---------------------------> 25.0
# ==========
# Lista de números original ----------> [1.1, 2.2, 3.3, 4.4]
# Promedio ---------------------------> 2.75
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 28
# Crea una función que busque y devuelva el primer elemento duplicado de una lista dada. 
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función primer_duplicado.
def primer_duplicado(lista):
    """
    Función que recibe una lista y devuelve el primer elemento duplicado. 
    Si no hay elementos duplicados devuelve None.

    Args:
        - lista (list): Lista de elementos a analizar.

    Returns:
        Esta función puede devolver dos tipos de resultados:

        - Cualquier tipo de elemento de una lista (int, float, bool, str, ...): Si la lista contiene elementos duplicados, devuelve el primer elemento duplicado.

        - None: Si la lista no contiene elementos duplicados, la función devuelve None.
    """


                    # Se crea un set vacío para almacenar los elementos de la lista que han sido revisados.
    set_revisados = set()


                    # Se utiliza un bucle for para recorrer cada elemento de la lista.
    for elemento in lista:
                    # Se emplea un condicional if para evaluar si el elemento actual de la lista se encuentra en el set de los elementos que ya han sido revisados.
        if elemento in set_revisados:
                    # En caso afirmativo, la función devuelve el elemento actual (primer elemento duplicado) y finaliza su ejecución.
            return elemento
                    # Si el elemento actual no cumple la condición previa (el elemento no está en el set de elementos revisados),
        else:
                    # Se hace uso del método add() para añadir el elemento actual al set de elementos revisados.
            set_revisados.add(elemento)
                    # Por último, si ninguno de los elementos de lista está duplicado (y, por tanto, no se ha ejecutado el primer return), la función devuelve None.
    return None


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias listas (list).
lista1 = ["agua", "chocolate", 1989, "coronel", "agua", "carta", 1961]
lista2 = ["agua", "chocolate", 1989, "coronel", "carta", 1989, 1961]
lista3 = ["agua", "chocolate", 1989, "coronel", "carta", 1961]


                    # Se llama a la función con las listas como argumentos y se imprime el resultado.
print("====================================================================================================")
print("KATA 28")
print("====================================================================================================")  
print("==========")
print(f"Lista original ---------------------------------> {lista1}")
print(f"Primer elemento duplicado de la lista ----------> {primer_duplicado(lista1)}")
print("==========")
print(f"Lista original ---------------------------------> {lista2}")
print(f"Primer elemento duplicado de la lista ----------> {primer_duplicado(lista2)}")
print("==========")
print(f"Lista original ---------------------------------> {lista3}")
print(f"Primer elemento duplicado de la lista ----------> {primer_duplicado(lista3)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 28
# ====================================================================================================
# ==========
# Lista original ---------------------------------> ['agua', 'chocolate', 1989, 'coronel', 'agua', 'carta', 1961]
# Primer elemento duplicado de la lista ----------> agua
# ==========
# Lista original ---------------------------------> ['agua', 'chocolate', 1989, 'coronel', 'carta', 1989, 1961]
# Primer elemento duplicado de la lista ----------> 1989
# ==========
# Lista original ---------------------------------> ['agua', 'chocolate', 1989, 'coronel', 'carta', 1961]
# Primer elemento duplicado de la lista ----------> None
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 29
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función enmascarar.
def enmascarar(variable):
    """
    Función que recibe una variable, la convierte en una cadena de texto y enmascara todos los caracteres con el carácter #, excepto los últimos cuatro.

    Args:
        - variable (-): Variable de cualquier tipo que admita ser convertida a una cadena de texto (int, float, bool, str, ...).

    Returns:
        - str: Cadena de texto obtenida a partir de la variable original, donde todos sus carácteres han sido sustituidos por '#', excepto los últimos cuatro.
    """


                    # Se hace uso de la función str para convertir la variable original en una cadena de texto (str).
    texto = str(variable)


                    # Se utiliza la función len() para contar el número de caracteres de la cadena de texto obtenida. 
                    # Se emplea un condicional if para evaluar si la cadena de texto obtenida tiene 4 o menos caracteres. 
    if len(texto) <= 4:
                    # En caso afirmativo, el resultado es la cadena de texto obtenida.
        resultado = texto
                    # Si la cadena de texto no cumple la condición previa (cuenta con más de 4 caracteres),
    else:
                    # El resultado es una nueva cadena de texto de la misma longitud que la cadena de texto original donde:
                    # - todos sus caracteres excepto los últimos 4 son '#'. 
                    # - sus 4 últimos caracteres coinciden con los 4 últimos caracteres de la cadena de texto original.
        resultado = ("#"*(len(texto)-4)) + texto[-4:]
                    # Finalmente, la función devuelve el resultado obtenido.
    return resultado


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias variables de diversos tipos.
variable1 = 123456789                   # Variable de tipo int (con más de 4 caracteres)
variable2 = 1234                        # Variable de tipo int (con 4 o menos caracteres)
variable3 = 12345.06789                 # Variable de tipo float
variable4 = "macondo"                   # Variable de tipo str
variable5 = [1, 2, 3, 4]                # Variable de tipo list


                    # Se llama a la función con las variables como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 29")
print("====================================================================================================")  
print("==========")
print(f"Variable original -------------> {variable1}")
print(f"Variable enmascarada ----------> {enmascarar(variable1)}")
print("==========")
print(f"Variable original -------------> {variable2}")
print(f"Variable enmascarada ----------> {enmascarar(variable2)}")
print("==========")
print(f"Variable original -------------> {variable3}")
print(f"Variable enmascarada ----------> {enmascarar(variable3)}")
print("==========")
print(f"Variable original -------------> {variable4}")
print(f"Variable enmascarada ----------> {enmascarar(variable4)}")
print("==========")
print(f"Variable original -------------> {variable5}")
print(f"Variable enmascarada ----------> {enmascarar(variable5)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 29
# ====================================================================================================
# ==========
# Variable original -------------> 123456789
# Variable enmascarada ----------> #####6789
# ==========
# Variable original -------------> 1234
# Variable enmascarada ----------> 1234
# ==========
# Variable original -------------> 12345.06789
# Variable enmascarada ----------> #######6789
# ==========
# Variable original -------------> macondo
# Variable enmascarada ----------> ###ondo
# ==========
# Variable original -------------> [1, 2, 3, 4]
# Variable enmascarada ----------> ########, 4]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 30
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función anagramas.
def anagramas(palabra1, palabra2):
    """
    Función que recibe dos palabras, comprueba si son anagramas, y devuelve una tupla con el resultado en forma de mensaje de texto y en formato booleano.
    Se ignoran las diferencias entre mayúsculas y minúsculas.

    Args:
        - palabra1 (str): Primera palabra a analizar.
        - palabra2 (str): Segunda palabra a analizar.

    Returns:
        - tuple: Tupla de dos elementos 
                - Primer elemento (str): Mensaje que informa si las dos palabras son o no anagramas.
                - Segundo elemento (bool): Resultado del análisis en formato booleano (True si las dos palabras son anagramas, False si las dos palabras no son anagramas).    
    """


                    # Se hace uso del método lower() para convertir todos los caracteres de las palabras originales a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive)
                    # Se trata de un enfoque de programación defensiva.

                    # Se emplea la función sorted() para ordenar alfabéticamente los carácteres de las palabras (en minúsculas).
                    # En este caso, el resultado de sorted() es una lista de caracteres con las letras de la palabra ordenadas alfabéticamente.
    palabra_ordenada1 = sorted(palabra1.lower())
    palabra_ordenada2 = sorted(palabra2.lower())


                    # Se emplea un condicional if para evaluar si las listas de letras ordenadas de ambas palabras son iguales,
                    # situación que solo se produce cuando ambas palabras son anagramas. 
    if palabra_ordenada1 == palabra_ordenada2:
                    # En caso afirmativo, la función devuelve una tupla con un mensaje de texto informando que ambas palabras son anagramas y con el valor booleano True. 
        return ("Las palabras " + palabra1 + " y " + palabra2 + " son anagramas", True)
                    # Si ambas palabras no cumplen la condición previa (no son anagramas),
    else:
                    # La función devuelve una tupla con un mensaje de texto informando que ambas palabras no son anagramas y con el valor booleano False.
        return ("Las palabras " + palabra1 + " y " + palabra2 + " no son anagramas", False)
  

# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias palabras (str).
p1 = "amor"
p2 = "roma"
p3 = "Roma"
p4 = "remar"


                    # Se llama a la función con las palabras como argumento y se muestra el resultado.
print("====================================================================================================")
print("KATA 30")
print("====================================================================================================")  
print("==========")
print(anagramas(p1,p2)[0])
print(f"Resultado booleano ----------> {anagramas(p1,p2)[1]}")
print("==========")
print(anagramas(p1,p3)[0])
print(f"Resultado booleano ----------> {anagramas(p1,p3)[1]}")
print("==========")
print(anagramas(p1,p4)[0])
print(f"Resultado booleano ----------> {anagramas(p1,p4)[1]}")
print("==========")
print("")
print("")


# Output esperado
# ====================================================================================================
# KATA 30
# ====================================================================================================
# ==========
# Las palabras amor y roma son anagramas
# Resultado booleano ----------> True
# ==========
# Las palabras amor y Roma son anagramas
# Resultado booleano ----------> True
# ==========
# Las palabras amor y remar no son anagramas
# Resultado booleano ----------> False
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 31
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.  
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función buscar_nombre.
def buscar_nombre():
    """
    Función que solicita al usuario ingresar una lista de nombres y un nombre para buscar en esa lista. 
    Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario se lanza una excepción.
    
    Se ignoran las diferencias entre mayúsculas y minúsculas.
    """


                    # Se utiliza la función input() para pedir al usuario que introduzca una lista de nombres (separados por comas).
                    # La función input() devuelve una cadena de texto (str).
    nombres_str = input("Por favor, introduzca una lista de nombres separados por comas (Ejemplo:ana,carlos,alicia,juan):")


                    # Se hace uso del método lower() para convertir todos los caracteres de la cadena de texto a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.
    nombres_str_minus = nombres_str.lower()


                    # Se hace uso del método split() para dividir el string (str) obtenido y devolverlo en forma de lista (list) de nombres (str),
                    # empleando las comas ',' como separadores.
    nombres_lista = nombres_str_minus.split(",")


                    # Se utiliza la función input() para pedir al usuario que introduzca un nombre para buscar en la lista.
                    # La función input() devuelve una cadena de texto (str).
    nombre_objetivo = input("Por favor, Introduzca un nombre para buscar en la lista: ")
    
    
                    # Se hace uso del método lower() para convertir todos los caracteres de la cadena de texto a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.
    nombre_objetivo_minus = nombre_objetivo.lower()


    print("====================================================================================================")
    print("KATA 31")
    print("====================================================================================================") 
                    # Se emplea un condicional if para evaluar si el nombre objetivo se encuentra en la lista de nombres.
    if nombre_objetivo_minus in nombres_lista:
                    # En caso afirmativo, se muestra un mensaje informando que el nombre ha sido encontrado en la lista.
            print("==========")
            print(f"El nombre {nombre_objetivo} ha sido encontrado en la lista")
            print("==========")
            print("")
            print("")
                    # Si no se cumple la condición previa (el nombre objetivo no está en la lista),
    else:   
                    # Se lanza una excepción y se muestra un mensaje informando que el nombre no ha sido encontrado en la lista.
            raise Exception (f"El nombre {nombre_objetivo} no ha sido encontrado en la lista")
            

# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN
# ====================================================================================================

                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Ejecutar la función buscar_nombre()
                    # Introducir como lista: ana,carlos,alicia,juan
                    # Introducir como nombre objetivo: alicia                   
# Output esperado:
# ====================================================================================================
# KATA 31
# ====================================================================================================
# ==========
# El nombre alicia ha sido encontrado en la lista
# ==========


                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Ejecutar la función buscar_nombre()
                    # Introducir como lista: Ana,CARLOS,alicia,juan
                    # Introducir como nombre objetivo: Alicia                   
# Output esperado:
# ====================================================================================================
# KATA 31
# ====================================================================================================
# ==========
# El nombre Alicia ha sido encontrado en la lista
# ==========


                    # ==========
                    # Ejemplo 3
                    # ==========
                    # Ejecutar la función buscar_nombre()
                    # Introducir como lista: ana,carlos,alicia,juan
                    # Introducir como nombre objetivo: marina                 
# Output esperado:
# ====================================================================================================
# KATA 31
# ====================================================================================================
# (...)
# Exception: El nombre marina no ha sido encontrado en la lista




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 32
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista  
# y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================
                    
                    # Se define la función buscar_empleado.
def buscar_empleado(nombre_completo, lista_empleados):
    """
    Función que recibe un nombre completo y una lista de empleados, busca el nombre completo en la lista 
    y devuelve el puesto del empleado si está en la lista o un mensaje indicando que la persona no trabaja en la empresa en caso contrario.
    Se ignoran las diferencias entre mayúsculas y minúsculas. 

    Args:
        - nombre_completo (str): Nombre completo del empleado cuyo puesto se quiere conocer.
        - lista_empleados (list): Lista de diccionarios (dict) donde cada elemento es un diccionario con el nombre completo de un empleado y el puesto que ocupa.

    Returns:
        - str: La función devuelve el puesto que ocupa el empleado en caso de que el empleado esté en la lista. 
               En caso de no estar en la lista, la función devuelve un mensaje indicando que el empleado no trabaja en la empresa.
    """


                    # Se hace uso de un bucle for para recorrer todos los elementos de la lista de empleados.
    for empleado in lista_empleados:


                    # Se emplea un condicional if para evaluar si el nombre actual de un empleado coincide con el nombre completo que se está buscando.
                    # Se hace uso del método lower() para convertir todos los caracteres de la cadena de texto a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.
        if empleado["nombre"].lower() == nombre_completo.lower():
                    # En caso afirmativo, la función devuelve el puesto que ocupa el empleado.
            return empleado["puesto"]
        

                    # Por último, tras recorrer la lista completa de empleados, si el nombre de ninguno de ellos coincide con el nombre que se está buscando,
                    # la función muestra un mensaje informando que la persona buscada no trabaja en la empresa.
    return f"El empleado {nombre_completo} no trabaja en esta empresa"


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN
# ====================================================================================================

                    # Se crea una lista (list) de diccionarios (dict) con información de empleados (nombre completo, puesto).
lista_empleados1 = [
    {"nombre":"Ana Ozores", "puesto":"Gerente"},
    {"nombre":"Carlos Deza", "puesto":"Desarrollador"},
    {"nombre":"Alicia Gris", "puesto":"Desarrollador"},
    {"nombre":"Juan Preciado", "puesto":"Ingeniero"}]


                    # Se crean varios nombres de empleados (str).
nombre_completo1 = "Alicia Gris"
nombre_completo2 = "alicia gris"
nombre_completo3 = "Marina Vidal"


                    # Se llama a la función con los nombres de empleados y la lista como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 32")
print("====================================================================================================") 
print("==========")
print(f"Empleado ----------> {nombre_completo1}")
print(f"Puesto ------------> {buscar_empleado(nombre_completo1, lista_empleados1)}")
print("==========")
print(f"Empleado ----------> {nombre_completo2}")
print(f"Puesto ------------> {buscar_empleado(nombre_completo2, lista_empleados1)}")
print("==========")
print(f"Empleado ----------> {nombre_completo3}")
print(f"Puesto ------------> {buscar_empleado(nombre_completo3, lista_empleados1)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 32
# ====================================================================================================
# ==========
# Empleado ----------> Alicia Gris
# Puesto ------------> Desarrollador
# ==========
# Empleado ----------> alicia gris
# Puesto ------------> Desarrollador
# ==========
# Empleado ----------> Marina Vidal
# Puesto ------------> El empleado Marina Vidal no trabaja en esta empresa
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 33
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define una función lambda llamada sumar_listas que recibe dos listas (list) de números (int, float)
                    # y devuelve otra lista (list) con la suma elemento a elemento de ambas listas (int, float). 
                    # La función está diseñada para trabajar con listas de distinta longitud.

                    # Se emplea la función len() para obtener las longitudes de ambas listas
                    # y la función max() para determinar la lista de mayor longitud.
                    # Mediante la función range() se crea una secuencia de números desde 0 hasta el tamaño de la lista con más elementos (sin incluirlo).

                    # Usando como índices la secuencia de números creada, se recorren ambas lista simultáneamente sumando sus elementos:
                    # - Si una lista tiene un elemento en la posición i, se utiliza ese valor.
                    # - Si una lista no tiene elemento en la posición i (porque es más corta), se utiliza el valor 0.

                    # Por último, se devuelve la lista de números con la suma de los elementos correspondientes de las lista originales.
                    # La nueva lista ha sido creada usando una list comprehension.          

sumar_listas = lambda lista1, lista2: [
               (lista1[i] if i < len(lista1) else 0) + 
               (lista2[i] if i < len(lista2) else 0) 
               for i in range(max(len(lista1), len(lista2)))]


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN  
# ====================================================================================================
               
                    # Se crean varias listas (list) de números (int, float). 
lista_numeros1 = [1, 2, -3, 4.4]
lista_numeros2 = [1, 2, -3, 4.4, 5]
lista_numeros3 = [1, 2, -3]


                    # Se llama a la función con las listas de números como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 33")
print("====================================================================================================")                   
print("==========")
print(f"Primera lista de números -------------> {lista_numeros1}")
print(f"Segunda lista de números -------------> {lista_numeros2}")
print(f"Lista de números resultante ----------> {sumar_listas(lista_numeros1, lista_numeros2)}")
print("==========")
print(f"Primera lista de números -------------> {lista_numeros2}")
print(f"Segunda lista de números -------------> {lista_numeros3}")
print(f"Lista de números resultante ----------> {sumar_listas(lista_numeros2, lista_numeros3)}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 33
# ====================================================================================================
# ==========
# Primera lista de números -------------> [1, 2, -3, 4.4]
# Segunda lista de números -------------> [1, 2, -3, 4.4, 5]
# Lista de números resultante ----------> [2, 4, -6, 8.8, 5]
# ==========
# Primera lista de números -------------> [1, 2, -3, 4.4, 5]
# Segunda lista de números -------------> [1, 2, -3]
# Lista de números resultante ----------> [2, 4, -6, 4.4, 5]
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 34
# Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos.  
# Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.  
# El objetivo es implementar estos métodos para manipular la estructura del árbol.
#
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# CLASE 
# ====================================================================================================
                    
                    # Se crea la clase Arbol.
                    # Siguiendo criterios de buenas prácticas, el nombre de la clase se escribe con mayúscula inicial.
class Arbol:
    """
    Clase que representa un arbol genérico con un tronco y ramas como atributos.
    """


                    # Se define el método constructor de la clase Arbol.
    def __init__(self, tronco = 1, ramas = []):
        """
        Método constructor de la clase Arbol.

        Args:
            - tronco (int): Número entero positivo que representa la longitud del tronco. 
                            Por defecto su valor es 1.
            - ramas (list): Lista de números enteros (int) que representan la longitud de las distintas ramas del árbol. 
                            Por defecto es una lista vacía, lo cual representa un arbol sin ramas.
        """
                    # Se crean los atributos y se les asigna el valor de los parámetros del método constructor.
        self.tronco = tronco
        self.ramas = ramas


                    # Se define el método crecer_tronco de la clase Arbol.
    def crecer_tronco(self):
        """
        Método de la clase Arbol que aumenta la longitud del tronco en una unidad.
        """
                    # Se aumenta la longitud del tronco en una unidad.
        self.tronco += 1


                    # Se define el método nueva_rama de la clase Arbol.
    def nueva_rama(self):
        """
        Método de la clase Arbol que agrega una nueva rama de longitud 1 a la lista de ramas.
        """
                    # Se hace uso del método append(1) para añadir un elemento de valor 1 a la lista de ramas.
        self.ramas.append(1)


                    # Se define el método crecer_ramas de la clase Arbol.
    def crecer_ramas(self):
        """
        Método de la clase Arbol que aumenta en una unidad la longitud de todas las ramas existentes.
        """
                    # Se hace uso de una list comprehension para indicar con un bucle for que se recorran todos los elementos (rama) de la lista (self.ramas),
                    # aumentando su longitud en una unidad (rama+1).
        self.ramas = [rama+1 for rama in self.ramas]


                    # Se define el método quitar_rama de la clase Arbol.
    def quitar_rama(self,posicion_rama):
        """
        Método de la clase Arbol que elimina una rama en una posición específica.

        Args:
            - posicion_rama (int): Número entero que representa la posición de la rama que desea eliminarse (índice de la lista de ramas). 
                                   Se sigue la nomenclatura habitual de Python, donde 0 es la primera posición, 1 la segunda, 2 la tercera (tercer elemento de la lista), etc.
        """
                    # Se hace uso del método pop() para eliminar de la lista de ramas el elemento en la posición indicada enter paréntesis.
        self.ramas.pop(posicion_rama)


                    # Se define el método info_arbol de la clase Arbol.
    def info_arbol(self):
        """
        Método de la clase Arbol que devuelve en forma de diccionario información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

        Returns:
            - dict: Diccionario que contiene información sobre la longitud del tronco (int), 
                    el número de ramas (int) y las longitudes de las mismas (lista (list) de números enteros (int)).
        """
                    # El método devuelve en forma de diccionario información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
        return {
            "longitud_tronco":self.tronco,
            "numero_ramas":len(self.ramas),
            "longitud_ramas":self.ramas}
        

# ====================================================================================================
# CASO DE USO 
# ====================================================================================================   

print("====================================================================================================")
print("KATA 34")
print("====================================================================================================")   


# ==================================================
# 1. Crear un árbol
# ==================================================
                    # Se instancia un nuevo objeto llamado arbol1 de la clase Arbol (se crea un nuevo arbol).
arbol1 = Arbol() 
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("1. Crear un árbol")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 2. Hacer crecer el tronco del árbol una unidad
# ==================================================
                    # Se llama al método crecer_tronco para aumentar la longitud del tronco en una unidad.
arbol1.crecer_tronco()
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("2. Hacer crecer el tronco del árbol una unidad")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 3. Añadir una nueva rama al árbol
# ==================================================
                    # Se llama al método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
arbol1.nueva_rama()
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("3. Añadir una nueva rama al árbol")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 4. Hacer crecer todas las ramas del árbol una unidad
# ==================================================
                    # Se llama al método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
arbol1.crecer_ramas()
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("4. Hacer crecer todas las ramas del árbol una unidad")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 5. Añadir dos nuevas ramas al árbol
# ==================================================
                    # Se llama dos veces al método nueva_rama para agregar dos nuevas rama de longitud 1 a la lista de ramas.
arbol1.nueva_rama()
arbol1.nueva_rama()
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("5. Añadir dos nuevas ramas al árbol")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 6. Retirar la rama situada en la posición 2
# ==================================================
                    # Se llama al método quitar_rama() con el argumento 2 para eliminar la rama situada en el posición 2.
arbol1.quitar_rama(2)
                    # Se muestran todos los atributos del arbol1 para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("6. Retirar la rama situada en la posición 2")
print(f"   Atributos del arbol1 ------------------------------> {arbol1.__dict__}")


# ==================================================
# 7. Obtener información sobre el árbol
# ==================================================
                    # Se llama al método info_arbol() para mostrar todos los atributos del arbol1.
print("==========")
print("7. Obtener información sobre el árbol")
print (arbol1.info_arbol())
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 34
# ====================================================================================================
# ==========
# 1. Crear un árbol
#    Atributos del arbol1 ------------------------------> {'tronco': 1, 'ramas': []}
# ==========
# 2. Hacer crecer el tronco del árbol una unidad
#    Atributos del arbol1 ------------------------------> {'tronco': 2, 'ramas': []}
# ==========
# 3. Añadir una nueva rama al árbol
#    Atributos del arbol1 ------------------------------> {'tronco': 2, 'ramas': [1]}
# ==========
# 4. Hacer crecer todas las ramas del árbol una unidad
#    Atributos del arbol1 ------------------------------> {'tronco': 2, 'ramas': [2]}
# ==========
# 5. Añadir dos nuevas ramas al árbol
#    Atributos del arbol1 ------------------------------> {'tronco': 2, 'ramas': [2, 1, 1]}
# ==========
# 6. Retirar la rama situada en la posición 2
#    Atributos del arbol1 ------------------------------> {'tronco': 2, 'ramas': [2, 1]}
# ==========
# 7. Obtener información sobre el árbol
# {'longitud_tronco': 2, 'numero_ramas': 2, 'longitud_ramas': [2, 1]}
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 35
# Enunciado vacío.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

print("====================================================================================================")
print("KATA 35")
print("====================================================================================================")   
print("==========")
print("Enunciado vacío")
print("==========")
print("")
print("")




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 36
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.  
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.  
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario.  
#    Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.  
#    Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#
# Caso de uso:
# 1. Crear dos usuarios: 'Alicia' con saldo inicial de 100 y 'Bob' con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de 'Bob'.
# 3. Hacer una transferencia de 80 unidades desde 'Bob' a 'Alicia'.
# 4. Retirar 50 unidades de saldo a 'Alicia'.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# CLASE 
# ====================================================================================================
                    
                    # Se crea la clase UsuarioBanco.
                    # Siguiendo criterios de buenas prácticas, el nombre de la clase se escribe con mayúscula inicial.
class UsuarioBanco:
    """
    Clase que representa un usuario de un banco con su nombre, el saldo de su cuenta corriente y si tiene o no cuenta (True, False) como atributos.
    """


                    # Se define el método constructor de la clase UsuarioBanco.
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Método constructor de la clase UsuarioBanco.

        Args:
            - nombre (str): Nombre del usuario de un banco.
            - saldo (float): Cantidad de dinero almacenado en la cuenta corriente.
            - cuenta_corriente (bool): Booleano que representa si un usuario tiene cuenta corriente (True) o no (False).
        """
                    # Se crean los atributos y se les asigna el valor de los parámetros del método constructor.
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente


                    # Se define el método retirar_dinero de la clase UsuarioBanco.
    def retirar_dinero(self, cantidad):
        """
        Método de la clase UsuarioBanco para retirar dinero del saldo del usuario.

        Args:
            - cantidad (float): Dinero que desea retirarse del saldo del usuario.
        """
                    # Se emplea un condicional if para evaluar si la cantidad a retirar no es positiva. 
        if cantidad <= 0:
                    # En caso afirmativo, se lanza una excepción informando que solo pueden retirarse cantidades de dinero positivas.
            raise Exception (f"La cantidad que desea retirar debe ser mayor que cero")
                    # Se emplea un condicional elif para evaluar si el usuario carece de cuenta corriente.
        elif self.cuenta_corriente == False:
                    # En caso afirmativo (usuario sin cuenta corriente), se lanza una excepción informando que el usuario no tiene cuenta corriente.
            raise Exception (f"El usuario {self.nombre} no tiene cuenta corriente")
                    # Se emplea un condicional elif para evaluar si la cantidad a retirar supera el saldo de la cuenta corriente.
        elif cantidad > self.saldo:
                    # En caso afirmativo, se lanza una excepción informando que la cuenta corriente no tiene saldo suficiente.
            raise Exception (f"El usuario {self.nombre} no tiene saldo suficiente en su cuenta corriente")
                    # Si no se cumplen las condiciones previas,
        else:
                    # se modifica el saldo del usuario restándole al saldo inicial la cantidad indicada como argumento. 
            self.saldo -= cantidad


                    # Se define el método transferir_dinero de la clase UsuarioBanco.
    def transferir_dinero(self, usuario_emisor, cantidad):
        """
        Método de la clase UsuarioBanco para transferir dinero desde la cuenta de otro usuario al usuario actual.

        Args:
            - usuario_emisor (object): Usuario de cuya cuenta va a retirarse dinero para ingresarlo en la cuenta del usuario actual.
            - cantidad (float): Dinero que desea retirarse de la cuenta del usuario emisor e ingresarse en la del usuario actual.
        """
                    # Se emplea un condicional if para evaluar si la cantidad a transferir no es positiva.
        if cantidad <= 0:
                    # En caso afirmativo, se lanza una excepción informando que solo pueden transferirse cantidades de dinero positivas.
            raise Exception (f"La cantidad que desea transferir debe ser mayor que cero")
                    # Se emplea un condicional elif para evaluar si el usuario carece de cuenta corriente.
        elif self.cuenta_corriente == False:
                    # En caso afirmativo (usuario sin cuenta corriente), se lanza una excepción informando que el usuario no tiene cuenta corriente.
            raise Exception (f"El usuario {self.nombre} no tiene cuenta corriente")
                    # Se emplea un condicional elif para evaluar si el usuario emisor carece de cuenta corriente.
        elif usuario_emisor.cuenta_corriente == False:
                    # En caso afirmativo (usuario emisor sin cuenta corriente), se lanza una excepción informando que el usuario emisor no tiene cuenta corriente.
            raise Exception (f"El usuario {usuario_emisor.nombre} no tiene cuenta corriente")
                    # Se emplea un condicional elif para evaluar si la cantidad a transferir supera el saldo de la cuenta corriente del usuario emisor.
        elif cantidad > usuario_emisor.saldo:
                    # En caso afirmativo, se lanza una excepción informando que la cuenta corriente del usuario emisor no tiene saldo suficiente.
            raise Exception (f"El usuario {usuario_emisor.nombre} no tiene saldo suficiente en su cuenta corriente para realizar la transferencia")
                    # Si no se cumplen las condiciones previas, 
        else:
                    # Se modifica el saldo del usuario emisor restándole al saldo inicial la cantidad indicada como argumento. 
            usuario_emisor.saldo -= cantidad
                    # Se modifica el saldo del usuario actual sumándole al saldo inicial la cantidad indicada como argumento.
            self.saldo += cantidad


                    # Se define el método agregar_dinero de la clase UsuarioBanco.
    def agregar_dinero(self, cantidad):
        """
        Método de la clase UsuarioBanco para agregar dinero al saldo del usuario.

        Args:
            - cantidad (float): Cantidad de dinero que desea ingresarse en la cuenta corriente del usuario.
        """
                    # Se modifica el saldo del usuario sumándole al saldo inicial la cantidad indicada como argumento.
        self.saldo += cantidad


# ====================================================================================================
# CASO DE USO 
# ====================================================================================================   

print("====================================================================================================")
print("KATA 36")
print("====================================================================================================")   


# ==================================================
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente
# ==================================================
                    # Se instancian dos nuevos objetos de la clase UsuarioBanco llamados Alicia y Bob.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
                    # Se muestran todos los atributos de los objetos alicia y bob para comprobar que el código se ha ejecutado correctamente.
print("==========")
print("1. Crear dos usuarios: 'Alicia' con saldo inicial de 100 y 'Bob' con saldo inicial de 50, ambos con cuenta corriente")
print(f"Atributos de Alicia ----------> {alicia.__dict__}")
print(f"Atributos de Bob -------------> {bob.__dict__}")


# ==================================================
# 2. Agregar 20 unidades de saldo de "Bob"
# ==================================================
                    # Se llama al método agregar_dinero() con el atributo 20 sobre el objeto bob.
bob.agregar_dinero(20)
                    # Se muestran todos los atributos de los objetos alicia y bob para comprobar que el código se ha ejecutado correctamente.      
print("==========")
print("2. Agregar 20 unidades de saldo de 'Bob'")
print(f"Atributos de Alicia ----------> {alicia.__dict__}")
print(f"Atributos de Bob -------------> {bob.__dict__}")


# ==================================================
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
# ==================================================
                    # Se define un bloque try para contener el código que puede generar errores.
try:
                    # Se llama al método transferir_dinero() con los atributos bob y 80 sobre el objeto alicia (receptor de la transferencia).
        alicia.transferir_dinero(bob,80)
                    # Se muestran todos los atributos de los objetos alicia y bob para comprobar que el código se ha ejecutado correctamente.      
        print("==========")
        print("3. Hacer una transferencia de 80 unidades desde 'Bob' a 'Alicia'")
        print(f"Atributos de Alicia ----------> {alicia.__dict__}")
        print(f"Atributos de Bob -------------> {bob.__dict__}")

                    # Se define un bloque except para capturar la excepción.
except Exception as excepcion1:
                    # Se muestra un mensaje que informa al usuario del motivo que impide realizar la transferencia.
        print("==========")
        print("3. Hacer una transferencia de 80 unidades desde 'Bob' a 'Alicia'")          
        print(f"ERROR: {excepcion1}")


# ==================================================
# 4. Retirar 50 unidades de saldo a "Alicia"
# ==================================================
                    # Se llama al método transferir_dinero() con los atributos bob y 80 sobre el objeto alicia (receptor de la transferencia).
alicia.retirar_dinero(50)
                    # Se muestran todos los atributos de los objetos alicia y bob para comprobar que el código se ha ejecutado correctamente.      
print("==========")
print("4. Retirar 50 unidades de saldo a 'Alicia'")
print(f"Atributos de Alicia ----------> {alicia.__dict__}")
print(f"Atributos de Bob -------------> {bob.__dict__}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 36
# ====================================================================================================
# ==========
# 1. Crear dos usuarios: 'Alicia' con saldo inicial de 100 y 'Bob' con saldo inicial de 50, ambos con cuenta corriente
# Atributos de Alicia ----------> {'nombre': 'Alicia', 'saldo': 100, 'cuenta_corriente': True}
# Atributos de Bob -------------> {'nombre': 'Bob', 'saldo': 50, 'cuenta_corriente': True}
# ==========
# 2. Agregar 20 unidades de saldo de 'Bob'
# Atributos de Alicia ----------> {'nombre': 'Alicia', 'saldo': 100, 'cuenta_corriente': True}
# Atributos de Bob -------------> {'nombre': 'Bob', 'saldo': 70, 'cuenta_corriente': True}
# ==========
# 3. Hacer una transferencia de 80 unidades desde 'Bob' a 'Alicia'
# ERROR: El usuario Bob no tiene saldo suficiente en su cuenta corriente para realizar la transferencia
# ==========
# 4. Retirar 50 unidades de saldo a 'Alicia'
# Atributos de Alicia ----------> {'nombre': 'Alicia', 'saldo': 50, 'cuenta_corriente': True}
# Atributos de Bob -------------> {'nombre': 'Bob', 'saldo': 70, 'cuenta_corriente': True}
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 37
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabras.
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
#
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el reemplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar palabras del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción (entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# 
# Caso de uso:  
# Compruebe el funcionamiento completo de la función procesar_texto.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN | contar_palabras
# ====================================================================================================

                    # Se define la función contar_palabras.
def contar_palabras(texto):
    """
    Función que recibe un texto, cuenta el número de veces que aparece cada palabra en el texto y devuelve el resultado en forma de diccionario.

    Args:
        - texto (str): Cadena de texto a analizar.

    Returns:
        - dict: Diccionario cuyas claves son las palabras que aparecen en el texto (str) y los valores su frecuencia de aparición (int).     
    
    """
                    # Se hace uso del método lower() para convertir todos los caracteres de la cadena de texto original a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.

                    # Se hace uso del método split() para dividir el texto original (str) en palabras (str) y devolverlas en forma de lista (list).
                    # En este caso, no es necesario indicar ningún argumento dentro de split(), 
                    # ya que este método divide por defecto usando los espacios en blanco como separadores.
    lista_palabras = texto.lower().split()


                    # Se crea un diccionario vacío para almacenar las palabras de la lista y el número de veces que aparecen en el texto.
    diccionario_palabras = {}


                    # Se utiliza un bucle for para recorrer cada palabra de la lista de palabras.
    for palabra in lista_palabras:


                    # Se emplea un condicional if para evaluar si la palabra actual está incluida en el diccionario.
        if palabra in diccionario_palabras:
                    # En caso afirmativo, se incrementa en 1 el valor asociado a dicha clave (se aumenta en una unidad la frecuencia de aparición de la palabra en el texto).
            diccionario_palabras[palabra] += 1 
                    # Si no se cumple la condición previa (palabra no incluida en el diccionario), 
        else:
                    # Se añade la palabra actual como clave del diccionario y se le asigna el valor 1.
            diccionario_palabras[palabra] = 1
    

                    # Por último, tras recorrer todas las palabras de la lista, la función devuelve un diccionario 
                    # con todas las palabras del texto y el número de veces que aparecen en él.
    return diccionario_palabras


# ====================================================================================================
# FUNCIÓN | reemplazar_palabras
# ====================================================================================================

                    # Se define la función reemplazar_palabras.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Función que reemplaza una palabra de un texto por una palabra nueva.

    Args:
        - texto (str): Texto que contiene una palabra que quiere ser reemplazada por una palabra nueva.
        - palabra_original (str): Palabra incluida en el texto original.
        - palabra_nueva (str): Palabra nueva que sustituye a la palabra original.

    Returns:
        - str: Texto obtenido a partir del texto original donde se ha sustituido por una nueva palabra la palabra original indicada.
    """
                    # Se hace uso del método replace() para reemplazar una palabra original del texto por una nueva palabra.
                    # Por último, la función devuelve el texto tras realizar la sustitución de palabras.
    return texto.replace(palabra_original, palabra_nueva)


# ====================================================================================================
# FUNCIÓN | eliminar_palabras
# ====================================================================================================

                    # Se define la función eliminar_palabra.
def eliminar_palabra(texto, palabra):
    """
    Función que elimina una palabra de un texto. 

    Args:
        - texto (str): Texto original del que desea eliminarse una palabra.
        - palabra (str): Palabra que desea eliminarse del texto original.

    Returns:
        - str: Texto obtenido a partir del texto original donde se ha eliminado la palabra indicada.
    """
                    # Se hace uso del método split() para dividir el texto original (str) en palabras (str) y devolverlas en forma de lista (list).
                    # En este caso, no es necesario indicar ningún argumento dentro de split(), 
                    # ya que este método divide por defecto usando los espacios en blanco como separadores.
    lista_palabras = texto.split()


                    # Se crea una nueva lista de palabras sin la palabra a eliminar.
                    # Para ello se recorre todas la lista de palabras, conservandose únicamente las palabras que son distintas a la palabra a eliminar.
                    # La nueva lista ha sido creada usando una list comprehension.
    lista_palabras_mod = [p for p in lista_palabras if p != palabra]


                    # Se hace uso del método join() para unir las palabras de la lista que no incluye la palabra eliminada, usando un espacio en blanco como separador.
                    # Por último, la función devuelve el texto tras eliminar la palabra.
    return " ".join(lista_palabras_mod)


# ====================================================================================================
# FUNCIÓN | procesar_texto
# ====================================================================================================

                    # Se define la función procesar_texto.
def procesar_texto(texto, opcion, *args):
    """
    Función que recibe un texto, una opción ("contar", "reemplazar" o "eliminar") y un número de argumentos variable según la opción indicada;
    para realizar un procesamiento del texto en función de la opción elegida.

    Args:
        - texto (str): Texto a procesar.

        - opcion (str): Tipo de procesamiento que desea aplicarse al texto. A escoger entre:
                            - contar, si desea contarse el número de palabras.
                            - reemplazar, si desea reemplazarse una palabra del texto original por otra palabra nueva.
                            - eliminar, si desea eliminarse del texto una palabra del texto original.

        - *args: Según la opción escogida:
                            - contar 
                                        No requiere argumentos variables.

                            - reemplazar
                                        - palabra_original (str): Palabra incluida en el texto original.
                                        - palabra_nueva (str): Palabra nueva que sustituye a la palabra original.

                            - eliminar
                                        - palabra (str): Palabra que desea eliminarse del texto original.

    Returns:
        Según la opción escogida:
        
        - Para la opción "contar"
            - dict: Diccionario cuyas claves son las palabras que aparecen en el texto (str) y los valores su frecuencia de aparición (int).   


        - Para la opción "reemplazar"
            - str: Texto obtenido a partir del texto original donde se ha sustituido por una nueva palabra la palabra original indicada.
        
        - Para la opción "eliminar"

            - str: Texto obtenido a partir del texto original donde se ha eliminado la palabra indicada.    
    """
                    # Se hace uso del método lower() para convertir la opción escogida a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive).
                    # Se trata de un enfoque de programación defensiva.

                    # Se emplea un condicional if para evaluar si la opción indicada es 'contar'.
    if opcion.lower() == "contar":
                    # En caso afirmativo, se ejecuta la función contar_palabras con el texto original como argumento.
                    # La función devuelve el resultado alcanzado.
        return contar_palabras(texto)


                    # Se emplea un condicional elif para evaluar si la opción indicada es 'reemplazar'.
    elif opcion.lower() == "reemplazar":
                    # En caso afirmativo, se ejecuta la función reemplazar_palabras con el texto original, la palabra a reemplazar y la palabra de reemplazo como argumentos.
                    # La función devuelve el resultado alcanzado.
        return reemplazar_palabras(texto,*args)


                    # Se emplea un condicional elif para evaluar si la opción indicada es 'eliminar'.
    elif opcion.lower() == "eliminar":
                    # En caso afirmativo, se ejecuta la función eliminar_palabra con el texto original y la palabra a eliminar como argumentos.
                    # La función devuelve el resultado alcanzado.
        return eliminar_palabra(texto, *args)


                    # Si la opción indicada no cumple las condiciones previas (no es 'contar', 'reemplazar' o 'eliminar).
    else:
                    # La función muestra un mensaje informando que la opción escogida en es válida.
        return f"La opción {opcion} no es válida. Elija entre las opciones 'contar', 'reemplazar' o 'eliminar'"
        
        
# ====================================================================================================
# COMPROBACIÓN COMPLETA DE LA FUNCIÓN procesar_texto
# ====================================================================================================
               
                    # Se crea un texto (str) y varias palabras (str).
texto1 = "tres tristes tigres comen trigo en un trigal"
palabra_original1 = "comen"
palabra_nueva1 = "tragan"
palabra1 = "tristes"


                    # Se llama a la función con el texto y las palabras como argumentos y se muestra el resultado.
print("====================================================================================================")
print("KATA 37")
print("====================================================================================================")                   
print("==========")
print("Texto original")
print(f"{texto1}")
print("==========")
print("Indicando la opción 'contar' el resultado es el siguiente diccionario:")
print(f"{procesar_texto(texto1,"contar")}")
print("==========")
print(f"Indicando la opción 'reemplazar' para sustituir la palabra {palabra_original1} por {palabra_nueva1}, resulta el siguiente texto:")
print(f"{procesar_texto(texto1, "reemplazar",palabra_original1, palabra_nueva1)}")
print("==========")
print(f"Indicando la opción 'eliminar' para eliminar del texto la palabra {palabra1}, resulta el siguiente texto:")
print(f"{procesar_texto(texto1, "eliminar", palabra1)}")
print("==========")
print(f"Indicando una opción no válida (ejemplo:'borrar'), la función devuelve el siguiente mensaje:")
print(f"{procesar_texto(texto1, "borrar")}")
print("==========")
print("")
print("")


# Output esperado:
# ====================================================================================================
# KATA 37
# ====================================================================================================
# ==========
# Texto original
# tres tristes tigres comen trigo en un trigal
# ==========
# Indicando la opción 'contar' el resultado es el siguiente diccionario:
# {'tres': 1, 'tristes': 1, 'tigres': 1, 'comen': 1, 'trigo': 1, 'en': 1, 'un': 1, 'trigal': 1}
# ==========
# Indicando la opción 'reemplazar' para sustituir la palabra comen por tragan, resulta el siguiente texto:
# tres tristes tigres tragan trigo en un trigal
# ==========
# Indicando la opción 'eliminar' para eliminar del texto la palabra tristes, resulta el siguiente texto:
# tres tigres comen trigo en un trigal
# ==========
# Indicando una opción no válida (ejemplo:'borrar'), la función devuelve el siguiente mensaje:
# La opción borrar no es válida. Elija entre las opciones 'contar', 'reemplazar' o 'eliminar'
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 38
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# PROGRAMA 
# ====================================================================================================

                    # Se utiliza la función input() para pedir al usuario que introduzca una hora en formato HH:MM (por ejemplo, 14:30).
                    # La función input() siempre devuelve el valor introducido como una cadena de texto (str). 
hora_hhmm = input("Por favor, introduzca una hora en formato HH:MM (Por ejemplo, 14:30)")


                    # Se hace uso del método split() para dividir la cadena de texto usando ":" como separador.
                    # El resultado es una lista (list) de cadenas de texto (str), donde:
                    # - El primer elemento corresponde a la hora
                    # - El segundo elemento corresponde a los minutos
hora_lista = hora_hhmm.split(":")


                    # Se convierten los elementos de la lista a números enteros (int) usando la función int().
hora = int(hora_lista[0])
minutos = int(hora_lista[1])
       

print("====================================================================================================")
print("KATA 38")
print("====================================================================================================")  


                    # Se emplea un condicional if para evaluar si la hora o los minutos están fuera de los rangos válidos.
if not (0 <= hora <= 23 and 0 <= minutos <= 59):
                    # En caso afirmativo (hora o minutos fuera de los rangos permitidos), se muestra un mensaje informando que la hora introducida no es válida.
    print("==========")
    print(f"{hora_hhmm} ----------> La hora introducida no es válida")  
    print("==========")                     


                    # Se emplea un condicional elif para evaluar si la hora, cuando no cumple la primera condición (y por tanto es una hora válida), 
                    # está comprendida entre las 6 (inclusive) y las 12 (no inclusive).
elif 6 <= hora < 12:
                    # En caso afirmativo, se muestra un mensaje informando que es de día (mañana).
    print("==========")
    print(f"{hora_hhmm} ----------> Es de día (mañana)")
    print("==========")
        

                    # Se emplea un condicional elif para evaluar si la hora, cuando no cumple las condiciones anteriores.
                    # (y por tanto es una hora válida fuera del rango de mañana)
                    # está comprendida entre las 12 (inclusive) y las 21 (no inclusive).
elif 12 <= hora < 21:
                    # En caso afirmativo, se muestra un mensaje informando que es por la tarde.
    print("==========")
    print(f"{hora_hhmm} ----------> Es por la tarde")
    print("==========")


                    # Si la hora no cumple ninguna de las condiciones previas (y por tanto es una hora válida fuera del rango de mañana y de tarde).
else:
                    # Se muestra un mensaje informando que es de noche.
    print("==========")
    print(f"{hora_hhmm} ----------> Es de noche")
    print("==========")


print("")
print("")


# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA 
# ====================================================================================================

                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Introducir la hora 25:00 
# Output esperado:
# ====================================================================================================
# KATA 38
# ====================================================================================================
# ==========
# 25:00 ----------> La hora introducida no es válida
# ==========

                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Introducir la hora 10:45 
# Output esperado:
# ====================================================================================================
# KATA 38
# ====================================================================================================
# ==========
# 10:45 ----------> Es de día (mañana)
# ==========

                    # ==========
                    # Ejemplo 3
                    # ==========
                    # Introducir la hora 15:30 
# Output esperado:
# ====================================================================================================
# KATA 38
# ====================================================================================================
# ==========
# 15:30 ----------> Es por la tarde
# ==========

                    # ==========
                    # Ejemplo 4
                    # ==========
                    # Introducir la hora 22:20 
# Output esperado:
# ====================================================================================================
# KATA 38
# ====================================================================================================
# ==========
# 22:20 ----------> Es de noche
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 39
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.  
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función calificacion
def calificacion (calificacion_numerica):
    """
    Función que recibe una calificación numérica y devuelve una calificación en formato texto.

    Args:
        - calificacion_numerica (int, float): Nota numérica de un alumno entre 0 y 100.

    Returns:
        - str: Nota en formato texto de un alumno ('insuficiente', 'bien', 'muy bien' o 'excelente')
    """
                    # Se emplea un condicional if para evaluar si la calificación numérica tiene un valor entre 0 y 69 (ambos inclusive).
    if 0 <= calificacion_numerica <= 69:
                    # En caso afirmativo, se asigna el valor "insuficiente" a la variable calificacion_texto.
        calificacion_texto = "insuficiente"
                    # Se emplea un condicional elif para evaluar si la calificación numérica, cuando no cumple la condición anterior, tiene un valor enter 70 y 79.
    elif 70 <= calificacion_numerica <= 79:
                    # En caso afirmativo, se asigna el valor "bien" a la variable calificacion_texto.
        calificacion_texto = "bien"
                    # Se emplea un condicional elif para evaluar si la calificación numérica, cuando no cumple las condiciones anteriores, tiene un valor enter 80 y 89.
    elif 80 <= calificacion_numerica <= 89:
                    # En caso afirmativo, se asigna el valor "muy bien" a la variable calificacion_texto.
        calificacion_texto = "muy bien"
                    # Se emplea un condicional elif para evaluar si la calificación numérica, cuando no cumple las condiciones anteriores, tiene un valor entre 90 y 100.
    elif 90 <= calificacion_numerica <= 100:
                    # En caso afirmativo, se asigna el valor "excelente" a la variable calificacion_texto.
        calificacion_texto = "excelente"
                    # Por último, la función devuelve la calificación de texto.
    return calificacion_texto      




# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias calificaciones numéricas (números enteros (int) entre 0 y 100).
cnum1 = 55
cnum2 = 69
cnum3 = 70
cnum4 = 85
cnum5 = 95


                    # Se llama a la función con las calificaciones numéricas como argumentos y se muestran los resultados. 
print("====================================================================================================")
print("KATA 39")
print("====================================================================================================") 
print("==========")
print(f"Nota numérica: {cnum1} ----------> Calificación: {calificacion(cnum1)}")
print(f"Nota numérica: {cnum2} ----------> Calificación: {calificacion(cnum2)}")
print(f"Nota numérica: {cnum3} ----------> Calificación: {calificacion(cnum3)}")
print(f"Nota numérica: {cnum4} ----------> Calificación: {calificacion(cnum4)}")
print(f"Nota numérica: {cnum5} ----------> Calificación: {calificacion(cnum5)}")
print("==========")
print("")
print("")


# Ouput esperado:
# ====================================================================================================
# KATA 39
# ====================================================================================================
# ==========
# Nota numérica: 55 ----------> Calificación: insuficiente
# Nota numérica: 69 ----------> Calificación: insuficiente
# Nota numérica: 70 ----------> Calificación: bien
# Nota numérica: 85 ----------> Calificación: muy bien
# Nota numérica: 95 ----------> Calificación: excelente
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 40
#  Escribe una función que tome dos parámetros:
# - figura (una cadena que puede ser 'rectangulo', 'circulo' o 'triángulo') 
# - datos (una tupla con los datos necesarios para calcular el área de la figura)
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================

# ====================================================================================================
# FUNCIÓN 
# ====================================================================================================

                    # Se define la función calcular_area
def calcular_area (figura, datos):
    """
    Función que calcula el área de una figura geométrica a partir del tipo de figura (rectángulo, triángulo o círculo) y de sus datos geométricos. 

    Args:
        - figura (str): Figura geómetrica cuya área quiere conocerse. 
                        Las opciones permitidas son: "rectangulo", "triangulo" o "circulo".

        - datos (tuple): Tupla con los datos necesarios para calcular el área de la figura.
                            - Rectángulo ---> (base (int, float), altura (int, float))
                            - Triángulo ----> (base (int, float), altura (int, float))
                            - Círculo ------> (radio (int, float))
        
    Returns:
        int, float: Área de la figura geométrica.
    """


                    # Se hace uso del método lower() para convertir a minúsculas la cadena de texto con el nombre de la figura,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive)
                    # Se trata de un enfoque de programación defensiva.
    figura_minus = figura.lower()


                    # Se emplea un condicional if para evaluar si la figura es un rectángulo.
    if figura_minus == "rectangulo":
                    # En caso afirmativo, se extra la base y la altura de la tupla de datos.
        base = datos[0]
        altura = datos[1]
                    # y se calcula su área con la fórmula correspondiente, redondeada a dos decimales con la función round().
        area = round(base*altura,2)            # RECTÁNGULO


                    # Se emplea un condicional elif para evaluar si la figura, cuando no cumple la condición anterior, es un triángulo.
    elif figura_minus == "triangulo":
                    # En caso afirmativo, se extra la base y la altura de la tupla de datos.
        base = datos[0]
        altura = datos[1]
                    # y se calcula su área con la fórmula correspondiente, redondeada a dos decimales con la función round().
        area = round((base*altura)/2,2)        # TRIÁNGULO


                    # Se emplea un condicional elif para evaluar si la figura, cuando no cumple las condiciones anteriores, es un círculo.
    elif figura_minus == "circulo":
                    # En caso afirmativo, se extrae el radio de la tupla de datos.
        radio = datos[0]
                    # Se importa del módulo math el valor de la constante numérica pi, necesaria para calcular el área del círculo. 
        from math import pi
                    # y se calcula su área con la fórmula correspondiente, redondeada a dos decimales con la función round().
        area = round(pi*(radio**2),2)           # CÍRCULO
    

                    # Por último, la función devuelve el área de la figura.
    return area


# ====================================================================================================
# COMPROBACIÓN DE LA FUNCIÓN 
# ====================================================================================================

                    # Se crean varias figuras geométricas (str).
figura1 = "rectangulo"
figura2 = "Rectangulo"
figura3 = "triangulo"
figura4 = "circulo"


                    # y varias tuplas (tuple) con los datos necesarios (int, float) para calcular su área.
datos_geo1 = (2, 3.5)
datos_geo2 = (4, )


                    # Se llama a la función con los diferentes tipos de figuras y las tuplas de datos geométricos como argumentos, y se muestran los resultados.
print("====================================================================================================")
print("KATA 40")
print("====================================================================================================")                     
print("==========")
print(f"Figura geométrica ----------> {figura1}")
print(f"Base -----------------------> {datos_geo1[0]}")
print(f"Altura ---------------------> {datos_geo1[1]}")
print(f"Área -----------------------> {calcular_area(figura1, datos_geo1)}")
print(f"==========")
print(f"Figura geométrica ----------> {figura2}")
print(f"Base -----------------------> {datos_geo1[0]}")
print(f"Altura ---------------------> {datos_geo1[1]}")
print(f"Área -----------------------> {calcular_area(figura2, datos_geo1)}")
print("==========")
print(f"Figura geométrica ----------> {figura3}")
print(f"Base -----------------------> {datos_geo1[0]}")
print(f"Altura ---------------------> {datos_geo1[1]}")
print(f"Área -----------------------> {calcular_area(figura3, datos_geo1)}")
print("==========")
print(f"Figura geométrica ----------> {figura4}")
print(f"Radio -- -------------------> {datos_geo1[0]}")
print(f"Área -----------------------> {calcular_area(figura4, datos_geo2)}")
print("==========")
print("")
print("")


# Ouput esperado:
# ====================================================================================================
# KATA 40
# ====================================================================================================
# ==========
# Figura geométrica ----------> rectangulo
# Base -----------------------> 2
# Altura ---------------------> 3.5
# Área -----------------------> 7.0
# ==========
# Figura geométrica ----------> Rectangulo
# Base -----------------------> 2
# Altura ---------------------> 3.5
# Área -----------------------> 7.0
# ==========
# Figura geométrica ----------> triangulo
# Base -----------------------> 2
# Altura ---------------------> 3.5
# Área -----------------------> 3.5
# ==========
# Figura geométrica ----------> circulo
# Radio -- -------------------> 2
# Área -----------------------> 50.27
# ==========




# ==========================================================================================================================================================================
# ==========================================================================================================================================================================
# KATA 41
# En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, 
# después de aplicar un descuento. El programa debe hacer lo siguiente:  
# 
# 1. Solicita al usuario que ingrese el precio original de un artículo.  
# 
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).  
# 
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.  
# 
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
# a cero). Por ejemplo, descuento de 15€.  
# 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.  
#
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
# programa de Python.  
# ==========================================================================================================================================================================
# ==========================================================================================================================================================================


# ====================================================================================================
# PROGRAMA 
# ====================================================================================================


                    # Se utiliza la función input() para solicitar al usuario que ingrese el precio original de un artículo.
                    # La función input() devuelve el valor introducido como una cadena de texto (str), para convertirlo a un número decimal se emplea la función float().
precio_original = float(input("Por favor, introduzca el precio del artículo (Por ejemplo: 39.99):"))


                    # Se utiliza la función input() para solicitar al usuario que indique si tienen un cupón de descuento (si/no).
                    # Se hace uso del método lower() para convertir la respuesta a minúsculas,
                    # lo que ayuda a evitar posibles errores al comparar textos, ya que Python diferencia entre mayúsculas y minúsculas (case sensitive)
                    # Se trata de un enfoque de programación defensiva.
cupon_descuento = input("¿Tiene un cupón de descuento? (si/no):").lower()


print("====================================================================================================")
print("KATA 41")
print("====================================================================================================")  


                    # Se emplea un condicional if para evaluar si el usuario dispone de un cupón de descuento.
                    # El código admite como respuesta afirmativa tanto "si" como "sí".
if cupon_descuento == "si" or cupon_descuento =="sí":
                    # En caso afirmativo, se utiliza la función input() para solicitar al usuario el valor del cupón de descuento.
                    # La función input() devuelve el valor introducido como una cadena de texto (str), para convertirlo a un número decimal se emplea la función float().
    valor_cupon = float(input("Por favor, introduzca el valor del cupón de descuento (por ejemplo, 10.50):"))


                    # Se emplea un condicional if anidado para evaluar si el valor del cupón de descuento es superior a 0.
    if valor_cupon > 0:
                    # En caso afirmativo, el descuento a realizar tendrá el mismo valor del cupón de descuento.
        descuento = valor_cupon
                    # Si el valor del cupón no cumple la condición anterior (y por tanto, se ha indicado un valor cero o negativo)
    else:
                    # Se muestra un mensaje informando que el cupón no es válido,
        print("==========")
        print("El cupón de descuento no es válido. No se aplicará descuento")
                    # y no se aplicará descuento (se aplicará un descuento de valor 0)
        descuento = 0


                    # Se emplea un condicional elif para evaluar si, tras comprobar que el usuario no ha respondido "si", 
                    # el usuario ha respondido que "no" dispone de un cupón de descuento. 
elif cupon_descuento == "no":
                    # En caso afirmativo (el usuario ha introducido "no" como respuesta), no se aplicará descuento (se aplicará un descuento de valor 0)
    descuento = 0


                    # Si la respuesta introducida por el usuario no cumple las condiciones previas (no se ha contestado ni "si" ni "no")
else:
                    # Se muestra un mensaje informando que la respuesta no es válida, 
    print("==========")
    print("La respuesta no es válida. No se aplicará descuento")
                    # y no se aplicará descuento (se aplicará un descuento de valor 0)
    descuento = 0


                    # Se calcula el precio final a pagar como el precio original de la compra menos el descuento aplicado
                    # Se utiliza la función round() para redondear el resultado (a 2 decimales)
precio_final = round(precio_original - descuento, 2)


                    # Aunque el enunciado del ejercicio no lo especifica, se ha considerado oportuno evitar precios finales negativos.
                    # Para ello, se emplea un condicional if que evalúa si el precio final es inferior a 0. 
if precio_final < 0:
                    # En caso afirmativo, el precio final será cero. 
    precio_final = 0


                    # Por último, se muestra el precio final a pagar
print("==========")
print(f"Precio original ----------> {precio_original}")
print(f"Descuento ----------------> {descuento}")
print(f"Precio final -------------> {precio_final}")
print("==========")
print("")
print("")


# ====================================================================================================
# COMPROBACIÓN DEL PROGRAMA 
# ====================================================================================================

                    # ==========
                    # Ejemplo 1
                    # ==========
                    # Introducir 79.99 como precio original de la compra e indicar que "sí" se tiene un cupón de descuento cuyo valor es 20.50
# Output esperado:
# ====================================================================================================
# KATA 41
# ====================================================================================================
# ==========
# Precio original ----------> 79.99
# Descuento ----------------> 20.5
# Precio final -------------> 59.49
# ==========


                    # ==========
                    # Ejemplo 2
                    # ==========
                    # Introducir 79.99 como precio original de la compra e indicar que "sí" se tiene un cupón de descuento cuyo valor es 0
# Output esperado:
# ====================================================================================================
# KATA 41
# ====================================================================================================
# ==========
# El cupón de descuento no es válido. No se aplicará descuento
# ==========
# Precio original ----------> 79.99
# Descuento ----------------> 0
# Precio final -------------> 79.99
# ==========


                    # ==========
                    # Ejemplo 3
                    # ==========
                    # Introducir 79.99 como precio original de la compra e indicar que "no" se tiene un cupón de descuento
# Output esperado:
# ====================================================================================================
# KATA 41
# ====================================================================================================
# ==========
# Precio original ----------> 79.99
# Descuento ----------------> 0
# Precio final -------------> 79.99
# ==========


                    # ==========
                    # Ejemplo 4
                    # ==========
                    # Introducir 79.99 como precio original de la compra e indicar que "quizas" se tiene un cupón de descuento
# Output esperado:
# ====================================================================================================
# KATA 41
# ====================================================================================================
# ==========
# La respuesta no es válida. No se aplicará descuento
# ==========
# Precio original ----------> 79.99
# Descuento ----------------> 0
# Precio final -------------> 79.99
# ==========


                    # ==========
                    # Ejemplo 5
                    # ==========
                    # Introducir 79.99 como precio original de la compra e indicar que "sí" se tiene un cupón de descuento cuyo valor es 90.00
# Output esperado:
# ====================================================================================================
# KATA 41
# ====================================================================================================
# ==========
# Precio original ----------> 79.99
# Descuento ----------------> 90.0
# Precio final -------------> 0
# ==========