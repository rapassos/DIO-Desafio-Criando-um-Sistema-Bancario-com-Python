from datetime import datetime
from Conta import Conta

class Operacoes:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.extrato = []
    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"{datetime.now()} - Conta {self.numero_conta} - Depósito: +{valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"{datetime.now()} - Conta {self.numero_conta} - Saque: -{valor:.2f}")
            return True
        return False

    def exibir_extrato(self):
        return "\n".join(self.extrato)
