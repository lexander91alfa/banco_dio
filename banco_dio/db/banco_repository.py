import sqlite3

DATABASE = 'banco_dio/db/banco.db'

def criar_tabela():
   
   with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                tipo TEXT NOT NULL,
                valor REAL NOT NULL,
                conta_id INTEGER NOT NULL,
                constraint check_tipo check (tipo in ('saque', 'deposito')),
                FOREIGN KEY (conta_id) REFERENCES contas (id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                data_nascimento DATE NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL UNIQUE,
                saldo REAL NOT NULL,
                usuario_id INTEGER NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            );
        """)

        conn.commit()

def salvar_transacao(tipo: str, valor: float, conta_id: int) -> None:
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
    
            cursor.execute("""
                INSERT INTO transacoes (data, tipo, valor, conta_id) VALUES (date('now'), ?, ?, ?);
            """, (tipo, valor, conta_id))
    
            conn.commit()

def inserir_usuario(nome: str, cpf: str, data_nascimento: str) -> None:
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nome, cpf, data_nascimento) VALUES (?, ?, ?);
        """, (nome, cpf, data_nascimento))

        conn.commit()

def criar_conta(numero: int, saldo: float, usuario_id: int) -> None:
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO contas (numero, saldo, usuario_id) VALUES (?, ?, ?);
        """, (numero, saldo, usuario_id))

        conn.commit()

def listar_contas() -> list:
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
    
            cursor.execute("""
                SELECT * FROM contas;
            """)
    
            contas = cursor.fetchall()
    
            return contas
        
def buscar_conta(numero: int) -> tuple:
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
    
            cursor.execute("""
                SELECT * FROM contas WHERE numero = ?;
            """, (numero,))
    
            conta = cursor.fetchone()
    
            return conta

def buscar_usuario(cpf: str) -> tuple:
            
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
        
                cursor.execute("""
                    SELECT * FROM usuarios WHERE cpf = ?;
                """, (cpf,))
        
                usuario = cursor.fetchone()
        
                return usuario
            
def listar_transacoes() -> list:
     with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT transacoes.data, transacoes.tipo, transacoes.valor FROM transacoes
        """)

        transacoes = cursor.fetchall()

        return transacoes
     
def atualizar_saldo(saldo: float, conta_id: int) -> None:
     with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE contas SET saldo = ? WHERE id = ?;
        """, (saldo, conta_id))

        conn.commit()
          
          
