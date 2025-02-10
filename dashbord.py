import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QComboBox, QFrame, QScrollArea
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from Database import Database  # Importa a classe Database

class TelaDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()  # Conexão com banco de dados
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

        # Estatísticas do estoque
        self.labelTotalEstoque = QLabel("Total no Estoque: 0")
        self.labelProdutoMaisVendido = QLabel("Produto Mais Vendido: -")
        self.labelMaiorPreco = QLabel("Maior Preço: R$ 0.00")

        for label in [self.labelTotalEstoque, self.labelProdutoMaisVendido, self.labelMaiorPreco]:
            label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layoutEstatisticas = QHBoxLayout()
        layoutEstatisticas.addWidget(self.labelTotalEstoque)
        layoutEstatisticas.addWidget(self.labelProdutoMaisVendido)
        layoutEstatisticas.addWidget(self.labelMaiorPreco)

        # Área de exibição dos dados
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
        self.labelDados.setWordWrap(True)

        # Layout do frame de dados
        layoutFrame = QVBoxLayout()
        layoutFrame.addWidget(self.labelDados)
        self.frameDados.setLayout(layoutFrame)

        # Área de gráficos
        self.figure, self.ax = plt.subplots(figsize=(5, 3))  # Criando a figura do gráfico
        self.canvas = FigureCanvas(self.figure)

        layoutMain.addLayout(layoutFiltros)
        layoutMain.addLayout(layoutEstatisticas)
        layoutMain.addWidget(scrollArea)
        layoutMain.addWidget(self.canvas)  # Adicionando o gráfico

        # Carregar dados ao iniciar
        self.carregar_dados()

    def carregar_dados(self):
        """ Carrega os dados do banco de dados e atualiza o gráfico """
        categoria = self.comboFiltro.currentText()
        busca = self.inputBusca.text()

        produtos = self.db.buscar_produtos(categoria, busca)

        if produtos:
            dados_formatados = "\n\n".join([f"<b>{row[0]}</b> - {row[1]} - <b>R${row[2]:.2f}</b>" for row in produtos])
        else:
            dados_formatados = "Nenhum resultado encontrado."

        self.labelDados.setText(f"<p>{dados_formatados}</p>")

        # Atualizar estatísticas
        self.atualizar_estatisticas(produtos)

        # Atualizar gráfico com os produtos
        self.atualizar_grafico(produtos)

    def atualizar_estatisticas(self, produtos):
        """ Atualiza as estatísticas do dashboard """
        if not produtos:
            self.labelTotalEstoque.setText("Total no Estoque: 0")
            self.labelProdutoMaisVendido.setText("Produto Mais Vendido: -")
            self.labelMaiorPreco.setText("Maior Preço: R$ 0.00")
            return

        total_estoque = sum(row[3] for row in produtos)  # Soma das quantidades
        produto_mais_vendido = max(produtos, key=lambda x: x[4])[0]  # Produto com maior venda
        maior_preco = max(produtos, key=lambda x: x[2])[2]  # Maior preço

        self.labelTotalEstoque.setText(f"Total no Estoque: {total_estoque}")
        self.labelProdutoMaisVendido.setText(f"Produto Mais Vendido: {produto_mais_vendido}")
        self.labelMaiorPreco.setText(f"Maior Preço: R$ {maior_preco:.2f}")

    def atualizar_grafico(self, produtos):
        """ Atualiza o gráfico com base nos produtos do banco """
        self.ax.clear()  # Limpa o gráfico anterior

        if produtos:
            nomes = [row[0] for row in produtos]  # Nome dos produtos
            precos = [row[2] for row in produtos]  # Preços dos produtos

            barras = self.ax.bar(nomes, precos, color='#45c4b0', label="Preço dos Produtos")  # Criar gráfico de barras
            self.ax.set_xlabel("Produtos")
            self.ax.set_ylabel("Preço (R$)")
            self.ax.set_title("Preço dos Produtos")
            self.ax.tick_params(axis='x', rotation=45)  # Rotaciona os nomes dos produtos

            # Adicionando legenda ao gráfico
            self.ax.legend(loc="upper right", fontsize=10, frameon=False)

        else:
            self.ax.text(0.5, 0.5, "Sem dados para exibir", fontsize=12, ha='center')

        self.canvas.draw()  # Atualiza o gráfico

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard_window = TelaDashboard()
    dashboard_window.show()
    sys.exit(app.exec())
