url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
import requests
from random import choice
from string import ascii_letters ##punctuation
p = requests.get(url)
palavras = p.text.lower()
palavras = palavras.split()
sorteada = choice(palavras)
r = True
forca = [''' ''', ''' o ''', ''' o_ ''', ''' _o_ ''', '''_o_/''', '''\_o_/''']

def escolhe():
    return choice(palavras)

def desenha(erradas):
    return print( forca[len(erradas)] )

def jogar_novamente():
    r = 's'
    r = input('Deseja jogar novamente(S/n)? ')
    return 's' in r.lower()

def ganhou(sorteada, certas):
    return set(sorteada) == set(certas)

def chute(letras):
    while True:
        x = input('Digite letra:')
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
    
    while not ganhou(sorteada, certas):
        print(sorteada)
        letra = chute(certas + erradas)
        if letra in sorteada:
            certas += letra
        else:
            erradas += letra    
        for c in sorteada:
            if c in certas:
                print(c, end = ' ')
            else:
                print('_', end = ' ')
        desenha(erradas)
        
     r = jogar_novamente()

#if jogar_novamente(r): 
