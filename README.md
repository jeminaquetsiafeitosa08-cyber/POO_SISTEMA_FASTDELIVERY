# POO_SISTEMA_FASTDELIVERY
Desenvolvimento de um Sistema Fast Delivery utilizando POO em Python
Fast Delivery
Sistema de gerenciamento de entregas desenvolvido em Python utilizando os conceitos de Programação Orientada a Objetos (POO).
Nele, temos as seguintes funcionalidades:
Cadastro de clientes
Cadastro de entregadores
Cadastro de pedidos
Cálculo de frete
Atualização de status dos pedidos
Listagem de pedidos
Estrutura do Projeto
O projeto está organizado em camadas para separar responsabilidades:
modelos: entidades do sistema
interfaces: contratos para cálculo de frete
services: regras de negócio
util: funções auxiliares
main.py: execução da aplicação


fast_delivery/
│
├── main.py
│
├── modelos/
│ ├── pessoa.py
│ ├── cliente.py
│ ├── entregador.py
│ ├── pedido.py
│ └── entrega.py
│ └── entrega_comum.py
│ └── entrega_expressa.py
││ └── entrega_premium.py
├── interfaces/
│ └── calculo_frete_interface.py
│
├── services/
│ ├── pedido_service.py
│ ├── cliente_service.py
│ └── entrega_service.py
│
├── util/
│ ├── validador.py
│ ├── menu.py
│ └── formatador.py



Conceitos Aplicados
Herança
Encapsulamento
Interface
Polimorfismo
Separação de responsabilidades


Regras de Frete
Entrega Comum: distância × 1,5
Entrega Expressa: distância × 3
Entrega Premium: distância × 5 + 20


Status dos Pedidos
Em preparação
Saiu para entrega
Entregue
Cancelado


Extensões utilizadas
Python 3
Programação Orientada a Objetos (POO)
Indentador
Material Icon Themer



Meu método de execução:
Executei o projeto pelo terminal:
python -m main.main


Autora
Jemina Quetsia Feitosa Teixeira
Acadêmica em Bacharelado em Ciências da Computação
