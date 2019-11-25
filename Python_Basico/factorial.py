# -*- coding: utf-8 -*-

def factorial(number):
	if number == 0:
		return 1

	return number * factorial (number - 1)

if __name__ == '__main__':
	print("CALCULA EL FACTORIAL DE UN NUMERO")
	number = int(input("Indica un numero: "))
	
	factorial(number)

	result = factorial(number)

print('El factoria es {}'.format(result))