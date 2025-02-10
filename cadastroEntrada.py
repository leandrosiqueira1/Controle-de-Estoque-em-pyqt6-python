import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QFormLayout, QFrame, QMessageBox, QComboBox
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from Database import Database


class TelaCadastroEntrada(QWidget):
    def __init__(self):
        super().__init__()

        # Cores da interface
        self.corButton = "#3084F2"
        self.corBranco = "#F2F2F2"
        self.corEsqForm = "#222602"
        self.corDirForm = "#DCF230"
        self.corTitle = "#000000"

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro de Entrada")
        self.setFixedSize(1280, 800)

        layoutPrincipal = QHBoxLayout(self)
        layoutPrincipal.setSpacing(0)
        layoutPrincipal.setContentsMargins(0, 0, 0, 0)

        # Frame esquerdo (menu lateral)
        frameEsquerda = QFrame(self)
        frameEsquerda.setStyleSheet(f"background-color:{self.corEsqForm};")
        frameEsquerda.setFixedSize(350, 800)
        layoutEsquerda = QVBoxLayout(frameEsquerda)

        # Botões do menu lateral
        btnCadastrarProduto = QPushButton("Cadastrar Novo Produto", self)
        btnCadastrarProduto.setFixedSize(300, 60)
        btnCadastrarProduto.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco};")
        layoutEsquerda.addWidget(btnCadastrarProduto)

        btnCadastrarFornecedor = QPushButton("Cadastrar Novo Fornecedor", self)
        btnCadastrarFornecedor.setFixedSize(300, 60)
        btnCadastrarFornecedor.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco};")
        layoutEsquerda.addWidget(btnCadastrarFornecedor)

        btnEntradaProduto = QPushButton("Cadastrar Entrada de Produto", self)
        btnEntradaProduto.setFixedSize(300, 60)
        btnEntradaProduto.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco};")
        layoutEsquerda.addWidget(btnEntradaProduto)

        layoutEsquerda.addStretch()

        # Frame direito (formulário)
        frameDireita = QFrame(self)
        frameDireita.setStyleSheet(f"background-color:{self.corDirForm}; border: 1px solid {self.corBranco};")
        frameDireita.setFixedSize(932, 800)
        layoutDireita = QVBoxLayout(frameDireita)

        # Título do formulário
        tituloFornecedor = QLabel("Cadastro de Entrada")
        tituloFornecedor.setFont(QFont("Roboto", 50))
        tituloFornecedor.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {self.corTitle};")
        layoutDireita.addWidget(tituloFornecedor, alignment=Qt.AlignmentFlag.AlignCenter)

        # Formulário
        formularioWidget = QWidget()
        formularioWidget.setStyleSheet("""
            QWidget { background-color: #Dcf230; border: none; }
            QLabel { color: #000000; font-size: 18px; }
            QLineEdit, QComboBox {
                background-color: #F0F0F0;
                border-radius: 10px;
                padding: 10px;
                margin: 5px;
            }
        """)
        formulario = QFormLayout(formularioWidget)

        # Campos do formulário
        self.nomeInput = QComboBox(self)
        self.unidadeInput = QComboBox(self)
        self.categoriaInput = QComboBox(self)
        self.quantidadeInput = QLineEdit(self)
        self.quantidadeInput.setPlaceholderText("Ex: 50")

        self.nfeInput = QLineEdit(self)
        self.nfeInput.setPlaceholderText("Ex: 1234")

        self.dataEmissaonfeInput = QLineEdit(self)
        self.dataEmissaonfeInput.setPlaceholderText("Ex: 24/02/2025")

        self.dataCadastroInput = QLineEdit(self)
        self.dataCadastroInput.setPlaceholderText("Ex: 24/02/2025")

        self.fornecedorInput = QLineEdit(self)
        self.fornecedorInput.setPlaceholderText("Nome da empresa")

        formulario.addRow("Produto", self.nomeInput)
        formulario.addRow("Unidade", self.unidadeInput)
        formulario.addRow("Categoria", self.categoriaInput)
        formulario.addRow("Quantidade", self.quantidadeInput)
        formulario.addRow("NFE", self.nfeInput)
        formulario.addRow("Data de Emissão", self.dataEmissaonfeInput)
        formulario.addRow("Data do Cadastro", self.dataCadastroInput)
        formulario.addRow("Fornecedor", self.fornecedorInput)

        # Populando os ComboBox com dados do banco
        db = Database()
        unidades = db.buscar_unidades()
        categorias = db.buscar_categorias()
        produtos = db.buscar_produtos()

        for unidade in unidades:
            self.unidadeInput.addItem(unidade[0])

        for categoria in categorias:
            self.categoriaInput.addItem(categoria[0])

        for produto in produtos:
            self.nomeInput.addItem(produto[0])

        # Botão "Salvar"
        layoutbtnSalvar = QHBoxLayout()
        layoutbtnSalvar.addStretch()
        btnSalvar = QPushButton("Salvar", self)
        btnSalvar.setFixedSize(300, 60)
        btnSalvar.setStyleSheet(f"background-color: {self.corButton}; color: {self.corBranco}; border-radius: 10px; font-size: 16px;")
        btnSalvar.clicked.connect(self.cadastrarEntrada)
        layoutbtnSalvar.addWidget(btnSalvar)
        layoutbtnSalvar.addStretch()
        formulario.addRow(layoutbtnSalvar)

        layoutDireita.addWidget(formularioWidget)
        layoutDireita.addStretch()

        # Adicionando os frames ao layout principal
        layoutPrincipal.addWidget(frameEsquerda, alignment=Qt.AlignmentFlag.AlignLeft)
        layoutPrincipal.addWidget(frameDireita)

    def cadastrarEntrada(self):
        # Obtendo os dados do formulário
        produto = self.nomeInput.currentText()
        unidade = self.unidadeInput.currentText()
        categoria = self.categoriaInput.currentText()
        quantidade = self.quantidadeInput.text()
        nfe = self.nfeInput.text()
        dataEmissao = self.dataEmissaonfeInput.text()
        dataCadastro = self.dataCadastroInput.text()
        fornecedor = self.fornecedorInput.text()

        # Verificando se todos os campos foram preenchidos
        if not (produto and unidade and categoria and quantidade and nfe and dataEmissao and dataCadastro and fornecedor):
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            quantidade = float(quantidade)  # Converte para número

            # Criar instância do banco de dados e salvar os dados
            db = Database()
            sucesso = db.salvarEntradaProduto(produto, unidade, categoria, quantidade, nfe, dataEmissao, dataCadastro, fornecedor)

            if sucesso:
                QMessageBox.information(self, "Sucesso", "Entrada cadastrada com sucesso!")

                # Limpa os campos após o cadastro
                self.nomeInput.setCurrentIndex(-1)
                self.unidadeInput.setCurrentIndex(-1)
                self.categoriaInput.setCurrentIndex(-1)
                self.quantidadeInput.clear()
                self.nfeInput.clear()
                self.dataEmissaonfeInput.clear()
                self.dataCadastroInput.clear()
                self.fornecedorInput.clear()
            else:
                QMessageBox.critical(self, "Erro", "Erro ao cadastrar entrada!")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Quantidade deve ser um número válido!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar entrada: {e}")  


# Inicialização da aplicação
app = QApplication(sys.argv)
fornecedor_window = TelaCadastroEntrada()
fornecedor_window.show()
sys.exit(app.exec())
