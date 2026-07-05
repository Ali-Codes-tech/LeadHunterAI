from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

from PySide6.QtWidgets import QHeaderView

from services.business_service import BusinessService
from services.export_service import ExportService
from ui.lead_details import LeadDetails


class MainWindow(QMainWindow):

    def __init__(self, database):
        super().__init__()

        self.database = database
        self.business_service = BusinessService()
        self.export_service = ExportService()

        self.current_results = []

        self.setWindowTitle("🚀 LeadHunter Pro")
        self.resize(1200, 700)

        # ==========================
        # Central Widget
        # ==========================

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # ==========================
        # Title
        # ==========================

        title = QLabel("🚀 LeadHunter Pro")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:10px;
        """)

        main_layout.addWidget(title)

        # ==========================
        # Search Layout
        # ==========================

        search_layout = QHBoxLayout()

        self.business_input = QLineEdit()
        self.business_input.setPlaceholderText(
            "Business Type (Example: Car Dealers)"
        )

        self.country_combo = QComboBox()
        self.country_combo.addItems(["USA"])

        self.state_combo = QComboBox()
        self.state_combo.addItems(["Texas"])

        self.city_combo = QComboBox()
        self.city_combo.addItems(["Dallas"])

        self.provider_combo = QComboBox()
        self.provider_combo.addItems([
            "Dummy"
        ])

        self.search_btn = QPushButton("🔍 Search")
        self.search_btn.clicked.connect(
            self.search_businesses
        )

        self.export_btn = QPushButton("📤 Export CSV")
        self.export_btn.clicked.connect(
            self.export_csv
        )

        search_layout.addWidget(self.business_input)
        search_layout.addWidget(self.country_combo)
        search_layout.addWidget(self.state_combo)
        search_layout.addWidget(self.city_combo)
        search_layout.addWidget(self.provider_combo)
        search_layout.addWidget(self.search_btn)
        search_layout.addWidget(self.export_btn)

        main_layout.addLayout(search_layout)

        # ==========================
        # Results Table
        # ==========================

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Business",
            "Rating",
            "Reviews",
            "Phone",
            "Website",
            "Score"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.table.cellDoubleClicked.connect(
            self.open_lead
        )

        main_layout.addWidget(self.table)

        # ==========================
        # Status Bar
        # ==========================

        self.statusBar().showMessage("Ready")

        # ==========================
        # Load Saved Businesses
        # ==========================

        try:

            saved = self.database.get_all_businesses()

            if saved:
                self.display_businesses(saved)

        except Exception as e:
            print("Database Error:", e)

    # ===================================================
    # Display Businesses
    # ===================================================

    def display_businesses(self, businesses):

        self.table.setRowCount(len(businesses))

        for row, item in enumerate(businesses):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(item.get("name", "")))
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(str(item.get("rating", "")))
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(str(item.get("reviews", "")))
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(str(item.get("phone", "")))
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(str(item.get("website", "")))
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(str(item.get("score", "")))
            )

    # ===================================================
    # Search
    # ===================================================

    def search_businesses(self):

        business = self.business_input.text().strip()

        if not business:

            QMessageBox.warning(
                self,
                "Warning",
                "Please enter a business type."
            )

            return

        provider = self.provider_combo.currentText()

        self.business_service.set_provider(provider)

        country = self.country_combo.currentText()
        state = self.state_combo.currentText()
        city = self.city_combo.currentText()

        try:

            results = self.business_service.search(
                business,
                country,
                state,
                city
            )

            self.current_results = results

            for item in results:
                self.database.save_business(item)

            self.display_businesses(results)

            self.statusBar().showMessage(
                f"Found {len(results)} businesses."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Search Error",
                str(e)
            )

    # ===================================================
    # Export CSV
    # ===================================================

    def export_csv(self):

        if not self.current_results:

            QMessageBox.information(
                self,
                "Export",
                "Nothing to export."
            )

            return

        filename = (
            self.business_input.text().replace(" ", "_")
            + ".csv"
        )

        filepath = self.export_service.export_csv(
            self.current_results,
            filename
        )

        QMessageBox.information(
            self,
            "Success",
            f"CSV exported successfully!\n\n{filepath}"
        )

    # ===================================================
    # Lead Details
    # ===================================================

    def open_lead(self, row, column):

        if not self.current_results:
            return

        lead = self.current_results[row]

        dialog = LeadDetails(lead)

        dialog.exec()