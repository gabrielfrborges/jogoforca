url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
import requests
from random import choice
from string import ascii_letters
p = requests.get(url)
palavras = p.text.lower()
palavras = palavras.split()
sorteada = choice(palavras)
r = True
forca = ['''
    +-----+
    |     |
          |
          |
          |
          |
============''',
         '''
    +-----+
    |     |
    O     |
          |
          |
          |
============''',
         '''
    +-----+
    |     |
    O     |
    |     |
          |
          |
============''',
         '''
    +-----+
    |     |
    O     |
   /|     |
          |
          |
============''',
         '''
    +-----+
    |     |
    O     |
   /|\    |
          |
          |
============''',
         '''
    +-----+
    |     |
    O     |
   /|\    |
   /      |
          |
============''',
         '''
    +-----+
    |     |
    O     |
   /|\    |
   / \    |
          |
============''']

def escolhe():
    return choice(palavras)

def desenha(erradas):
    return print(forca[len(erradas)] )

def jogar_novamente():
    global sorteada
    sorteada = choice(palavras)
    r = input('Deseja jogar novamente(S/n)? ').lower()
    return r in 'sim'

def ganhou(sorteada, certas):
    return set(sorteada) == set(certas)

def fim_de_jogo(sorteada, certas):
    if set(sorteada) == set(certas):
        return print(f'PARABÉNS! Você acertou a palavra "{sorteada}" =D')
    else:
        return print(f'Você não acertou a palavra "{sorteada}" =(')

def chute(letras):
    while True:
        x = input('\nDigite letra:')
        if x in letras:
            print('Letra repitida')
        elif x not in ascii_letters:
            print('Caracter inválido')
        elif len(x) != 1:
            print('Digite somente uma letra')
        else:
            return x

while r:
    certas = erradas = ''
    desenha(erradas)

    while not ganhou(sorteada, certas):
        letra = chute(certas + erradas)
        if letra in sorteada:
            certas += letra
        else:
            erradas += letra
        desenha(erradas)
        for c in sorteada:
            if c in certas:
                print(c, end = ' ')
            else:
                print('_', end = ' ')
        print()
        if len(erradas) == (len(forca)-1):
            break
    fim_de_jogo(sorteada, certas)
    r = jogar_novamente()
