from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)


class LeadDetails(QDialog):

    def __init__(self, lead):
        super().__init__()

        self.setWindowTitle(lead.business_name)
        self.resize(500, 500)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"<h2>{lead.business_name}</h2>"))
        layout.addWidget(QLabel(f"⭐ Rating: {lead.rating}"))
        layout.addWidget(QLabel(f"📝 Reviews: {lead.reviews}"))
        layout.addWidget(QLabel(f"📞 Phone: {lead.phone}"))
        layout.addWidget(QLabel(f"🌐 Website: {lead.website}"))
        layout.addWidget(QLabel(f"📧 Email: {lead.email}"))
        layout.addWidget(QLabel(f"🔥 Opportunity Score: {lead.score}"))
        layout.addWidget(QLabel(f"📋 Status: {lead.status}"))

        layout.addWidget(QLabel("Notes"))

        self.notes = QTextEdit()
        self.notes.setPlainText(lead.notes)
        layout.addWidget(self.notes)

        self.save_btn = QPushButton("Save")
        layout.addWidget(self.save_btn)

        self.setLayout(layout)