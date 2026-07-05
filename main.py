import sys

from PySide6.QtWidgets import QApplication

from database.database_manager import DatabaseManager
from ui.main_window import MainWindow
from styles.app_style import APP_STYLE


def main():

    app = QApplication(sys.argv)

    # Apply global application style
    app.setStyleSheet(APP_STYLE)

    # Initialize database
    database = DatabaseManager()

    # Create main window
    window = MainWindow(database)

    # Show application
    window.show()

    # Start application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()