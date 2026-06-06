from modelos.pessoa import Pessoa


class Entregador(Pessoa):

    def __init__(self, nome, veiculo, cnh):
        super().__init__(nome)

        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def cnh(self):
        return self.__cnh

    @veiculo.setter
    def veiculo(self, veiculo):
        self.__veiculo = veiculo

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Veículo: {self.veiculo} | "
            f"CNH: {self.cnh}"
        )