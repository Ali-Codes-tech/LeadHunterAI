import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

app = QApplication(sys.argv)

theme_path = Path("assets/styles/dark_theme.qss")

if theme_path.exists():
    with open(theme_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

window = MainWindow()
window.show()

sys.exit(app.exec())