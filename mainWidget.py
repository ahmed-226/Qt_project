from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QLineEdit, QHBoxLayout, QTableWidgetItem
from mainWidget_ui import Ui_mainWidget

class MainWidget(QWidget,Ui_mainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_ui()

    # Note : 
    # This part was prototype to test only functional parts 
    # for out GUI part we use QT designer  

    # def init_ui(self):
    #     layout = QVBoxLayout()

    #     self.add_button = QPushButton("Add", self)  # Wide button to add data
    #     layout.addWidget(self.add_button)

    #     button_box = QHBoxLayout()
    #     self.student_data_button = QPushButton("Student Data", self)
    #     self.class_data_button = QPushButton("Class Data", self)
    #     self.professor_data_button = QPushButton("Professor Data", self)
    #     button_box.addWidget(self.student_data_button)
    #     button_box.addWidget(self.professor_data_button)
    #     button_box.addWidget(self.class_data_button)
    #     layout.addLayout(button_box)

    #     button_layout = QHBoxLayout()
    #     self.delete_button = QPushButton("Delete", self)
    #     button_layout.addWidget(self.delete_button)
    #     self.edit_button = QPushButton("Edit", self)
    #     button_layout.addWidget(self.edit_button)
    #     self.import_button = QPushButton("Import", self)
    #     button_layout.addWidget(self.import_button)
    #     layout.addLayout(button_layout)

    #     search_box = QHBoxLayout()
    #     self.search_label = QLabel("Search:", self)
    #     search_box.addWidget(self.search_label)
    #     self.search_field = QLineEdit(self)
    #     search_box.addWidget(self.search_field)
    #     layout.addLayout(search_box)

    #     self.table = QTableWidget(self)
    #     layout.addWidget(self.table)

        # self.go_to_second_button = QPushButton("Go to Second Widget", self)
        # layout.addWidget(self.go_to_second_button)

        # self.setLayout(layout)

    def update_table(self, data, selected_data:str):
        num_rows = len(data)
        num_cols = len(data[0]) if num_rows > 0 else 0

        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        if num_rows > 0:
            if selected_data == "student":
                headers = ["Frist Name","Last Name","Age","Email","Mobile","Grade","Class"]  # Default headers
            elif selected_data == "professor":
                headers = ["Frist Name","Last Name","Age","Email","Mobile", "Title", "Department"]  # Default headers
            elif selected_data == "class":
                headers = ["class", "Professors", "Lecture Hall", "Time"]  # Default headers
            self.table.setHorizontalHeaderLabels(headers)

            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(col))

    def connect_table_double_click(self, callback):
        self.table.doubleClicked.connect(callback)
