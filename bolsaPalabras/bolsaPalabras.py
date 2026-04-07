import re
import textos

vocabulario = ["investigación","Desarrollo", "Datos", "Importante", "Avances", "Tecnología",
"Futuro", "Historia", "Mundo", "Cambio", "Sociedad", "Humanidad", "Descubrimiento",
"Impacto", "Ambiente", "Ciencia", "Reto", "Solución", "Necesidad", "Visión", "Antigüedad",
"Civilización", "Revolución", "Imperio", "Conquista", "Renacimiento", "Edad Media",
"Colonialismo", "Independencia", "Evolución"]

    
# Genera una lista de diccionarios con {indice, palabra} para cada palabra del vocabulario.
# Además convierte todas las letras a minusculas.
def vocabulario_indexado():
    vocabulario_indexado = []
    indice_actual = 0
    
    for palabra in vocabulario:
        vocabulario_indexado.append({"indice": indice_actual, "palabra": palabra.lower()})
        indice_actual += 1

    return vocabulario_indexado



# Cuenta las apariciones de cada palabra del vocabulario en el texto dado
# y usa expresiones regulares para separar las palabras del texto, 
# ignorando simbolos y convirtiendo a minusculas    
def contar_palabras(texto):
    vocab_indexado = vocabulario_indexado()
    
    # inicializo vector con ceros, con la misma longitud que el vocabulario indexado
    vector = [0] * len(vocab_indexado)
    
    palabras = re.findall(r'\b\w+\b', texto.lower())
    
    for palabra in palabras:
        for item in vocab_indexado:
            if palabra == item['palabra']:
                vector[item['indice']] += 1
                
    return vector


# Devuelve el vector normalizado
def normalizar(conteos):
    total = sum(conteos)
    return [c / total for c in conteos]


# Combina las funciones de contar palabras y normalizar en un solo paso
def contar_y_normalizar(texto):
    conteos = contar_palabras(texto)
    return normalizar(conteos)

# Calcula la similitud coseno entre dos vectores dados
def calcular_similitud_coseno(vector1, vector2):
    producto_punto = sum(a * b for a, b in zip(vector1, vector2))
    magnitud_vector1 = sum(a ** 2 for a in vector1) ** 0.5
    magnitud_vector2 = sum(b ** 2 for b in vector2) ** 0.5
    
    if magnitud_vector1 == 0 or magnitud_vector2 == 0:
        return 0.0
    
    similitud = producto_punto / (magnitud_vector1 * magnitud_vector2)
    return similitud



def punto1():
    print("Punto 1: Vocabulario indexado:\n\n")
    contador = 0;
    
    print ("INDICE     PALABRA")
    
    for palabra in vocabulario:
        print(f"{ str(contador).ljust(10)} {palabra}")
        contador += 1
    
    print("\n\n")


    
def punto2():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_ciencia_tecnologia = contar_palabras(textos.ciencia_y_tecnologia)
    conteo_palabras_historia_sociedad = contar_palabras(textos.historia_y_sociedad)
    conteo_palabras_medio_ambiente = contar_palabras(textos.medio_ambiente)
    
    print("Punto 2: Conteo de palabras en cada texto dado.\n")
    print("VOCABULARIO              CONTADOR CIENCIA Y TECNOLOGIA    CONTADOR HISTORIA Y SOCIEDAD     CONTADOR MEDIO AMBIENTE")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(round(conteo_palabras_ciencia_tecnologia[contador], 5)).ljust(33) 
            + str(round(conteo_palabras_historia_sociedad[contador], 5)).ljust(33) 
            + str(round(conteo_palabras_medio_ambiente[contador], 5)))
        
        contador += 1
        
    print("\n\n")    
    
        
def punto3():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    vector_normalizado_ciencia_tecnologia = contar_y_normalizar(textos.ciencia_y_tecnologia)
    vector_normalizado_historia_sociedad = contar_y_normalizar(textos.historia_y_sociedad)      
    vector_normalizado_medio_ambiente = contar_y_normalizar(textos.medio_ambiente)
    
    
    print("Punto 3: Vector de palabras normalizado para los textos dados.\n")
    print("VOCABULARIO              CIENCIA Y TECNOLOGIA NORMALIZADO    HISTORIA Y SOCIEDAD NORMALIZADO    MEDIO AMBIENTE NORMALIZADO")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(round(vector_normalizado_ciencia_tecnologia[contador], 5)).ljust(36) 
            + str(round(vector_normalizado_historia_sociedad[contador], 5)).ljust(35) 
            + str(round(vector_normalizado_medio_ambiente[contador], 5)).ljust(35))
        
        contador += 1
        
    print("\n\n")
        

def punto3b():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    vector_normalizado_tema_desconocido_0 = contar_y_normalizar(textos.tema_desconocido_0)
    vector_normalizado_tema_desconocido_1 = contar_y_normalizar(textos.tema_desconocido_1)
    vector_normalizado_tema_desconocido_2 = contar_y_normalizar(textos.tema_desconocido_2)  
    
    print("Vector de palabras normalizado para los textos desconocidos.\n")
    print("VOCABULARIO              DESCONOCIDO 0 NORMALIZADO           DESCONOCIDO 1 NORMALIZADO          DESCONOCIDO 2 NORMALIZADO")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(round(vector_normalizado_tema_desconocido_0[contador], 5)).ljust(36) 
            + str(round(vector_normalizado_tema_desconocido_1[contador], 5)).ljust(35) 
            + str(round(vector_normalizado_tema_desconocido_2[contador], 5)))
        
        contador += 1

    print("\n\n")
    

def punto4():
    similitud_ciencia_tecnologia_y_desconocido_0 = calcular_similitud_coseno(
        contar_y_normalizar(textos.ciencia_y_tecnologia),
        contar_y_normalizar(textos.tema_desconocido_0)
    )
    similitud_medio_ambiente_y_desconocido_0 = calcular_similitud_coseno(
        contar_y_normalizar(textos.medio_ambiente),
        contar_y_normalizar(textos.tema_desconocido_0)  
    )
    similitud_historia_sociedad_y_desconocido_0 = calcular_similitud_coseno(
        contar_y_normalizar(textos.historia_y_sociedad),
        contar_y_normalizar(textos.tema_desconocido_0)
    )

    similitud_ciencia_tecnologia_y_desconocido1 = calcular_similitud_coseno(
        contar_y_normalizar(textos.ciencia_y_tecnologia),
        contar_y_normalizar(textos.tema_desconocido_1)
    )
    similitud_medio_ambiente_y_desconocido_1 = calcular_similitud_coseno(
        contar_y_normalizar(textos.medio_ambiente),
        contar_y_normalizar(textos.tema_desconocido_1)
    )
    similitud_historia_sociedad_y_desconocido_1 = calcular_similitud_coseno(
        contar_y_normalizar(textos.historia_y_sociedad),
        contar_y_normalizar(textos.tema_desconocido_1)
    )

    similitud_ciencia_tecnologia_y_desconocido_2 = calcular_similitud_coseno(
        contar_y_normalizar(textos.ciencia_y_tecnologia),
        contar_y_normalizar(textos.tema_desconocido_2)
    )
    similitud_medio_ambiente_y_desconocido_2 = calcular_similitud_coseno(
        contar_y_normalizar(textos.medio_ambiente),
        contar_y_normalizar(textos.tema_desconocido_2)
    )
    similitud_historia_sociedad_y_desconocido_2 = calcular_similitud_coseno(
        contar_y_normalizar(textos.historia_y_sociedad),
        contar_y_normalizar(textos.tema_desconocido_2)
    )

    print("Punto 4: Calculo de similitud coseno entre los textos desconocidos y los temas conocidos:\n(La similitud coseno de cada comparacion se muestra en la interseccion de cada fila y columna correspondientes)\n\n")

    print("-                          DESCONOCIDO 0                     DESCONOCIDO 1                     DESCONOCIDO 2   ")
    print(f"CIENCIA Y TECNOLOGIA         { str(round(similitud_ciencia_tecnologia_y_desconocido_0, 2)).ljust(34) + str(round(similitud_ciencia_tecnologia_y_desconocido1, 2)).ljust(34) + str(round(similitud_ciencia_tecnologia_y_desconocido_2, 2)).ljust(34)}")
    print(f"HISTORIA Y SOCIEDAD          { str(round(similitud_historia_sociedad_y_desconocido_0, 2)).ljust(34) + str(round(similitud_historia_sociedad_y_desconocido_1, 2)).ljust(34) + str(round(similitud_historia_sociedad_y_desconocido_2, 2)).ljust(34)}")
    print(f"MEDIO AMBIENTE               { str(round(similitud_medio_ambiente_y_desconocido_0, 2)).ljust(34) + str(round(similitud_medio_ambiente_y_desconocido_1, 2)).ljust(34) + str(round(similitud_medio_ambiente_y_desconocido_2, 2)).ljust(34)}")

    print("\n\n")


punto1()        
punto2()
punto3()
punto3b()
punto4()


