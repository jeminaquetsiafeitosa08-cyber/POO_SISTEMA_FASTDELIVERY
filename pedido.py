class Pedido:

    def __init__(self, codigo, cliente, peso, distancia, tipo_entrega):
        self.codigo = codigo
        self.cliente = cliente
        self.peso = peso
        self.distancia = distancia
        self.tipo_entrega = tipo_entrega

        self.__status = "Em preparação"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status