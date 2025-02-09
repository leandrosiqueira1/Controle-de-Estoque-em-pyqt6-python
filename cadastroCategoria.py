import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QFormLayout, QFrame,QMessageBox
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from Database import Database

class TelaCategoria(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #DCF230;")
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Tela de Categoria")
        self.setGeometry(100,30,1280,800)
        self.setFixedSize(1280, 800)

               # Layout principal
        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout do formulário
        self.frameFundo = QFrame(self)
        self.frameFundo.setFixedSize(500, 450)
        self.frameFundo.setStyleSheet("background-color: #ccc;border-radius: 10px;box-sizing: border-box; margin: 10px;")
        

        layoutForm = QVBoxLayout(self.frameFundo)
        layoutForm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Título do formulário
        labelTitulo = QLabel("Categoria", self)
        labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelTitulo.setStyleSheet("""
                QLabel{
                    color: #000000;
                    padding: 10px 5px;
                    font-size: 25px;                 
            }
        
        """)
        layoutForm.addWidget(labelTitulo)

        # Texto de categoria
        labelCategoria = QLabel("Categoria", self)
        labelCategoria.setFixedHeight(60)
        labelCategoria.setStyleSheet("""
                QLabel{
                    color: #000000;
                    padding: 10px 10px 0px 0px;
                    font-size: 14px;
                                  
            }
        
        """)
        layoutForm.addWidget(labelCategoria)
       
        #Campo categoria 
        self.campoCategoria = QLineEdit(self)
        self.campoCategoria.setStyleSheet("font-size: 14px;border: 1px solid #555555; padding: 8px;")
        self.campoCategoria.setPlaceholderText("Digite categoria")
        layoutForm.addWidget(self.campoCategoria)
        
        # Botão de salvar
        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.setFixedHeight(60)
        self.btnSalvar.clicked.connect(self.salvarCategoria)
        self.btnSalvar.setStyleSheet("""
            QPushButton {
                background-color: #3084F2;
                color: white;
                font-size: 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2BAFF5;
            }
        """)
        layoutForm.addWidget(self.btnSalvar)
        # Texto para registro
        layoutForm.addSpacing(5)
        
        layoutPrincipal.addWidget(self.frameFundo)

    def salvarCategoria(self):

        categoria = self.campoCategoria.text().strip().upper()
        db = Database() 
        sucesso = db.adicionar_categoria(categoria)

        if sucesso: 
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            
            self.campoCategoria.clear()
        else: 
            QMessageBox.warning(self,"Erro","Erro ao salvar categiria")

if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    categoria_Window = TelaCategoria()
    categoria_Window.show()
    sys.exit(app.exec())
    