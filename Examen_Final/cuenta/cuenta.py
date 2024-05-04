# cuenta.py
class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")
   
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso: {cantidad} unidades. Saldo actual: {self.saldo}")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para el retiro.")
        else:
            print("El monto a retirar debe ser positivo.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo} unidades.")
