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
    QTableWidgetItem
)

from services.business_service import BusinessService


class MainWindow(QMainWindow):

    def __init__(self, database):
        super().__init__()

        self.database = database
        self.business_service = BusinessService()

        self.setWindowTitle("🚀 LeadHunter Pro")
        self.resize(1200, 700)

        # Store current search results
        self.current_results = []

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
            font-size:26px;
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

        # Provider
        self.provider_combo = QComboBox()
        self.provider_combo.addItems([
            "Dummy"
        ])

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.search_businesses)

        search_layout.addWidget(self.business_input)
        search_layout.addWidget(self.country_combo)
        search_layout.addWidget(self.state_combo)
        search_layout.addWidget(self.city_combo)
        search_layout.addWidget(self.provider_combo)
        search_layout.addWidget(self.search_btn)

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
            print("Database load error:", e)

    # ==========================
    # Display Businesses
    # ==========================
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

    # ==========================
    # Search Businesses
    # ==========================
    def search_businesses(self):

        business = self.business_input.text().strip()

        if not business:
            self.statusBar().showMessage(
                "Please enter a business type."
            )
            return

        country = self.country_combo.currentText()
        state = self.state_combo.currentText()
        city = self.city_combo.currentText()

        provider = self.provider_combo.currentText()
        self.business_service.set_provider(provider)

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
            print(e)
            self.statusBar().showMessage(
                "Search failed."
            )