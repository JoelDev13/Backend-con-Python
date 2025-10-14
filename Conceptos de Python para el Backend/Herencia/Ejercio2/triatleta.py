from nadador import Nadador
from corredor import Corredor

class Triatleta(Nadador, Corredor):
    def competir(self):
        return f"El triatleta {self.nadar()} y {self.correr()}"
