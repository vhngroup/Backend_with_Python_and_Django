#cifrar mensaje con 4 diccionarios
import random

lista = ' ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz.,?!0123456789;:_()@$#¡¿'
lista_0 = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y',
           'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y',
           'z','.',',','?','!','0','1','2','3','4','5','6','7','8','9',';',':','_','(',')','@','$','#','!','¿']
lista_1 = ['+','?', 'B', 'z', 'm', 'K', 'e', 's', '1', 'O', 'y', '_', '3', 'M', '6', 'g', 'N', 'H', 'd', 'J', 'h',
           '¡', 'r', 'E', '2', 'x', 'i', 'G', 'q', 'f', 'F', 'D', 'v', 'c', ':', 'Y', 'L', 't', '7', 'ñ', '0', 'w',
           'l', 'X', 'A', '5', 'n', '#', 'V', '¿', '9', '.', 'k', 'b', 'Ñ', ')', 'C', '$', 'Q', ',', '8', 'j', 'I',
           'T', '@', 'W', 'Z', '4', 'o', 'a', 'U', 'u', 'p', 'S', 'P', '!', 'R', '(', ';']
lista_2 = ['-','l', ':', ',', '#', 'a', 'g', 'y', ')', 'Q', 'L', 'N', 'E', '2', '¡', 'c', '7', 'W', 'h', 'D', 'U', '!',
           'u', 'P', '3', 'H', 'Ñ', '9', 'w', '8', 'i', 'F', ';', 'ñ', 'V', 'x', 'b', 'n', 'T', 'S', 'q', '@', 'j',
           '5', 'C', '¿', 'Y', 'A', 'r', 'M', 'O', '4', 'd', 's', '(', 'R', '1', '_', 'k', 'z', 'e', 'Z', 'f',
           'J', 't', 'v', '6', '$', '0', 'o', '.', 'I', 'p', 'G', 'X', '?', 'B', 'K', 'm']
lista_3 = ['*','¿', '?', 'E', 'I', 'l', '_', 'V', 'i', '!', 'g', 't', 'r', 'L', 'Y', 'O', 'z', 'x', 'm', 'T', 'D', 'X',
           'h', 'k', '@', ';', '8', 'H', 'S', 'Q', 'v', 'u', 'Ñ', '4', ':', 'F', '5', 'ñ', 'K', '(', 'U', 'C',
           '9', 'e', 'B', 'o', 'P', 'p', 'w', '1', '$', '0', 'Z', '¡', 'G', 'c', 'R', '2', 'a', 'N', 'A', 'b', 'J',
           '6', 'M', 'f', 'W', '7', '3', 'y', 'd', '.', ')', 'n', '#', 'j', ',', 'q', 's']
lista_4 = ['/','j', 'n', 'N', 'A', 'h', 'X', '¡', '6', 'v', '3', 'e', 'Y', '0', 'Ñ', '8', '#', 'p', '¿', 'x', 'ñ', 'm',
           'r', 'l', 's', ')', 'C', 'W', '5', 'H', '7', 'E', 'c', 'M', 'g', 'Z', '!', '.', 'u', 'G', '1', '?',
           'B', 'b', 'K', 'd', 'o', 'D', '@', 't', 'P', 'V', 'I', 'O', ';', 'i', 'F', '4', 'z', 'w', 'k', ':', 'Q',
           '(', 'q', 'J', 'a', 'U', 'y', 'f', '2', 'L', 'S', ',', 'R', 'T', '9', '_', '$']

aux =[1,2,3,4]

diccionario_1 = dict(zip(lista, lista_1))
diccionario_2 = dict(zip(lista, lista_2))
diccionario_3 = dict(zip(lista, lista_3))
diccionario_4 = dict(zip(lista, lista_4))

def cypher(message):
    words = message.split(' ')
    cypher_message = []
    for word in words:
        cypher_word_aux = ''
        random.shuffle(aux, random.random)
        if aux[0] == 1:
            cypher_word = cypher_word_aux+'+'
            for letter in word:
                cypher_word += diccionario_1[letter]

            cypher_message.append(cypher_word)
        elif aux[0] == 2:
            cypher_word = cypher_word_aux + '-'
            for letter in word:
                cypher_word += diccionario_2[letter]

            cypher_message.append(cypher_word)
        elif aux[0] == 3:
            cypher_word = cypher_word_aux + '*'
            for letter in word:
                cypher_word += diccionario_3[letter]

            cypher_message.append(cypher_word)
        elif aux[0] == 4:
            cypher_word = cypher_word_aux + '/'
            for letter in word:
                cypher_word += diccionario_4[letter]

            cypher_message.append(cypher_word)

    return' '.join(cypher_message)

def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''
        split_word = list(word[0])
        if split_word[0] == '+':
            for letter in word:

                for key, value in diccionario_1.items():
                    if value == letter:
                        decipher_word += key

            decipher_message.append(decipher_word)
        elif split_word[0] == '-':
            for letter in word:

                for key, value in diccionario_2.items():
                    if value == letter:
                        decipher_word += key

            decipher_message.append(decipher_word)
        elif split_word[0] == '*':
            for letter in word:

                for key, value in diccionario_3.items():
                    if value == letter:
                        decipher_word += key

            decipher_message.append(decipher_word)
        elif split_word[0] == '/':
            for letter in word:

                for key, value in diccionario_4.items():
                    if value == letter:
                        decipher_word += key

            decipher_message.append(decipher_word)

    return' '.join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)

        elif command == 's':
            break

        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
