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

def invertertexto(palavra):
    terxto_invetido=""
    for letra in palavra:
        terxto_invetido=letra+terxto_invetido
    return terxto_invetido

"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""

def texto_alternado(palavra):
    texto=""
    for i in range(0,len(palavra,2)):
        texto=texto+palavra[i]
    return texto

def main():
    letras_iguais()
    letrasiguais_versao2()
    numeros_pares()

if __name__=="__main__":
    main()
