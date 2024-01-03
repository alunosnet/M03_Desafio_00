"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""
def letras_iguais(palavra):
    for posição in range (len(palavra)-1):
        if palavra[posição]==palavra[posição+1]:
            print(palavra[posição])

letras_iguais("hellow")
        

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""
def numerosdepares(n1,n2,n3):
    contar=0
    if n1%2 ==0:
        contar = contar +1
    if n2%2 ==0:
        contar = contar +1
    if n3%2 ==0:
        contar = contar +1
    print(contar)

    
"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""
def invertertexto(palavra):
    texto_invertido=""
    for letra in palavra:
        texto_invertido = letra + texto_invertido
    return texto_invertido

"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""
def textoalternado(palavra):
    texto=""
    for i in range(0,len(palavra),2):
        texto = texto + palavra[i]
    returntexto




def main():
    #numerosdepares(10,4,8)
    #numerosdepares(1,3,5)
    #numerosdepares(10,3,8)
    #print(invertertexto("hello"))
    print(textoalternado("hello"))


if __name__=="__main__":
    main()
