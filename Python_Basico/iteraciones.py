
#range() permite listar toda la secuencia que compone un numero
range(5) #Trae [0,1,2,3,4]

# usar range() en un ciclo FOR
for i in range(5):
	print(i) 
	""" nos da como resultado 0,1,2,3,4 """
for i in range(5):
	print("Hello World")
	""" imprime:
	Hello World
	Hello World
	Hello World
	Hello World
	Hello World """

#Usar Range y FOR para operar un numero

for i in range(30):
	if i % 3 !=0:
		continue
	else:
		print(i**2)

#Usar Range y FOR para operar un numero

for i in range(30):
	if i % 3 ==0:
		print(i)
	elif i == 22:
		break

# Recorrer un String desde el For 
r = 'ferrocarril'
for letter in r:
 	print (letter)