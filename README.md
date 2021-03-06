# csv-psql
Script en python que convierte una tabla csv en una tabla para una base de datos postgresql

Se deberán copiar los ficheros *csv-psql.py* y *librería.py* en una carpeta incluida dentro de la variable $PATH del entorno del usuario como por ejemplo *$HOME/bin*.

## Requisitos
Este script está escrito en python version 3. Necesita tener instalada la librería *python3-pygresql*.

## Funcionamiento
En la primera fila del fichero csv están los nombres de los campos de la tabla con el formato siguiente:

	nombreCampo1#tipo de dato campo 1,nombreCampo2#tipo de dato campo 2,...,nombreCampon#tipo de campo n

Por ejemplo

	id#integer,Nombre#varchar(50),Apellidos#varchar(50),Fecha de nacimiento#date
El resto de las lineas del fichero csv tendran los datos de la tabla a crear. Deberán tener todas las lineas el mismo número de campos que el título.
	
A la hora de invocar el script se deberá indicar en qué base de datos se desea añadir la tabla.
La tabla que nos crea, tendrá el mismo nombre que el del fichero que vamos a leer (sin la extensión csv). 
Argumentos del script:

	-h : ayuda
	-b --basedatos <nombre base de datos> El nombre de la base de datos existente en el sistema y que tenemos que tener derechos de acceso.
	-m --host <nombre host> El nombre del equipo donde está la base de datos (por defecto *localhost*)
	-p --puerto <numero> El puerto donde está la base de datos (por defecto 5432).
	-u --user <usuario> Nombre de usuario de la base de datos (si tenemos un fichero *.pgpass* se puede omitir)
	-c --password <contraseña> Contraseña del usuario de postgresql (si tenemos un fichero *.pgpass* se puede omitir).
	-d Para que el script borre la tabla si esta ya existe
	-k Para que el script añada los registros a la tabla si ya existe


