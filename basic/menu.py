import forca
import adivinhacao

print("*****************************************************")
print("*****************Escolha o seu Jogo!*****************")
print("*****************************************************")

print("Digite (1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo deseja? ... "))

match jogo:
    case 1:
        forca.jogar()
    case 2:
        adivinhacao.jogar()
    case _:
        print("Jogo invalido!")
