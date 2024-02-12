from PySide6.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox
import csv
import os

class AddPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.student_button = QPushButton("Student", self)
        self.professor_button = QPushButton("Professor", self)
        self.class_button = QPushButton("Class", self)
        self.save_button = QPushButton("Save", self)

        self.student_button.clicked.connect(self.show_student_fields)
        self.professor_button.clicked.connect(self.show_professor_fields)
        self.class_button.clicked.connect(self.show_class_fields)
        self.save_button.clicked.connect(self.save_to_csv)

        buttons_box = QHBoxLayout()
        buttons_box.addWidget(self.student_button)
        buttons_box.addWidget(self.professor_button)
        buttons_box.addWidget(self.class_button)
        layout.addLayout(buttons_box)

        input_box = QHBoxLayout()
        self.class_name_label = QLabel("Class Name:", self)
        self.class_name_field = QLineEdit(self)
        input_box.addWidget(self.class_name_label)
        input_box.addWidget(self.class_name_field)
        layout.addLayout(input_box)

        # Additional fields for students
        self.student_fields = [
            {"label": QLabel("First Name:", self), "field": QLineEdit()},
            {"label": QLabel("Last Name:", self), "field": QLineEdit()},
            {"label": QLabel("Age:", self), "field": QLineEdit()},
            {"label": QLabel("Mobile:", self), "field": QLineEdit()},
            {"label": QLabel("Email: ", self), "field": QLineEdit()},
            {"label": QLabel("Grade:", self), "field": QLineEdit()}
        ]

        self.professor_fields = [
            {"label": QLabel("First Name:", self), "field": QLineEdit()},
            {"label": QLabel("Last Name:", self), "field": QLineEdit()},
            {"label": QLabel("Department:", self), "field": QLineEdit()},
            {"label": QLabel("Email:", self), "field": QLineEdit()}
        ]

        for field in self.student_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"])
            layout.addLayout(input_box)
        
        for field in self.professor_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"])
            layout.addLayout(input_box)

        layout.addWidget(self.save_button)

        self.button = QPushButton("Back", self)
        layout.addWidget(self.button)

        self.setLayout(layout)
        
        # self.hide_all_fields()

    def show_student_fields(self):
        self.hide_all_fields()
        for field in self.student_fields:
            field["field"].show()
            field["label"].show()
        self.class_name_label.show()
        self.class_name_field.show()

    def show_professor_fields(self):
        self.hide_all_fields()
        for field in self.professor_fields:
            field["field"].show()
            field["label"].show()

    def show_class_fields(self):
        self.hide_all_fields()
        self.class_name_label.show()
        self.class_name_field.show()

    def hide_all_fields(self):
        for field in self.student_fields + self.professor_fields:
            field["field"].hide()
            field["label"].hide()
        self.class_name_label.hide()
        self.class_name_field.hide()

    def clear_fields(self):
        for field in self.student_fields + self.professor_fields:
            field["field"].clear()
        self.class_name_field.clear()

    def save_to_csv(self):
        first_name = self.student_fields[0]["field"].text()
        last_name = self.student_fields[1]["field"].text()
        age = self.student_fields[2]["field"].text()
        mobile = self.student_fields[3]["field"].text()
        email = self.student_fields[4]["field"].text()
        grade = self.student_fields[5]["field"].text()
        class_name = self.class_name_field.text()

        first_name_prof = self.professor_fields[0]["field"].text()
        last_name_prof = self.professor_fields[1]["field"].text()
        email_prof = self.professor_fields[2]["field"].text()
        department = self.professor_fields[3]["field"].text()


        if first_name and last_name and age and mobile and email and grade:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "student.csv")

            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, age, mobile, email, grade, class_name])
                
                self.class_name_field.clear()
                for field in self.student_fields:
                    field["field"].clear()
        elif first_name_prof and last_name_prof and email_prof and department:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "profs.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name_prof,last_name_prof, email_prof, department])
                
                self.class_name_field.clear()
                for field in self.professor_fields:
                    field["field"].clear()
        elif class_name:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "classes.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([class_name])
                
                self.class_name_field.clear()
        else:
            QMessageBox.information(self," Not enough Args ", "Please fill the fields")

