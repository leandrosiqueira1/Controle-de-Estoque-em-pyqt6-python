import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QFrame, QFormLayout, QCheckBox, QMessageBox, QStyle
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *
from Database import Database
from cadastroUsuario import TelaUsuario

class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Definição das cores usadas na interface
        self.corVerdeEscuro = "#1D6373"  # Cor verde escuro
        self.corVerdeclaro1 = "#378C74"  # Verde mais claro
        self.corVerdeclaro2 = "#49A671"  # Verde ainda mais claro
        self.corButton = "#3084F2"  # Cor dos botões entrar 
        self.corBranco = "#F2F2F2"       # Cor branca para fundo
        self.corEsqForm = "#222602" #Cor do lado esquerdo do formulário
        self.corDirForm = "#DCF230" #Cor do lador direito do formulario
        self.corTitle = "#000000" 
        self.corBtnHover = "#2BAFF5" #cor do botao ao passar o mauser hover

        self.initUI()

    def initUI(self):
        # Configurações da janela
        self.setWindowTitle("Tela de Login")
        self.setFixedSize(1280, 800)

        # Layout principal
        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout do formulário
        self.frameFundo = QFrame(self)
        self.frameFundo.setFixedSize(500, 450)

        layoutForm = QVBoxLayout(self.frameFundo)
        layoutForm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Título do formulário
        labelTitulo = QLabel("Login", self)
        labelTitulo.setStyleSheet("""
                QLabel{
                    color: #000000;
                    padding: 10px 5px;
                    font-size: 25px;                 
            }
        
        """)

        labelTitulo.setFont(QFont("Roboto", 25, QFont.Weight.Bold))
        labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutForm.addWidget(labelTitulo)

        # Campo de email
        labelEmail = QLabel("Seu e-mail", self)
        labelEmail.setStyleSheet("""
                QLabel{
                    color: #000000;
                    padding: 5px 5px 2px 2px;
                    font-size: 18px;
                                  
            }
        
        """)
        layoutForm.addWidget(labelEmail)

        self.campoEmail = QLineEdit(self)
        self.campoEmail.setPlaceholderText("Digite seu e-mail")
        layoutForm.addWidget(self.campoEmail)

        # Campo de senha
        labelSenha = QLabel("Sua senha", self)
        labelSenha.setStyleSheet("""
                QLabel{
                    color: #000000;
                    padding: 5px 5px 2px 5px;
                    font-size: 18px;
                                  
            }
        
        """)
        layoutForm.addWidget(labelSenha)

        self.campoSenha = QLineEdit(self)
        self.campoSenha.setPlaceholderText("Digite sua senha")
        self.campoSenha.setEchoMode(QLineEdit.EchoMode.Password)
        layoutForm.addWidget(self.campoSenha)

        # Checkbox "Manter-me logado"
        self.checkboxLembrar = QCheckBox("Manter-me logado", self)
        self.checkboxLembrar.setStyleSheet("""
                QCheckBox{
                    background-color: #ffffff;
                    padding: 8px;
                    border-radius: 5px;
            }
        """)
        layoutForm.addWidget(self.checkboxLembrar)

        # Botão de login
        self.btnEntrar = QPushButton("Logar", self)
        self.btnEntrar.setFixedHeight(40)
        self.btnEntrar.setStyleSheet("""
            QPushButton {
                background-color: #3084F2;
                color: white;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2BAFF5;
            }
        """)
        layoutForm.addWidget(self.btnEntrar)

        # Texto para registro
        layoutForm.addSpacing(5)
        layoutCadastro = QHBoxLayout()
        layoutCadastro.addStretch()
        labelCadastro = QLabel("Ainda não tem conta?", self)
        labelCadastro.setStyleSheet("color: #00000;")
        labelCadastro.setFont(QFont("Arial", 12))
       
        btnCadastro = QPushButton("Cadastre-se", self)
        btnCadastro.setStyleSheet("color: #3084F2; background: transparent; border: none; text-decoration: underline;")
        btnCadastro.clicked.connect(self.realizarCadastro)

        layoutCadastro.addWidget(labelCadastro)
        layoutCadastro.addWidget(btnCadastro)
        layoutCadastro.addStretch()

        layoutForm.addLayout(layoutCadastro)

        # Estilo CSS para o formulário
        self.setStyleSheet("""
            QWidget {
                background-color: #Dcf230 ;
            }
            QLabel {
                color: #1D6373;
                font-size: 14px;
                padding: 8px 2px;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #1D6373;
                padding: 8px 2px;
                border-radius: 5px;
                font-size: 14px;
            }
            QCheckBox {
                font-size: 12px;
                color: #1D6373;
            }
            QFrame {
                background-color: #F2F2F2;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        layoutPrincipal.addWidget(self.frameFundo)

    def realizarLogin(self):
        username = self.campoEmail.text()
        password = self.campoSenha.text()
        db = Database('estoque.db')
        user = db.checkLogin(username, password)
        if user:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválida!")

    def abrirDialogoRecuperacaoSenha(self):
        QMessageBox.information(self, "Recuperação de Senha", "Instruções de recuperação enviadas para o seu e-mail!")

    def realizarCadastro(self):
        print("Cadastro realizado com sucesso!")
        self.cadastroUsuario = TelaUsuario()
        self.cadastroUsuario.show()
        self.hide()


# Criar a aplicação PyQt6
app = QApplication(sys.argv)

# Criar a janela de login
login_window = TelaPrincipal()
login_window.show()

# Executar o loop de eventos
sys.exit(app.exec())
