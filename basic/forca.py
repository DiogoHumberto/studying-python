import random


def jogar():
    exibirMsgIncioJogo()
    arquivo = open('palavras.txt', 'r')
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    letras_acertadas = ["_" for _ in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual a letra ? ").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            print("Letra não encontrada!")
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")

    print("FIM DE JOGO")


def exibirMsgIncioJogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


if __name__ == "__main__":
    jogar()
