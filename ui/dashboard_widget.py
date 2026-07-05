from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QGraphicsDropShadowEffect
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class StatCard(QFrame):

    def __init__(self, title, value="0"):
        super().__init__()

        self.setMinimumHeight(120)

        # Modern gradient style
        self.setStyleSheet("""
        QFrame{
            background:qlineargradient(
                x1:0,y1:0,
                x2:1,y2:1,
                stop:0 #0078D7,
                stop:1 #00A2FF
            );
            border:none;
            border-radius:15px;
        }
        """)

        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(8)

        # Title
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("""
            color:white;
            font-size:13px;
            font-weight:bold;
        """)

        # Value
        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
            color:white;
            font-size:34px;
            font-weight:bold;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

    def setValue(self, value):
        self.value.setText(str(value))


class DashboardWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 10)

        self.searches = StatCard("🔍 Today's Searches")
        self.saved = StatCard("💾 Saved Leads")
        self.high = StatCard("⭐ High Score")
        self.average = StatCard("📈 Average Score")

        layout.addWidget(self.searches)
        layout.addWidget(self.saved)
        layout.addWidget(self.high)
        layout.addWidget(self.average)