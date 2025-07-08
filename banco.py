# Constantes
LIMITE_SAQUE: float = 500
LIMITE_SAQUES_DIARIOS: int = 3

# Variáveis do sistema
saldo: float = 0
extrato: list[str] = []
numero_saques: int = 0

def menu() -> str:
    print("\n====== MENU ======")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def realizar_deposito(saldo: float, extrato: list[str], valor: float) -> tuple[float, list[str]]:
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido. Depósitos devem ser positivos.")
    return saldo, extrato

def realizar_saque(
    saldo: float, 
    extrato: list[str], 
    numero_saques: int, 
    valor: float
) -> tuple[float, list[str], int]:
    
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("❌ Limite de saques diários atingido.")
    elif valor <= 0:
        print("❌ Valor inválido. Saques devem ser positivos.")
    elif valor > LIMITE_SAQUE:
        print(f"❌ Limite de R$ {LIMITE_SAQUE:.2f} por saque excedido.")
    elif valor > saldo:
        print("❌ Saldo insuficiente para saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque:     R$ {valor:.2f}")
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo: float, extrato: list[str]) -> None:
    print("\n====== EXTRATO ======")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("======================")

# Loop principal
while True:
    opcao = menu()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = realizar_deposito(saldo, extrato, valor)
        except ValueError:
            print("❌ Entrada inválida. Digite um número.")
    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques, valor)
        except ValueError:
            print("❌ Entrada inválida. Digite um número.")
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "4":
        print("👋 Obrigado por usar o sistema bancário. Até logo!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")

