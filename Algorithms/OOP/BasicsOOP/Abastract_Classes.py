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
