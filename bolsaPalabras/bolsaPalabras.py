import re
import textos

vocabulario = ["investigación","Desarrollo", "Datos", "Importante", "Avances", "Tecnología",
"Futuro", "Historia", "Mundo", "Cambio", "Sociedad", "Humanidad", "Descubrimiento",
"Impacto", "Ambiente", "Ciencia", "Reto", "Solución", "Necesidad", "Visión", "Antigüedad",
"Civilización", "Revolución", "Imperio", "Conquista", "Renacimiento", "Edad Media",
"Colonialismo", "Independencia", "Evolución"]
    
# Genera una lista de diccionarios con {indice, palabra} para cada palabra del vocabulario.
# Además convierte las palabras a minusculas.

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



def punto1():
  print("1) VOCABULARIO INDEXADO:\n")
  
  for palabra in vocabulario_indexado():
    print(f"id:{palabra['indice']} palabra: {palabra['palabra']}")
    

    
def punto2():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_ciencia_tecnologia = contar_palabras(textos.ciencia_y_tecnologia)
    conteo_palabras_historia_sociedad = contar_palabras(textos.historia_y_sociedad)
    conteo_palabras_medio_ambiente = contar_palabras(textos.medio_ambiente)
    
    print("VOCABULARIO              CONTADOR CIENCIA Y TECNOLOGIA    CONTADOR HISTORIA Y SOCIEDAD    CONTADOR MEDIO AMBIENTE")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(conteo_palabras_ciencia_tecnologia[contador]).ljust(30) 
            + str(conteo_palabras_historia_sociedad[contador]).ljust(30) 
            + str(conteo_palabras_medio_ambiente[contador]))
        
        contador += 1
        

    
def punto2():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_ciencia_tecnologia = contar_palabras(textos.ciencia_y_tecnologia)
    conteo_palabras_historia_sociedad = contar_palabras(textos.historia_y_sociedad)
    conteo_palabras_medio_ambiente = contar_palabras(textos.medio_ambiente)
    
    print("VOCABULARIO              CONTADOR CIENCIA Y TECNOLOGIA    CONTADOR HISTORIA Y SOCIEDAD    CONTADOR MEDIO AMBIENTE")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(conteo_palabras_ciencia_tecnologia[contador]).ljust(33) 
            + str(conteo_palabras_historia_sociedad[contador]).ljust(33) 
            + str(conteo_palabras_medio_ambiente[contador]))
        
        contador += 1
        
        
def sumar(numeros):
    suma = 0
    for numero in numeros:
        suma += numero              
    return suma
        
        
def punto3():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_ciencia_tecnologia = contar_palabras(textos.ciencia_y_tecnologia)
    conteo_palabras_historia_sociedad = contar_palabras(textos.historia_y_sociedad)
    conteo_palabras_medio_ambiente = contar_palabras(textos.medio_ambiente)
    
    suma_ciencia_tecnologia = sumar(conteo_palabras_ciencia_tecnologia)
    suma_historia_sociedad = sumar(conteo_palabras_historia_sociedad)
    suma_medio_ambiente = sumar(conteo_palabras_medio_ambiente)

    
    print("\n\nVOCABULARIO              CIENCIA Y TECNOLOGIA NORMALIZADO    HISTORIA Y SOCIEDAD NORMALIZADO   MEDIO AMBIENTE NORMALIZADO")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(
                conteo_palabras_ciencia_tecnologia[contador] / suma_ciencia_tecnologia
                ).ljust(36) 
            + str(
                conteo_palabras_historia_sociedad[contador] / suma_historia_sociedad
                ).ljust(35) 
            + str(
                conteo_palabras_medio_ambiente[contador] / suma_medio_ambiente
                ).ljust(35))
        
        contador += 1
        
        
def punto3():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_ciencia_tecnologia = contar_palabras(textos.ciencia_y_tecnologia)
    conteo_palabras_historia_sociedad = contar_palabras(textos.historia_y_sociedad)
    conteo_palabras_medio_ambiente = contar_palabras(textos.medio_ambiente)
    
    suma_ciencia_tecnologia = sumar(conteo_palabras_ciencia_tecnologia)
    suma_historia_sociedad = sumar(conteo_palabras_historia_sociedad)
    suma_medio_ambiente = sumar(conteo_palabras_medio_ambiente)

    
    print("\n\nVOCABULARIO              CIENCIA Y TECNOLOGIA NORMALIZADO    HISTORIA Y SOCIEDAD NORMALIZADO   MEDIO AMBIENTE NORMALIZADO")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(
                conteo_palabras_ciencia_tecnologia[contador] / suma_ciencia_tecnologia
                ).ljust(36) 
            + str(
                conteo_palabras_historia_sociedad[contador] / suma_historia_sociedad
                ).ljust(35) 
            + str(
                conteo_palabras_medio_ambiente[contador] / suma_medio_ambiente
                ).ljust(35))
        
        contador += 1
        

def punto3b():
    cant_palabras = len(vocabulario)
    contador = 0;
    
    conteo_palabras_tema_desconocido_0 = contar_palabras(textos.tema_desconocido_0)
    conteo_palabras_tema_desconocido_1 = contar_palabras(textos.tema_desconocido_1)
    conteo_palabras_tema_desconocido_2   = contar_palabras(textos.tema_desconocido_2  )
    
    suma_tema_desconocido_0 = sumar(conteo_palabras_tema_desconocido_0)
    suma_tema_desconocido_1 = sumar(conteo_palabras_tema_desconocido_1)
    suma_tema_desconocido_2   = sumar(conteo_palabras_tema_desconocido_2)

    
    print("\n\nVOCABULARIO              DESCONOCIDO 0 NORMALIZADO    DESCONOCIDO 1 NORMALIZADO   DESCONOCIDO 3 NORMALIZADO")
    
    while contador < cant_palabras:
        print(vocabulario[contador].ljust(25) 
            + str(
                conteo_palabras_tema_desconocido_0[contador] / suma_tema_desconocido_0
                ).ljust(36) 
            + str(
                conteo_palabras_tema_desconocido_1[contador] / suma_tema_desconocido_1
                ).ljust(35) 
            + str(
                conteo_palabras_tema_desconocido_2[contador] / suma_tema_desconocido_2
                ))
        
        contador += 1
        

        
punto2()
punto3()
punto3b()
