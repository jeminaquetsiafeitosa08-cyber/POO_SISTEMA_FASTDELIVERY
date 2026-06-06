class PedidoService:

    def __init__(self):
        self.pedidos = []

    def cadastrar(self, pedido):
        self.pedidos.append(pedido)

    def listar(self):
        return self.pedidos

    def buscar_por_codigo(self, codigo):
        for pedido in self.pedidos:
            if pedido.codigo == codigo:
                return pedido

        return None

    def atualizar_status(self, pedido, status):
        pedido.status = status