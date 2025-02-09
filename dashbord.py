import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QComboBox, QFrame, QScrollArea,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from Database import Database  # Importa a classe Database

class TelaDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()  # Cria a instância do banco de dados
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 20, 1280, 800)
        self.setFixedSize(1280, 800)
        self.setWindowTitle("Dashboard de Produtos")
        self.setStyleSheet("""
            background-color: #f0f4f8;
            font-family: Arial, sans-serif;
        """)

        # Layout principal
        layoutMain = QVBoxLayout()
        self.setLayout(layoutMain)

        # Barra de Filtros
        layoutFiltros = QHBoxLayout()
        layoutFiltros.setContentsMargins(20, 10, 20, 10)
        layoutFiltros.setSpacing(10)

        self.comboFiltro = QComboBox()
        self.comboFiltro.addItems(["Todos", "Categoria A", "Categoria B", "Categoria C"])
        self.comboFiltro.setStyleSheet("padding: 5px; font-size: 14px;")

        self.inputBusca = QLineEdit()
        self.inputBusca.setPlaceholderText("Buscar Produto...")
        self.inputBusca.setStyleSheet("padding: 5px; font-size: 14px;")

        btnBuscar = QPushButton("Buscar")
        btnBuscar.setStyleSheet("""
            background-color: #45c4b0;
            color: white;
            padding: 5px 15px;
            font-size: 14px;
            border-radius: 5px;
        """)
        btnBuscar.clicked.connect(self.carregar_dados)

        layoutFiltros.addWidget(QLabel("Filtrar por Categoria:"))
        layoutFiltros.addWidget(self.comboFiltro)
        layoutFiltros.addWidget(self.inputBusca)
        layoutFiltros.addWidget(btnBuscar)

        # Frame para exibir os dados
        self.frameDados = QFrame()
        self.frameDados.setStyleSheet("background-color: #fff; border-radius: 10px; border: 2px solid #9aeba3;")
        self.frameDados.setFixedSize(1200, 600)

        # Área de rolagem
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(self.frameDados)

        # Label para mostrar os dados
        self.labelDados = QLabel("Nenhum dado carregado.")
        self.labelDados.setFont(QFont("Arial", 12))
        self.labelDados.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.labelDados.setWordWrap(True)  # Permitir que o texto seja quebrado automaticamente

        # Layout do frame de dados
        layoutFrame = QVBoxLayout()
        layoutFrame.addWidget(self.labelDados)
        self.frameDados.setLayout(layoutFrame)

        # Adiciona os widgets no layout principal
        layoutMain.addLayout(layoutFiltros)
        layoutMain.addWidget(scrollArea)

        # Carregar dados ao iniciar
        self.carregar_dados()

    def carregar_dados(self):
        """ Carrega os dados do banco de dados de acordo com o filtro selecionado """
        categoria = self.comboFiltro.currentText()
        busca = self.inputBusca.text()

        produtos = self.db.buscar_produtos(categoria, busca)

        if produtos:
            dados_formatados = "\n\n".join([f"<b>{row[0]}</b> - {row[1]} - <b>R${row[2]:.2f}</b>" for row in produtos])
        else:
            dados_formatados = "Nenhum resultado encontrado."

        self.labelDados.setText(f"<p>{dados_formatados}</p>")  # Exibe em formato HTML para melhor formatação


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard_window = TelaDashboard()
    dashboard_window.show()
    sys.exit(app.exec())
