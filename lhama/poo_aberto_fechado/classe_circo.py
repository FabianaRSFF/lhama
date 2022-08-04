"""class Circo:
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()
    
    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show.')
    
    def apresentar_palhaco(self):
        print('Palhaco apresentando o seu show.')

circo = Circo()
circo.apresentar(1)
circo.apresentar(2)"""

class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando o seu show.')
    

class Palhaco:
    def apresentar_show(self):
        print('Palhaco apresentando o seu show.')


class Magico:
    def apresentar_show(self):
        print('Magico apresentando o seu show.')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
magico = Magico()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(magico)