import sys

from barberShop import BarberShop
from dataHandler import save_customers, save_employees
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(shop.name)
        button_add_customer = QPushButton('Add Customer')
        self.setCentralWidget(button_add_customer)


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
    app = QApplication()
    window = MainWindow()
    window.show()
    # End of GUI Code

    running = True

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





