from config.Database import Database


class EmpresaDAO:

    def __init__(self):
        pass

    # Funções de manipulação da tabela Carro

    def cadastrarCarro(self, carro):
        # 1 — Conexão com o banco de dados
        bd = Database().conectar()
        # 2 - Receber o cursor
        cursor = bd.cursor()
        # 3 - Executar script
        script = f"insert into Carro (marca, modelo, placa, valoraluguel, valorvenda) values ( '{carro.get_marca()}','{carro.get_modelo()}','{carro.get_disponibilidade()}','{carro.get_placa()}','{carro.get_aluguel()}','{carro.get_venda()}')"
        cursor.execute(script)
        bd.commit()
        print("Carro cadastrado!!")

    def editarCarro(self, idcarro, categoria, valor):
        bd = Database().conectar()
        cursor = bd.cursor()
        print(categoria)
        script = f"update Carro set {categoria} = '{valor}' where idcarro = {idcarro}"

        cursor.execute(script)
        bd.commit()

        print(f" --->> Cadastro do carro {idcarro} foi alterado ---")

    def buscarCarro(self, idCarro):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"select * from Carro where idcarro={idCarro}")
        return cursor.fetchone()


    def listarCarro(self):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from Carro order by idcarro")
        return cursor.fetchall()

    def deletarCarro(self, idCarro):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"delete from Carro where idcarro={idCarro}")
        print(f" --->> Carro {idCarro} foi removido --- ")
        bd.commit()

    def mudarDisponibilidade(self, idcarro, disp):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"update Carro set disponivel = {disp} where idcarro = {idcarro}")
        print(f" --->> Disponibilidade do carro {idcarro} foi mudada para {disp}")
        bd.commit()


    # Funções de manipulação da tabela Cliente

    def cadastrarCliente(self, cliente):

        # 1 — Conexão com o banco de dados
        bd = Database().conectar()
        # 2 - Receber o cursor
        cursor = bd.cursor()
        # 3 - Executar script
        script = f"insert into Cliente (nome,cpf,telefone) values ( '{cliente.get_nome()}','{cliente.get_cpf()}','{cliente.get_telefone()}')"
        cursor.execute(script)
        bd.commit()
        print(" --->> Cliente cadastrado!!")

    def editarCliente(self, idcliente, categoria, valor):
        bd = Database().conectar()
        cursor = bd.cursor()

        script = f"update Cliente set {categoria} = '{valor}' where idcliente = {idcliente}"

        cursor.execute(script)
        bd.commit()

        print(f" --->> Cadastro do cliente {idcliente} foi alterado ---")

    def listarCliente(self):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from Cliente order by idcliente")
        return cursor.fetchall()

    def buscarCliente(self, idCliente):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"select * from Cliente where idcliente={idCliente}")
        return cursor.fetchone()

    def deletarCliente(self, idCliente):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"delete from Carro where idcarro={idCliente}")
        print(f" --->> Cliente {idCliente} deletado")
        bd.commit()

    # Funções de Relação Carro-Cliente

    def registrarAluguel(self, idcarro, idcliente):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"update Carro set idcliente = {idcliente} where Carro.idcarro = {idcarro}")
        cursor.execute(f"update Carro set disponivel = {False} where Carro.idcarro = {idcarro}")
        bd.commit()
        print(" --->> Aluguel Registrado")

    def registrarDevolucao(self, idcarro):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute(f"update Carro set idcliente = null where idcarro={idcarro}")
        cursor.execute(f"update Carro set disponivel=False where idcarro={idcarro}")
        print(" --->> Devolução Registrada")
        bd.commit()



