# mi_diccionario = {} 									Como se inicializa un diccionario
# mi_diccionario['Primer_Elemento'] = 'Hola' 			Como se establece las variables y contenidos
# mi_diccionario['Segundo_Elemento'] = 'Adios' 			Como se establece las variables y contenidos

# mi_diccionario['Primer_Elemento']						Como se trae el contenido de un primer elemento


#Programa para calcular el promedio de las calificaciones usando python, para el ejercicio se llaman indices "key "y se llaman valores de los indices "value".
calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_Datos'] = 10

for key in calificaciones:
	print(key)

for value in calificaciones.values():
	print(value)

for key, value in calificaciones.items():
	print ('Llaves¨: {}, Valor: {}'.format(key, value) )

suma_de_calificaciones = 0

for calificacion in calificaciones.values():
	suma_de_calificaciones += calificacion

	promedio = suma_de_calificaciones / len(calificaciones.values())

print('Nuestro promedio es: {}'.format(promedio))