from datetime import datetime
from typing import List
import textwrap

def layout_menu_principal() -> str:
    header = f"Ben-vindo ao menu principal - Banco DIO S.A. - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    tamanho_header = len(header)


    menu =  f"""
        {header}

        {'-' * tamanho_header}

        O que gostaria de fazer hoje?
            
        [nc] - Nova conta
        [lc] - Listar contas
        [nu] - Novo usuário
        [s] - Serviços
        [q] - Sair

        Escolha uma das opções acima: """

    clear_terminal()
    return input(textwrap.dedent(menu))

def layout_menu_login() -> str:
    header = f"Ben-vindo ao menu de login - Banco DIO S.A. - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    tamanho_header = len(header)


    menu =  f"""
        {header}

        {'-' * tamanho_header}

        Digite o número da conta: """

    clear_terminal()
    return input(textwrap.dedent(menu))

def layout_menu_conta() -> str:
    header = f"Ben-vindo ao menu de serviços do Banco DIO S.A. - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    tamanho_header = len(header)


    menu =  f"""
        {header}

        {'-' * tamanho_header}

        O que gostaria de fazer hoje?
            
        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Sair

        Escolha uma das opções acima: """

    clear_terminal()
    return input(textwrap.dedent(menu))

def layout_extrato_dinamico(transacoes: List[str], saldo: float) -> str:
    header = f"Extrato bancário - Banco DIO S.A. - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    tamanho_header = len(header)

    transacoes_extrato = '\n'.join(transacoes)

    extrato = f"""
    {header}
    {'-' * tamanho_header}
    Transações:

    {transacoes_extrato}

    Saldo atual: R$ {saldo}

    {'-' * tamanho_header}
    """
    clear_terminal()
    return input(textwrap.dedent(extrato))


def clear_terminal() -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')