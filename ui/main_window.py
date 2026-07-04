from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LeadHunter AI")
        self.resize(1200, 800)

        label = QLabel("🚀 LeadHunter AI", self)
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)