import sqlite3
from tkinter import messagebox

class BancoDeDados:
    def __init__(self, nome_bd="controle_de_estoque.db"):
        self.nome_bd = nome_bd
        self.criar_tabelas()
        
    def executar_comando(self, comando, parametros=()):
        try:
            with sqlite3.connect(self.nome_bd) as conn:
                cursor = conn.cursor()
                cursor.execute(comando, parametros)
                conn.commit()
                return cursor.fetchall()
        except sqlite3.DatabaseError as e:
            messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro ao acessar o banco de dados: {e}")
            return []
        except Exception as e:
            messagebox.showerror("Um erro inesperado aconteceu", f"Detalhes do erro: {e}")
            return []

    def verificar_existencia(self, nome, fornecedor):
        resultado = self.executar_comando("SELECT COUNT(*) FROM produtos WHERE nome = ? AND fornecedor = ?", (nome, fornecedor))
        count = resultado[0][0] if resultado else 0
        return count > 0

    def criar_tabelas(self):
        self.executar_comando(''' 
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,  
                preco REAL NOT NULL,           
                quantidade INTEGER NOT NULL,
                fornecedor TEXT NOT NULL,
                categoria TEXT NOT NULL
                )                                   
            ''')

    def adicionar_produto(self, nome, preco, quantidade, fornecedor, categoria):
        self.executar_comando("INSERT INTO produtos (nome, preco, quantidade, fornecedor, categoria) VALUES (?,?,?,?,?)",
            (nome, preco, quantidade, fornecedor, categoria))

    def listar_produtos(self):
        return self.executar_comando("SELECT * FROM produtos")


    def excluir_produto(self, produto_id):
        self.executar_comando("DELETE FROM produtos WHERE id = ?", (produto_id,))

    def editar_produto(self, produto_id, nome, preco, quantidade, fornecedor, categoria):
            self.executar_comando(''' 
                UPDATE produtos SET nome = ?, preco = ?, quantidade = ?, fornecedor = ?, categoria = ? 
                WHERE id = ? 
            ''', (nome, preco, quantidade, fornecedor, categoria, produto_id))
