from time import sleep # Importando a função sleep do módulo time
from Banco import Banco
#from Cliente import Cliente

def menu(banco):
    print("".center(80, "#"))
    print(banco.nome.center(80))
    print("".center(80, "#"))
    if banco.conta:
        saldo = f"{banco.conta.saldo:.2f}"
    print(f"{'Conta atual: '+banco.conta.numero+'-'+banco.conta.agencia+'\t' if banco.conta else ''}{'Saldo: R$'+saldo+'\t' if banco.conta else ''}Cliente: {banco.cliente.nome if banco.cliente else 'Nenhum'}")
    print("".center(80, "-"))
    print("Menu:")
    print("1 - Adicionar cliente")
    print("2 - Listar/Selecionar cliente")
    print("3 - Adicionar conta")
    print("4 - Selecionar Conta")
    print("5 - Exibir saldo")
    print("6 - Deposito")
    print("7 - Saque")
    print("8 - Extrato")
    print("0 - Sair")
    op = input("Escolha uma opção: ")
    return op

def carregando(total_sleep,cadencia,msg):
    #input("\nEnter para continuar")
    tempo = 0
    msg
    while tempo < total_sleep:
        msg += "."
        print(msg, end="\r")
        sleep(cadencia)
        tempo += cadencia
    print("\n")


def main():
    banco = Banco("Rapassos Bank")

    def add_conta():
        agencia = "1".zfill(2)
        conta = str(len(banco.contas) + 1).zfill(4)
        banco.adicionar_conta(agencia,conta)
        
    #Fluxo de execução
    while True:
        carregando(2,0.1,"Carregando")
        opt = menu(banco)

        match opt:
            case "1": # Adicionar cliente
                nome = input("Informe o nome do cliente:")
                if not nome:
                    print("Nome inválido!")
                    continue
                cpf = input("Informe o CPF do cliente:")
                if not banco.busca_cpf(cpf):
                    print("CPF já cadastrado!")
                    continue
                banco.adicionar_cliente(nome, cpf)
                add_conta()

            case "2": # Listar/Selecionar cliente
                banco.listar_clientes()
                cpf = input("Informe o CPF do cliente:")
                banco.selecionar_clientes(cpf)

            case "3": # Adicionar conta
                if not banco.cliente:
                    print("Selecione um cliente")
                    continue
                add_conta()
            
            case "4": # Listar/Selecionar conta
                if not banco.cliente:
                    print("Selecione uma Conta")
                    continue
                banco.listar_contas()
                conta = input("Informe o número da conta:")
                banco.selecionar_conta(conta)

            case "5": # Exibir saldo
                if not banco.conta:
                    print("\nSelecione uma conta!\n")
                    continue
                banco.exibir_saldo(banco.conta)

            case "6": # Deposito
                if not banco.conta:
                    print("\nSelecione uma conta!\n")
                    continue
                try:    
                    valor = float(input("Informe o valor do depósito:"))
                    banco.deposito(banco.conta, valor)
                except ValueError:
                    print("Valor invàlido!")

            case "7": # Saque
                if not banco.conta:
                    print("\nSelecione uma conta!\n")
                    continue
                try:
                    valor = float(input("Informe o valor do saque:"))
                    banco.saque(banco.conta,valor)
                except ValueError:
                    print("Valor invàlido!")

            case "8": # Extrato
                if not banco.conta:
                    print("\nSelecione uma conta!\n")
                    continue
                banco.exibir_extrato(banco.conta)
                input("Pressione Enter para continuar...")
                
            case "0": # Sair
                print("Sair")
                break

            case _:
                print("Opção inválida")

if __name__ == '__main__':
    main()
