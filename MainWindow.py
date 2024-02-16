import sys
import csv
import os
from mainWidget import MainWidget
from profileWidget import SecondWidget
from PySide6.QtWidgets import QApplication,QFileDialog, QMainWindow, QStackedWidget, QTableWidgetItem
from PySide6.QtGui import QKeySequence,QShortcut
from add_page import AddPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.resize(1100, 700)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_widget = MainWidget()
        self.second_widget = SecondWidget()
        self.add_page = AddPage()

        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.second_widget)
        self.stacked_widget.addWidget(self.add_page)

        self.main_widget.add_button.clicked.connect(self.switch_to_add_page)

        self.main_widget.delete_button.clicked.connect(self.delete_selected_items)
        self.main_widget.edit_button.clicked.connect(self.edit_selected_items)
        QShortcut(QKeySequence("Ctrl+I"), self).activated.connect(self.import_csv)
        self.second_widget.button.clicked.connect(self.switch_to_main_widget)
        self.add_page.button.clicked.connect(self.switch_to_main_widget)
        self.main_widget.student_data_button.clicked.connect(self.display_student_data)
        self.main_widget.class_data_button.clicked.connect(self.display_class_data)
        self.main_widget.professor_data_button.clicked.connect(self.display_professor_data)

        # Add buttons to layout

        self.main_widget.search_field.textChanged.connect(self.filter_table) 

        self.main_widget.connect_table_double_click(self.handle_table_double_click)

        self.main_widget.import_button.clicked.connect(self.import_csv)

        self.main_widget.search_field.textChanged.connect(self.filter_table)
        self.current_displayed_data = None

    def switch_to_add_page(self):
        self.stacked_widget.setCurrentWidget(self.add_page)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Delete):
            self.delete_selected_items()
        else:
            super().keyPressEvent(event)

    def filter_table(self, text):
        text = text.lower()  
        for row in range(self.main_widget.table.rowCount()):
            item_email = self.main_widget.table.item(row, 3)
            item_first_name = self.main_widget.table.item(row, 1)
            if item_email and item_first_name:  
                class_text = item_email.text().lower()
                student_text = item_first_name.text().lower()
                # Check if the search text is present in any of the cell texts
                if text in class_text or text in student_text:  
                # Show the row if it matches the search text
                    self.main_widget.table.setRowHidden(row, False)  
                else:
                    self.main_widget.table.setRowHidden(row, True)

    def import_csv(self):
        num_cols = self.main_widget.table.columnCount()
        
        current_dir = os.path.dirname(os.path.realpath(__file__))
        if num_cols==7:
            data_file_path = os.path.join(current_dir, "student.csv")
        elif num_cols==4:
            data_file_path = os.path.join(current_dir, "profs.csv")
        elif num_cols==1:
            data_file_path = os.path.join(current_dir, "classes.csv")

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
                        
                        if data and data[0]:
                            data = data[1:]
                        writer.writerows(data)

    def handle_table_double_click(self, index):
        row = index.row()
        num_columns = self.main_widget.table.columnCount()
        first_name_item = self.main_widget.table.item(row, 0)
        last_name_item = self.main_widget.table.item(row, 1)

        if first_name_item is None or last_name_item is None:
            return

        first_name = first_name_item.text()
        last_name = last_name_item.text()
        
        # Check if the selected item is from the student table or class table
        if self.main_widget.table.objectName() == "student_table":
            # Check if the selected first name and last name appear more than once
            student_name = f"{first_name} {last_name}"
            class_names = []

            for r in range(self.main_widget.table.rowCount()):
                if r != row:
                    current_first_name = self.main_widget.table.item(r, 0).text()
                    current_last_name = self.main_widget.table.item(r, 1).text()

                    if current_first_name == first_name and current_last_name == last_name:
                        class_name = self.main_widget.table.item(r, 6).text()
                        class_names.append(class_name)

            # Collect information from the clicked row
            row_data = {}
            for col in range(num_columns):
                header_text = self.main_widget.table.horizontalHeaderItem(col).text()
                item_text = self.main_widget.table.item(row, col).text()
                row_data[header_text] = item_text

            # Add class names to the profile text if the student is in multiple classes
            if class_names:
                row_data['Class'] = ', '.join(class_names)

            # Update the profile in the SecondWidget
            self.second_widget.update_profile(row_data)
            self.stacked_widget.setCurrentWidget(self.second_widget)
        else:
            # Collect information from the clicked row
            row_data = {}
            for col in range(num_columns):
                header_text = self.main_widget.table.horizontalHeaderItem(col).text()
                item_text = self.main_widget.table.item(row, col).text()
                row_data[header_text] = item_text

            # Update the profile in the SecondWidget
            self.second_widget.update_profile(row_data)
            self.stacked_widget.setCurrentWidget(self.second_widget)
        
    def display_student_data(self):
        # Load and display student data
        student_data = self.load_data_from_csv("student.csv")
        self.main_widget.update_table(student_data, "student")
        self.current_displayed_data = "student"

    def display_class_data(self):
        # Load and display class data
        class_data = self.load_data_from_csv("classes.csv")
        self.main_widget.update_table(class_data, "class")
        self.current_displayed_data = "class"

    def display_professor_data(self):
        # Load and display professor data
        professor_data = self.load_data_from_csv("profs.csv")
        self.main_widget.update_table(professor_data, "professor")
        self.current_displayed_data = "professor"

    def load_data_from_csv(self, file_name):
        # Load data from CSV file
        data = []
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, file_name)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        return data
    
    
    
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
            data = []
            num_cols = self.main_widget.table.columnCount()
            for item in selected_items:
                row_index = item.row()
                col_index = item.column()
                cell_data = item.text()
                data.append((row_index, col_index, cell_data))

            for row_index, col_index, cell_data in data:
                self.main_widget.table.setItem(row_index, col_index, QTableWidgetItem(cell_data))

            self.save_table_to_csv()

    def save_table_to_csv(self):
        num_cols = self.main_widget.table.columnCount()
        if self.current_displayed_data == "student":  
            file_name = "student.csv"
        elif self.current_displayed_data == "professor":
            file_name = "profs.csv"
        elif self.current_displayed_data == "class":  
            file_name = "classes.csv"
        else:
            print("Unknown data type")
            return

        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, file_name)

        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            num_rows = self.main_widget.table.rowCount()
            for row in range(num_rows):
                row_data = []
                for col in range(num_cols):
                    item = self.main_widget.table.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  # Empty cell
                writer.writerow(row_data)

    def switch_to_second_widget(self):
        self.stacked_widget.setCurrentWidget(self.second_widget)
    
    def switch_to_main_widget(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
