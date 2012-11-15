# Tipos de datos #

## Numeros ##

### Enteros ###

Los números enteros son aquellos números positivos o negativos y el cero, no tienen numeros decimales, en python pueden ser de dos tupos int o long.

La única diferencia es que el tipo long permite almacenar números más grandes. 

El tipo int de Python se implementa a bajo nivel mediante un tipo long de C. El rango de los valores que un entero puede usar en python depende de la plataforma. En plataformas de 32 bits el rango es de -2.147.483.648 a 2.147.483.647 y en plataformas de 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807.
El tipo long de Python permite almacenar números de cualquier precisión y solo estando limitados por la memoria disponible en la máquina.

	entero = 1
	entero_negativo = -1
	cero = 0
	entero_largo = 10L	

### Reales ###

Los números reales son los que tienen decimales. En python se expresan mediante el tipo float. Python implementa el tipo float a bajo nivel mediante una variable de tipo double de C, es decir, utilizando 64 bits.
	
Para representar un número flotante en python se escribe primero la parte entera, seguido de un punto y por último la parte decimal.

	flotante = 1.5
	flotante_exp = 0.5e-3

## Cadenas ##

### Definicion de cadenas ###

Las cadenas son texto encerrado en comillas que pueden ser simples o dobles. En el caso de las comillas dobles podemos poner caracteres especiales como **\n** y estos seran interpretados.

Tambien se pueden usar tres comillas para encerrar el texto, la particularidad de esta forma es que si tenemos texto con multilineas estas se mantienen.

	comillas_dobles = "Esto es una cadena"
	comillas_simpls = 'Esto tambien es una cadena'
	triples_comillas_dobles = """Esto 
								es una
								cadena tambie"""	

Podemos preceder las cadenas con los caracteres **r** o **u** esto es para indicar que tipo de cadena sera si raw, que son cadenas que no escapan los caracteres o unicode que son cadenas unicode.

	cadena_u = u"áéí"
	cadena_r = r"hola\n"


### Metodos de las cadenas ###

Las cadenas al ser tambien objetos tienen una serie de metodos que nos puden ayudar a manipularlas.

**cadena.count(sub[, start[, end]])**

Busca sub en la cadena y devuelve el numero de veces que aparece. Con los parametros ocionales **start** y **end** podemos definir una subcadena a buscar.

**cadena.find(sub[, start[, end]])**

Busca sub en la cadena y devuelve la primera pocición donde se encontro de no ser encontrado devuelve -1.

**cadena.join(lista)**

Concaqueta los elementos de la lista separandolos por la cadena.

**cadena.partition(sep)**

Busca el separador sep en la cadena y devuelve una tupla con la subcadena hasta dicho separador, el separador, y la subcadena del separador hasta el final de la cadena. Si no se encuentra el separador, la tupla contendrá la cadena y dos cadenas vacías.
**cadena.replace(old, new[, count])**

Reemplaza las coincidencias indicadas con el parametro old con lo indicado en el parametro new y devuelve una cadena con los cambios. Con el parametro opcional count podemos especificar el numero maximo de coincidencias a reemplazar.

**cadena.split([sep [,maxsplit]])**

Devuelve una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por  sep. Con el parametro opcional maxsplit podemos indicar cuantos elementos se crearan para la lista.

**cadena.capitalize()**

Devuelve una cadena con la primera letra mayuscula y las demas minusculas.

**cadena.title()**

Devuelve una cadena con la primera letra de cada palabra en mayuscula y las demas en minusculas.

**cadena.upper()**

Devuelve una cadena con todas las letras en mayusculas.

**cadena.lower()**

Devuelve una cadena con todas las letras en minusculas.

**cadena.isalnum()**

Devuelve True si la cadena es alfa numerica de lo contrario devuelve False.

**cadena.isalpha()**

Devuelve True si la cadena son letras de lo contrario devuelve False.

**cadena.isdigit()** 

Devuelve True si la cadena son numeros de lo contrario devuelve False.

**cadena.islower()**

Devuelve True si la cadena esta en minusculas de lo contrario devuelve False.

**cadena.isspace()**

Devuelve True si la cadena es un espacio de lo contrario devuelve False.
 
**cadena.istitle()**

Devuelve True si la cadena esta en formato de titulo de lo contrario devuelve False.

**cadena.isupper()**

Devuelve True si la cadena esta en mayusculas de lo contrario devuelve False.

**cadena.startswith(sub)**

Devuelve True si la cadena inicia con el valor del parametro sub de lo contrario devuelve False.

**cadena.endswith(sub)** 

Devuelve True si la cadena termina con el valor del parametro sub de lo contrario devuelve False.

## Booleanos ##

El tipo de dato booleano solo puede tener dos valores True o False. Realmente este tipo de dato es una extencion del tipo int.

	booleano = True
	booleano = False

## Operadores ##

**Operador de suma:** 

		variable = 2 + 3

**Operador de resta:**

		variable = 3 - 2

**Operador de negación:**

		variable = -3

**Operador de multiplicación:**

		variable = 3 * 2

**Operador de exponente:**

		variable = 2**2

**Operador de divición:**

		variable = 5.0 / 2.0

**Operador de divición entera:**

		variable = 5 // 2

**Operador de módulo:**  

		variable = 5 % 2

**Operador igual a:**  

		variable = 5 == 2

**Operador diferente a:**  

		variable = 5 != 2

**Operador de mayor a :**  

		variable = 5 > 2

**Operador de menor a:**  

		variable = 5 < 2

**Operador de mayor o igual a:**  

		variable = 5 >= 2

**Operador de menor o igual a:**  

		variable = 5 <= 2

**Operador and:**  

		variable = (3 != 2) and (2 == 2)

**Operador or:**  

		variable = (3 != 2) or (2 == 2)

**Operador not:**  

		variable = 1 not 5


## Tipado ##

Con el comando type podemos saber el tipo de dato o la clase de la cual se deriva un objeto, por ejemplo:

	type("Cadena")
	type(1)
	type(True)
	type(1.5)
	type(5j)
	type(True)
	type(u"áéíñoñu")

Tambien podemos convertir un tipo de dato en otro:

	entero = "12345"
	type(entero)
	type(int(entero))
