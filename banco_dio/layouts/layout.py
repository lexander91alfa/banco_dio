from datetime import datetime
from typing import List

menu_principal = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

Escolha uma das opções acima: """


def extrato_dinamico(transacoes: List[str], saldo: float) -> str:
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

    return extrato


