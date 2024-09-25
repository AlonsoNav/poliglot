# Manual de Usuario

Este proyecto utiliza las siguientes dependencias:

- `pydrive2`: Permite interactuar con la API de Google Drive.
- `radon`: Herramienta de análisis de código.
- `pandas`: Biblioteca para manipulación y análisis de datos.
- `pyodbc`: Permite conectarse a bases de datos ODBC.
- `python-dotenv`: Carga variables de entorno desde un archivo `.env`.
- `pdfplumber`: Permite extraer texto de archivos PDF.

Además, se requieren los siguientes archivos:

- `client_secrets.json`: Contiene las credenciales para autenticarse con la API de Google Drive.
- `.env`: Contiene variables de entorno, como la cadena de conexión a la base de datos.

## Uso

Para ejecutar el script, utilice el siguiente comando:

```bash
python .\main.py [-h] [-dg DRIVE_GROUP] [-de DRIVE_EXERCISES]
```

Las opciones disponibles son:

- `-h`, `--help`: Muestra el mensaje de ayuda y sale.
- `-dg DRIVE_GROUP`, `--drive_group DRIVE_GROUP`: Descarga grupos desde la ruta de Google Drive y los carga en la base de datos. La ruta debe ser "DATOS/year-semester/".
- `-de DRIVE_EXERCISES`, `--drive_exercises DRIVE_EXERCISES`: Descarga ejercicios desde la ruta de Google Drive y los carga en la base de datos. La ruta debe ser "DATOS/year-semester/profesor nombre completo".

## Ejemplo de uso

Para descargar grupos desde Google Drive y cargarlos en la base de datos, ejecute:

```bash
python .\main.py -dg "DATOS/2024-1/"
```

Para descargar ejercicios desde Google Drive y cargarlos en la base de datos, ejecute:

```bash
python .\main.py -de "DATOS/2024-1/Coto Sarmiento Laura"
```

Asegúrese de tener los archivos `client_secrets.json` y `.env` en el mismo directorio que el script `main.py`.

# Guía de Estandarización
## Estructura General

```markdown-tree
DATOS
	2024-1
		Avilés Cisnero Mauricio
			...
		Coto Sarmiento Laura
			...
		Mata Rodríguez William
			...
		Mora Rojas Diego
		Solano Fernández Ericka
```

La estructura general consiste en una carpeta para cada profesor cuyos grupos de estudiantes dieron su consentimiento y de los cuales se lograron obtener datos. Cada carpeta contiene la información correspondiente a los grupos específicos de ese profesor para los que se consiguió acceso a los datos.
## Mauricio Avilés Cisnero
En la carpeta principal de este profesor tenemos la siguiente estructura de carpetas y archivos:

```markdown-tree
Avilés Cisnero Mauricio
	IC-1802 Introducción a la programación G41
		...
	IC-1803 Taller de programación G41
		...
	2024 - 1 - IC1802 - Grupo 41 - AVILES CISNEROS MAURICIO_1724800706370.xlsx
	2024 - 1 - IC1803 - Grupo 41 - AVILES CISNEROS MAURICIO_1724801669415.xlsx
```

Como se puede apreciar, hay dos archivos *xlsx* donde se tienen los datos fundamentales de los estudiantes de los estudiantes; tanto de Introducción a la Programación como de Taller de Programación. Además, se tienen dos carpetas donde estarán los datos de cada evaluación realizada por los estudiantes en cada uno de los cursos.

```markdown-tree
	IC-1802 Introducción a la programación G41
		Parcial 1
			<Estudiantes>
				borrado recursivo.py
				familias de números enteros.py
				suma estacionaria.py
				desglose.xlsx
			enunciado.pdf
			keywords1.csv
			notas.csv
		Parcial 2
			<Estudiantes>
				elementos repetidos en una lista.py
				quick sort descendente.py
				validación de sudoku.py
				desglose.xlsx
			enunciado.pdf
			keywords1.csv
			notas.csv
```

Para la estructura correspondiente a la carpeta de Introducción a la Programación es importante tomar en cuenta los siguientes elementos:
- **< Estudiantes > :** Corresponden a subcarpetas por cada uno de los estudiantes del grupo, nombradas con el número de carnet del mismo. 
- **enunciado.pdf :** Consiste en un archivo con las intrucciones entregadas por el profesor a los estudiantes para la realización de los ejercicios.
- **notas.csv :** En este archivo encontraremos una tabla en formato *csv* donde se tendrá el nombre completo y carnet de los estudiantes junto a la nota obtenida en el parcial correspondiente.
- **keywords(n).csv :** Este archivo contiene una serie de palabras clave que serán de utilidad para la posterior manipulación y acceso a los datos.
- **desglose.xlsx :** Es un archivo donde se tiene una tabla para poder almacenar la nota obtenida por el estudiante en cada uno de los ejercicios.

```markdown-tree
IC-1803 Taller de programación G41
	Tarea 4
		enunciado.pdf
		<estudiante>.py
	Tarea 5
		enunciado.pdf
		<estudiante>.py
	Tarea 6
		enunciado.pdf
		<estudiante>.py
	Tarea 7
		enunciado.pdf
		<estudiante>.py
```

Para la carpeta correspondiente al curso de Taller de Programación es importante tomar en cuenta los siguientes elementos:
- **enunciado.pdf :** Consiste en un archivo con las intrucciones entregadas por el profesor a los estudiantes para la realización de los ejercicios.
- **< estudiante >.py :** Archivo *.py* correspondiente a la entrega del estudiante para dicha evaluación. Nombrado con el número de carnet del estudiante en cuestión.
## William Mata Rodríguez
En la carpeta principal de este profesor tenemos la siguiente estructura de carpetas y archivos:

```markdown-tree
Mata Rodríguez William
	IC1802-Introducción a la programación G03
		...
	IC1802-Introducción a la programación G04
		...
	( Formateado ) 2024 - 1 - IC1802 - Grupo 3 - MATA RODRIGUEZ WILLIAM_1724800641967.xlsx
	( Formateado ) 2024 - 1 - IC1802 - Grupo 4 - MATA RODRIGUEZ WILLIAM_1724800655648.xlsx
```

Como podemos ver, tenemos dos archivos de tipo *xlsx* donde están los datos fundamentales de los estudiantes de ambos grupos del curso Introducción a la programación (IC1802). Entre estos datos están el número de carnet, nombre completo, correo electrónico, correo secundario y estado respectivamente. Además de estos archivos, tendremos dos carpetas donde estarán los datos de cada evaluación realizada por los estudiantes.

```markdown-tree
IC1802-Introducción a la programación G03
	Parcial 1
		(SIN DATOS)
	Parcial 2
		<Estudiantes>
			Calificaciones_Por_Estudiante.py
			Cuadrado_Magico.py
			Orden.py
			Matriz_DSI.py
			desglose.xlsx
		Enunciado.pdf
		notas.csv
		Comprimido.zip
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
	Parcial 3
		<Estudiantes>
			Lista_Estudiantes.py
			Altamente_Abundante.py
			Extraer_Lista.py
			Formatear_Texto.py
			desglose.xlsx
		Enunciado.pdf
		notas.csv
		Comprimido.zip
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
	Parcial 4
		<Estudiantes>
			Crear_Diccionario.py
			Rango_Compuestos.py
			Mayores_Menores.py
			Listas_Ordenadas.py
			desglose.xlsx
		Enunciado.pdf
		notas.csv
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
```

```markdown-tree
IC1802-Introducción a la programación G04
	Parcial 1
		(SIN DATOS)
	Parcial 2
		<Estudiantes>
			Es_Keith.py
			Crear_Listas.py
			Mayores_Menores.py
			Diagonales.py
			desglose.xlsx
		Enunciado.pdf
		notas.csv
		Comprimido.zip
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
	Parcial 3
		<Estudiantes>
			Diccionarios_Estudiantes.py
			Contrasenna_Correcta.py
			Diagonal_Triangulares.py
			Altamente_Compuesto.py
			desglose.xlsx
		Comprimido.zip
		Enunciado.pdf
		notas.csv
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
	Parcial 4
		<Estudiantes>
			Crear_Diccionario.py
			Altamente_Abundantes.py
			Determinar_Cercano.py
			Extraer_Matriz.py
			desglose.xlsx
		Enunciado.pdf
		notas.csv
		keywords1.csv
		keywords2.csv
		keywords3.csv
		keywords4.csv
```

Como podemos ver, ambas carpetas tienen una estructura similar donde se destacan los siguientes elementos:
- **< Estudiantes > :** Corresponden a subcarpetas por cada uno de los estudiantes del grupo, nombradas con el número de carnet del mismo. Cabe recalcar que además de cada uno de los archivos *.py* que corresponden a los ejercicios, hay un archivo *.py* general con el nombre del estudiante, el cual contiene la entrega oficial.
- **Enunciado.pdf :** Consiste en un archivo con las intrucciones entregadas por el profesor a los estudiantes para la realización de los ejercicios.
- **notas.csv :** En este archivo encontraremos una tabla en formato *csv* donde se tendrá el nombre completo y carnet de los estudiantes junto a la nota obtenida en el parcial correspondiente.
- **keywords(n).csv :** Este archivo contiene una serie de palabras clave que serán de utilidad para la posterior manipulación y acceso a los datos.
- **Comprimido.zip :** Es un archivo comprimido que contiene los datos originales, sin ser estandarizados. Puede funcionar como un respaldo de la información.