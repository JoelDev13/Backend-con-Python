class Carro:
    def __init__(self, marca,modelo,color,velocidadMax):
        self.marca = marca;
        self.modelo = modelo;
        self.color = color;
        self.velocidadMax = velocidadMax ;

    def conducir(self):
        print(f"Joel va conduciendo el coche {self.marca} {self.modelo} de color {self.color} a una velocidad de {self.velocidadMax} km/h")


mi_coche = Carro("Toyota", "Corolla", "Negro", 75)

mi_coche.conducir()

    