class ClienteService:

    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente):
        self.clientes.append(cliente)

    def listar(self):
        return self.clientes

    def buscar_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente

        return None