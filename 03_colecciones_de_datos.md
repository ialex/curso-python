# Colecciones de datos #

## Listas ##


### Definicion de listas ###

Las listas en python son el equivalente de los arrays de otros lenguajes. Son listas de elementos ordenados y los elementos pueden ser cualquier tipo de dato.

Las listas se definen con los corchetes **[]** y dentro de los corchetes van los elementos separados por comas, por ejemplo:

	mi_lista = [variable, 1, 'cadena', [False, otra_variable]] 

### Indices ###

Podemos acceder a un elemento usando los indices de la lista, que van de 0 a n, donde n es la logintud de la lista menos uno.

	print mi_lista[2]

Podemos usar numeros negativos en los indices para empezar a contar desde el final de la lista al inicio.

	print mi_lista[-2]

Haciendo referencia a un elemento de la lista mediante su indice tambien podemos cambiar su valor.

	mi_lista[-2] = 100

### Slicing ###

En python hay algo llamado slicing para las listas, que consta en seleccionar rangos de indices de las listas para obtener una sub cadena.

	mi_lista = ['a', 1, True, 'lista', 100, False]
	mi_lista[2:4]
	mi_lista[:3]
	mi_lista[2:-2]

### Metodos de las listas ###

**lista.append(object)**

Añade un objeto al final de la lista.
**lista.count(value)**

Devuelve el número de veces que se encontró value en la lista.
**lista.extend(otra_lista)**

Añade los elementos de la otra_lista a la lista.

**lista.index(value[, start[, stop]])**

Devuelve la posición en la que se encontró la primera ocurrencia de value. Si se especifican, start y stop definen las posiciones de inicio y fin de una sublista en la que buscar.
**lista.insert(index, object)**

Inserta el objeto object en la posición index.
**lista.pop([index])**

Devuelve el valor en la posición index y lo elimina de la lista. Si no se especifica la posición, se utiliza el último elemento de la lista.

**lista.remove(value)**

Eliminar la primera ocurrencia de value en la lista.
**lista.reverse()**

Invierte la lista. Esta función trabaja sobre la propia lista desde la que se invoca el método, no sobre una copia.
**lista.sort()**

Ordena la lista. 

## Tuplas ##

Las tuplas son listas inmutables, esto quiere decir que una vez definidas no pueden modificarse, por lo mismo, son mas ligeras que las listas.

El constrcutor de las tuplas es la coma **,** pero por convencion se usan los parentesis **()**.

	variable = (1,2,)

Las tuplas se manejan igual que las listas pero con la unica diferencia que no podemos usar las funciones y metodos para modificarlas.

## Diccionarios ##

### Definicion de diccionarios ###

Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un valor.

Se definen con los corchetes **{}** cada elemento se separa por comas y cada elemento esta compuesto de una clave y valor separadas por dos puntos **:**.

	diccionario = {'clave1':1, 'clave2':'b'}

La diferencia principal entre los diccionarios y las listas o las tuplas es que a los valores almacenados en un diccionario se les accede por la clave y no por el indice ya que no tienen un orden.

	diccionario['clave1']

### Metodos de los diccionarios ###

**diccionario.get(k[, d])**

Busca el valor de la clave k en el diccionario. Es equivalente a utilizar diccionario[k] pero al utilizar este método podemos indicar un valor a devolver por defecto si no se encuentra la clave, mientras que con la sintaxis diccionario[k], de no existir la clave se lanzaría una excepción.

**diccionario.has_key(k)**

Comprueba si el diccionario tiene la clave k. Es equivalente a la sintaxis k in D.
**diccionario.items()**

Devuelve una lista de tuplas con pares clave-valor.

**diccionario.keys()**

Devuelve una lista de las claves del diccionario.
**diccionario.pop(k[, d])**

Borra la clave k del diccionario y devuelve su valor. Si no se encuentra dicha clave se devuelve d si se especificó el parámetro o bien se lanza una excepción.
**diccionario.values()**

Devuelve una lista de los valores del diccionario.
