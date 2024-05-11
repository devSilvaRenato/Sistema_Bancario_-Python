#V1

def menu():
    menu = '''
            ================= MENU ==================
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Nova Conta
            [5] - Novo usuario
            [6] - Listar Contas
            [0] - Sair
            =========================================
                Obrigado por usar nosso sistema!
                
Digite a sua opcao: '''
    return int(input(menu))


def depositar(valor_deposito, saldo, extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito concluído")
    else:
        print("Valor digitado inválido. Por favor, refaça a operação.")
        
    return saldo, extrato
        
    
        
def saque(valor_saque, saldo, limite_valor, extrato, numero_saques, limites_saques):
    if valor_saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente")
    elif valor_saque > limite_valor:
        print("Operação falhou! O valor do saque excede o limite")
    elif numero_saques >= limites_saques:
        print("Operação falhou! Número máximo de saques excedido")
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque concluído")
        
    else: 
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques
        
def funcao_extrato(saldo, /,*, extrato):
    print("============= Extrato =============")
    print(f"Saldo: R$ {saldo:.2f}\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("==================================")
    
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente Numeros): ')
    cpf_do_usuario = verifica_usuario(cpf, usuarios)
    
    if cpf_do_usuario:
        print("Ja existe usuartio com esse CPF! \n")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    


def criar_conta(agencia,contas,usuarios):
    numero_conta = len(contas) + 1
    cpf = input('Informe o CPF (Somente Numeros): ')
    usuario = verifica_usuario(cpf, usuarios)
    
    if usuario:
        print("*** Conta criada com Sucesso! *** \n")
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("Usuario nao encontrando, fluxo de criacao de conta encerrado! ")
    
    return
    
def verifica_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        
        Agencia:{conta['agencia']}
        Agencia:{conta['numero_conta']}
        Agencia:{conta['usuario']['nome']}
        =================================================
        
        """
        print(linha)



def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == 1:
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor_deposito, saldo, extrato)
            
        elif opcao == 2:
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                valor_saque=valor_saque,
                saldo=saldo,
                limite_valor=limite,
                extrato=extrato,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES
            )
            
        elif opcao == 3:
            
            funcao_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criar_usuario(usuarios)
            print(usuarios)
        elif opcao == 5:
            
            conta = criar_conta(AGENCIA, contas, usuarios)
            print(contas)
        elif opcao == 6: 
            listar_contas(contas)
            
        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada.")
            
            
main()