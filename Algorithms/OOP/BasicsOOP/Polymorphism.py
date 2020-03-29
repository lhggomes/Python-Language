class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qt_funcionarios ):
        super().__init__(nome,cpf, salario)
        self._senha = senha
        self._qt_func = qt_funcionarios


    def get_bonificacao(self):
        return self._salario * 0.15


gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)
print(gerente.get_bonificacao())
