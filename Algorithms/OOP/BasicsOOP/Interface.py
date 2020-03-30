import abc

class Controlador(abc.ABC):
    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def abrir_menu(self):
        pass

    @abc.abstractmethod
    def fechar_menu(self):
        pass

    @abc.abstractmethod
    def mais_volume(self):
        pass

    @abc.abstractmethod
    def menos_volume(self):
        pass


