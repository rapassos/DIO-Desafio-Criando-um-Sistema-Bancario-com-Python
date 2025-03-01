from Conta import Conta
from Cliente import Cliente
from datetime import datetime

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.MAXSAQUE = 500
        self.MAXOP = 10
        self.cliente = None
        self.conta = None

    def adicionar_cliente(self, nome, cpf):
        self.cliente = Cliente(nome, cpf)
        self.clientes.append(self.cliente)
        return self.cliente

    def busca_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return False
        return True
    
    def listar_clientes(self):
        print("Clientes:")
        for cliente in self.clientes:
            print(f"{cliente.cpf}\t{cliente.nome}")

    def selecionar_clientes(self, cpf):
        encontrado = False
        for cliente in self.clientes:
            if cliente.cpf == cpf:                
                self.cliente = cliente
                for conta in self.contas:
                    if conta.cliente == cliente:
                        self.selecionar_conta(f"{conta.numero}-{conta.agencia}")
                        encontrado = True
                        break
        if not encontrado:
            print("Cliente não encontrado")

    def adicionar_conta(self,agencia,numero):
        self.conta = Conta(self.cliente,agencia,numero)
        self.contas.append(self.conta)
        return self.conta

    def listar_contas(self):
        print("Contas:")
        for conta in self.contas:
            print(f"{conta.numero}-{conta.agencia}\t{conta.cliente.cpf}\t{conta.cliente.nome}")

    def selecionar_conta(self, numero_conta):
        for conta in self.contas:
            if f"{conta.numero}-{conta.agencia}" == numero_conta:
                self.conta = conta
                self.cliente = conta.cliente
                return conta
        print("Conta não encontrada")
        return

    def exibir_saldo(self, conta):
        # conta = self.buscar_conta(numero_conta)
        if conta in self.contas:
            print(f"Seu saldo é de R${conta.saldo:.2f}")
        else:
            print("Conta não encontrada")

    def deposito(self, conta, valor):
        if conta.count_op >= self.MAXOP:    
            print("Limite de operações excedido!")
            return
        
        if valor <= 0:
            print("Valor inválido!")
            return

        conta.count_op += 1
        conta.saldo += valor
        self.registrador(conta,tipo="Depósito",valor=valor)
        print("Depósito realizado com sucesso!")            

    def saque(self, conta, valor):
        if conta.count_op >= self.MAXOP:    
            print("Limite de operações excedido!")
            return
        
        if valor > self.MAXSAQUE:
            print("Valor superior ao limite por operação!")
            return
        
        if valor <= 0:
            print("Valor inválido!")
            return

        if valor > conta.saldo:
            print("Saldo insuficiente!")
            return
        
        conta.count_op += 1
        conta.saldo -= valor
        self.registrador(conta,tipo="Saque",valor=valor)
        print("Saque realizado com sucesso!")
            

    def exibir_extrato(self, conta):
        print("Extrato:".center(80,"#"))
        print(f"Conta: {conta.numero}-{conta.agencia}\tCPF: {conta.cliente.cpf}\tNome: {conta.cliente.nome}")
        print("".center(80,"-"))
        for item in conta.extrato:
            print(f"{item["datahora"].strftime("%d/%m/%Y %H:%M:%S")}\t{item["valor"]:.2f}\t{item["tipo"]}")
        print("".center(80,"-"))
        self.exibir_saldo(conta)
        print("".center(80,"#"))

    def registrador(self, conta, valor, tipo):
        conta.extrato.append({"tipo":tipo,"valor":(valor),"datahora":datetime.now()})