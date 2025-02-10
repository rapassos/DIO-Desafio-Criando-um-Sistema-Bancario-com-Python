from time import sleep # Importando a função sleep do módulo time

#Definição de Variáveis
nome_banco = "Rapassos Bank"
saldo = float(0);
limite_saque = 500;
max_saque = 3;
conta_saque = 0;
extrato = [];


menu_tela = f"""
Bem vindo ao {nome_banco}!

    Escolha uma opção:
    
    1 - Exibir saldo
    2 - Depositar
    3 - Sacar
    4 - Exibir extrato
    5 - Sair

Digite o número da opção desejada:"""

#Definição de Funções
def menu():
    return input(menu_tela)


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

def exibir_saldo():
    print(f"Seu saldo é de R${saldo:.2f}")
    carregando(2,0.1,"Carregando")

def deposito():
    global saldo
    valor_deposito = float(input("Digite o valor do depósito: R$"))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Depósito de R${valor_deposito:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")
    carregando(2,0.1,"Carregando")

def saque():
    global saldo
    global max_saque
    global conta_saque
    valor_saque = float(input("Digite o valor do saque: R$"))
    if conta_saque < max_saque:     
        if valor_saque > 0:
            if saldo >= valor_saque:
                if valor_saque > limite_saque:
                    print(f"Valor solicitado acima do seu limite por saque R${limite_saque:.2f}")
                else:
                    conta_saque += 1
                    saldo -= valor_saque
                    extrato.append(f"Saque de R${valor_saque:.2f}")
                    print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor inválido!")
    else:
        print("Limite de saques diários atingido!")
    carregando(2,0.1,"Carregando")

def exibir_extrato():
    print("Extrato:")
    for item in extrato:
        print(item)
    print(f"Saldo atual: R${saldo:.2f}")
    carregando(2,0.1,"Carregando")


#Fluxo de execução
while True:
    opt = menu()

    match opt:
        case "1":
            exibir_saldo()

        case "2":
            deposito()

        case "3":
            saque()
        
        case "4":
            exibir_extrato()
        
        case "5":
            print("Sair")
            break
        
        case _:
            print("Opção inválida")
            carregando(2,0.1,"Carregando")
            