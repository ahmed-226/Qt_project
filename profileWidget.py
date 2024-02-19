from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QLineEdit, QTableWidget, QHBoxLayout, QTableWidgetItem

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

    def update_profile_table(self, data, name:str):
        num_rows = len(data)
        num_cols = 2

        self.table = QTableWidget(self)
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        if num_rows > 0:
            headers = ["Name", "Grade"]
            self.table.setHorizontalHeaderLabels(headers)
            rows_to_delete = []
            for i, row in enumerate(data):
                if row[6] == name:
                    self.table.setItem(i, 0, QTableWidgetItem(f'{row[0]} {row[1]}'))
                    self.table.setItem(i, 1, QTableWidgetItem(row[5]))
                else:
                    rows_to_delete.append(i)
            for i in range(len(rows_to_delete)):
                    self.table.removeRow(rows_to_delete[-1])
                    rows_to_delete.pop()
        
        self.layout().insertWidget(self.layout().count() - 1, self.table)