from modelos.entrega import Entrega
from interfaces.calculo_frete_interface import CalculoFreteInterface


class EntregaComum(Entrega, CalculoFreteInterface):

    def calcular_frete(self):
        return self.pedido.distancia * 1.5