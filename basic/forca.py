
def jogar():
    print("*********Bem vido ao jogo da Forca!*********")

    palavra_secreta = "pyhton"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual a letra ? ").strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Enontrado a letra {} na posição {}".format(chute, index))
            index = index + 1
        print("Jogando!!")

if(__name__ == "__main__"):
    jogar()