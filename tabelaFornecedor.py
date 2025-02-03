import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QPainter, QPageLayout, QPageSize
from PyQt6.QtCore import QMarginsF
from Database import Database
import sqlite3

class TabelaFornecedores(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabela de Fornecedores com Pesquisa")
        self.setGeometry(100, 100, 1280, 800)

        self.layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Pesquisar...")
        self.search_bar.textChanged.connect(self.filter_data)
        self.layout.addWidget(self.search_bar)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.print_button = QPushButton("Imprimir")
        self.print_button.clicked.connect(self.print_table)
        self.layout.addWidget(self.print_button)

        self.save_pdf_button = QPushButton("Salvar como PDF")
        self.save_pdf_button.clicked.connect(self.save_pdf)
        self.layout.addWidget(self.save_pdf_button)

        self.delete_button = QPushButton("Deletar")
        self.delete_button.clicked.connect(self.delete_item)
        self.layout.addWidget(self.delete_button)

        self.modify_button = QPushButton("Modificar")
        self.modify_button.clicked.connect(self.modify_item)
        self.layout.addWidget(self.modify_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        try:
            self.db_manager = Database('estoque.db')
            self.db_manager.connect()
            self.load_data()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def load_data(self):
        try:
            query = "SELECT * FROM fornecedor"  # Nome correto da tabela
            self.fornecedores = self.db_manager.fetch_all(query)
            self.display_data(self.fornecedores)
        except sqlite3.Error as e:
            print(f"Erro ao buscar dados: {e}")

    def display_data(self, data):
        if data:
            self.table_widget.setRowCount(len(data))
            self.table_widget.setColumnCount(len(data[0]))

            column_names = [description[0] for description in self.db_manager.cursor.description]
            self.table_widget.setHorizontalHeaderLabels(column_names)

            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            for i in range(len(data[0])):
                self.table_widget.resizeColumnToContents(i)
        else:
            self.table_widget.setRowCount(0)
            self.table_widget.setColumnCount(0)

        self.table_widget.setStyleSheet("""
            QTableWidget {
                border: 1px solid #dcdcdc;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #f0f0f0;
                padding: 4px;
                border: 1px solid #dcdcdc.
            }
            QTableWidget::item {
                padding: 4px.
            }
            QTableWidget::item:selected {
                background-color: #a0c4ff;
                color: black.
            }
        """)

    def filter_data(self):
        search_text = self.search_bar.text().lower()
        filtered_data = [row for row in self.fornecedores if search_text in row[1].lower()]
        self.display_data(filtered_data)

    def delete_item(self):
        selected_items = self.table_widget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            item_id = self.table_widget.item(row, 0).text()  # Assumindo que a primeira coluna é o ID
            try:
                query = f"DELETE FROM fornecedor WHERE id = ?"
                self.db_manager.execute_query(query, (item_id,))
                self.load_data()
                QMessageBox.information(self, "Sucesso", "Fornecedor deletado com sucesso.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao deletar fornecedor: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Selecione um fornecedor para deletar.")

    def modify_item(self):
        selected_items = self.table_widget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            item_id = self.table_widget.item(row, 0).text()  # Assumindo que a primeira coluna é o ID
            # Aqui você pode adicionar uma janela ou diálogo para modificar os dados do item
            # Exemplo de atualização de um campo específico:
            try:
                novo_nome = "Novo Nome do Fornecedor"  # Aqui você pode obter o valor de um input do usuário
                query = f"UPDATE fornecedor SET nome = ? WHERE id = ?"
                self.db_manager.execute_query(query, (novo_nome, item_id))
                self.load_data()
                QMessageBox.information(self, "Sucesso", "Fornecedor modificado com sucesso.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao modificar fornecedor: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Selecione um fornecedor para modificar.")

    def print_table(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        page_layout = QPageLayout(QPageSize(QPageSize.PageSizeId.A4), QPageLayout.Orientation.Portrait, QMarginsF(10, 10, 10, 10))
        printer.setPageLayout(page_layout)

        dialog = QPrintDialog(printer)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            painter = QPainter(printer)
            self.table_widget.render(painter)
            painter.end()

    def save_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
        if filename:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(filename)
            painter = QPainter(printer)
            self.table_widget.render(painter)
            painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TabelaFornecedores()
    main_window.show()
    sys.exit(app.exec())
