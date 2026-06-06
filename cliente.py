from modelos.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome)

        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Telefone: {self.telefone}"
        )