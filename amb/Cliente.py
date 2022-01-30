class Cliente:

    def __init__(self, id_cliente,nome, cpf, telefone):
        self.id = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    #Getters
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_telefone(self):
        return self.telefone

    #Setters
    def set_id(self, id_cliente):
        self.id = id_cliente

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_telefone(self, telefone):
        self.telefone = telefone
