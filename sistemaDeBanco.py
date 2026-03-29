import sys

usuarios = {}
tentativa = 0
limite = 3

print("1 - Criar conta")
print("2 - Sair")

opcEscolhida = int(input("Escolha uma opção: "))

if opcEscolhida == 1:

    create_usuario = input("Criar nome de usuário: ")

    if create_usuario in usuarios:
        print("Esse usuário já existe!")

    else:
        create_password = input("Criar senha: ")

        usuarios[create_usuario] = {
            "senha": create_password,
            "saldo": 1000
        }

        print("\nConta criada com sucesso!")
        print("0 - Fazer login")
        print("1 - Sair")

        c_s = int(input("Deseja continuar? "))

        if c_s == 0:

            while tentativa < limite:

                usuario = input("\nUsuário: ")
                senha = input("Senha: ")

                if usuario in usuarios and senha == usuarios[usuario]["senha"]:

                    print("Login realizado com sucesso!")

                    saldo = usuarios[usuario]["saldo"]

                    print(f"\nSaldo atual: R$ {saldo}")
                    print("1 - Sacar")
                    print("2 - Depositar")

                    fzr = int(input("O que deseja fazer? "))

                    if fzr == 1:
                        valor_de_saque = int(input("Quanto deseja sacar? "))

                        if valor_de_saque > saldo:
                            print("Saldo insuficiente!")

                        else:
                            saldo -= valor_de_saque
                            usuarios[usuario]["saldo"] = saldo
                            print(f"Saque realizado! Novo saldo: {saldo}")

                    elif fzr == 2:
                        valor_de_deposito = int(input("Quanto deseja depositar? "))

                        saldo += valor_de_deposito
                        usuarios[usuario]["saldo"] = saldo

                        print(f"Depósito realizado! Novo saldo: {saldo}")

                    break

                else:
                    tentativa += 1
                    print(f"Login incorreto! Tentativas restantes: {limite - tentativa}")

                    if tentativa == limite:
                        print("Conta bloqueada!")

elif opcEscolhida == 2:
    print("Saindo do sistema...")
    