class ControleRemoto:
    def __init__(self, tv, comodo):
        self.tv = tv
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avancado')

    def retrosceder_canal(self):
        print('Voltar canal')
    
    def escolher_canal(self, canal):
        print(f'Canal escolhido: {canal}')


controle_sala = ControleRemoto('sony', 'sala')
print(controle_sala.comodo)
print(controle_sala.tv)
controle_sala.avancar_canal()
controle_sala.escolher_canal(30)
controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.tv)
controle_quarto.avancar_canal
controle_quarto.escolher_canal(22)
