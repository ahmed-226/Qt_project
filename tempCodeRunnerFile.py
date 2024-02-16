LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 781, 541))
        self.widget.setStyleSheet("background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                             stop: 0 rgba(10,10,10,255), stop: 1 rgba(150,150,50,255));\n"
"")
        self.widget.setObjectName("widget")
        
        self.user_form = QtWidgets.QLineEdit(parent=self.widget)
        self.user_form.setGeometry(QtCore.QRect(250, 190, 261, 51))
        self.user_form.setText("")
        self.user_form.setObjectName("user_form")
        self.user_form.setStyleSheet("color:white; font-size:15pt; padding-left:5%;")
        self.password_form = QtWidgets.QLineEdit(parent=self.widget)
        self.password_form.setGeometry(QtCore.QRect(250, 310, 261, 51))
        self.password_form.setText("")
        self.password_form.setObjectName("password_form")
        self.password_form.setStyleSheet("color:white; font-size:15pt; padding-left:5%;")
        self.login_label = QtWidgets.QLabel(parent=self.widget)
        self.login_label.setGeometry(QtCore.QRect(330, 70, 111, 51))
        self.login_label.setStyleSheet("font-size:20pt;\n"
"font-weight:bold;\n"
"color:white;\n"
"background-color:rgba(255,255,255,0)")
        self.login_label.setObjectName("login_label")
        self.user_label = QtWidgets.QLabel(parent=self.widget)
        self.user_label.setGeometry(QtCore.QRect(250, 170, 91, 16))
        self.user_label.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"background-color:rgba(255,255,255,0)")
        self.user_label.setObjectName("user_label")
        self.password_label = QtWidgets.QLabel(parent=self.widget)
        self.password_label.setGeometry(QtCore.QRect(250, 290, 81, 16))
        self.password_label.setStyleSheet("color:white;\n"
"font-size:10pt;\n"
"background-color:rgba(255,255,255,0)")
        self.password_label.setObjectName("password_label")
        self.submit_PushButton = QtWidgets.QPushButton(parent=self.widget)
        self.submit_PushButton.setGeometry(QtCore.QRect(310, 420, 141, 41))
        self.submit_PushButton.setStyleSheet("color:black;\n"
"background-color:rgba(255,255,0,255);\n"
"font-size:15pt;\n"
"font-weight:bold;\n"
"padding-left:2%;\n"
"padding-right:2%;\n"
"padding-top:5%;\n"
"padding-bottom:5%;\n"
"border-radius:10;")
        
        self.submit_PushButton.setObjectName("submit_PushButton")
        self.error_label=QtWidgets.QLabel(parent=self.widget)
        self.error_label.setGeometry(QtCore.QRect(250, 470, 261, 21))
        self.error_label.setStyleSheet("color:red; background-color:rgba(255,255,255,0);font-size:15pt;")
        
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
