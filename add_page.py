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


class AddPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.student_button = QPushButton("Student", self)
        self.professor_button = QPushButton("Professor", self)
        self.class_button = QPushButton("Class", self)
        self.save_button = QPushButton("Save", self)

        self.student_button.clicked.connect(self.show_student_fields)
        self.professor_button.clicked.connect(self.show_professor_fields)
        self.class_button.clicked.connect(self.show_class_fields)
        self.save_button.clicked.connect(self.save_to_csv)

        buttons_box = QHBoxLayout()
        buttons_box.addWidget(self.student_button,0,Qt.AlignHCenter)
        buttons_box.addWidget(self.professor_button,0,Qt.AlignHCenter)
        buttons_box.addWidget(self.class_button,0,Qt.AlignHCenter)
        self.layout.addLayout(buttons_box)

        input_box = QHBoxLayout()
        self.class_name_label = QLabel("Class Name:", self)
        self.class_name_field = QLineEdit(self)
        input_box.addWidget(self.class_name_label)
        input_box.addWidget(self.class_name_field)
        self.layout.addLayout(input_box)

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
            input_box.addWidget(field["field"])
            self.layout.addLayout(input_box)
        
        for field in self.professor_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"])
            self.layout.addLayout(input_box)

        for field in self.class_fields:
            input_box=QHBoxLayout()
            input_box.addWidget(field["label"])
            input_box.addWidget(field["field"])
            self.layout.addLayout(input_box)

        self.layout.addWidget(self.save_button,0,Qt.AlignHCenter)

        self.back_button = QPushButton("Back", self)
        self.layout.addWidget(self.back_button,0,Qt.AlignHCenter)

        self.setLayout(self.layout)
        
        self.hide_all_fields()

        self.age_validator = QIntValidator(self)
        self.age_validator.setBottom(0)  # Age should be a positive integer
        self.professor_fields[2]["field"].setValidator(self.age_validator)
        self.student_fields[2]["field"].setValidator(self.age_validator)
        
        self.mobile_validator = QIntValidator(self)
        self.mobile_validator.setBottom(0)  # Mobile number should be positive
        self.student_fields[3]["field"].setValidator(self.mobile_validator)
        self.professor_fields[3]["field"].setValidator(self.mobile_validator)

        self.set_style()
        
        # self.student_fields[4]["field"].setValidator(EmailValidator())
        # self.professor_fields[4]["field"].setValidator(EmailValidator())
        # self.student_fields[4]["field"].setValidator(self.email_validator)
        # self.professor_fields[4]["field"].setValidator(self.email_validator)
        
        
    def set_style(self):
        button_box=QVBoxLayout()
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(150, 40))
        self.back_button.setMaximumSize(QSize(150, 40))
        font3 = QFont()
        font3.setPointSize(11)
        self.back_button.setFont(font3)
        self.back_button.setStyleSheet(u"#back_button\n"
        "{\n"
        "	border:none;\n"
        "	background:#F33253;\n"
        "	color:white;\n"
        "	border-radius:16px;\n"
        "}\n"
        "\n"
        "#back_button:hover\n"
        "{\n"
        "	border:2px solid #F33253;\n"
        "	background:#2D2D2D;\n"
        "	color:#F33253;\n"
        "	border-radius:16px;\n"
        "}")
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(150, 40))
        self.save_button.setMaximumSize(QSize(150, 40))
        font3 = QFont()
        font3.setPointSize(11)
        self.save_button.setFont(font3)
        self.save_button.setStyleSheet(u"#save_button\n"
        "{\n"
        "	border:none;\n"
        "	background:#F33253;\n"
        "	color:white;\n"
        "	border-radius:16px;\n"
        "}\n"
        "\n"
        "#save_button:hover\n"
        "{\n"
        "	border:2px solid #F33253;\n"
        "	background:#2D2D2D;\n"
        "	color:#F33253;\n"
        "	border-radius:16px;\n"
        "}")
        button_box.addWidget(self.save_button,0,Qt.AlignHCenter)
        button_box.addWidget(self.back_button,0,Qt.AlignHCenter)
        self.layout.addLayout(button_box)
        #class button
        self.class_button.setObjectName(u"class_button")
        self.class_button.setMinimumSize(QSize(250, 100))
        self.class_button.setMaximumSize(QSize(250, 100))
        font3 = QFont()
        font3.setPointSize(11)
        self.class_button.setFont(font3)
        self.class_button.setStyleSheet(u"#class_button\n"
        "{\n"
        "background-color:rgb(85, 124, 85);\n"
        "border:none;\n"
        "height:100%;\n"
        "width:100%;\n"
        "border-radius: 10px ;\n"
        "color:white;\n"
        "font-weight: 700;\n"
        "font-size: 15px;\n"
        "}")
        #student button
        self.student_button.setObjectName(u"student_button")
        self.student_button.setMinimumSize(QSize(250, 100))
        self.student_button.setMaximumSize(QSize(250, 100))
        font3 = QFont()
        font3.setPointSize(11)
        self.student_button.setFont(font3)
        self.student_button.setStyleSheet(u"#student_button\n"
        "{\n"
        "background-color:rgb(191, 49, 49);\n"
        "border:none;\n"
        "height:100%;\n"
        "width:100%;\n"
        "border-radius: 10px ;\n"
        "color:white;\n"
        "font-weight: 700;\n"
        "font-size: 15px;\n"
        "}")
        #prof button
        self.professor_button.setObjectName(u"professor_button")
        self.professor_button.setMinimumSize(QSize(250, 100))
        self.professor_button.setMaximumSize(QSize(250, 100))
        font3 = QFont()
        font3.setPointSize(11)
        self.professor_button.setFont(font3)
        self.professor_button.setStyleSheet(u"#professor_button\n"
        "{\n"
        "background-color:rgb(97, 163, 186);\n"
        "border:none;\n"
        "height:100%;\n"
        "width:100%;\n"
        "border-radius: 10px ;\n"
        "color:white;\n"
        "font-weight: 700;\n"
        "font-size: 15px;\n"
        "}")
        
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
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "student.csv")

            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, age, email,mobile, grade, class_name])
                
                self.class_name_field.clear()
                for field in self.student_fields:
                    field["field"].clear()
        elif title :
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "profs.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name_prof,last_name_prof,age_prof, email_prof,mobile_prof, title, department])
                
                self.class_name_field.clear()
                for field in self.professor_fields:
                    field["field"].clear()
        elif hall:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_dir, "classes.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([class_, professors, hall, time])
                
                self.class_name_field.clear()
                for field in self.class_fields:
                    field["field"].clear()
        else:
            QMessageBox.information(self," Not enough Args ", "Please fill the fields")

