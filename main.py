import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from database.database_manager import DatabaseManager

app = QApplication(sys.argv)

# Load dark theme
theme_path = Path("assets/styles/dark_theme.qss")

if theme_path.exists():
    with open(theme_path, "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

# Create database
database = DatabaseManager()

# Create main window
window = MainWindow(database)
window.show()

sys.exit(app.exec())