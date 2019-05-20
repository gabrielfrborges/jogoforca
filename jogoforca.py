url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
import requests
from random import choice
p = requests.get(url)
palavras = p.text.lower()
palavras = palavras.split()
sorteada = choice(palavras)

def escolhe():
    from random import choice
    return choice(palavras)

def desenha(erradas):
    return print( forca[len(erradas)] )

def jogar_novamente():
    r = input('Deseja jogar novamente?')
    return r in 'Sim'
    

def ganhou(sorteada, certas):
    return set(sorteada) == set(certas)

def chute(letras):
    from string import ascii_letters ##punctuation
    while True:
        x = input('Digite letra:')[0]
        if x in letras:
            print('Letra repitida')
        elif x not in ascii_letters:
            print('Caracter inválido')
        elif len(x) != 1:
            print('Só uma letra1')
        else:
            return x

forca = [''' ''', ''' o ''', ''' o_ ''', ''' _o_ ''', '''_o_/''', '''\_o_/''']
certas = erradas = ''

ganhou(sorteada,certas)

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
    
#if jogar_novamente(r): 
