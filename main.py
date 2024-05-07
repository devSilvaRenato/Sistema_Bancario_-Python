#V1
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = '''

        ================= MENU ==================
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [0] - Sair
        =========================================
            Obrigado por usar nosso sistema!
'''


while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Depósito concluído")
        else:
            print("Valor digitado inválido. Por favor, refaça a operação.")

    elif opcao == 2:
        valor_saque = float(input("Informe o valor do saque: "))

        if valor_saque > saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        elif valor_saque > limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print("Saque concluído")
        else: 
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("============= Extrato =============")
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("==================================")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")
