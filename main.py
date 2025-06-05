import sys

from barberShop import BarberShop
from dataHandler import save_customers, save_employees
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(shop.name)

        button_add_customer = QPushButton("Add Customer")
        button_add_employee = QPushButton("Add Emplyee")
        button_add_service = QPushButton("Add Service")
        button_book_appointment = QPushButton("Book Appointment")
        button_quit = QPushButton("Quit")
        label_customer_name = QLabel("Customer Name: ")
        line_edit_customer_name = QLineEdit()
        label_customer_telephone = QLabel("Customer Telephone #: ")
        line_edit_customer_telephone = QLineEdit()
        label_customer_email = QLabel("Customer Email: ")
        line_edit_customer_email = QLineEdit()

        layout_vertical1 = QVBoxLayout()
        layout_vertical2 = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()

        layout_vertical1.addWidget(button_add_customer)
        layout_vertical1.addWidget(button_add_employee)
        layout_vertical1.addWidget(button_add_service)
        layout_vertical1.addWidget(button_book_appointment)
        layout_vertical1.addWidget(button_quit)

        layout_horizontal2.addWidget(label_customer_name)
        layout_horizontal3.addWidget(label_customer_telephone)
        layout_horizontal4.addWidget(label_customer_email)

        layout_horizontal2.addWidget(line_edit_customer_name)
        layout_horizontal3.addWidget(line_edit_customer_telephone)
        layout_horizontal4.addWidget(line_edit_customer_email)

        layout_horizontal1.addLayout(layout_vertical1)
        layout_horizontal1.addSpacing(20)
        layout_vertical2.addLayout(layout_horizontal2)
        layout_vertical2.addLayout(layout_horizontal3)
        layout_vertical2.addLayout(layout_horizontal4)
        layout_horizontal1.addLayout(layout_vertical2)

        widget = QWidget()
        widget.setLayout(layout_horizontal1)
        self.setCentralWidget(widget)

        button_quit.clicked.connect(self.close)



def get_action():
    print('1. Add Customer')
    print('2. Add Employee')
    print('3. Add Service')
    print('4. Book Appointment')
    print('5. Quit \n')

    return input('Enter your selectio 1-5 \n')


if __name__ == '__main__':

    shop = BarberShop('JanoCutz')

    # Start of GUI Code
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    # End of GUI Code

    running = False

    while running:
        match get_action():
            case '1':
                shop.add_customer()
            case '2':
                shop.add_employee()
            case '3':
                shop.add_service()
            case '4':
                shop.add_appointment()
            case '5':
                running = False

    for customer in shop.customers:
        print(customer)

    for employee in shop.employees:
        if employee.active:
            print(employee)

    for appointment in shop.appointments:
        print(appointment)


    save_customers(shop.customers)
    save_employees(shop.employees)