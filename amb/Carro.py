class Carro:

    def __init__(self, id_carro, marca, modelo, disponibilidade, placa, aluguel, venda):
        self.id = id_carro
        self.marca = marca
        self.modelo = modelo
        self.disponibilidade = disponibilidade
        self.placa = placa
        self.aluguel = aluguel
        self.venda = venda

    #Getters
    def get_id(self):
        return self.id

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_disponibilidade(self):
        return self.disponibilidade

    def get_placa(self):
        return self.placa

    def get_aluguel(self):
        return self.aluguel

    def get_venda(self):
        return self.venda

    #Setters
    def set_id(self, id_carro):
        self.id = id_carro

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_disponibilidade(self, disponibilidade):
        self.disponibilidade = disponibilidade

    def set_placa(self, placa):
        self.placa = placa

    def set_aluguel(self, aluguel):
        self.aluguel = aluguel

    def set_venda(self, venda):
        self.venda = venda
