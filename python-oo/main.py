from entity.conta import Conta

def testeConta():

    conta1 = Conta("teste", "Diogo", 0, 300)

    print(conta1.numero)
    print(conta1)
    print(conta1.saldo)
    conta1.sacar(500)


if __name__ == '__main__':
    testeConta()

