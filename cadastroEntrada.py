import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QFormLayout, QFrame
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


# Classe principal que define a tela de cadastro de entrada
class TelaCadastroEntrada(QWidget):
    def __init__(self):
        super().__init__()  # Chama o construtor da classe QWidget

        # Definição das cores usadas na interface
        self.corVerdeEscuro = "#1D6373"  # Cor verde escuro
        self.corVerdeclaro1 = "#378C74"  # Verde mais claro
        self.corVerdeclaro2 = "#49A671"  # Verde ainda mais claro
        self.corButton = "#3084F2"  # Cor dos botões entrar 
        self.corBranco = "#F2F2F2"       # Cor branca para fundo
        self.corEsqForm = "#222602" #Cor do lado esquerdo do formulário
        self.corDirForm = "#DCF230" #Cor do lador direito do formulario
        self.corTitle = "#000000" 


        #self.fontRoboto = QFont("Roboto",25)

        self.initUI()  # Chama o método que inicializa a interface

    def initUI(self):
        # Configurações básicas da janela
        self.setWindowTitle("Cadastro de Entrada")  # Define o título da janela
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
        btnCadastrarProduto.setIcon(QIcon('img/logo_50.png'))  # Define um ícone para o botão
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
        btnEntradaProduto = QPushButton("Cadastre Entrada de produto", self)
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
        tituloFornecedor = QLabel("Cadastro de Entrada")  # Texto do título
        tituloFornecedor.setFont(QFont("Roboto",50))
        tituloFornecedor.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {self.corTitle};border: none;")  # Estilo do texto
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
        nomeInput = QLineEdit(self)
        nomeInput.setPlaceholderText("Nome do Produto")  # Texto de exemplo
        formulario.addRow("Produto", nomeInput)  # Adiciona o campo de nome

        unidadeInput = QLineEdit(self)
        unidadeInput.setPlaceholderText("kg")  # Texto de exemplo
        formulario.addRow("Unidade", unidadeInput)  # Adiciona o campo de Unidade

        categoriaInput = QLineEdit(self)
        categoriaInput.setPlaceholderText("Imovel")
        formulario.addRow("Categoria",categoriaInput)

        quantidadeInput = QLineEdit(self)
        quantidadeInput.setPlaceholderText("50")
        formulario.addRow("Quantidade:",quantidadeInput)

        nfeInput = QLineEdit(self)
        nfeInput.setPlaceholderText("1234")
        formulario.addRow("Nfe",nfeInput)

        dataEmissaonfeInput = QLineEdit(self)
        dataEmissaonfeInput.setPlaceholderText("24/02/2025")
        formulario.addRow("Data de Emissão",dataEmissaonfeInput)
      
        dataCadastroInput = QLineEdit(self)
        dataCadastroInput.setPlaceholderText("24/02/2025")
        formulario.addRow("Data do cadastro",dataCadastroInput)

        fornecedorInput = QLineEdit(self)
        fornecedorInput.setPlaceholderText("Nome da empresa")
        formulario.addRow("Empresa",fornecedorInput)
      
        

        # Botão "Salvar" no formulário
        btnSalvar = QPushButton("Salvar", self)
        btnSalvar.setFixedSize(300,60)
        btnSalvar.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco}; border-radius: 10px;font-size: 16px;")  # Estilo do botão
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


    def cadastrarEntrada(self):
        pass

# Inicialização da aplicação
app = QApplication(sys.argv)  # Cria a aplicação
fornecedor_window = TelaCadastroEntrada()  # Cria a janela principal
fornecedor_window.show()  # Exibe a janela
sys.exit(app.exec())  # Executa o loop da aplicação
