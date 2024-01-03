"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""

def letras_iguais(palavra):
    palavra=input("Escreva uma palavra:")
    for i in range(len(palavra)-1):
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])
letras_iguais("hello"):

def letrasiguais_versao2():
    posicao=0
    while posicao<len(palavra)-1:
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])
        posicao=posicao+1
"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""

def numeros_pares():
    for i in range(3):
        n=int(input("Escreva um numero:"))


"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
