import sys

from PySide6 import QtWidgets
from MainWindow import MainWindow
from login import Ui_LoginWindow

app = QtWidgets.QApplication(sys.argv)

LoginPage = QtWidgets.QMainWindow()
ui = Ui_LoginWindow()
ui.setupUi(LoginPage)
ui.submit_PushButton.clicked.connect(ui.On_submit_clicked)
LoginPage.show()

app.exec()