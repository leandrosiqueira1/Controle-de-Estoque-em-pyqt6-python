import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

# Tabela usuarios para armazenar dados dos usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_nascimento DATE DEFAULT CURRENT_DATE
);
''')

# Tabela entrada_produto para armazenar dados de entrada de produto
cursor.execute('''
CREATE TABLE IF NOT EXISTS entrada_produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    unidade TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade REAL NOT NULL,
    nfe TEXT NOT NULL,
    dataEmissaoNfe DATE DEFAULT CURRENT_DATE,
    dataCadastroNfe DATE DEFAULT CURRENT_DATE,
    fornecedor TEXT NOT NULL
);
''')

# Tabela fornecedor para armazenar dados dos fornecedores
cursor.execute('''
CREATE TABLE IF NOT EXISTS fornecedor (
    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,  
    nome_empresa TEXT NOT NULL,                      
    cnpj_cpf TEXT NOT NULL,                         
    endereco TEXT,                                   
    numero TEXT,                                     
    bairro TEXT,                                    
    cidade TEXT,                                     
    complemento TEXT,                                
    uf TEXT,                                         
    inscricao_estadual TEXT,                         
    data_cadastro DATE DEFAULT CURRENT_DATE,         
    telefone_celular TEXT,                           
    email TEXT                                       
);
''')

# Tabela categoria para categorizar produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,  
    categoria TEXT NOT NULL
);
''')

# Tabela unidade para unidades de medida dos produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS unidade (
    id_unidade INTEGER PRIMARY KEY AUTOINCREMENT,    
    unidade TEXT NOT NULL
);
''')

# Tabela produto para armazenar dados dos produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,    
    nome_produto TEXT NOT NULL,                      
    id_unidade INTEGER,                              
    id_categoria INTEGER,                            
    data_cadastro DATE DEFAULT CURRENT_DATE,         
    usuario TEXT,                                    
    FOREIGN KEY (id_unidade) REFERENCES unidade(id_unidade),  
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);
''')

# Tabela registro_modificacoes para registrar modificações nas entradas e saídas de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS registro_modificacoes (
    id_modificacao INTEGER PRIMARY KEY AUTOINCREMENT,  
    id_entrada INTEGER,                                
    id_saida INTEGER,                                  
    data_modificacao DATE DEFAULT CURRENT_DATE,        
    tipo_modificacao TEXT,                             
    FOREIGN KEY (id_entrada) REFERENCES entrada_produto(id_produto),  
    FOREIGN KEY (id_saida) REFERENCES produto(id_produto)
);
''')

conexao.commit()
conexao.close()

