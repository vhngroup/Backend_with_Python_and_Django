# -*- coding: utf-8 -*-

"""Como asignar o cambiar el contenido de una variable string"""
r='hola'
m= 'l' + r[1:]
print("El contenido de M es {} y cambio de R que es {}".format(m, r))

"""Como recorrer un string y conocer su longitud."""

my_string = 'platzi'
my_string [len(my_string)-1] # Se debe restar un valor, para recorrer completo el string.

#Manejo de strings en Python
name = "platzi"

len(name) >>> 6 
# devuelve el tamaño del string
name.upper() >>> "PLATZI" 
# convierte a mayusculas
name.lower() >>> "platzi"
 # convierte a minusculas
name.find("a") >>> 2
 # devuelve la posicion
name.join(['hola ',' vamos ', ' a aprender']) >>> "hola platzi vamos platzi a aprender"
#ingresa dentro de [] caracteres que seran insertados entre cada string

name2 = "nunca pares de aprender"
name2.split() >>> ['nunca', 'pares', 'de', 'aprender']
#devuelve en un array el string separada por grupos```