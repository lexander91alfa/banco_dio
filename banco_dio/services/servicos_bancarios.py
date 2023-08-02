from banco_dio.db.banco_repository import salvar_transacao, buscar_conta, listar_contas, inserir_usuario, criar_conta, buscar_usuario, listar_transacoes


def nova_conta(numero: int, saldo: float, cpf: str) -> bool:
    usuario = buscar_usuario(cpf)

    if usuario is None:
        print("Usuário não encontrado, favor cadastrar antes de criar uma conta!")
        return False
    
    criar_conta(numero, saldo, usuario[0])
    return True

def listar_contas_service() -> list:
    return listar_contas()

def inserir_usuario_service(nome: str, cpf: str, data_nascimento: str) -> None:
    inserir_usuario(nome, cpf, data_nascimento)

def login(numero_conta: int) -> tuple:

    conta = buscar_conta(numero_conta)

    if conta is None:
        print("Conta não encontrada!")
        return None

    return conta

def sacar(numero_conta: int, valor: float) -> None:
    conta = buscar_conta(numero_conta)

    if conta is None:
        print("Conta não encontrada!")
        return

    if valor > conta[1]:
        print("Saldo insuficiente!")
        return

    if valor > 500:
        print("Valor máximo por saque é de R$ 500,00!")
        return

    if conta[2] == 3:
        print("Limite máximo de saques diários atingido!")
        return

    conta[1] -= valor
    conta[2] += 1

    salvar_transacao("saque", valor, conta[0])

    print(f"Saque realizado com sucesso! Saldo atual: R$ {conta[1]}")

def depositar(numero_conta: int, valor: float) -> None:
    conta = buscar_conta(numero_conta)

    if conta is None:
        print("Conta não encontrada!")
        return

    conta[1] += valor

    salvar_transacao("deposito", valor, conta[0])

    print(f"Depósito realizado com sucesso! Saldo atual: R$ {conta[1]}")

def listar_transacoes(numero_conta: int) -> list:
    conta = buscar_conta(numero_conta)

    if conta is None:
        print("Conta não encontrada!")
        return

    transacoes_fomatadas = []

    transacoes = listar_transacoes(conta[0])

    if any(transacoes) is False:
        return []

    for trasancao in transacoes:
        transacoes_fomatadas.append(f"Data: {trasancao[0]} | Tipo: {trasancao[1]} | Valor: R$ {trasancao[2]}")