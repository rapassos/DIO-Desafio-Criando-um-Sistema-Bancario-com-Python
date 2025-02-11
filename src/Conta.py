
class Conta:
    def __init__(self, cliente,numero):
        self.numero = numero
        self.cliente = cliente
        self.count_op = 0
        self.saldo = 0
        self.extrato = []