"""
1 - Cria uma função que recebe um texto. A função deve mostrar uma letra sempre que existirem duas letras seguidas iguais.
Por exemplo: 
    Hello - deve mostrar l
"""

def duplicatedLetters(word):
    letter = ""
    final = ""
    
    for i in word:
        if i == letter:
            final = final + letter
        letter = i

    print("Duplicated letters: ", final)

"""
V2 do exercisio 1 usando um ciclo while
"""

def duplicatedLettersV2(word):
    position = 0

    while position < len(word) - 1:
        if word[position] == word[position + 1]:
            print(word[position])
        position = position + 1

"""
2 - Cria uma função que recebe três números. Esta função deve mostrar, para os números passados, quantos são pares.
"""

def howManyPairNumbers(n1, n2, n3):
    howMany = 0

    if n1 % 2 == 0:
        howMany = howMany + 1
    if n2 % 2 == 0:
        howMany = howMany + 1
    if n3 % 3 == 0:
        howMany = howMany + 1

    print("Ammount of pair numbers: ", howMany)

"""
3 - Faz uma função que recebe um texto e devolve o texto invertido.
"""

def revertText(Text):
    reversedText = ""

    for i in range(len(Text)):
        reversedText = reversedText + Text[len(Text) -1 -i]

    return reversedText

"""
4 - Faz uma função que recebe um texto e devolve esse texto removendo uma letra alternadamente.
Por exemplo:
    Hello - deve devolver Hlo
"""

def removeLettersAlternately(word):
    text = ""

    for i in range(0, len(word), 2):
        text = text + word[i]

    return text