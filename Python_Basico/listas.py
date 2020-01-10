#promedio de temperaturas usando listas

def average_temps(temps):
	sum_of_temps=0

	for temp in temps:
		sum_of_temps += float(temp)
#float: cambia el formato de numero a decimales
	return sum_of_temps / len(temps)
#len: determina la cantidad de elementos de una secuencia 	

if __name__ == '__main__':

	temps=[21,24,24,22,20,23,24]

	average = average_temps(temps)

	print('La temperatura promedio es: {}'.format(average)  )