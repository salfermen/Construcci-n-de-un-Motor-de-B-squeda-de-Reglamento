import math
import re

# Paso 1: Dataset sugerido (10 documentos simulando el reglamento)
documentos_reglamento = [
    "Artículo 15: La pérdida de cupo ocurre por promedio inferior a 3.0 o falta disciplinaria grave.",
    "Artículo 22: El estudiante tiene derecho a solicitar supletorios en los tres días siguientes a la falta.",
    "Artículo 45: Las becas por excelencia académica se otorgan al promedio más alto de cada facultad.",
    "Artículo 50: La cancelación de semestre debe hacerse antes de la semana 10 del calendario académico.",
    "Artículo 12: Las faltas disciplinarias se dividen en leves, graves y gravísimas según el manual.",
    "Artículo 18: El trabajo de grado es requisito obligatorio para optar por el título profesional.",
    "Artículo 33: Las pasantías empresariales podrán ser homologadas como trabajo de grado.",
    "Artículo 8: El fraude en exámenes será considerado una falta disciplinaria gravísima.",
    "Artículo 25: El estudiante podrá cancelar materias máximo hasta la cuarta semana de clases.",
    "Artículo 10: Para mantener la beca, el estudiante no puede tener ninguna falta disciplinaria."
]

# Función auxiliar para limpiar y tokenizar el texto (pasar a minúsculas y quitar comas/puntos)
def tokenizar(texto):
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    return texto_limpio.split()

# Procesamos todos los documentos
docs_tokenizados = [tokenizar(doc) for doc in documentos_reglamento]
total_docs = len(docs_tokenizados)

# Paso 2: Implementación de funciones

def calcular_tf(palabra, doc_tokens):
    """Calcula el TF: frecuencia_palabra / total_palabras_doc"""
    frecuencia = doc_tokens.count(palabra)
    total_palabras = len(doc_tokens)
    if total_palabras == 0: return 0
    return frecuencia / total_palabras

def calcular_idf(palabra, todos_los_docs_tokens):
    """Calcula el IDF: log(Total_Docs / Docs_con_la_palabra)"""
    docs_con_palabra = sum(1 for doc in todos_los_docs_tokens if palabra in doc)
    if docs_con_palabra == 0: return 0 # Evitar división por cero si la palabra no existe
    # Usamos logaritmo en base 10 (puede ser base e también)
    return math.log10(total_docs / docs_con_palabra)

def calcular_score_final(consulta, doc_index, todos_los_docs_tokens):
    """Suma el TF-IDF de cada palabra de la consulta para un documento específico"""
    tokens_consulta = tokenizar(consulta)
    doc_tokens = todos_los_docs_tokens[doc_index]
    score_final = 0
    
    for palabra in tokens_consulta:
        tf = calcular_tf(palabra, doc_tokens)
        idf = calcular_idf(palabra, todos_los_docs_tokens)
        score_final += (tf * idf)
        
    return score_final

# Paso 3: Ejecutar búsquedas
def buscar(consulta, top_n=3):
    resultados = []
    for i, doc in enumerate(documentos_reglamento):
        score = calcular_score_final(consulta, i, docs_tokenizados)
        if score > 0: # Solo guardamos si el score es mayor a 0
            resultados.append({"documento": doc, "score": score})
    
    # Ordenar de mayor a menor score
    resultados_ordenados = sorted(resultados, key=lambda x: x["score"], reverse=True)
    
    print(f"\n--- Resultados para la búsqueda: '{consulta}' ---")
    if not resultados_ordenados:
        print("No se encontraron documentos relevantes.")
    for rank, res in enumerate(resultados_ordenados[:top_n]):
        print(f"Top {rank+1} (Score: {res['score']:.4f}) -> {res['documento']}")

# ================= EJECUCIÓN DE PRUEBAS =================

# 1. Pruebas de Búsqueda (Para tu presentación)
buscar("falta disciplinaria grave")
buscar("cancelar semestre")
buscar("beca por excelencia")

# 2. Obtener Palabras con mayor y menor IDF (Para tu presentación)
vocabulario = set(palabra for doc in docs_tokenizados for palabra in doc)
idf_diccionario = {palabra: calcular_idf(palabra, docs_tokenizados) for palabra in vocabulario}

# Ordenar por IDF
idf_ordenado = sorted(idf_diccionario.items(), key=lambda x: x[1])

print("\n--- Análisis de IDF ---")
print("Top 5 palabras con IDF MÁS BAJO (Comunes):")
for palabra, idf in idf_ordenado[:5]: print(f"- '{palabra}': {idf:.4f}")

print("\nTop 5 palabras con IDF MÁS ALTO (Raras/Específicas):")
for palabra, idf in idf_ordenado[-5:]: print(f"- '{palabra}': {idf:.4f}")