## Clases ##
### Definición de clases ###

	class NombreClase:

		atributo = 'valor'
		
		def metodo(self):
			return self.atributo
				

### Herencia ###

	class Animal:

		patas = 4

		def caminar(self):
			return self.patas

	class Ave(Animal):

			patas = 2
			alas = 2

			def volar(self)
				return self.alas						

### Encapsulamiento ###

	class NombreClase:

		atributo = 'valor'
		__privado = True

		def __init__(self, parm1):
				print parm1

		def __local(self):
			return self.__privado

		def metodo(self):
			return self.atributo

	obj = NombreClase(parm1)


