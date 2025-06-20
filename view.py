# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 550)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(0, 10, 901, 511))
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_left = QtWidgets.QFrame(parent=self.frame_main)
        self.frame_left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_buttons = QtWidgets.QFrame(parent=self.frame_left)
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_appointments = QtWidgets.QFrame(parent=self.frame_buttons)
        self.frame_appointments.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_appointments.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_appointments.setObjectName("frame_appointments")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_appointments)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_appointment_buttons = QtWidgets.QLabel(parent=self.frame_appointments)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_appointment_buttons.setFont(font)
        self.label_appointment_buttons.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_appointment_buttons.setObjectName("label_appointment_buttons")
        self.verticalLayout_2.addWidget(self.label_appointment_buttons)
        self.pushButton_appointment_book = QtWidgets.QPushButton(parent=self.frame_appointments)
        self.pushButton_appointment_book.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_appointment_book.setObjectName("pushButton_appointment_book")
        self.verticalLayout_2.addWidget(self.pushButton_appointment_book)
        self.pushButton_appointment_update = QtWidgets.QPushButton(parent=self.frame_appointments)
        self.pushButton_appointment_update.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_appointment_update.setObjectName("pushButton_appointment_update")
        self.verticalLayout_2.addWidget(self.pushButton_appointment_update)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame_appointments)
        self.frame_admin = QtWidgets.QFrame(parent=self.frame_buttons)
        self.frame_admin.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_admin.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_admin.setObjectName("frame_admin")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_admin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_admin_buttons = QtWidgets.QLabel(parent=self.frame_admin)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_admin_buttons.setFont(font)
        self.label_admin_buttons.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_admin_buttons.setObjectName("label_admin_buttons")
        self.verticalLayout.addWidget(self.label_admin_buttons)
        self.pushButton_admin_add_customer = QtWidgets.QPushButton(parent=self.frame_admin)
        self.pushButton_admin_add_customer.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_admin_add_customer.setObjectName("pushButton_admin_add_customer")
        self.verticalLayout.addWidget(self.pushButton_admin_add_customer)
        self.pushButton_admin_add_employee = QtWidgets.QPushButton(parent=self.frame_admin)
        self.pushButton_admin_add_employee.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_admin_add_employee.setObjectName("pushButton_admin_add_employee")
        self.verticalLayout.addWidget(self.pushButton_admin_add_employee)
        self.pushButton_admin_add_service = QtWidgets.QPushButton(parent=self.frame_admin)
        self.pushButton_admin_add_service.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_admin_add_service.setObjectName("pushButton_admin_add_service")
        self.verticalLayout.addWidget(self.pushButton_admin_add_service)
        self.pushButton_admin_quit = QtWidgets.QPushButton(parent=self.frame_admin)
        self.pushButton_admin_quit.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_admin_quit.setObjectName("pushButton_admin_quit")
        self.verticalLayout.addWidget(self.pushButton_admin_quit)
        self.horizontalLayout_2.addWidget(self.frame_admin)
        self.verticalLayout_4.addWidget(self.frame_buttons)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_left)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_6)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_add_service = QtWidgets.QFrame(parent=self.page_3)
        self.frame_add_service.setGeometry(QtCore.QRect(0, 10, 341, 141))
        self.frame_add_service.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_add_service.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_add_service.setObjectName("frame_add_service")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_add_service)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_new_service = QtWidgets.QLabel(parent=self.frame_add_service)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_new_service.setFont(font)
        self.label_new_service.setObjectName("label_new_service")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_new_service)
        self.label_service_name = QtWidgets.QLabel(parent=self.frame_add_service)
        self.label_service_name.setObjectName("label_service_name")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_name)
        self.lineEdit_service_name = QtWidgets.QLineEdit(parent=self.frame_add_service)
        self.lineEdit_service_name.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.lineEdit_service_name.setFont(font)
        self.lineEdit_service_name.setObjectName("lineEdit_service_name")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_service_name)
        self.label_service_description = QtWidgets.QLabel(parent=self.frame_add_service)
        self.label_service_description.setObjectName("label_service_description")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_description)
        self.lineEdit_service_description = QtWidgets.QLineEdit(parent=self.frame_add_service)
        self.lineEdit_service_description.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_service_description.setObjectName("lineEdit_service_description")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_service_description)
        self.label_service_price = QtWidgets.QLabel(parent=self.frame_add_service)
        self.label_service_price.setObjectName("label_service_price")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_price)
        self.lineEdit_service_price = QtWidgets.QLineEdit(parent=self.frame_add_service)
        self.lineEdit_service_price.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_service_price.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_service_price.setObjectName("lineEdit_service_price")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_service_price)
        self.label_service_duration = QtWidgets.QLabel(parent=self.frame_add_service)
        self.label_service_duration.setObjectName("label_service_duration")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_duration)
        self.lineEdit_service_duration = QtWidgets.QLineEdit(parent=self.frame_add_service)
        self.lineEdit_service_duration.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_service_duration.setObjectName("lineEdit_service_duration")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_service_duration)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_book_appointment = QtWidgets.QFrame(parent=self.page_4)
        self.frame_book_appointment.setGeometry(QtCore.QRect(10, 10, 391, 148))
        self.frame_book_appointment.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_book_appointment.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_book_appointment.setObjectName("frame_book_appointment")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_book_appointment)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label = QtWidgets.QLabel(parent=self.frame_book_appointment)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_book_customer_name = QtWidgets.QLabel(parent=self.frame_book_appointment)
        self.label_book_customer_name.setObjectName("label_book_customer_name")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_book_customer_name)
        self.lineEdit_book_customer_name = QtWidgets.QLineEdit(parent=self.frame_book_appointment)
        self.lineEdit_book_customer_name.setObjectName("lineEdit_book_customer_name")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_book_customer_name)
        self.label_book_service_name = QtWidgets.QLabel(parent=self.frame_book_appointment)
        self.label_book_service_name.setObjectName("label_book_service_name")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_book_service_name)
        self.label_book_employee_name = QtWidgets.QLabel(parent=self.frame_book_appointment)
        self.label_book_employee_name.setObjectName("label_book_employee_name")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_book_employee_name)
        self.lineEdit_book_employee_name = QtWidgets.QLineEdit(parent=self.frame_book_appointment)
        self.lineEdit_book_employee_name.setObjectName("lineEdit_book_employee_name")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_book_employee_name)
        self.label_book_date_time = QtWidgets.QLabel(parent=self.frame_book_appointment)
        self.label_book_date_time.setObjectName("label_book_date_time")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_book_date_time)
        self.dateTimeEdit_book_date_time = QtWidgets.QDateTimeEdit(parent=self.frame_book_appointment)
        self.dateTimeEdit_book_date_time.setObjectName("dateTimeEdit_book_date_time")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateTimeEdit_book_date_time)
        self.comboBox_book_service_name = QtWidgets.QComboBox(parent=self.frame_book_appointment)
        self.comboBox_book_service_name.setObjectName("comboBox_book_service_name")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_book_service_name)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_add_customer = QtWidgets.QFrame(parent=self.page)
        self.frame_add_customer.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_add_customer.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_add_customer.setObjectName("frame_add_customer")
        self.formLayout = QtWidgets.QFormLayout(self.frame_add_customer)
        self.formLayout.setObjectName("formLayout")
        self.label_new_customer = QtWidgets.QLabel(parent=self.frame_add_customer)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_new_customer.setFont(font)
        self.label_new_customer.setObjectName("label_new_customer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_new_customer)
        self.label_customer_name = QtWidgets.QLabel(parent=self.frame_add_customer)
        self.label_customer_name.setObjectName("label_customer_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_customer_name)
        self.lineEdit_customer_name = QtWidgets.QLineEdit(parent=self.frame_add_customer)
        self.lineEdit_customer_name.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_customer_name.setObjectName("lineEdit_customer_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_customer_name)
        self.label_customer_telephone = QtWidgets.QLabel(parent=self.frame_add_customer)
        self.label_customer_telephone.setObjectName("label_customer_telephone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_customer_telephone)
        self.lineEdit_customer_telephone = QtWidgets.QLineEdit(parent=self.frame_add_customer)
        self.lineEdit_customer_telephone.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_customer_telephone.setObjectName("lineEdit_customer_telephone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_customer_telephone)
        self.label_customer_email = QtWidgets.QLabel(parent=self.frame_add_customer)
        self.label_customer_email.setObjectName("label_customer_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_customer_email)
        self.lineEdit_customer_email = QtWidgets.QLineEdit(parent=self.frame_add_customer)
        self.lineEdit_customer_email.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_customer_email.setObjectName("lineEdit_customer_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_customer_email)
        self.verticalLayout_3.addWidget(self.frame_add_customer)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_add_employee = QtWidgets.QFrame(parent=self.page_2)
        self.frame_add_employee.setGeometry(QtCore.QRect(0, 20, 341, 101))
        self.frame_add_employee.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_add_employee.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_add_employee.setObjectName("frame_add_employee")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_add_employee)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_new_employee = QtWidgets.QLabel(parent=self.frame_add_employee)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_new_employee.setFont(font)
        self.label_new_employee.setObjectName("label_new_employee")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_new_employee)
        self.label_employee_name = QtWidgets.QLabel(parent=self.frame_add_employee)
        self.label_employee_name.setObjectName("label_employee_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_employee_name)
        self.lineEdit_employee_name = QtWidgets.QLineEdit(parent=self.frame_add_employee)
        self.lineEdit_employee_name.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_employee_name.setObjectName("lineEdit_employee_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_employee_name)
        self.label_employee_telephone = QtWidgets.QLabel(parent=self.frame_add_employee)
        self.label_employee_telephone.setObjectName("label_employee_telephone")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_employee_telephone)
        self.lineEdit_employee_telephone = QtWidgets.QLineEdit(parent=self.frame_add_employee)
        self.lineEdit_employee_telephone.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_employee_telephone.setObjectName("lineEdit_employee_telephone")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_employee_telephone)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_ok_cancel = QtWidgets.QFrame(parent=self.frame_left)
        self.frame_ok_cancel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ok_cancel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ok_cancel.setObjectName("frame_ok_cancel")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_ok_cancel)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_okay = QtWidgets.QPushButton(parent=self.frame_ok_cancel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_okay.sizePolicy().hasHeightForWidth())
        self.pushButton_okay.setSizePolicy(sizePolicy)
        self.pushButton_okay.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_okay.setObjectName("pushButton_okay")
        self.horizontalLayout_4.addWidget(self.pushButton_okay)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.frame_ok_cancel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_cancel)
        self.verticalLayout_4.addWidget(self.frame_ok_cancel)
        self.horizontalLayout_3.addWidget(self.frame_left)
        self.frame_right = QtWidgets.QFrame(parent=self.frame_main)
        self.frame_right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_right.setObjectName("frame_right")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_right)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_shop_name = QtWidgets.QLabel(parent=self.frame_right)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_shop_name.setFont(font)
        self.label_shop_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_shop_name.setObjectName("label_shop_name")
        self.verticalLayout_5.addWidget(self.label_shop_name)
        self.label_appointments = QtWidgets.QLabel(parent=self.frame_right)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_appointments.setFont(font)
        self.label_appointments.setObjectName("label_appointments")
        self.verticalLayout_5.addWidget(self.label_appointments)
        self.tableWidget_appointments = QtWidgets.QTableWidget(parent=self.frame_right)
        self.tableWidget_appointments.setObjectName("tableWidget_appointments")
        self.tableWidget_appointments.setColumnCount(0)
        self.tableWidget_appointments.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget_appointments)
        self.horizontalLayout_3.addWidget(self.frame_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_appointment_buttons.setText(_translate("MainWindow", "Appointments"))
        self.pushButton_appointment_book.setText(_translate("MainWindow", "Book"))
        self.pushButton_appointment_update.setText(_translate("MainWindow", "Update"))
        self.label_admin_buttons.setText(_translate("MainWindow", "Admin"))
        self.pushButton_admin_add_customer.setText(_translate("MainWindow", "Add Customer"))
        self.pushButton_admin_add_employee.setText(_translate("MainWindow", "Add Employee"))
        self.pushButton_admin_add_service.setText(_translate("MainWindow", "Add Service"))
        self.pushButton_admin_quit.setText(_translate("MainWindow", "Quit"))
        self.label_new_service.setText(_translate("MainWindow", "Add New Service"))
        self.label_service_name.setText(_translate("MainWindow", "Name:"))
        self.label_service_description.setText(_translate("MainWindow", "Description:"))
        self.label_service_price.setText(_translate("MainWindow", "Price"))
        self.label_service_duration.setText(_translate("MainWindow", "Duration"))
        self.label.setText(_translate("MainWindow", "Book Appointment"))
        self.label_book_customer_name.setText(_translate("MainWindow", "Customer Name:"))
        self.label_book_service_name.setText(_translate("MainWindow", "Service:"))
        self.label_book_employee_name.setText(_translate("MainWindow", "Employee Name:"))
        self.label_book_date_time.setText(_translate("MainWindow", "Date / Time:"))
        self.label_new_customer.setText(_translate("MainWindow", "Add New Customer"))
        self.label_customer_name.setText(_translate("MainWindow", "Name:"))
        self.label_customer_telephone.setText(_translate("MainWindow", "Telephone Number:"))
        self.label_customer_email.setText(_translate("MainWindow", "Email:"))
        self.label_new_employee.setText(_translate("MainWindow", "Add New Employee"))
        self.label_employee_name.setText(_translate("MainWindow", "Name:"))
        self.label_employee_telephone.setText(_translate("MainWindow", "Telephone Number:"))
        self.pushButton_okay.setText(_translate("MainWindow", "Okay"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_shop_name.setText(_translate("MainWindow", "Baraber Shop Name"))
        self.label_appointments.setText(_translate("MainWindow", "Today\'s Appointments:"))