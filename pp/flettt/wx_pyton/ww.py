import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide2.QtGui import QIcon
from PySide2 import QtCore  # Tambahkan impor untuk QtCore

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PySide2 UI Example')
        self.setWindowIcon(QIcon('j.png'))  # Ubah 'icon.png' menjadi nama file ikon Anda

        layout = QVBoxLayout()

        label = QLabel('Hello, PySide2!', self)
        label.setAlignment(QtCore.Qt.AlignCenter)  # Perbaiki pemanggilan QtCore.Qt.AlignCenter
        layout.addWidget(label)

        button = QPushButton('Click Me', self)
        button.clicked.connect(self.buttonClicked)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def buttonClicked(self):
        QMessageBox.information(self, 'Message', 'Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
