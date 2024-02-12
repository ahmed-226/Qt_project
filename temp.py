import sys
import csv
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QStackedWidget, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Main Window")
        self.resize(400, 300)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.main_widget = MainWidget()
        self.second_widget = SecondWidget()
        
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.second_widget)
        
        self.main_widget.save_button.clicked.connect(self.save_to_csv)
        self.main_widget.display_button.clicked.connect(self.display_csv)
        self.main_widget.go_to_second_button.clicked.connect(self.switch_to_second_widget)
        self.second_widget.button.clicked.connect(self.switch_to_main_widget)
    
    def save_to_csv(self):
        class_name = self.main_widget.class_field.text()
        student_name = self.main_widget.student_field.text()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data.csv")

        
        
        if class_name and student_name:
            
            with open(file_path, "a") as file:
                file.write(f"{class_name},{student_name}\n")
                
        
        self.main_widget.class_field.clear()
        self.main_widget.student_field.clear()
    
    def display_csv(self):
        self.second_widget.table.clearContents()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data.csv")

        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            self.second_widget.table.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    self.second_widget.table.setItem(i, j, QTableWidgetItem(col))
    
    def switch_to_second_widget(self):
        self.display_csv()
        self.stacked_widget.setCurrentWidget(self.second_widget)
    
    def switch_to_main_widget(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)

    def save_to_csv(self):
        first_name = self.student_fields[0]["field"].text()
        last_name = self.student_fields[1]["field"].text()
        age = self.student_fields[2]["field"].text()
        mobile = self.student_fields[3]["field"].text()
        email = self.student_fields[4]["field"].text()
        grade = self.student_fields[5]["field"].text()
        class_name = self.class_name_field.text()

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data.csv")

        if first_name and last_name and age and mobile and email and grade:
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, age, mobile, email, grade, class_name])
                # Clear the fields after saving
                self.class_name_field.clear()
                for field in self.student_fields:
                    field["field"].clear()

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Main Widget", self)
        layout.addWidget(self.label)
        
        self.class_label = QLabel("Class:", self)
        self.class_field = QLineEdit(self)
        layout.addWidget(self.class_label)
        layout.addWidget(self.class_field)
        
        self.student_label = QLabel("Student:", self)
        self.student_field = QLineEdit(self)
        layout.addWidget(self.student_label)
        layout.addWidget(self.student_field)
        
        button_layout = QVBoxLayout()
        
        self.save_button = QPushButton("Save", self)
        button_layout.addWidget(self.save_button)
        
        self.display_button = QPushButton("Display", self)
        button_layout.addWidget(self.display_button)
        
        self.go_to_second_button = QPushButton("Go to Second Widget", self)
        button_layout.addWidget(self.go_to_second_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Second Widget", self)
        layout.addWidget(self.label)
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Class", "Student"])
        layout.addWidget(self.table)
        
        self.button = QPushButton("Go to Main Widget", self)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
