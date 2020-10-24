#Here we'll use the abc module (Abstract Base Classes)
import abc

class Pessoa(abc.ABC):

   @abc.abstractmethod
   def get_bonificacao(self):
       pass



class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @abc.abstractmethod
    def atualiza(self):
        pass

    @abc.abstractmethod
    def imprimir_titular(self):
        print(self._numero)
        print(self._titular)
        print(self._saldo)
        print(self._limite)
        pass


class PJ(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo=0, limite=1000.0)




C = PJ("1435", "Lucas Henrique")
