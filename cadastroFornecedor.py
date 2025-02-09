import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QFormLayout, QFrame, QMessageBox,QComboBox
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt , QSize
import sqlite3
from Database import Database
from datetime import datetime  # Importa datetime

# Classe principal que define a tela de cadastro de fornecedores
class TelaCadastroFornecedor(QWidget):
    def __init__(self):
        super().__init__()  # Chama o construtor da classe QWidget

        # Definição das cores usadas na interface
        self.corVerdeEscuro = "#1D6373"  # Cor verde escuro
        self.corVerdeclaro1 = "#378C74"  # Verde mais claro
        self.corVerdeclaro2 = "#49A671"  # Verde ainda mais claro
        self.corButton = "#3084F2"  # Cor dos botões entrar 
        self.corBranco = "#F2F2F2"  # Cor branca para fundo
        self.corEsqForm = "#222602"  # Cor do lado esquerdo do formulário
        self.corDirForm = "#DCF230"  # Cor do lado direito do formulário
        self.corTitle = "#000000" 

        self.initUI()  # Chama o método que inicializa a interface

    def initUI(self):
        # Configurações básicas da janela
        self.setWindowTitle("Cadastro de Fornecedor")  # Define o título da janela
        self.setFixedSize(1280, 800)  # Define o tamanho fixo da janela

        # Layout principal horizontal que organiza os elementos lado a lado
        layoutPrincipal = QHBoxLayout(self)
        layoutPrincipal.setSpacing(0)  # Sem espaçamento entre os elementos
        layoutPrincipal.setContentsMargins(0, 0, 0, 0)  # Sem margens no layout principal

        # Criação do frame à esquerda (menu lateral)
        frameEsquerda = QFrame(self)
        frameEsquerda.setStyleSheet(f"background-color:{self.corEsqForm};")  # Fundo branco
        frameEsquerda.setFixedSize(350, 800)  # Largura fixa
        layoutEsquerda = QVBoxLayout(frameEsquerda)  # Layout vertical para organizar os botões

        # Botão para "Cadastrar Novo Produto"
        btnCadastrarProduto = QPushButton("Cadastrar Novo Produto", self)
        btnCadastrarProduto.setIcon(QIcon('img/novo.png'))  # Define um ícone para o botão
        btnCadastrarProduto.setFixedSize(300, 60)  # Tamanho fixo do botão
        btnCadastrarProduto.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco};")  # Estilo do botão
        layoutEsquerda.addWidget(btnCadastrarProduto)  # Adiciona o botão ao layout da esquerda

        # Botão para "Cadastrar Novo Fornecedor"
        btnCadastrarFornecedor = QPushButton("Cadastrar Novo Fornecedor", self)
        btnCadastrarFornecedor.setIcon(QIcon('img/logo_250.png'))
        btnCadastrarFornecedor.setFixedSize(300, 60)
        btnCadastrarFornecedor.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco}")
        layoutEsquerda.addWidget(btnCadastrarFornecedor)

        # Botão para "Cadastrar Entrada de Produto"
        btnEntradaProduto = QPushButton("Cadastrar Entrada de Produto", self)
        btnEntradaProduto.setIcon(QIcon('img/logo_250.png'))
        btnEntradaProduto.setFixedSize(300, 60)
        btnEntradaProduto.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco}")
        layoutEsquerda.addWidget(btnEntradaProduto)

        layoutEsquerda.addStretch()  # Adiciona um espaço flexível no final (empurra os botões para cima)

        # Criação do frame à direita (formulário principal)
        frameDireita = QFrame(self)
        frameDireita.setStyleSheet(f"background-color:{self.corDirForm}; border: 1px solid {self.corBranco};")  # Fundo branco com borda cinza
        frameDireita.setFixedSize(932, 800)  # Tamanho fixo
        layoutDireita = QVBoxLayout(frameDireita)  # Layout vertical para os elementos do formulário

        # Título do formulário
        layoutTitulo = QVBoxLayout()  # Layout horizontal para centralizar o título
        tituloFornecedor = QLabel("Cadastro de Fornecedor")  # Texto do título
        tituloFornecedor.setFont(QFont("Roboto", 50))
        tituloFornecedor.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {self.corTitle}; border: none;")  # Estilo do texto
        layoutTitulo.addWidget(tituloFornecedor, alignment=Qt.AlignmentFlag.AlignCenter)  # Centraliza o título
        layoutDireita.addLayout(layoutTitulo)  # Adiciona o título ao layout da direita

        # Widget para o formulário com borda arredondada
        formularioWidget = QWidget()
        formularioWidget.setStyleSheet("""
            QWidget {
                background-color:#Dcf230;  /* Cor de fundo do formulário */
                border: none;
            }
            QLabel {
                color: #000000;
                font-size: 18px;
                border: none;
            }
            QLineEdit{
                background-color: #F0F0F0;
                border-color: 1px solid #F0F0F0;
                color: #000000;
                border-radius: 10px;       
                padding: 10px;
                margin: 5px;        
            }
        """)
        formulario = QFormLayout(formularioWidget)  # Layout de formulário para organizar campos
        formulario.setFormAlignment(Qt.AlignmentFlag.AlignCenter)  # Centraliza o formulário

        layoutbtnSalvar = QHBoxLayout()
        layoutbtnSalvar.addStretch()

        # Campos do formulário (inputs)
        self.nomeInput = QLineEdit(self)
        self.nomeInput.setPlaceholderText("Nome do Fornecedor")  # Texto de exemplo
        formulario.addRow("Nome:", self.nomeInput)  # Adiciona o campo de nome

        self.cnpjInput = QLineEdit(self)
        self.cnpjInput.setPlaceholderText("CNPJ")  # Texto de exemplo
        formulario.addRow("CNPJ:", self.cnpjInput)  # Adiciona o campo de CNPJ

        self.enderecoInput = QLineEdit(self)
        self.enderecoInput.setPlaceholderText("Rua Monsenhor Tabosa")
        formulario.addRow("Endereço:", self.enderecoInput)

        self.numeroInput = QLineEdit(self)
        self.numeroInput.setPlaceholderText("1234")
        formulario.addRow("Nº:", self.numeroInput)

        self.complementoInput = QLineEdit(self)
        self.complementoInput.setPlaceholderText("Bloco 5, Apto 213")
        formulario.addRow("Complemento:", self.complementoInput)

        self.cidadeInput = QLineEdit(self)
        self.cidadeInput.setPlaceholderText("Fortaleza")
        formulario.addRow("Cidade:", self.cidadeInput)

        self.bairroInput = QLineEdit(self)
        self.bairroInput.setPlaceholderText("Bairro")
        formulario.addRow("Bairro:", self.bairroInput)

        self.ufInput = QComboBox(self)
        self.ufInput.setStyleSheet('background-color: #F0F0F0; border-radius: 8px; padding: 10px 8px;')
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        self.ufInput.addItems(estados)
        formulario.addRow("UF:", self.ufInput)

        self.insEstadualInput = QLineEdit(self)
        self.insEstadualInput.setPlaceholderText("Incrição Estadual")
        formulario.addRow("Incrição Estadual", self.insEstadualInput)

        self.telefoneInput = QLineEdit(self)
        self.telefoneInput.setPlaceholderText("Telefone")  # Texto de exemplo
        formulario.addRow("Telefone:", self.telefoneInput)  # Adiciona o campo de telefone

        self.emailInput = QLineEdit(self)
        self.emailInput.setPlaceholderText("E-mail")  # Texto de exemplo
        formulario.addRow("E-mail:", self.emailInput)  # Adiciona o campo de e-mail

        # Campo Data de Cadastro
        self.dataCadastro = QLineEdit(self)
        self.dataCadastro.setText(datetime.today().strftime("%d/%m/%Y"))  # Define a data atual
        self.dataCadastro.setReadOnly(True)  # Impede edição manual
        self.dataCadastro.setStyleSheet("background-color: #E0E0E0; color: #000000; border-radius: 10px; padding: 10px;")
        formulario.addRow("Data de Cadastro",self.dataCadastro)

        # Botão "Salvar" no formulário
        btnSalvar = QPushButton("Salvar", self)
        btnSalvar.setFixedSize(300, 60)
        btnSalvar.setStyleSheet("""
                QPushButton {
                    background-color: "#3084F2"; 
                    color: "#F2F2F2"; 
                    border-radius: 10px; 
                    font-size: 16px;
                }
                QPushButton:hover{
                    background-color: "#2FC5FB"; 
                    color: "#F2F2F2"; 
                }
        """)

        #btnSalvar.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco}; border-radius: 10px; font-size: 16px;")  # Estilo do botão
        btnSalvar.clicked.connect(self.cadastrarFornecedor)  # Conecta o clique do botão ao método cadastrarFornecedor
        layoutbtnSalvar.addWidget(btnSalvar)
        layoutbtnSalvar.addStretch()

        # Adiciona o layout do botão centralizado ao formulário
        formulario.addRow(layoutbtnSalvar)  # Adiciona o botão ao formulário

        # Adiciona o formulário ao layout da direita
        layoutDireita.addWidget(formularioWidget)

        # Adiciona um espaço flexível para empurrar o formulário para o topo
        # Esse espaço ajuda a ajustar a posição do formulário dentro do layout
        layoutDireita.addStretch()

        # Adiciona os frames (esquerda e direita) ao layout principal
        layoutPrincipal.addWidget(frameEsquerda, alignment=Qt.AlignmentFlag.AlignLeft)
        layoutPrincipal.addWidget(frameDireita)

 
    def cadastrarFornecedor(self):
        fornecedor = self.nomeInput.text()
        cnpj = self.cnpjInput.text()
        endereco = self.enderecoInput.text()
        numero = self.numeroInput.text()
        complemento = self.complementoInput.text()
        cidade = self.cidadeInput.text()
        bairro = self.bairroInput.text()
        telefone = self.telefoneInput.text()
        email = self.emailInput.text()
        datacadastro = self.dataCadastro.text()
        uf = self.ufInput.currentText()  # Corrigido para pegar o estado correto
        inscricaoestadual = self.insEstadualInput.text()  # Corrigido para pegar o campo correto

        if not fornecedor or not cnpj or not endereco or not numero or not cidade or not telefone or not email:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos obrigatórios.")
            return
    
        db = Database('estoque.db')
        db.connect()

        if db.salvarFornecedor(fornecedor, cnpj, endereco, numero, complemento, cidade, bairro, uf, inscricaoestadual, datacadastro, telefone, email):
            QMessageBox.information(self, "Sucesso", "Fornecedor cadastrado com sucesso!")
            self.limparCampos()
        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar o fornecedor!")

    def limparCampos(self):
        #resposta = QMessageBox.question(self, "Limpar Campos", "Tem certeza que deseja limpar os campos?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        #if resposta == QMessageBox.StandardButton.Yes:
            self.nomeInput.clear()
            self.cnpjInput.clear()
            self.enderecoInput.clear()
            self.numeroInput.clear()
            self.complementoInput.clear()
            self.cidadeInput.clear()
            self.bairroInput.clear()
            self.telefoneInput.clear()
            self.emailInput.clear()

# Inicialização da aplicação
app = QApplication(sys.argv)  # Cria a aplicação
fornecedor_window = TelaCadastroFornecedor()  # Cria a janela principal
fornecedor_window.show()  # Exibe a janela
sys.exit(app.exec())  # Executa o loop da aplicação
