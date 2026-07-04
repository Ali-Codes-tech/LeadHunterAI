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

        self.setWindowTitle("LeadHunter AI")
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
        title = QLabel("🚀 LeadHunter AI")
        title.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            padding: 10px;
        """)

        main_layout.addWidget(title)

        # ==========================
        # Search Area
        # ==========================
        search_layout = QHBoxLayout()

        self.business_input = QLineEdit()
        self.business_input.setPlaceholderText(
            "Business Type (e.g. Car Dealers)"
        )

        self.country_combo = QComboBox()
        self.country_combo.addItems(["USA"])

        self.state_combo = QComboBox()
        self.state_combo.addItems(["Texas"])

        self.city_combo = QComboBox()
        self.city_combo.addItems(["Dallas"])

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.search_businesses)

        search_layout.addWidget(self.business_input)
        search_layout.addWidget(self.country_combo)
        search_layout.addWidget(self.state_combo)
        search_layout.addWidget(self.city_combo)
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

        # Load saved businesses
        saved = self.database.get_all_businesses()
        self.display_businesses(saved)

    # ==========================
    # Display Businesses
    # ==========================
    def display_businesses(self, businesses):

        self.table.setRowCount(len(businesses))

        for row, item in enumerate(businesses):

            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(item["rating"]))
            self.table.setItem(row, 2, QTableWidgetItem(item["reviews"]))
            self.table.setItem(row, 3, QTableWidgetItem(item["phone"]))
            self.table.setItem(row, 4, QTableWidgetItem(item["website"]))
            self.table.setItem(row, 5, QTableWidgetItem(item["score"]))

    # ==========================
    # Search Businesses
    # ==========================
    def search_businesses(self):

        business = self.business_input.text()
        country = self.country_combo.currentText()
        state = self.state_combo.currentText()
        city = self.city_combo.currentText()

        results = self.business_service.search(
            business,
            country,
            state,
            city
        )

        # Save businesses to database
        for item in results:
            self.database.save_business(item)

        # Show businesses in table
        self.display_businesses(results)

        self.statusBar().showMessage(
            f"Found {len(results)} businesses"
        )