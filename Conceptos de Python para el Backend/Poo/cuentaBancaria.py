class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        
    def depositar(self, monto):
        self.saldo += monto
        print(f"Su nuevo saldo: {self.saldo}")
        pass

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto  
                print(f"Retiro realizado")
            else:
                print("No tiene suficiente dinero para retirar esa cantidad de dinero")
        else:
            print("El monto debe ser mayor a 0")

    def mostrar_informacion(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo}")




cuenta1 = CuentaBancaria("Joel", 1000)


monto_deposito = float(input("Ingrese el monto a depositar: "))
cuenta1.depositar(monto_deposito)

monto_retiro = float(input("Ingrese el monto a retirar: "))
cuenta1.retirar(monto_retiro)

cuenta1.mostrar_informacion()