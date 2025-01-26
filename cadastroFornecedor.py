import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QFrame
from PyQt6.QtGui import QPixmap, QFont,QIcon
from PyQt6.QtCore import Qt

class TelaCadastroFornecedor(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

        self.corRosa = "#F279B2"
        self.corCinza = "#ccc"

    
    def initUI(self):
        self.setWindowTitle("Cadastro de Fornecedor")
        self.setFixedSize(1280,800)

        

        # Layout principal horizontal
        layoutPrincipal = QHBoxLayout(self)
        layoutPrincipal.setSpacing(0)  # Define o espaçamento entre os frames
        layoutPrincipal.setContentsMargins(0, 0, 0, 0)  # Define margens ao redor do layout
        
        # Frame da esquerda
        frameEsquerda = QFrame(self)
        frameEsquerda.setStyleSheet(f"background-color:#ffffff;")
        #frameEsquerda.setStyleSheet(f"background-color:{self.corRosa};border: 1px solid{self.corCinza};")
        frameEsquerda.setFixedSize(350,800)
        
        #
        layoutEsquerda = QVBoxLayout(frameEsquerda)
        #Botão para cadastrar novos produtos 

        btnCadastrarProduto = QPushButton("Cadastrar Novo Produto",self)
        btnCadastrarProduto.setIcon(QIcon('img/logo_50.png'))
        btnCadastrarProduto.setFixedSize(300,50)
        btnCadastrarProduto.setStyleSheet("background-color: #F27F3D;color: #ffffff")
        layoutEsquerda.addWidget(btnCadastrarProduto)

        #Botão para cadastrat novos fornecedores 
        btnCadastraFornecedor = QPushButton("Cadastrar Novo Fornecedor",self)
        btnCadastraFornecedor.setIcon(QIcon('img/logo_250.png'))
        btnCadastraFornecedor.setFixedSize(300,50)
        layoutEsquerda.addWidget(btnCadastraFornecedor)

        #Botão para cadastrar entrada de novos produtos 
        btnEntradaProduto = QPushButton("Cadastre Entrada de produto",self)
        btnEntradaProduto.setIcon(QIcon('img/logo_250.png'))
        btnEntradaProduto.setFixedSize(300,50)
        layoutEsquerda.addWidget(btnEntradaProduto)

        layoutEsquerda.addStretch()



        
        # Frame da dereita para colocar os imput e label 
        frameDireita = QFrame(self)
        frameDireita.setStyleSheet("background-color:#EBEBEB; border: 1px solid #ccc;")
        frameDireita.setFixedSize(932,800)
        
        layoutDireita = QVBoxLayout(frameDireita)
        bntDeletar = QPushButton("Deletar",self)
        layoutEsquerda.addWidget(bntDeletar)
        layoutDireita.addStretch()
        
          # Adicionar os frames ao layout principal

        layoutPrincipal.addWidget(frameEsquerda,alignment=Qt.AlignmentFlag.AlignLeft)
        layoutPrincipal.addWidget(frameDireita)


app = QApplication(sys.argv)

fornecedor_window = TelaCadastroFornecedor()
fornecedor_window.show()
sys.exit(app.exec())