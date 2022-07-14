

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__limiteDisponivel = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular.title()

    @titular.setter
    def titular(self, nome):
        self.__titular = nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.__saldo, self.titular))

    def sacar(self, valor):
        if self.__saldo > 0 and self.__saldo - valor >= 0:
            self.__saldo -= valor
            print("saque de {} efetivado com sucesso, saldo agora é de {}".format(valor, self.__saldo))
            return
        if self.__limiteDisponivel > 0 and self.__limiteDisponivel - valor >= 0:
            self.__limiteDisponivel -= valor
            print("saque de {} efetivado com sucesso, usando limite disponivel atual de {}".format(valor, self.__saldo))
        else:
            print("Sua conta não possui saldo ou limite disponivel para saque")

    def depositar(self, valor):
        if self.__saldo < 0:
            if valor + self.__limiteDisponivel > self.__limite:
                usoLimite = self.limite - self.__limiteDisponivel
                self.__limiteDisponivel = self.limite
                self.__saldo += valor - usoLimite
            else:
                self.__limiteDisponivel += valor
        else:
            self.__saldo += valor

    def usoLimite(self):
        return self.__limite - self.__limiteDisponivel
