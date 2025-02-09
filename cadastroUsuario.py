import sys
import hashlib
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QMessageBox, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from Database import Database

class TelaUsuario(QWidget):
    def __init__(self):
        super().__init__()

        # Cor do formulário
        self.corForm = "#DCF230"

        self.initUI()

    def initUI(self):
        """Inicializa a interface gráfica"""
        self.setWindowTitle("Tela de Cadastro")
        self.setFixedSize(1280, 800)

        # Layout principal para centralizar tudo
        layoutPrincipal = QVBoxLayout()
        layoutPrincipal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layoutPrincipal)

        # Layout centralizado
        layoutCentro = QVBoxLayout()
        layoutCentro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Imagem no topo
        layoutImagem = QHBoxLayout()
        layoutImagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo = QLabel()
        logo.setPixmap(QPixmap("img/user-tipo_02-03.png").scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        layoutImagem.addWidget(logo)

        # Formulário
        self.frameFundo = QFrame()
        self.frameFundo.setFixedSize(600, 700)
        self.frameFundo.setStyleSheet(f"background-color: {self.corForm}; border-radius: 10px;")
        layoutForm = QVBoxLayout(self.frameFundo)
        layoutForm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutForm.setContentsMargins(30, 30, 30, 30)
        layoutForm.setSpacing(8)

        # Título
        labelLegenda = QLabel("Cadastro de Usuário")
        labelLegenda.setFont(QFont("Roboto", 20, 600))
        labelLegenda.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Estilo para os campos de entrada
        estiloCaixaTexto = """
            QLineEdit {
                background-color: white;
                border: 1px solid #888;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
        """

        # Método para criar campos com a label acima
        def criar_campo(label_texto, placeholder):
            layout = QVBoxLayout()
            label = QLabel(label_texto)
            label.setFont(QFont("Roboto", 14))
            campo = QLineEdit()
            campo.setPlaceholderText(placeholder)
            campo.setStyleSheet(estiloCaixaTexto)
            layout.addWidget(label)
            layout.addWidget(campo)
            return layout, campo

        # Criando os campos
        layoutNome,self.campoNome = criar_campo("Nome","Digite seu nome")
        layoutSobreNome,self.campoSobrenome = criar_campo("Sobrenome","Sobrenome")
        layoutUsuario, self.campoUsuario = criar_campo("Usuário", "Digite seu nome de usuário")
        layoutEmail, self.campoEmail = criar_campo("E-mail", "Digite seu e-mail")
        layoutSenha, self.campoSenha = criar_campo("Senha", "Digite sua senha")
        self.campoSenha.setEchoMode(QLineEdit.EchoMode.Password)
        layoutConfirmarSenha, self.campoConfirmarSenha = criar_campo("Confirmar Senha", "Confirme sua senha")
        self.campoConfirmarSenha.setEchoMode(QLineEdit.EchoMode.Password)
        layoutDataNascimento, self.campoDataNascimento = criar_campo("Data de Nascimento", "Digite sua data de nascimento (YYYY-MM-DD)")

        # Botão de cadastro
        self.btnCadastrar = QPushButton("Cadastrar")
        self.btnCadastrar.setFixedHeight(50)
        self.btnCadastrar.setStyleSheet("""
            QPushButton {
                background-color: #3084F2;
                color: white;
                font-size: 14px;
                border-radius: 10px;
                margin-top: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: "#2FC5FB";
            }
        """)
        self.btnCadastrar.clicked.connect(self.realizarCadastro)

        # Adicionando elementos ao layout do formulário
        
        layoutForm.addWidget(labelLegenda)

        layoutForm.addLayout(layoutNome)
        layoutForm.addLayout(layoutSobreNome)
        layoutForm.addLayout(layoutUsuario)
        layoutForm.addLayout(layoutEmail)
        layoutForm.addLayout(layoutSenha)
        layoutForm.addLayout(layoutConfirmarSenha)
        layoutForm.addLayout(layoutDataNascimento)
        layoutForm.addWidget(self.btnCadastrar)

        # Adicionando imagem e formulário ao layout central
        layoutCentro.addLayout(layoutImagem)
        layoutCentro.addWidget(self.frameFundo, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionando espaçadores para centralizar tudo
        layoutPrincipal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layoutPrincipal.addLayout(layoutCentro)
        layoutPrincipal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def realizarCadastro(self):
        nome = self.campoNome.text().strip()
        sobrenome = self.campoSobrenome.text().strip()
        usuario = self.campoUsuario.text().strip()
        email = self.campoEmail.text().strip()
        senha = self.campoSenha.text().strip()
        confirmar_senha = self.campoConfirmarSenha.text().strip()
        data_nascimento = self.campoDataNascimento.text().strip()

        if not usuario or not email or not senha or not confirmar_senha or not data_nascimento:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")
            return

        if senha != confirmar_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return

        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        
        db = Database()
        sucesso = db.adicionar_usuario(nome, sobrenome, usuario, email, senha_hash, data_nascimento)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            
            self.limparCampos

        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar o usuário.")

    def limparCampos(self):
        self.campoNome.clear()
        self.campoSobrenome.clear()
        self.campoUsuario.clear()
        self.campoEmail.clear()
        self.campoSenha.clear()
        self.campoConfirmarSenha.clear()
        self.campoDataNascimento.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    usuario_window = TelaUsuario()
    usuario_window.show()
    sys.exit(app.exec())
