"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""

def letra():
    palavra=input("palavra:")
    palavra=palavra.lower()
    for posiçao in range(len(palavra)-1):
        if palavra[posiçao]==palavra[posiçao+1]:
            print(palavra[posiçao])

letra()
def letra2():
    palavra=input("palavra:")
    posicao=0
    while posicao< len(palavra)-1:
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])
        posicao=posicao+1
letra2()

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""



"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def invertida():
    palavra=input("palavra:")
    palavra=palavra.lower()
    for letra in palavra:
        pass



"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
