# Control de flujo #

## Condicionales ##

### if ###
	variable = 1
	if variable == 1:
		print 'Es correcto'

### if - else ###

	if variable == 1:
		print 'Es correcto'
	else:
		print 'Es incorrecto'

### if - elif - else ###

	if variable == 1:
		print 'Es correcto'
	elif variable == 2:
		print 'Tambien es correcto'
	else:
		print 'Es incorrecto'

### Operador ternario ###

	'es correcto' if variable == 1 else 'no es correcto'

## Iteraciones ##

### while ###

	count = 0
	while count < 100:
		count = count + 1
		print count

### for in ###

	for count in range(0,100):
		print count

### break ###

	count = 0
	while count < 100:
		if count == 50:
			break
		count = count + 1
		print count


## Excepciones ##

### Definicion de excepciones ###
	a = 1
	b = 0
	try:
		variable = a / c
	except:
		print "Ocurrio un error"

### Tipos de excepciones ###

	try:
		variable = a / b
	except ZeroDivisionError:
		print "No puedes dividir por cero"
	finally:
		print "Siempre se ejecuta"

### Excepciones personalizadas ###

	class MyError(Exception):
    	def __init__(self, valor):
        	self.valor = valor
    	def __str__(self):
        	return “Error “ + str(self.valor)
	try:
    	if resultado > 20:
        	raise MyError(33)
	except MyError, e:
    	print e

