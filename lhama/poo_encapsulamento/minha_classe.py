class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Minhas características estão aqui.'
        self.meu_atributo2 = att

    def meu_metodo(self):
        print('Estou no metodo!')

    def meu_metodo2(self, num, mult):
        return num * mult


objeto = MinhaClasse('Meu 2º atributo')
objeto.meu_metodo()
result = objeto.meu_metodo2(3, 3)
print(result)
objeto.meu_metodo()
att = objeto.meu_atributo

print(att, objeto.meu_atributo2)
