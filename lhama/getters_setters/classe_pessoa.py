class Pessoa: # Substantivo

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome           # Substantivo
        self.idade = idade         # Substantivo
    
    def dirigir(self, nome:str, veiculo: str) -> None:       # Verbos
        print(f'{nome} está dirigindo um/a {veiculo}')
        
    def cantar(self) -> None:                       # Verbos
        print("La la la...")    
    
    def apresentar_idade(self) -> int:             # Verbos
        return self.idade
