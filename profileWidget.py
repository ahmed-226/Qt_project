from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget

class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.profile_label = QLabel("", self) 
        layout.addWidget(self.profile_label)

        self.button = QPushButton("Go to Main Widget", self)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def update_profile(self, profile_data):
        # Clear previous labels
        for i in reversed(range(self.layout().count()-1)):
            widget = self.layout().itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Add new labels for each header-value pair
        for header, value in profile_data.items():
            label_text = f"{header}: {value}"
            label = QLabel(label_text)
            self.layout().insertWidget(self.layout().count() - 1, label)
