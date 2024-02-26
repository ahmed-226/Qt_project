from PySide6.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox
from PySide6.QtGui import QIntValidator,QValidator
from PySide6.QtCore import  Qt
import csv
import os
import re
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
from designs.addPage_ui import Ui_Form


class AddPage(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # self.layout = QVBoxLayout()

        # self.student_button = QPushButton("Student", self)
        # self.professor_button = QPushButton("Professor", self)
        # self.class_button = QPushButton("Class", self)
        # self.save_button = QPushButton("Save", self)

        self.student_button.clicked.connect(self.show_student_fields)
        self.professor_button.clicked.connect(self.show_professor_fields)
        self.class_button.clicked.connect(self.show_class_fields)
        self.save_button.clicked.connect(self.save_to_csv)

        # buttons_box = QHBoxLayout()
        # buttons_box.addWidget(self.student_button,0,Qt.AlignHCenter)
        # buttons_box.addWidget(self.professor_button,0,Qt.AlignHCenter)
        # buttons_box.addWidget(self.class_button,0,Qt.AlignHCenter)
        # self.layout.addLayout(buttons_box)

        input_box = QHBoxLayout()
        self.class_name_label = QLabel("Class Name:", self)
        self.class_name_field = QLineEdit(self)
        self.set_style(self.class_name_label,self.class_name_field)
        input_box.addWidget(self.class_name_label)
        input_box.addWidget(self.class_name_field)
        self.data_box.addLayout(input_box)

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
            {"label": QLabel("Age:", self), "field": QLineEdit()},
            {"label": QLabel("Mobile:", self), "field": QLineEdit()},
            {"label": QLabel("Email: ", self), "field": QLineEdit()},
            {"label": QLabel("Title:", self), "field": QLineEdit()},
            {"label": QLabel("Department:", self), "field": QLineEdit()}
        ]

        self.class_fields = [
            {"label": QLabel("Class:", self), "field": QLineEdit()},
            {"label": QLabel("Professors:", self), "field": QLineEdit()},
            {"label": QLabel("Lecture Hall:", self), "field": QLineEdit()},
            {"label": QLabel("Time:", self), "field": QLineEdit()},
        ]

        for field in self.student_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])
            self.data_box.addLayout(input_box)
        
        for field in self.professor_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])

            self.data_box.addLayout(input_box)

        for field in self.class_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])

            self.data_box.addLayout(input_box)

        # self.layout.addWidget(self.save_button,0,Qt.AlignHCenter)

        # self.back_button = QPushButton("Back", self)
        # self.layout.addWidget(self.back_button,0,Qt.AlignHCenter)

        # self.setLayout(self.layout)
        
        self.show_student_fields()

        self.age_validator = QIntValidator(self)
        self.age_validator.setBottom(0)  # Age should be a positive integer
        self.professor_fields[2]["field"].setValidator(self.age_validator)
        self.student_fields[2]["field"].setValidator(self.age_validator)
        
        self.mobile_validator = QIntValidator(self)
        self.mobile_validator.setBottom(0)  # Mobile number should be positive
        self.student_fields[3]["field"].setValidator(self.mobile_validator)
        self.professor_fields[3]["field"].setValidator(self.mobile_validator)

        
    def set_style(self,label,field):
        label.setObjectName(u"label")
        label.setStyleSheet(u"#label\n"
        "{\n"
        "	border:none;\n"
        "	color:white;\n"
        "	font-size:18px;\n"
        "	font-weight:600;\n"
        "}\n"
        )
        
        field.setObjectName(u"field")
        field.setMinimumSize(QSize(800, 40))
        field.setMaximumSize(QSize(800, 40))
        field.setStyleSheet(u"#field\n"
        "{\n"
        "	border:none;\n"
        "	background-color:white;\n"
        "	color:black;\n"
        "	border-radius:10px;\n"
        "	font-size:18px;\n"
        "	font-weight:600;\n"
        "}\n"
        )

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
        for field in self.class_fields:
            field["field"].show()
            field["label"].show()


    def hide_all_fields(self):
        for field in self.student_fields + self.professor_fields + self.class_fields:
            field["field"].hide()
            field["label"].hide()
        self.class_name_label.hide()
        self.class_name_field.hide()

    def clear_fields(self):
        for field in self.student_fields + self.professor_fields + self.class_fields:
            field["field"].clear()
        self.class_name_field.clear()

    def save_to_csv(self):
        # self.submit()
        first_name = self.student_fields[0]["field"].text()
        last_name = self.student_fields[1]["field"].text()
        age = self.student_fields[2]["field"].text()
        mobile = self.student_fields[3]["field"].text()
        email = self.student_fields[4]["field"].text()
        grade = self.student_fields[5]["field"].text()
        class_name = self.class_name_field.text()

        first_name_prof = self.professor_fields[0]["field"].text()
        last_name_prof = self.professor_fields[1]["field"].text()
        age_prof = self.professor_fields[2]["field"].text()
        mobile_prof = self.professor_fields[3]["field"].text()
        email_prof = self.professor_fields[4]["field"].text()
        title = self.professor_fields[5]["field"].text()
        department = self.professor_fields[6]["field"].text()

        class_ = self.class_fields[0]["field"].text()
        professors = self.class_fields[1]["field"].text()
        hall = self.class_fields[2]["field"].text()
        time = self.class_fields[3]["field"].text()


        if grade:
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "student.csv")

            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, age, email,mobile, grade, class_name])
                
                self.class_name_field.clear()
                for field in self.student_fields:
                    field["field"].clear()
        elif title :
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "profs.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name_prof,last_name_prof,age_prof, email_prof,mobile_prof, title, department])
                
                self.class_name_field.clear()
                for field in self.professor_fields:
                    field["field"].clear()
        elif hall:
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "classes.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([class_, professors, hall, time])
                
                self.class_name_field.clear()
                for field in self.class_fields:
                    field["field"].clear()
        else:
            QMessageBox.information(self," Not enough Args ", "Please fill the fields")
    

