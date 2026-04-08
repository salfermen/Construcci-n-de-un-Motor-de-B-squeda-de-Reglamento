# 🔍 Motor de Búsqueda TF-IDF — Reglamento Universitario

Motor de búsqueda semántico basado en el algoritmo **TF-IDF** (Term Frequency – Inverse Document Frequency), aplicado sobre artículos de un reglamento universitario. El sistema recupera los documentos más relevantes para una consulta dada, ordenados por relevancia.

---

## 📋 Descripción del Proyecto

El proyecto implementa desde cero los componentes matemáticos del algoritmo TF-IDF para indexar y buscar dentro de un corpus de 10 artículos reglamentarios simulados. Dado un texto de búsqueda, el sistema calcula un score de relevancia por documento y retorna los resultados ordenados de mayor a menor.

### Componentes principales

- **Dataset**: 10 artículos del reglamento universitario (simulados).
- **Tokenizador**: limpieza de texto (minúsculas, eliminación de signos de puntuación) y división en tokens.
- **TF (Term Frequency)**: mide qué tan frecuente es una palabra dentro de un documento específico.
- **IDF (Inverse Document Frequency)**: mide qué tan rara o específica es una palabra en todo el corpus.
- **Score TF-IDF**: producto de TF × IDF para cada palabra de la consulta, sumado por documento.
- **Ranking**: los documentos se ordenan de mayor a menor score y se retornan los `top_n` más relevantes.

### Fórmulas utilizadas

```
TF(palabra, doc)  = frecuencia_de_palabra / total_palabras_en_doc

IDF(palabra)      = log₁₀(Total_documentos / Documentos_que_contienen_la_palabra)

Score(consulta, doc) = Σ TF(palabra, doc) × IDF(palabra)
                       para cada palabra en la consulta
```

---

## 📁 Estructura del Proyecto

```
.
└── main.py       # Código fuente completo del motor de búsqueda
```

---

## ⚙️ Requisitos

- Python **3.6 o superior**
- Módulos de la biblioteca estándar únicamente:
  - `math` — para la función logarítmica (`math.log10`)
  - `re` — para limpieza y tokenización de texto

No se requiere instalar ninguna dependencia externa.

---

## 🚀 Instrucciones de Ejecución

### 1. Clonar o descargar el archivo

Asegúrate de tener el archivo `main.py` en tu directorio de trabajo.

### 2. Ejecutar el script

Abre una terminal en el directorio donde se encuentra el archivo y ejecuta:

```bash
python main.py
```

> En algunos sistemas puede ser necesario usar `python3`:
> ```bash
> python3 main.py
> ```

### 3. Resultado esperado

Al ejecutar el script se corren automáticamente tres búsquedas de prueba y un análisis de IDF del vocabulario completo.

---

## 📊 Ejemplos de Ejecución

### Ejemplo 1 — Búsqueda: `"falta disciplinaria grave"`

El sistema identifica los artículos más relacionados con faltas disciplinarias:

```
--- Resultados para la búsqueda: 'falta disciplinaria grave' ---
Top 1 (Score: 0.1201) -> Artículo 15: La pérdida de cupo ocurre por promedio inferior a 3.0 o falta disciplinaria grave.
Top 2 (Score: 0.0767) -> Artículo 8:  El fraude en exámenes será considerado una falta disciplinaria gravísima.
Top 3 (Score: 0.0658) -> Artículo 10: Para mantener la beca, el estudiante no puede tener ninguna falta disciplinaria.
```

El Artículo 15 obtiene el score más alto porque contiene las tres palabras de la consulta con alta frecuencia relativa. El Artículo 8 también aparece porque comparte el término "falta disciplinaria", aunque la palabra "grave" no coincide exactamente (sí aparece "gravísima").

---

### Ejemplo 2 — Búsqueda: `"cancelar semestre"`

```
--- Resultados para la búsqueda: 'cancelar semestre' ---
Top 1 (Score: 0.0714) -> Artículo 25: El estudiante podrá cancelar materias máximo hasta la cuarta semana de clases.
Top 2 (Score: 0.0625) -> Artículo 50: La cancelación de semestre debe hacerse antes de la semana 10 del calendario académico.
```

El Artículo 25 lidera porque contiene el verbo "cancelar" de forma directa. El Artículo 50 aparece en segundo lugar por la presencia de "semestre" y la raíz "cancelación" (tratada como token diferente, pero relacionado semánticamente).

---

### Ejemplo 3 — Búsqueda: `"beca por excelencia"`

```
--- Resultados para la búsqueda: 'beca por excelencia' ---
Top 1 (Score: 0.0952) -> Artículo 45: Las becas por excelencia académica se otorgan al promedio más alto de cada facultad.
Top 2 (Score: 0.0714) -> Artículo 10: Para mantener la beca, el estudiante no puede tener ninguna falta disciplinaria.
Top 3 (Score: 0.0349) -> Artículo 18: El trabajo de grado es requisito obligatorio para optar por el título profesional.
```

El Artículo 45 obtiene el mayor score al contener tanto "becas" como "excelencia". El Artículo 10 aparece por la coincidencia con "beca". El Artículo 18 tiene el score más bajo porque solo comparte palabras comunes de baja especificidad.

---

### Ejemplo 4 — Análisis de IDF del vocabulario

El script también imprime las palabras con mayor y menor IDF del corpus completo:

```
--- Análisis de IDF ---
Top 5 palabras con IDF MÁS BAJO (Comunes en el corpus):
- 'artículo':  0.0000   ← aparece en los 10 documentos → IDF = log(10/10) = 0
- 'de':        0.2218
- 'el':        0.2218
- 'la':        0.3010
- 'falta':     0.3979

Top 5 palabras con IDF MÁS ALTO (Raras / Específicas):
- 'mantener':  1.0000   ← aparece solo en 1 documento → IDF = log(10/1) = 1
- 'debe':      1.0000
- '30':        1.0000
- 'ninguna':   1.0000
- '12':        1.0000
```

Las palabras con IDF = 0 (como "artículo") aparecen en todos los documentos y no aportan información discriminatoria. Las palabras con IDF = 1.0 son únicas en el corpus y son las más útiles para identificar documentos específicos.

---

## 🧠 Cómo funciona el algoritmo paso a paso

```
Consulta del usuario
        │
        ▼
  Tokenización
  (minúsculas + sin puntuación)
        │
        ▼
  Para cada documento:
  ┌─────────────────────────┐
  │  Calcular TF por palabra │
  │  Calcular IDF por palabra│
  │  Score += TF × IDF      │
  └─────────────────────────┘
        │
        ▼
  Ordenar documentos
  por score descendente
        │
        ▼
  Mostrar Top N resultados
```

---

## 🔧 Personalización

Puedes modificar fácilmente el comportamiento del script:

| Qué cambiar | Dónde | Cómo |
|---|---|---|
| El corpus de documentos | Variable `documentos_reglamento` | Agrega o reemplaza artículos en la lista |
| Las consultas de búsqueda | Llamadas a `buscar(...)` al final | Cambia el texto entre comillas |
| Número de resultados | Parámetro `top_n` en `buscar()` | Por defecto es 3; cámbialo a cualquier entero |
| Base del logaritmo | Función `calcular_idf()` | Reemplaza `math.log10` por `math.log` para base e |

---

## 📌 Notas técnicas

- El algoritmo **no** aplica stemming ni lematización. Las variantes de una misma palabra (`beca` / `becas`, `cancelar` / `cancelación`) se tratan como tokens distintos.
- Los documentos con **score = 0** se excluyen de los resultados automáticamente.
- El IDF usa **logaritmo en base 10**. Cambiarlo a base natural (`math.log`) modificará los valores absolutos pero no el orden de relevancia.
