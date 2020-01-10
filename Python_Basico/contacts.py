#Programa para ordenar y operar una libreta de contactos#

class Contact:
	"""docstring for ContacBook"""
	def __init__(self, name, phone, email):
		self._name = name
		self._phone = phone
		self._email = email

class ContactBook:
	"""docstring for ContacBook:"""
	def __init__(self):
		self.contacts = []

	def add(self, name, phone, email):
			print('name: {},phone: {}, Email: {}'.format(name, phone, email))
		

def run	():

	contact_book =ContactBook()
	while True:
		command = str(input('''
			Que deseas hacer?
			[a]ñadir Contacto
			[ac]tualizar Contacto
			[b]uscar Contact
			[e]liminar Contacto
			[l]istar Contacto
			[s]alir
			'''))
		if command == 'a':
			name = str(input('Escribe el nombre del contacto'))
			phone = str(input('Ingrese telefono del contacto'))
			email = str(input('Ingrese el email del contacto'))

			contact_book.add(name, phone, email)

		elif command == 'ac':
			print('Actualizar Contacto')
		elif command == 'b':
			print('Buscar Contacto')
		elif command == 'e':
			print('Eliminar contacto')
		elif command == 'l':
			print('Listar Contactos') 
		elif command == 's':
			break
		else:
			print('Comando no encontrado')

if __name__ == '__main__':
		run()	
	