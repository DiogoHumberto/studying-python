import random


def jogar():
    exibirMsgIncio()
    palavraSecreta = carregaPalavraSecreta()
    letrasAcertadas = inciaLayoutPalavraAcertadas(palavraSecreta)
    print(letrasAcertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = inputLetraChute()

        if chute in palavraSecreta:
            letrasAcertadas = preencheLetrasAcertadas(palavraSecreta, letrasAcertadas, chute)

        else:
            erros += 1
            print("Letra não encontrada!")
        enforcou = erros == 6
        acertou = "_" not in letrasAcertadas

        print(letrasAcertadas)

    if acertou:
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")

    print("FIM DE JOGO")


def exibirMsgIncio():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregaPalavraSecreta():
    arquivo = open('palavras.txt', 'r')
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()
    return palavras[random.randrange(0, len(palavras))].upper()


def inciaLayoutPalavraAcertadas(palavras):
    return ["_" for _ in palavras]


def inputLetraChute():
    chute = input("Qual a letra contem a palavra? ").strip().upper()
    while not len(chute) == 1:
        chute = input("Preencha somente uma letra! Qual a letra contem a palavra? ").strip().upper()
    return chute


def preencheLetrasAcertadas(palavraSecreta, letrasAcertadas, chute):
    for index, letra in enumerate(palavraSecreta):
        if chute == letra:
            letrasAcertadas[index] = letra
    return letrasAcertadas


if __name__ == "__main__":
    jogar()
