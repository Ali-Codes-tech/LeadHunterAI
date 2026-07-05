from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFrame
)

from PySide6.QtCore import Qt


class StatCard(QFrame):

    def __init__(self, title, value="0"):
        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        self.setStyleSheet("""
            QFrame{
                background:white;
                border:1px solid #dddddd;
                border-radius:10px;
                padding:12px;
            }
        """)

        layout = QVBoxLayout(self)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("""
            font-size:13px;
            color:gray;
        """)

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#0078D7;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

    def setValue(self, value):
        self.value.setText(str(value))


class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.searches = StatCard("Today's Searches")
        self.saved = StatCard("Saved Leads")
        self.high = StatCard("High Score")
        self.average = StatCard("Average Score")

        layout.addWidget(self.searches)
        layout.addWidget(self.saved)
        layout.addWidget(self.high)
        layout.addWidget(self.average)