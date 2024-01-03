"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""

def LetrasIguais(palavra):
    for posicao in range(len(palavra)-1):
        if palavra[posicao]==palavra[posicao+1]:
            print(palavra[posicao])

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def Pares(n1,n2,n3):
    contar=0
    if n1%2==0:
        contar=contar+1
    if n2%2==0:
        contar=contar+1
    if n3%2==0:
        contar=contar+1
    print(contar)

"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def InverterTexto(palavra):
    texto_invertido=""
    for letra in palavra:
        texto_invertido=
    return texto_invertido


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""


def main():
    LetrasIguais("Hello")
    Pares(10,4,8)
    Pares(23,6,3)

if __name__ == "__main__":
    main()