import sys
import csv
import os
from mainWidget import MainWidget
from profileWidget import SecondWidget
from PySide6.QtWidgets import QApplication,QFileDialog, QMainWindow, QStackedWidget, QTableWidgetItem
from add_page import AddPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.resize(800, 500)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_widget = MainWidget()
        self.second_widget = SecondWidget()
        self.add_page = AddPage()

        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.second_widget)
        self.stacked_widget.addWidget(self.add_page)

        self.main_widget.add_button.clicked.connect(self.switch_to_add_page)

        self.main_widget.display_button.clicked.connect(self.display_csv)
        self.main_widget.delete_button.clicked.connect(self.delete_selected_items)
        self.main_widget.edit_button.clicked.connect(self.edit_selected_items)
        self.main_widget.go_to_second_button.clicked.connect(self.switch_to_second_widget)
        self.second_widget.button.clicked.connect(self.switch_to_main_widget)
        self.add_page.button.clicked.connect(self.switch_to_main_widget)

        self.main_widget.search_field.textChanged.connect(self.filter_table)  # Connect textChanged signal to filter_table method

        self.main_widget.connect_table_double_click(self.handle_table_double_click)

        self.main_widget.import_button.clicked.connect(self.import_csv)

        # Connect search field textChanged signal to filter_table method
        self.main_widget.search_field.textChanged.connect(self.filter_table)


    def switch_to_add_page(self):
        self.stacked_widget.setCurrentWidget(self.add_page)


    def filter_table(self, text):
        text = text.lower()  # Convert the search text to lowercase for case-insensitive matching
        for row in range(self.main_widget.table.rowCount()):
            item_class = self.main_widget.table.item(row, 0)
            item_student = self.main_widget.table.item(row, 1)
            if item_class and item_student:  # Ensure there are valid items in the row
                class_text = item_class.text().lower()
                student_text = item_student.text().lower()
                if text in class_text or text in student_text:  # Check if the search text is present in any of the cell texts
                    self.main_widget.table.setRowHidden(row, False)  # Show the row if it matches the search text
                else:
                    self.main_widget.table.setRowHidden(row, True)


    def import_csv(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(current_dir, "data.csv")

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    data = list(reader)
                    with open(data_file_path, 'a', newline='') as data_file:
                        writer = csv.writer(data_file)
                        # Skip headers if they exist (assuming the first row is header)
                        if data and data[0]:
                            data = data[1:]
                        writer.writerows(data)


    def handle_table_double_click(self, index):
        first_name = self.main_widget.table.item(index.row(), 0).text()
        last_name = self.main_widget.table.item(index.row(), 1).text()
        classes_joined = []
        for row in range(self.main_widget.table.rowCount()):
            if self.main_widget.table.item(row, 0).text() == first_name and self.main_widget.table.item(row, 1).text() == last_name:
                class_name = self.main_widget.table.item(row, 6).text()
                if class_name not in classes_joined:
                    classes_joined.append(class_name)

        profile_text = f"Student Name: {first_name}\nClasses Joined: {', '.join(classes_joined)}"
        self.second_widget.profile_label.setText(profile_text)
        self.stacked_widget.setCurrentWidget(self.second_widget)
    
    # def save_to_csv(self):
    #     first_name = self.add_page.student_fields[0]["field"].text()
    #     last_name = self.add_page.student_fields[1]["field"].text()
    #     age = self.add_page.student_fields[2]["field"].text()
    #     mobile = self.add_page.student_fields[3]["field"].text()
    #     email = self.add_page.student_fields[4]["field"].text()
    #     grade = self.add_page.student_fields[5]["field"].text()
    #     class_name = self.add_page.class_name_field.text()

    #     current_dir = os.path.dirname(os.path.realpath(__file__))
    #     file_path = os.path.join(current_dir, "data.csv")

    #     if first_name and last_name and age and mobile and email and grade:
    #         with open(file_path, 'a', newline='') as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerow([first_name, last_name, age, mobile, email, grade, class_name])
    #             # Clear the fields after saving
    #             self.add_page.class_name_field.clear()
    #             for field in self.add_page.student_fields:
    #                 field["field"].clear()

        # self.stacked_widget.setCurrentWidget(self.main_widget)
        # self.display_csv()

    
    def display_csv(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data.csv")
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            self.main_widget.update_table(data)
    
    def delete_selected_items(self):
        selected_items = self.main_widget.table.selectedItems()
        if selected_items:
            rows_to_delete = set()
            for item in selected_items:
                rows_to_delete.add(item.row())
            rows_to_delete = sorted(rows_to_delete, reverse=True)
            for row in rows_to_delete:
                self.main_widget.table.removeRow(row)
            self.save_table_to_csv()
    
    def edit_selected_items(self):
        selected_items = self.main_widget.table.selectedItems()
        if selected_items:
            # if len(selected_items) == 2:  # Assuming only one cell from each column is selected
                new_class_name, new_student_name = None, None
                for item in selected_items:
                    if item.column() == 0:
                        new_student_name = item.text()
                    elif item.column() == 1:
                        new_class_name = item.text()
                if new_class_name and new_student_name:
                    self.save_table_to_csv()


    def save_table_to_csv(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data.csv")
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(self.main_widget.table.rowCount()):
                first_name = self.main_widget.table.item(row, 0).text()
                last_name = self.main_widget.table.item(row, 1).text()
                age = self.main_widget.table.item(row, 2).text()
                mobile = self.main_widget.table.item(row, 3).text()
                email = self.main_widget.table.item(row, 4).text()
                grade = self.main_widget.table.item(row, 5).text()
                class_name = self.main_widget.table.item(row, 6).text()
                writer.writerow([first_name,last_name,age,mobile,email,grade,class_name])

    def switch_to_second_widget(self):
        self.stacked_widget.setCurrentWidget(self.second_widget)
    
    def switch_to_main_widget(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
