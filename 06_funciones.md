# Funciones #

## Funciones internas ## 

Dentro de python ya vienen varias funciones que se cargan al iniciar el interprete estas son conocidas como **builtin functions** <http://docs.python.org/2/library/functions.html>.

Algunos ejemplos de funciones son:

**type()**

Que nos sirve para saber que tipo de dato tiene un objeto entre otras cosas.

**range()**

Que nos devuelve una lista con un rango de numeros definido en los parametros.

**isinstance()**

Devuelve True o False dependiendo si un objeto es instancia de una clase definida en los parametros.

## Funciones ##

### Definicion de funciones ###

Las funciones en python se definen con la palabra reservada **def**, se usan las mismas reglas para nombrar las variables.

Dentro de los parentesis podemos especificar los parametros que usaremos dentro de nuestra funcion.

	def nombre(parametro1, parametro2="valor"):
		""" Cadena de documentacion """
		return valor

Para ejecutar la  funcion la llamamos por su nombre y en el parentesis ponemos los parametros que deseamos pasarle.

	nombre(1)
	nombre(parametro2="nuevo_valor")

Si no se especifica un retorno devolvera None pero siempre se ejecutara el codigo de la funcion.

### Parametros especiales ###

Existen dos parametros que nos pueden ayudar si tenemos que definir funciones que acepten demasiados, los parametros precedidos con **\*** y **\*\***, cuando se usa un solo asterisco dentro de nuestra funcion los parametros pasados a la hora de llamarala sin especificar un valor se almacenaran en una lista en el caso de usar doble asterisco se almacenara en un diccionario los parametros con valor.

	def nombre(*args, **kwargs):
		print args
		print kwarks

	nombre(1,2,3,4,clave1='a', clave2='b')

