import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from database.database_manager import DatabaseManager

app = QApplication(sys.argv)

database = DatabaseManager()

window = MainWindow(database)

window.show()

sys.exit(app.exec())