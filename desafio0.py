"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""

def LetrasIguais(palavra):
    for posicao in range(len(palavra)-1):
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])

LetrasIguais('Hello')
print('-----')

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def Pares(n1,n2,n3):
    if n1%2==0:
        print('par')
    if n2%2==0:
        print('par')
    if n3%2==0:
        print('par')

Pares(6,20,9)

"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
