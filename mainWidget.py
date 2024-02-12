from PySide6.QtWidgets import  QPushButton, QVBoxLayout, QLabel, QWidget, QLineEdit, QTableWidget, QHBoxLayout,QTableWidgetItem


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # self.label = QLabel("Main Widget", self)
        # layout.addWidget(self.label)

        self.add_button = QPushButton("Add", self)  # Wide button to add data
        layout.addWidget(self.add_button)


        # layout.addLayout(form_layout)

        button_layout = QHBoxLayout()

        # self.save_button = QPushButton("Save", self)
        # button_layout.addWidget(self.save_button)

        self.display_button = QPushButton("Display", self)
        button_layout.addWidget(self.display_button)

        self.delete_button = QPushButton("Delete", self)
        button_layout.addWidget(self.delete_button)

        self.edit_button = QPushButton("Edit", self)
        button_layout.addWidget(self.edit_button)

        self.import_button = QPushButton("Import", self)
        button_layout.addWidget(self.import_button)

        layout.addLayout(button_layout)

        # Add search field below the buttons

        search_box=QHBoxLayout()


        self.search_label = QLabel("Search:", self)
        search_box.addWidget(self.search_label)

        self.search_field = QLineEdit(self)
        search_box.addWidget(self.search_field)

        layout.addLayout(search_box)
        # self.search_field.textChanged.connect(self.filter_table)  # Connect textChanged signal to filter_table method

        self.table = QTableWidget(self)
        self.table.setColumnCount(7)  # Number of columns for the new text fields
        self.table.setHorizontalHeaderLabels([ "First Name", "Last Name", "Age", "Mobile", "Email", "Grade","Class"])
        layout.addWidget(self.table)

        self.go_to_second_button = QPushButton("Go to Second Widget", self)
        layout.addWidget(self.go_to_second_button)

        self.setLayout(layout)

    def update_table(self, data):
        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(col))

    def connect_table_double_click(self, callback):
        self.table.doubleClicked.connect(callback)