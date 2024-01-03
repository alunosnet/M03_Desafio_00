"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""
def mostrar_letra (palavra):
    for posiçao in range(len(palavra)-1):
        if palavra[posiçao]==palavra[posiçao+1]:
            print(palavra[posiçao])


mostrar_letra("Hello")
def mostrar_letra_versao_2(palavra):
        pass
"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def num_pares(n1,n2,n3):
    pares=0
    if n1%2==0:
        pares=pares+1
    if n2%2==0:
        pares=pares+1
    if n3%2==0:
        pares=pares+1
    print(pares)



"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def Inverter_Texto(palavra):
    texto_invertido=""
    for letra in palavra:
        texto_invertido=letra+texto_invertido
    return texto_invertido


"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
def textoAlternado(palavra):
    texto=""
    for i in range(0,len(palavra),2):
        texto=texto+palavra[i]
    return texto

def main():
    print(Inverter_Texto("Hello"))
    print(textoAlternado("Hello"))

if __name__=="__main__":
    main()