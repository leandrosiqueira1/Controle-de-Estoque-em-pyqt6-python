import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import hashlib  

class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        # Configurações da janela (800x600)
        self.setWindowTitle("Tela de Cadastro")
        self.setFixedSize(1280, 800)

        # Layout principal
        layoutPrincipal = QVBoxLayout()
        self.setLayout(layoutPrincipal)

        # Layout para a imagem (centrada)
        layoutImagem = QHBoxLayout()
        layoutPrincipal.addLayout(layoutImagem)
        layoutImagem.addStretch()

        logo = QLabel()
        logo.setStyleSheet("background-color: transparent;")
        logo.setFixedSize(180, 180)  
    
        logo.setPixmap(QPixmap("img/user-tipo_02_02.png").scaled(150, 150))
        layoutImagem.addWidget(logo) 
        layoutImagem.addStretch() 
        layoutImagem.setAlignment(Qt.AlignmentFlag.AlignHCenter)  

      
        self.frameFundo = QFrame()
        self.frameFundo.setFixedSize(500, 500) 
        layoutForm = QFormLayout(self.frameFundo)
        layoutForm.setContentsMargins(40, 40, 40, 40) 
        layoutForm.setSpacing(20) 

        # Título do formulário
        labelLegenda = QLabel("Cadastro de Usuário")
        labelLegenda.setFont(QFont("Roboto", 24, 600))
        labelLegenda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutForm.addWidget(labelLegenda)

        # Campos do formulário
        labelUsuario = QLabel("Usuário")
        layoutForm.addWidget(labelUsuario)

        self.campoUsuario = QLineEdit()
        self.campoUsuario.setPlaceholderText("Digite seu nome de usuário")
        layoutForm.addWidget(self.campoUsuario)
        

        labelSenha = QLabel("Senha")
        layoutForm.addWidget(labelSenha)

        self.campoSenha = QLineEdit()
        self.campoSenha.setPlaceholderText("Digite sua senha")
        self.campoSenha.setEchoMode(QLineEdit.EchoMode.Password)
        layoutForm.addWidget(self.campoSenha)

        labelConfirmarSenha = QLabel("Confirmar Senha")
        layoutForm.addWidget(labelConfirmarSenha)

        self.campoConfirmarSenha = QLineEdit()
        self.campoConfirmarSenha.setPlaceholderText("Digite novamente a senha")
        self.campoConfirmarSenha.setEchoMode(QLineEdit.EchoMode.Password)
        layoutForm.addWidget(self.campoConfirmarSenha)

        # Botão de cadastro
        self.btnCadastrar = QPushButton("Cadastrar")
        self.btnCadastrar.setFixedHeight(50)
        self.btnCadastrar.setStyleSheet("""
            QPushButton {
                background-color: #1D6373;
                color: white;
                font-size: 18px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #378C74;
            }
        """)
        self.btnCadastrar.clicked.connect(self.realizarCadastro)
        layoutForm.addRow(self.btnCadastrar)

        # Adiciona o QFrame ao layout principal
        layoutPrincipal.addWidget(self.frameFundo, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Estilo CSS para os widgets
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }
            QLabel {
                font-size: 16px;
                color: #333333;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #1D6373;
                padding: 12px;
                border-radius: 10px;
                font-size: 16px;
                height: 35px;
            }
            QFrame {
                background-color: #f2f2f2;
                border-radius: 15px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            }
        """)

    def realizarCadastro(self):
        usuario = self.campoUsuario.text()
        senha = self.campoSenha.text()
        confirmar_senha = self.campoConfirmarSenha.text()

        if not usuario or not senha or not confirmar_senha:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")
            return

        if senha != confirmar_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return

        # Criptografar a senha
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        # Aqui, você pode inserir no banco de dados
        # Exemplo fictício de cadastro (substitua isso por uma função de inserção real no seu banco)
        sucesso = self.cadastrarUsuarioNoBanco(usuario, senha_hash)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar o usuário.")

    def cadastrarUsuarioNoBanco(self, usuario, senha_hash):
        # Função fictícia para cadastrar o usuário no banco de dados.
        # Substitua isso com o código de inserção real no seu banco.
        try:
            # Aqui você faria uma conexão com o banco de dados e faria a inserção
            # Por exemplo, com SQLite:
            # db = Database('estoque.db')
            # db.adicionar_usuario(usuario, senha_hash)
            # db.close()
            return True  # Simula que o cadastro foi bem-sucedido
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            return False
        

# Criar a aplicação PyQt6
if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Criar a janela de cadastro
    cadastro_window = TelaCadastro()
    cadastro_window.show()
    # Executar o loop de eventos
    sys.exit(app.exec())
