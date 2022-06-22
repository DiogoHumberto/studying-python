from random import randint

def jogar():
    print("*****************************************")
    print("Bem vindo ao Jogo da sorte! Tente a sorte amigão :P")
    print("*****************************************")

    intervaloInicio = int(input("Digite um número do intervalo de inicio para o Número secreto: "))

    intervaloFinal = int(input("Digite um número do intervalo final para o Número secreto: "))

    print("*****************************************")
    print("Intervalo de Jogo é de {} a {}".format(intervaloInicio, intervaloFinal))
    print("*****************************************")

    numeroSecreto = randint(intervaloInicio, intervaloFinal)

    qtdTentativas = int(3)

    numeroSorte = int(input("Digite o seu número da sorte: "))

    for rodada in range(qtdTentativas - 1):

        if numeroSorte == numeroSecreto:
            print("Iuuu você acertou, tá bem einnn!!")
            break
        elif numeroSorte > numeroSecreto:
            print("**** Não agora tente novamente! você possui {} tentativa(s) de {}".format(qtdTentativas - 1 - rodada,
                                                                                             qtdTentativas))
            numeroSorte = int(input("Está perto para CIMA, Digite o seu número da sorte: "))
        else:
            print("**** Não foi agora tente novamente! você possui {} tentativa(s) de {}".format(qtdTentativas - 1 - rodada,
                                                                                                 qtdTentativas))
            numeroSorte = int(input("Está perto para BAIXO, Digite o seu número da sorte: "))

    if numeroSorte != numeroSecreto:
        print("-----------------------------------------------------------------------")
        print(
            "QUAN QUAN QUANNNNNNNNNNNN ---->   Não foi dessa vez :( !!!! O NÚMERO SECRETO ERA *** {} ***  TENTE NOVAMENTE "
            .format(numeroSecreto))

if(__name__ == "__main__"):
    jogar()
