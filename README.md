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