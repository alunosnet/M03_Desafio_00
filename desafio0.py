"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""
def NumeroLetrasSeguidos(palav):
    letra1 = ""
    texto= ""
    for i in palav:
        if i == letra1:
            texto = texto + letra1
        letra1 = i
    print (texto)

""" versão dois do exercício um"""

def NumeroLetrasSeguidosVersao2(palav):
    numer1 = 0
    texto = ""
    while True:
        if palav[numer1] == palav[numer1+1]:
            texto = texto + palav[numer1]
        if len(palav)-1 > numer1:
            break
        numer1 += 1
    print (texto)



NumeroLetrasSeguidosVersao2("hello")

NumeroLetrasSeguidos("Feederico")


"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def TresPares():
    exit


"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def TextoInvertido():
    
    exit


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
