# Introducción #

## Un poco de historia ##

Python es un lenguaje de programación creado a finales de los 80 por Guido van Rossum y fue publicado a inicios de los 90. Fue creado para ser un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.

La idea del nombre proviene de los cómicos ingleses “Monty Python” dado que su autor era aficionado a estos.

## Caracteristicas ##

### Lenguaje de alto nivel ###

Python es el perfecto ejemplo de un lenguaje de programación de alto nivel, ya que desarrollar en python es mas rapido, facil y portable.

La diferencia entre un leguaje de alto nivel y uno de bajo nivel es basicamente que los de bajo nivel estan escritos en lenguaje maquina y se compilan para una arquitectura en especial generando binarios que son rapidos en tiempos de ejecución, tambien esta que los de bajo nivel tienen una sintaxys mas compleja y escribir programas es mas tardado.

### Multiparadigma ###

Python es un lenguaje de programación multiparadigma, esto quiere decir que los programadores pueden trabajar de mas de una forma con el:

- Programacion orientada a objetos
- Programación funcional
- Programacion imperativa 

### Interpretado ###

A diferencia de los lenguajes como C o C++, que son lenguajes compilados, python es un lenguaje interpretado. Esto quiere decir que necesita un interprete especifico para cada plataforma para poder ejecutar el mismo programa en todas.

Esto hace que python sea flexible y portable, sacrificando un poco de velocidad en la ejecución de los programas.

Tambien comparte caracteristicas con lenguajes como java que genera archivos bytecode para poder tener una version "compilada" del script desde la primera vez que se ejecuta y optimizar para esa maquina en particula de esta manera poder tener una mayor velocidad en tiempo de ejecución.

### Tipado dinamico ###

En python no es necesario declarar el tipo de dato que contendra una variable, esto quiere decir que el tipo de dato de la variable cambia segun el contenido de esta. Esta caracteristica hace que python tenga un tipado dinamico. 

### Fuertemente tipado ###

En python no se puede tratar a una variable de un tipo como si se fuese de otro. Por ejemplo una variable que contiene un valor de cadena no puede ser tratada como si fuese un numero.

Para poder tratar a una variable de un tipo como si fuese otro distinto hay que convertirlo de maneja explicita.

Por ejemplo si tenemos una cadena con numeros y queremos usarla para una operacion matematica tenemos que convertir esa cadena a un tipo numerico.

Esto hace que python sea un lenguaje fuerte mente tipado.

### Multiplataforma ###

Python por ser un lenguaje interpretado es tambien un lenguaje multiplataforma esto quiere decir que el mismo progama sin modificarse puede correr en cualquier plataforma que tenga un interprete python.


### Todo es un objeto ###

En python todo es un objeto, las variables, las funciones, las cadenas, las listas, etc, todo tiene una serie de metodos y atributos que podemos usar para manipular estos objetos.

### Diseñado para facil lectura ###

Un programador pasa mas tiempo leyendo codigo que escribiendolo, esta es la razon por la que python fue creado con una sintaxys sencilla y limpia. 

La sintaxys de python es muy parecida al idioma ingles esto lo hace que sea facil de entender y comprender.

Una caracteristica importante en su sintaxys es que la identancion cuenta, python nos obliga a identar nuestro codigo para separar los bloques, esto hace que el lenguaje sea mas compacto y cree una mejor experiencia al leer el codigo. 

### Extensible ###

Python puede ser extendido creando librerias en C o C++, esto es util cuando queremos escribir codigo que se ejecute con mucha rapides y usarlo dentro de python. 

## Ramas ##

Python maneja dos ramas actualmente la 2.7.X y la 3.3.X, entre ambas ramas existen cambios significativos en la sintaxys del lenguaje. Pero muchas de las caracteristicas importantes de python 3.3.X tambien estan disponibles en la 2.7.X

En este curso se manejara la la 2.7.X ya que es la mas usada para trabajar y la que tiene una mayor cantidad de modulos de terceros funcionando al 100%.

## Zen de python ##

Tim Peters resume con unos principios la filosofia de python, esto es conocido como el Zen de python.

- Bello es mejor que feo.
- Explícito es mejor que implícito.
- Simple es mejor que complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Escaso es mejor que denso.
- La legibilidad cuenta.
- Los casos especiales no son tan especiales como para romper las reglas.
- Aunque lo práctico vence a lo puro.
- Los errores nunca deben ocurrir silenciosamente.
- A menos que hayan sido silenciados explícitamente.
- Ante la ambigüedad, rehuye la tentación de adivinar.
- Debería haber una-- y preferiblemente solamente una --manera obvia de hacerlo.
- Aunque esa manera puede no ser obvia de inmediato a menos que seas Holandés.
- Ahora es mejor que nunca.
- Aunque nunca es muchas veces mejor que *ahorita*.
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, puede que sea una buena idea.
- Los espacios de nombres son una tremenda gran idea -- ¡hay que hacer más de esos!

## Instalación ##

Desde <http://www.python.org/download/> se pueden descargar los instalador y el condigo fuente para instalar python en distintas plataformas.

### Desde las fuentes ###

Podemos instalar python practicamente en cualquier plataforma si descargamos las fuentes y las compilamos para la plataforma que estemos usando.

<http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2>

### Linux ###

Desde linux podemos usar las fuentes y compilar el interprete o usar el gestor de paquetes de nuestra distribución favorita para instalarlo. Por ejemplo en debian/ubuntu seria de la siguiente forma.

	apt-get install python

### OSX ###

OSX ya viene con la version de 2.7 de python instalada, pero podemos instalarlo con las fuentes o usando el instalador para OSX <http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg>

### Windows ###

Para windows tenemos un instalador <http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi> que nos ayuda a instalar python de forma sencilla muy similar al instalador de OSX.

## La consola interactiva ##

Al ejecutar el comando *python* en una terminal nos ejecutara la consola interactiva. En esta consola podemos poner codigo python y se ejecutara de forma automatica.

Podemos probar haciendo una suma:

	2 + 2

O imprimiendo una cadena:

	print "Hola mundo"

## Ejecutando programas en python ##

Por convencion se los programas en python tiene la extencion *.py*. Para poder ejecutar un programa en python tenemos que ejcutar el interprete y como parmetro le pasamos el archivo .py que queremos ejecutar:

	python mi_programa.py

Tambien podemos darle permisos de ejecución a nuestro programa y en la primera linea añadir un **shebang**:

	#!/usr/bin/env python
	print "Hola mundo"

Lo ejecutamos como si se tratase de un aplicación normal desde la consola, no sin antes darle permisos de ejecución.

	chmod +x mi_programa.py
	./mi_programa.py