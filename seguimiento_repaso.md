EDA I
- Librerias arriba/quito numpy y dejo solo pandas
- llegamos a estas conclusións
    - La columna 'sex_' no es clara y tenemos la columna 'sexo' que esta mejor categorizada.
    - La columna 'fatal_(y/n)' es redundante y tenemos la columna 'fatal' mejor categorizada.
    - La columna 'href' tiene un link del cual no podemos obtener informacion para el analisis de los datos, ya que son fotografias.
    - La columna 'date' no tiene un orden logico en cada fila, es decir depende de como cada usuario inserto los datos.

LIMPIEZA I

- borramos ['area', 'location', 'name', 'time', 'href', 'fatal_(y/n)', 'injury', 'sex_']
- columnas que quedan:	case_number	year	type	country	activity	age	species_	date	mes_ataque	fatal	sexo
- ejercicio 3, cambiamos year de float a integer, porque no a date? --> por lo que quito la librería datetime de arriba
- Empezamos a guardar el archivo como pkl

EDA II
- quito las librerias de seaborn y matloplib, si queremos hacer algun gráfico habría que añadirlas pero no lo hicimos, solo utilizamos sidetable.


LIMPIEZA II
- ejercicio 1, creamos una nueva columna df["cat_species"] = df["species_"], mantenemos las dos, borrar species_????
- ejercicio 2, creamos una nueva columna df['edades'] = df['age'], mantenemos las dos, borrar age????


EDA III
- podríamos crear una lista para ordenar las gráfica de mayor a menor

LIMPIEZA IV
- librerias arriba
- pkl cambiado

LIMPIEZA V
- librerias arriba
- pkl cambiado 




