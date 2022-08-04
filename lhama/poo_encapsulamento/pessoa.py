class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade 
        self.__cpf = cpf

    """def print_cpf(self):
        print(self.__cpf)"""
    
    def correr(self):
        print('Estou correndo')
    
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')
           
    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 30, '999.999.000-00')
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')

