from banco_dio.db.banco_repository import criar_tabela
from banco_dio.layouts.layout import layout_menu_principal, clear_terminal, layout_menu_login, layout_menu_conta, layout_extrato_dinamico
from banco_dio.services.servicos_bancarios import nova_conta, listar_contas_service, inserir_usuario_service, login, sacar, depositar, listar_transacoes
from time import sleep
from datetime import datetime

conta = None
criar_tabela()

while True:

    opcoes = layout_menu_principal()

    match opcoes:
        case "nc":
            print("Opção escolhida: Nova conta")
            
            while True:
                
                cpf = input("Digite o CPF do usuário: ")

                match cpf:

                        case cpf if len(cpf) != 11:
                            print("CPF inválido!")
                            sleep(2)
                            clear_terminal()
                            continue
                        case _:
                            conta_criada = nova_conta(cpf)

                            if conta_criada:
                                print("Conta criada com sucesso!")
                                sleep(2)
                                break
                            else:
                                print("CPF não encontrado!")
                                sleep(2)
                                break
                            
                            
        case "lc":
            print("Opção escolhida: Listar contas")

            contas = listar_contas_service()

            if any(contas) is False:
                print("Nenhuma conta encontrada!")
                sleep(2)
                continue
        
            for conta in contas:
                print(f"Conta: {conta[1]} | Saldo: R$ {conta[2]}")

            sleep(2)

        case "nu":
            print("Opção escolhida: Novo usuário")

            while True:

                while True:
                
                    cpf = input("Digite o CPF do usuário: ")
                
                    match cpf:
                        case cpf if len(cpf) != 11:
                            print("CPF inválido!")
                            sleep(2)
                            clear_terminal()
                            continue
                        case _:
                            break
                
                while True:

                    nome = input("Digite o nome do usuário: ")
                
                    match nome:

                        case nome if len(nome) < 3 or nome.isnumeric() is True or len(nome) > 255:
                            print("Nome inválido!")
                            sleep(2)
                            clear_terminal()
                            continue
                        case _:
                            break
                
                while True:

                    data_nascimento = input("Digite a data de nascimento do usuário: ")

                    try:
                        data = datetime.strptime(data_nascimento, "%d%m%Y")
                    except ValueError:
                        print("Data inválida!")
                        sleep(2)
                        clear_terminal()
                        continue

                    match data:
                        case data if data > datetime.now():
                            print("Data inválida!")
                            sleep(2)
                            clear_terminal()
                            continue
                        case _:
                            break

                inserir_usuario_service(nome, cpf, data.strftime("%Y-%m-%d"))
                print("Usuário cadastrado com sucesso!")
                sleep(2)
                break
        
        case "s":
            print("Opção escolhida: Serviços")

            try:
                numero_conta = int(layout_menu_login())
                conta = login(numero_conta)
            except ValueError:
                print("Valor inválido!")
                continue

            if conta:
                print("Login realizado com sucesso!")
                sleep(2)
                clear_terminal()
            else:
                print("Conta não encontrada!")
                sleep(2)
                continue

            while True:

                opcoes_servicos = layout_menu_conta()

                match opcoes_servicos:
                    case "d":
                        print("Opção escolhida: Depósito")

                        while True:
                            try:
                                valor = float(input("Digite o valor do depósito: "))
                            except ValueError:
                                print("Valor inválido!")
                                continue

                            match valor:
                                case valor if valor <= 0:
                                    print("Valor inválido!")
                                    continue
                                case _:
                                    pass

                            depositar(conta[0], valor)
                            print("Depósito de R$ {valor} realizado com sucesso!")
                            sleep(2)
                            break
                    
                    case "s":
                        print("Opção escolhida: Saque")

                        while True:
                            try:
                                valor = float(input("Digite o valor do saque: "))
                            except ValueError:
                                print("Valor inválido!")
                                continue

                            match valor:
                                case valor if valor <= 0:
                                    print("Valor inválido!")
                                    continue
                                case _:
                                    pass

                            sacar(conta[0], valor)
                            print("Saque de R$ {valor} realizado com sucesso!")
                            sleep(2)
                            break
                    
                    case "e":
                        print("Opção escolhida: Extrato")

                        transacoes = listar_transacoes(conta[0])

                        extrato = layout_extrato_dinamico(transacoes)

                        print(extrato)
                        sleep(5)
                        continue


        case "q":
            print("Opção escolhida: Sair")
            print("Saindo...")
            sleep(2)
            clear_terminal()
            
            print("Obrigado por utilizar o Banco DIO S.A.!")

            sleep(3)
            clear_terminal()
            exit()
        
        case _:
            print("Opção inválida!")
            sleep(2)