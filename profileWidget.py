from PySide6.QtWidgets import  QPushButton, QVBoxLayout, QLabel, QWidget

class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Second Widget", self)
        layout.addWidget(self.label)

        self.profile_label = QLabel("", self)  # Label to display profile info
        layout.addWidget(self.profile_label)

        self.button = QPushButton("Go to Main Widget", self)
        layout.addWidget(self.button)

        self.setLayout(layout)