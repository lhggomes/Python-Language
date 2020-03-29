#Here we'll use the abc module (Abstract Base Classes)
import abc

class Funcionario(abc.ABC):

   @abc.abstractmethod
   def get_bonificacao(self):
       pass

if __name__ == '__main__':
    f = Funcionario()