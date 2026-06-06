from modelos.cliente import Cliente
from modelos.entregador import Entregador
from modelos.pedido import Pedido

from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService

from utils.menu import Menu


cliente_service = ClienteService()
pedido_service = PedidoService()
entrega_service = EntregaService()


entregador = Entregador(
    "Carlos",
    "Moto",
    "123456789"
)


while True:

    opcao = Menu.principal()

    if opcao == "1":

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        cliente = Cliente(
            nome,
            cpf,
            telefone,
            endereco
        )

        cliente_service.cadastrar(cliente)

        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":

        cpf = input("CPF do cliente: ")

        cliente = cliente_service.buscar_por_cpf(cpf)

        if not cliente:
            print("Cliente não encontrado!")
            continue

        codigo = int(input("Código do pedido: "))
        peso = float(input("Peso: "))
        distancia = float(input("Distância: "))
        tipo = input(
            "Tipo (Comum/Expressa/Premium): "
        )

        pedido = Pedido(
            codigo,
            cliente,
            peso,
            distancia,
            tipo
        )

        pedido_service.cadastrar(pedido)

        print("Pedido cadastrado com sucesso!")

    elif opcao == "3":

        for pedido in pedido_service.listar():

            frete = entrega_service.calcular_frete(
                pedido,
                entregador
            )

            print("\n------------------")
            print(f"Código: {pedido.codigo}")
            print(f"Cliente: {pedido.cliente.nome}")
            print(f"Tipo: {pedido.tipo_entrega}")
            print(f"Status: {pedido.status}")
            print(f"Frete: R$ {frete:.2f}")

    elif opcao == "4":

        codigo = int(input("Código do pedido: "))

        pedido = pedido_service.buscar_por_codigo(
            codigo
        )

        if pedido:

            print("\n1 - Em preparação")
            print("2 - Saiu para entrega")
            print("3 - Entregue")
            print("4 - Cancelado")

            escolha = input("Novo status: ")

            status = {
                "1": "Em preparação",
                "2": "Saiu para entrega",
                "3": "Entregue",
                "4": "Cancelado"
            }

            if escolha in status:
                pedido_service.atualizar_status(
                    pedido,
                    status[escolha]
                )

                print("Status atualizado!")

        else:
            print("Pedido não encontrado!")

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")