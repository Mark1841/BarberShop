import datetime
from unittest import case

from barberShop import BarberShop
from customer import Customer
from service import Service
from employee import Employee
from appointment import Appointment

def get_action():
    print('1. Add Customer')
    print('2. Add Employee')
    print('3. Add Service')
    print('4. Book Appointment')
    print('5. Quit \n')

    return input('Enter your selectio 1-5 \n')


if __name__ == '__main__':

    shop = BarberShop('JanoCutz')
    running = True

    while running:
        match get_action():
            case '1':
                shop.add_customer()
            case '2':
                shop.add_employee()
            case '3':
                pass
            case '4':
                pass
            case '5':
                running = False

    for customer in shop.customers:
        print(customer)

    for employee in shop.employees:
        if employee.active:
            print(employee)







