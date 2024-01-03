"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""
def LetrasIguais(palavra):
    for posicao in range(len(palavra)-1):
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])


def LetrasIguais_versao_2(palavra):
    posicao = 0
    while posicao < len(palavra)-1:
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])
        posicao = posicao + 1

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""

def NumeroDePares(n1,n2,n3):
    contar = 0
    if n1%2 == 0:
        contar = contar +1
    if n2%2 == 0:
        contar = contar +1
    if n3%2 == 0:
        contar = contar +1
    print(contar)

"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""

def main():
    #LetrasIguais("hello")
    #LetrasIguais_versao_2("hello")
    NumeroDePares(10,4,8)
    NumeroDePares(1,3,5)
    NumeroDePares(10,3,8)
    
    
if __name__=="__main__":
    main()