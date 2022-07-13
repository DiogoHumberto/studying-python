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
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas

        print(letrasAcertadas)

    if acertou:
        exibeMsgVencedor()
    else:
        exibeMsgPerdedor(palavraSecreta)


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


def exibeMsgPerdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def exibeMsgVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    match erros:
        case 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
        case 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")
        case 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")
        case 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")
        case 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")
        case 6:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
        case 7:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
