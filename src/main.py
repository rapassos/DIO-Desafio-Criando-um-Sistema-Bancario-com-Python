from Banco import Banco
from Cliente import Cliente

def menu(banco):
    print("Banco")
    print("".center(60, "-"))
    print(f"Cliente atual: {banco.cliente.nome if banco.cliente else 'Nenhum'}")
    print("".center(60, "-"))
    print("Menu:")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Adicionar conta")
    print("4 - Listar contas")
    print("5 - Exibir saldo")
    print("6 - Deposito")
    print("7 - Saque")
    print("8 - Extrato")
    print("0 - Sair")
    op = input("Escolha uma opção: ")
    return op


def main():
    banco = Banco()

    #Fluxo de execução
    while True:
        opt = menu(banco)

        match opt:
            case "1": # Adicionar cliente
                banco.adicionar_cliente("Fulano", "123.456.789-00")

            case "2": # Listar clientes
                banco.listar_clientes()

            case "3": # Adicionar conta
                cliente = banco.buscar_cliente("123.456.789-00")
                banco.adicionar_conta(cliente1,"1234-5")
            
            case "4": # Listar contas
                exibir_extrato()
            
            case "5": # Exibir saldo
                banco.exibir_saldo(conta1)

            case "6": # Deposito
                banco.deposito(conta1, 1000)

            case "7": # Saque
                banco.saque(conta1, 11)
            
            case "8": # Extrato
                banco.exibir_extrato(conta1)

            case "0": # Sair
                print("Sair")
                break

            case _:
                print("Opção inválida")
                carregando(2,0.1,"Carregando")


    # cliente1 = banco.adicionar_cliente("Fulano", "123.456.789-00")
    # cliente2 = banco.adicionar_cliente("Beltrano", "111.111.111-81")
    # # banco.listar_clientes()
    # conta1 = banco.adicionar_conta(cliente1,"1234-5")
    # conta2 = banco.adicionar_conta(cliente2,"1234-6")
    # # banco.listar_contas()

    # banco.deposito(conta1, 1000)
    # banco.saque(conta1, 11)


    # banco.deposito(conta2, 9999)
    # banco.saque(conta2, 557.5)

    # # banco.exibir_saldo(conta1)
    # # banco.exibir_saldo(conta2)

    # banco.exibir_extrato(conta2)

if __name__ == '__main__':
    main()