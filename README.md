# DA-promo-c-modulo-2-sprint-2-Anahi-Mai


Repositorio para los ejercicios de Limpieza, EDA y ETL de los pair-programing del módulo 2-sprint 2 del Bootcamp de Data Analyst PromoC
Anahi Morales y Marina Ruiz
---


LIMPIEZA

- Limpieza I: Introducción --> Hechos / Comentados
    - Eliminar columnas  con .drop().
    - Duplicados con .duplicated().
    - Cambio del tipo de datos en columnas a traves de .astype().
    - Uniformidad en los datos de las columnas.

- Limpieza II: Strings --> Hechos / Comentados
    - Extraccion de datos importantes a traves de patrones de Regex
    - Uso de .apply()
    - Cambio del tipo de datos en columnas a traves de pd.to_numeric().

- Limpieza III: Valores extremos/Outliers --> Hechos / Comentados
    - Deteccion de outliers en columnas numericas.
    - Uso de np.nanpercentile.
    - Visualizacion de boxplot.

- Limpieza IV: Valores nulos --> Hechos / Comentados
    - Uso de .stb.missing() para ver porcentajes de nulos.
    - Reemplazo de nulos a traves de metodo .fillna() y .replace().
   
- Limpieza V: Valores nulos Sklearn --> Hechos / Comentados
    - Uso del metodo Simple Imputer para reemplazar nulos.
    - Uso metodo KNN  y Interative Imputer para reemplazar valores nulos de columnas numericas.
    

---

EDA

- EDA I: Introducción --> Hechos / Comentados
    - Uso de metodos .head(), .shape, .columns para analisis exploratorio del dataframe.
    - Porcentaje de valores nulos.
    - Tipos de datos en cada columna con .dtypes.
    - Informacion general de dataframe con el uso de .info()
    - Uso de .describe() separando entre variables numericas y categoricas.
    - Creacion de un dataframe que contiene los unique de cada columna.
    

- EDA II: Nulos y valores extremos --> Hechos / Comentados
    - Uso de libreria sidetable para identificar valores nulos con **.stb.missing()**
    - Analisis de variables en columnas teniendo en cuenta la frecuecia de las mismas con distintos porcentajes de acumulados con .stb.freq()

- EDA III: Outliers --> Hechos / Comentados



---

ETL

- ETL I: Extracción- API's --> Hechos / Comentados

- ETL II : Transformación I - Limpieza --> 

- ETL III: Transformación II - Clases y Funciones de limpieza --> 

- ETL IV: Carga I - Creación BBDD e inserción de datos --> 

- ETL V: Carga II - Clases y Funciones BBDD e inserción --> 

- ETL VI: Transformación II - Ejecutable - Pipeline ETL --> 
