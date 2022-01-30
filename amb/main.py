from amb.Carro import Carro
from amb.Cliente import Cliente
from amb.EmpresaDAO import EmpresaDAO

dao = EmpresaDAO()
op1 = 1

while op1 != 0:
    op2 = 1
    print(" ----- Sistema Gerenciador de Agência de Aluguel de 1Carros ----- ")
    print(" --- Escolha a opção: ---")
    print("1 - Gerenciar Carros")
    print("2 - Gerenciar Clientes")
    print("3 - Registrar Aluguel de Carro")
    print("4 - Registrar Devolução de Carro")
    print("0 - Sair")
    op1 = int(input())

    if op1 == 1:
        while op2 != 0:
            print(" ------ GERENCIADOR DE CARROS -----")
            print("1 - Cadastrar novo carro")
            print("2 - Editar carro")
            print("3 - Listar carros")
            print("4 - Buscar carro")
            print("5 - Deletar carro")
            print("6 - Mudar disponibilidade de carro")
            print("0 - Sair")
            op2 = int(input())

            if op2 == 1:
                print("\n----- CADASTRO DE CARROS -----")
                marca = input("Insira a Marca do Carro: ")
                modelo = input("Insira o Modelo do Carro: ")
                placa = input("Insira a Placa do Carro: ")
                aluguel = input("Insira o Preço de Aluguel do Carro: ")
                venda = input("Insira o Preço de Venda do Carro: ")

                carro = Carro(id_carro=None,marca=marca,modelo=modelo,disponibilidade=False,placa=placa,aluguel=aluguel,venda=venda)
                dao.cadastrarCarro(carro)

            elif op2 == 2:
                idcarro = input("Insira o ID do carro:")
                categoria = input("Insira a categoria em que o carro será editado\n(marca,modelo,disponivel,placa,valorAluguel, valorVenda):")
                valor = input("Insira o novo valor:")

                dao.editarCarro(idcarro, categoria, valor)
            elif op2 == 3:
                print("\n----- LISTA DE CARROS -----")
                for tupla in dao.listarCarro():
                    print(tupla)

            elif op2 == 4:
                print("\n----- BUSCA DE CARRO -----")
                idcarro = input("insira ID do Carro:")
                print(dao.buscarCarro(idcarro))

            elif op2 == 5:
                print("\n----- REMOÇÃO DE CARRO -----")
                idcarro = input("insira ID do Carro:")
                dao.deletarCarro(idcarro)

            elif op2 == 6:
                print(" \n----- MUDANÇA DE DISPONIBILIDADE DE CARRO")
                idCarro = int(input("Insira ID do carro:"))
                cont = bool(int(input("Carro esta disponivel ? (0 - Não, 1 - Sim):")))
                dao.mudarDisponibilidade(idCarro, cont)

            elif op2 == 0:
                break

            else:
                print(" --->> Opção Inválida! Digite Novamente")

    elif op1 == 2:

        while op2 != 0:
            print("\nGerenciador de Clientes:")
            print("1 - Cadastrar novo cliente")
            print("2 - Editar cliente")
            print("3 - Listar clientes")
            print("4 - Buscar cliente")
            print("5 - Deletar cliente")
            print("0 - Sair")
            op2 = int(input())
            if op2 == 1:
                print("\n----- CADASTRO DE CLIENTES -----")
                nome = input("Insira a Nome do Cliente: ")
                cpf = input("Insira o Cpf do Cliente: ")
                telefone = input("Insira a Telefone do Cliente: ")

                c1 = Cliente(id_cliente=None, nome=nome, cpf=cpf, telefone=telefone)
                dao.cadastrarCliente(c1)

            elif op2 == 2:
                idcliente = input("Insira o ID do cliente:")
                categoria = input("Insira a categoria em que o carro será editado\n(nome, cpf, telefone):")
                valor = input("Insira o novo valor:")

                dao.editarCliente(idcliente, categoria, valor)

            elif op2 == 3:
                print("\n----- LISTA  DE CLIENTES -----")
                for tupla in dao.listarCliente():
                    print(tupla)

            elif op2 == 4:
                print("\n----- BUSCA DE CLIENTE -----")
                idcliente = input("insira ID do Cliente:")
                print(dao.buscarCarro(idcliente))

            elif op2 == 5:
                print("\n----- REMOÇÃO DE CLIENTE -----")
                idcliente = input("insira ID do Cliente:")
                dao.deletarCarro(idcliente)
            elif op2 == 0:
                break

            else:
                print("\n --->> Opção Inválida! Digite Novamente")
    elif op1 == 3:
        print(" ----- REGISTRO DE ALUGUEL -----")
        idCliente = int(input("Insira o ID do Cliente:"))
        idCarro = int(input("Insira o ID do Carro:"))

        dao.registrarAluguel(idcliente=idCliente, idcarro=idCarro)

    elif op1 == 4:
        print(" \n----- REGISTRO DE DEVOLUÇÃO -----")
        idCarro = int(input("Insira ID do carro:"))
        dao.registrarDevolucao(idCarro)

    elif op1 == 0:

        break

    else:
        print("\n --->> Opção Inválida! Digite Novamente")

