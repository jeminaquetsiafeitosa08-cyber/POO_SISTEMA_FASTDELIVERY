class Menu:

    @staticmethod
    def principal():

        print("\n=== FAST DELIVERY ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Pedido")
        print("3 - Listar Pedidos")
        print("4 - Atualizar Status")
        print("0 - Sair")

        return input("Escolha uma opção: ")