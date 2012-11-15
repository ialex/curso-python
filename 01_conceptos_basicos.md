# Conceptos basicos #

## Variables ##

### Palabras reservadas ###

En Python cuando necesitamos nombrar una variable, una función o cualquier otro objeto tenemos que cumplir con ciertas reglas para python no produzca un error. 

Una de las primeras cosas que debemos evitar es el uso de palabras reservadas, funciones internas de python o nombre objetos internos de python.

**Palabras reservadas**

	and	as	assert	break	class	continue
	def	del	elif	else	except	exec
	finally	for	from	 global	if 	import
	in	is	lambda	nonlocal	not	or
	pass	raise	return 	try	while	with
	yield	True	False	None	

**Funciones internas**

	abs()	divmod() input() 	open()	 staticmethod()
	all()	enumerate()	int()	ord()	str()
	any()	eval()	isinstance() 	pow()	sum()
	basestring()	execfile() 	issubclass()	 print()	 super()
	bin()	file() iter()	 property()	 tuple()
	bool()	filter()	 len()	 range()	 type()
	bytearray()	float()	list() 	raw_input()	unichr()
	callable()	format()	 locals()	reduce() 	unicode()
	chr()	frozenset()	long()	 reload()	 vars()
	classmethod()	getattr()	map()	repr() 	xrange()
	cmp()	globals()	max()	reversed()	 zip()
	compile()	hasattr()	memoryview()	 round()	 __import__()
	complex()	hash() 	min()	set()	apply()
	delattr()	help() 	next()	 setattr() 	buffer()
	dict()	hex()	object()	 slice() 	coerce()
	dir()	id()	oct()	sorted()	 intern()

### Nombres para variables ###

Python tiene unas reglas basicas para saber como nombrar a las variables:

- Puden tener letras, numeros y el caracter underscore **_**
- Solo pueden iniciar con letras o underscore
- Se recomienda usar el underscore para separar palabras, el camelcase solo se recomienda para las clases:

		mi_variable_1 = 10

- Python sabe diferenciar las minusculas de las mayusculas por lo tanto **mi_variable** es diferente a **Mi_variable**.

### Definición de variables ###

Para definir una variable se pone el nombre, el operador de asignación **=** y luego su valor.

	nomre_variable = valor

## Salida y entrada standar ##

### Salida ###

Para poder imprimir en la terminal con python se usa la sentencia **print**, con esta sentencia podemos imprimir el valor de una variable o cualquier otro objeto.

	mi_variable = "Contenido"
	print mi_variable
	print "Contenido"
	print 1
	print 2.3
	print 'Sustitucion en cadena %s' % ('texto')
	print mi_variable, 'otra cadena', 90
	print "Linea uno \nLinea dos"
	print 'Linea uno \nLinea dos'

### Entrada ###

Para poder leer datos desde la terminal tenemos que usar una de estas dos funciones **input** que el contenido es analisado y puesto en una variable con el tipo de dato segun el contenido y **raw_input** que toma la entrada y es almacenada como una cadena en la variable sin importar el tipo de contenido que tenga.

	variable = input('->')
	variable = raw_input('->')

## Comentarios ##

Los comentarios en python se ponen con el simbolo de **#** pueden ir una linea antes o despues de una sentencia o al final de esta.

	# Esto es un comentario
	# Esto es otro comentario 
	print "Demostracion de comentarios" # Esto es un comentario

## Lectura y escritura de archivos ##

Los archivos en python tambien son objetos. Para abrir un archivo usamos la función **open**.

Una vez abierto y asignado a una variable podemos acceder al contenido o escribir en el usando los metodos del objeto *file*.

### Escribir archivos ###

Para poder escribir archivos tenemos que abrirlos con el flag **w** que significa escritura o el flag **a** que es para añadir al final del archivo una nueva linea. Si el archivo no existe al abrirlo con la funcion open este se creara.

	mi_archivo = open("test.txt", "w")
	mi_archivo.write("# Nuevo archivo #\n")
	mi_archivo.write("---------------------------------\n")
	mi_archivo.write("Otra linea\n")
	mi_archivo.close()

	mi_archivo = open("test.txt", "a")
	mi_archivo.write("Una linea mas\n")
	mi_archivo.close()

### Leer archivos ###

Para abrir un archivo en modo de lectura usamos el flag **r**.

Con el metodo **read** del objeto file podemos leer todo el contenido de un archivo abierti previamente.

	mi_archivo = open("test.txt", "r")
	contenido = mi_archivo.read()
	mi_archivo()
	print contenido

### Leer archivos linea por linea ###

El metodo **readline** nos va mostrando una linea nueva cada vez que lo ejecutamos.

	mi_archivo = open("test.txt", "r")
	while True:                            
  	linea = mi_archivo.readline()   
    if len(linea) == 0: 
        break    
    print(linea, end="")

	mi_archivo.close()

### Leer archivos como si fuese una lista ###

El metodo **readlines** nos devuelve una lista donde cada elemento de la lista es una linea.

	mi_archivo = open("test.txt", "r")
	lineas = mi_archivo.readlines()
	mi_archivo.close()
	print lineas

### Archivos binarios ###

Tambien podemos leer y escribir archivos binarios en python con los flags **rb** y **wb** respectivamente.

Al parametro read le podemos pasar la cantidad de bytes que queremos leer.

	r = open("ejemplo.zip", "rb")
	w = open("output.zip", "wb")

	while True:
    	buf = r.read(1024)
    	if len(buf) == 0:
         	break
    	w.write(buf)

	r.close()
	w.close()

## Modulos y paquetes ##
### Modulos ###

En python para poder mantener el codigo ordenado y legible podemos agruparlo en modulos, de esta forma agrupamos elementos de forma logica en modulos. La representación fisica de estos modulos son archivos python.

Por ejemplo cremos un archivo llamado **modulo.py**:

	print "Cargando modulo"
	variable = 1
	def funcion():
		print "Esto es una funcion"

Si queremos usar ese modulo dentro de nuestro programa demos importar el archivo como modulo con la sentencia **import**:

	import modulo

Al importar el modulo podemos acceder a las funciones, clases y demas obejtos dentro del archivo **modulo.py** de la siguiente manera:

	print modulo.variable

Al usar la sentencia import se crea en nuestro programa un *namespace* con el nombre del modulo importado y dentro de el tenemos todo lo contenido dentro del modulo.

Al importar un modulo tambien se ejecuta todo el codigo que hay en este en el ejemplo anterior al hacer el import el print se ejecuta imprimiendo una cadena.

Tambien podemos optar por crear una referencia de un objeto que se encuentre dentro del modulo en nuestro programa actual con la sentencia **from .. import**:

	from modulo import variable
	print variable

la sentencia import tambien nos permite importar mas de un modulo a la vez separandolos por comas:

	import sys, os, modulo

Si un modulo no existe pytno lanzara una excepción del tipo *ImportError*.

Los modulos tambien son objetos de tipo module, esto quiere decir que tiene una serie de atributos y metodos algunos como el atributo __name__ nos sirve para saber el nombre del modulo importado, si el modulo no es importado y estamos en el namespace del programa principal el valor de __name__ sera __main__. Saber esto nos puede servir para poder ejecutar codigo siempre y cuando el modulo se ejecute directamente y no se importe desde otro programa.


### Paquetes ###

Ya tenemos los modulos que no sirven para organizar codigo y para organizar modulos tenemos los paquetes, que son simples directorios que dentro contiene uno o varios modulos mas un archivo llamado **__init__.py** que nos sirve para poder indicarle a python que ese directorio es un paquete y contiene modulos y podemos importarlo.

De la misma forma que los modulos tambien los paquetes y subpaquetes tienen su namespaces.

	import paquete.subpaquete.modulo
	print paquete.subpaquete.modulo.variable

En el ejemplo anterior tenemos un directorio llamado paquete que contiene un archivo __init__.py y un subdirectorio llamado subpaquete que tambien contiene un archivo __init__.py y un archivo llamado modulo.py.


## Libreria estandar ##

Por default python viene con una gran cantidad de paquetes y modulos que no son de utilidad, a esto se le conoce como la libreria estandar <http://docs.python.org/2.7/library/index.html> donde se listan todos estos modulos con las funciones y clases que contienen y nos pueden servir para desarrollar nuestros programas.


