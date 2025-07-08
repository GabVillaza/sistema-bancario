# Constantes
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3

# Variáveis do sistema
saldo = 0
extrato = []
numero_saques = 0

def menu():
    print("\n===== MENU =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def realizar_deposito(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        print("❌ Entrada inválida. Tente novamente com um número.")
        return saldo, extrato

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido. Depósitos devem ser positivos.")
    
    return saldo, extrato

def realizar_saque(saldo, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("❌ Limite de saques diários atingido.")
        return saldo, extrato, numero_saques

    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        print("❌ Entrada inválida. Tente novamente com um número.")
        return saldo, extrato, numero_saques

    if valor <= 0:
        print("❌ Valor inválido. Saques devem ser positivos.")
    elif valor > LIMITE_SAQUE:
        print(f"❌ Limite de R$ {LIMITE_SAQUE:.2f} por saque excedido.")
    elif valor > saldo:
        print("❌ Saldo insuficiente para saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================")

# Loop principal
while True:
    opcao = menu()

    if opcao == "1":
        saldo, extrato = realizar_deposito(saldo, extrato)

    elif opcao == "2":
        saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques)

    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        print("👋 Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")


