# DA-promo-c-modulo-2-sprint-2-Anahi-Mai


Repositorio para los ejercicios de Limpieza, EDA y ETL de los pair-programing del módulo 2-sprint 2 del Bootcamp de Data Analyst PromoC
Anahi Morales y Marina Ruiz
---

Librerias utilizadas:

- numpy
- panda
- datetime
- re
- ast
- requests
- sidetable
- seaborn
- matplotlib.pyplot 
- from sklearn.impute import SimpleImputer
- from sklearn.experimental import enable_iterative_imputer
- from sklearn.impute import IterativeImputer
- from sklearn.impute import KNNImputer
---

LIMPIEZA

- Limpieza I: Introducción 
    - Eliminar columnas  con _.drop()_.
    - Duplicados con _.duplicated()_.
    - Cambio del tipo de datos en columnas a traves de _.astype()_.
    - Uniformidad en los datos de las columnas.

- Limpieza II: Strings 
    - Extraccion de datos importantes a traves de patrones de _Regex_
    - Uso de _.apply()_.
    - Cambio del tipo de datos en columnas a traves de _pd.to_numeric()_.

- Limpieza III: Valores extremos/Outliers 
    - Deteccion de outliers en columnas numericas.
    - Uso de _np.nanpercentile_.
    - Visualizacion a traves de _boxplot_.

- Limpieza IV: Valores nulos 
    - Uso de ._stb.missing()_ para ver porcentajes de nulos.
    - Reemplazo de nulos a traves de metodo _.fillna()_ y _.replace()_.
   
- Limpieza V: Valores nulos Sklearn 
    - Uso del metodo _Simple Imputer- para reemplazar nulos.
    - Uso metodo _KNN_ y _Interative Imputer_ para reemplazar valores nulos de columnas numericas.
---

EDA

- EDA I: Introducción 
    - Uso de metodos _.head(), .shape, .columns_ para analisis exploratorio del dataframe.
    - Porcentaje de valores nulos.
    - Tipos de datos en cada columna con _.dtypes_.
    - Informacion general de dataframe con el uso de _.info()_.
    - Uso de _.describe()_ separando entre variables numericas y categoricas.
    - Creacion de un dataframe que contiene los unique de cada columna.
    

- EDA II: Nulos y valores extremos 
    - Uso de libreria sidetable para identificar valores nulos con _.stb.missing()_
    - Analisis de variables en columnas teniendo en cuenta la frecuecia de las mismas con distintos porcentajes de acumulados con _.stb.freq()_.
    

- EDA III: Outliers 
    - Visualizacion de datos a traves de _countplot_.
    - Uso de _pd.cut()_ para categorizar columnas.
    - Analisis de datos a traves de graficas.
---

ETL

- ETL I: Extracción- API's 
    - Extraccion de datos de API de clima.
    - Tratamiento para poder desempaquetar los datos obtenidos en un dataframe con el uso           de _pd.json_normalize_, for loop para iterar sobre los mismos y uso de _pd.concat()_           para union de datos.
        

- ETL II : Transformación I - Limpieza 
    - Transformacion de datos con el uso de _.apply(pd.Series)_.
    - Uso de _.groupby()_ para obtener la media por paises.
    - Union de archivos a traves de _.merge()_.
        

- ETL III: Transformación II - Clases y Funciones de limpieza 
    - Creamos clase que conecta con API de informacion meteorologica, que los limpia, los anexa con un dataframe y chequea su informacion.


- ETL IV: Carga I - Creación BBDD e inserción de datos
    - Definimos funciones para:
        - Crear base de datos
        - Crear tablas
        - Insertar datos

- ETL V: Carga II - Clases y Funciones BBDD e inserción
    - Creamos una clase automatizando la creacion de base de datos, creacion de tablas e insercion de datos.

- ETL VI: Transformación II - Ejecutable - Pipeline ETL
    - Creamos dos archivos con extension '.py' donde   almacenamos las distintas  clases creadas  en los anteriores pairprogrammings.
