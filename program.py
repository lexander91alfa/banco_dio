from banco_dio.layouts.layout import menu_principal, extrato_dinamico
from datetime import datetime

saldo = 0
transacoes = []
numero_saques = 1
VALOR_MAXIMO_POR_SAQUE = 500
LIMITE_MAXIMO_SAQUES_DIA = 3

while True:

    opcao = input(menu_principal)

    match opcao:
        case "d":
            print("Opção escolhida: Depositar")

            while True:

                valor_deposito = float(input("Digite o valor do depósito: "))

                match valor_deposito:
                    case valor_deposito if valor_deposito <= 0:
                        print("Valor inválido!")
                        continue
                    case _:
                        saldo += valor_deposito
                        transacoes.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Depósito: R$ {valor_deposito}")
                        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo}")
                        break

        case "s":
            print("Opção escolhida: Sacar")

            if numero_saques > LIMITE_MAXIMO_SAQUES_DIA:
                print("Limite de saques diários atingido!")
                continue
            elif saldo == 0:
                print("Saldo insuficiente!")
                continue

            while True:
                try:
                    valor_saque = float(input("Digite o valor do saque: "))
                except ValueError:
                    print("Valor inválido!")
                    continue

                match valor_saque:
                    case valor_saque if valor_saque <= 0:
                        print("Valor inválido!")
                        continue
                    case valor_saque if valor_saque > saldo:
                        print("Saldo insuficiente!")
                        continue
                    case valor_saque if valor_saque > VALOR_MAXIMO_POR_SAQUE:
                        print("Valor máximo por saque é de R$ 500,00!")
                        continue
                    case _:
                        saldo -= valor_saque
                        transacoes.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Saque: R$ {valor_saque}")
                        numero_saques += 1
                        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo}")
                        break
        
        case "e":
            print("Opção escolhida: Extrato")

            if any(transacoes) is False:
                print("Não há movimentações!")
                continue

            extrato_atual = extrato_dinamico(transacoes, saldo)
            print(extrato_atual)
        
        case "q":
            print("Opção escolhida: Sair")
            break

        case _:
            print("Opção inválida!")