from PyQt6 import QtWidgets
import sys
import view

class Controller(QtWidgets.QMainWindow, view.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.pushButton_admin_add_customer.clicked.connect(self.add_customer)
        self.pushButton_admin_add_employee.clicked.connect(self.add_employee)
        self.pushButton_admin_add_service.clicked.connect(self.add_service)
        self.pushButton_appointment_book.clicked.connect(self.book_appointment)

    def add_customer(self):
        print('Adding customer...')
        self.stackedWidget.setCurrentIndex(1)

    def add_employee(self):
            self.stackedWidget.setCurrentIndex(2)

    def add_service(self):
        self.stackedWidget.setCurrentIndex(3)

    def book_appointment(self):
        self.stackedWidget.setCurrentIndex(4)



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Controller()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()