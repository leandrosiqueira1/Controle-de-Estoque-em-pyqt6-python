import sqlite3

class Database:
    def __init__(self, db_name="estoque.db"):
        """Inicializa a classe com o nome do banco de dados."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados e cria um cursor."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=()):
        """Executa uma consulta SQL no banco de dados (INSERT, UPDATE, DELETE)."""
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao executar consulta: {e}")
            return False
        finally:
            self.close()

    def fetch_all(self, query, params=()):
        """Executa uma consulta SELECT e retorna todos os resultados."""
        try:
            self.connect()
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar dados: {e}")
            return []
        finally:
            self.close()

    def checkLogin(self, email, senha):
        """Verifica se o usuário existe no banco de dados."""
        self.connect()
        self.cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        user = self.cursor.fetchone()
        self.close()
        return user

    def salvarProduto(self, produto, unidade, categoria, usuario):
        """Salva um novo produto no banco de dados."""
        query = '''
            INSERT INTO produto (nome_produto, id_unidade, id_categoria, data_cadastro, usuario) 
            VALUES (?, ?, ?, CURRENT_DATE, ?)
        '''
        return self.execute_query(query, (produto, unidade, categoria, usuario))

    def salvarFornecedor(self, nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, telefone_celular, email):
        """Salva um novo fornecedor no banco de dados."""
        query = '''
            INSERT INTO fornecedor (nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, telefone_celular, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        return self.execute_query(query, (nome_empresa, cnpj_cpf, endereco, numero, bairro, cidade, complemento, uf, inscricao_estadual, telefone_celular, email))

    def salvarUsuario(self, nome, sobrenome, usuario, email, senha, dataNascimento):
        """Salva um novo usuário no banco de dados."""
        query = '''
            INSERT INTO usuarios (nome, sobrenome, usuario, email, senha, data_nascimento) 
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        return self.execute_query(query, (nome, sobrenome, usuario, email, senha, dataNascimento))

    def adicionar_categoria(self, categoria):
        """Adiciona categoria ao banco de dados."""
        query = '''
            INSERT INTO categoria(categoria) VALUES (?)
        '''
        return self.execute_query(query, (categoria,))


    def verificar_email_existente(self, email):
        """Verifica se um email já está cadastrado no banco"""
        self.connect()
        self.cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        existe = self.cursor.fetchone() is not None
        self.close()
        return existe

    def adicionar_usuario(self, nome, sobrenome, usuario, email, senha, dataNascimento):
        """Adiciona um novo usuário ao banco de dados."""
        if self.verificar_email_existente(email):
            print("E-mail já cadastrado.")
            return False
        return self.salvarUsuario(nome, sobrenome, usuario, email, senha, dataNascimento)
    
    def buscar_produtos(self, categoria=None, busca=None):
        """Retorna todos os produtos filtrados por categoria e/ou nome."""
        query = "SELECT nome, categoria, preco FROM produtos WHERE 1=1"
        params = []

        if categoria and categoria != "Todos":
            query += " AND categoria = ?"
            params.append(categoria)

        if busca:
            query += " AND nome LIKE ?"
            params.append(f"%{busca}%")

        return self.fetch_all(query, tuple(params))
    
    
    def salvarEntradaProduto(self, produto, unidade, categoria, quantidade, nfe, dataEmissao, dataCadastro, fornecedor):
    #Salva a entrada de um produto no banco de dados.
        query = '''
            INSERT INTO entrada_produto (produto, unidade, categoria, quantidade, nfe, dataEmissaoNfe, dataCadastroNfe, fornecedor)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        return self.execute_query(query, (produto, unidade, categoria, quantidade, nfe, dataEmissao, dataCadastro, fornecedor))
    

    def buscar_unidades(self):
    #Busca todas as unidades cadastradas no banco de dados."""
        query = "SELECT unidade FROM unidade"
        return self.fetch_all(query)
        

    def buscar_categorias(self):
        #Busca todas as categorias cadastradas no banco de dados."""
        query = "SELECT categoria FROM categoria"
        return self.fetch_all(query)

    def buscar_produtos(self):
        #Busca todos os produtos cadastrados no banco de dados."""
        query = "SELECT nome_produto FROM produto"
        return self.fetch_all(query)
    

