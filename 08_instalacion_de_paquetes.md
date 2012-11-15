# Instalacion de paquetes #


## Desde el codigo fuente ## 

Los paquetes preparados para ser distribuidos en python tienen un archivo **setup.py** que es el que nos sirve para instalarlo en el sistema.

	python setup.py install

Esto lo debemos hacer dentro del directorio del modulo que descargamos y descomprimimos.

## Pypi ##

Pypi <http://pypi.python.org/pypi> es la abreviacion de Python packages index, que es un repositorio de paquetes mantenido por la comunidad que podemos descargar para instalar en nuestra computadora.

## Easy install ##

Python tiene el comando **easy_install** que nos sirve para instalar paquetes desde internet usando el repositorio Pypi.

	easy_install nombre_paquete

## Pip ##

Pip es un comando que se instala aparte y nos permite buscar dentro de pypi e instalarlos. Es una version mas completa y avanzada de easy_install.

	pip search paquete
	pip install paquete

Tambien podemos sacar una lista de los paquetes instalados con pip para ser distribuida con nuestra aplicacion y tener una forma facil de instalar las dependencias.

	pip freeze
	pip install -r requiriments.txt



