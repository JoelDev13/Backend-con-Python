from Animal import Animal

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau"