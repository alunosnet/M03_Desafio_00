"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""
def LetraRepetida(palavra):
    for i in range(len(palavra) - 1):
        if palavra[i] == palavra[i + 1]:
            print(palavra[i])

LetraRepetida("Hello")

def LetraRepetidaV2(palavra):
    posicao = 0
    while posicao < len(palavra) - 1:
        if palavra[posicao] == palavra[posicao + 1]:
            print(palavra[posicao])
        posicao = posicao + 1

LetraRepetidaV2("Hello")

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def NumerosPares(n1,n2,n3):
    numeros_pares = 0
    if n1 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if n2 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if n3 % 2 == 0:
        numeros_pares = numeros_pares + 1
    print(numeros_pares)

NumerosPares(1,2,4)

"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def PalavraInvertida(palavra):
    palavra_invetida = ""
    for i in range(len(palavra)):
        palavra_invetida = palavra_invetida + palavra[-1 -i]
    print(palavra_invetida)

PalavraInvertida("Hello")

"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""

def PalavraAlternada(palavra):
    palavra_alternada = ""
    for i in range(len(palavra)):
        if i % 2 == 0:
            palavra_alternada += palavra[i]
    return (palavra_alternada)

print(PalavraAlternada("Hello"))
