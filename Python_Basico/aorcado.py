#-*-coding: utf-8 -*-
import random

IMAGES= ['''

+---+
|	|
	|
	|
	|
	|
	|
	|
	_______________
	_______________ ''',''' '''
]

WORDS = [ 'lavadora', 
		  'secadora',
		  'sofa',
		  'gobierno'
]

def random_word():
	idx = random.randint(0, len(WORDS) -1)
	return WORDS[idx]

def display_board(hidden__word, tries):
	print(IMAGES[tries])
	print('')
	print(hidden__word)
	print('___*___*___*___*___*___*___*___')

def run(): 
	word = random_word()
	hidden__word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden__word, tries)
		current_letter= str(input('Escoje una letra:'))
 

if __name__ == '__main__':
 	print(' BIENVENDOS AL JUEGO DE AORCADOS')
 	run()