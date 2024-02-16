from PySide6.QtCore import Qt, QModelIndex, QIODevice, QUrl,QDir,QStringListModel
from PySide6.QtWidgets import QWidget,QFileSystemModel,QMainWindow
from PySide6.QtGui import QStandardItemModel,QStandardItem
from mainWindow_ui import Ui_MainWindow

class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom TableModel")
