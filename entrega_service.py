from modelos.entrega_comum import EntregaComum
from modelos.entrega_expressa import EntregaExpressa
from modelos.entrega_premium import EntregaPremium


class EntregaService:

    def calcular_frete(self, pedido, entregador):

        if pedido.tipo_entrega.lower() == "comum":
            entrega = EntregaComum(pedido, entregador)

        elif pedido.tipo_entrega.lower() == "expressa":
            entrega = EntregaExpressa(pedido, entregador)

        else:
            entrega = EntregaPremium(pedido, entregador)

        return entrega.calcular_frete()