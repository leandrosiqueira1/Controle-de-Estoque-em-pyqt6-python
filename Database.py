import sqlite3

class Database:
    def __init__(self, db_name):
        """Inicializa a classe com o nome do banco de dados."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados e cria um cursor."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Conectado ao banco de dados: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados fechada.")
    
    def create_table(self, table_name, columns):
        """Cria uma tabela no banco de dados com o nome e as colunas especificadas."""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        try:
            self.cursor.execute(query)
            self.conn.commit()  # Comita a transação
            print(f"Tabela '{table_name}' criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
    
    def execute_query(self, query, params=()):
        """Executa uma consulta SQL no banco de dados (como INSERT, UPDATE, DELETE)."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Consulta executada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao executar consulta: {e}")
    
    def fetch_all(self, query, params=()):
        """Executa uma consulta SELECT e retorna todos os resultados."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar dados: {e}")
            return []
        
    def checkLogin(self, username, password):
        conn = self.connect()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (username, password))
            user = cursor.fetchone()
            conn.close()
            return user
        return None
    
    def salvarProduto(self, produto, unidade, categoria):
        try:
            query = '''
                INSERT INTO produto (nome_produto, id_unidade, id_categoria, data_cadastro, usuario)
                VALUES (?, (SELECT id_unidade FROM unidade WHERE unidade = ?), (SELECT id_categoria FROM categoria WHERE categoria = ?), CURRENT_DATE, ?)
            '''
            self.cursor.execute(query, (produto, unidade, categoria, "Usuário"))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao salvar produto: {e}")
            return False
        
    def salvarFornecedor(self, nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, data_cadastro, telefone_celular, email):
        try:
            query = '''
                INSERT INTO fornecedor (nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, data_cadastro, telefone_celular, email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            self.cursor.execute(query, (nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, data_cadastro, telefone_celular, email))
            self.conn.commit()
            print("Fornecedor salvo com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao salvar fornecedor: {e}")
            return False
