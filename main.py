import datetime

from barberShop import BarberShop
from customer import Customer
from service import Service
from employee import Employee
from appointment import Appointment

def display_menu():
    print('1. Add Customer')
    print('2. Add Employee')
    print('3. Add Service')
    print('4. Book Appointment')
    print('5. Quit \n')

    return input('Enter your selectio 1-5 \n')


if __name__ == '__main__':

    running = True

    while running:
        option = display_menu()

        if option == '5'5:
            running = False



    shop = BarberShop('JanoCutz')
    new_customer = Customer(len(shop.customers) + 1, "Mark Janovitz", "9059250766", "mjanovitz@outlook.com")
    shop.add_customer(new_customer)

    new_service = Service(len(shop.services) + 1, "The Beard Trim", "Reduce beard length, outline neck and cheeks", 30, 39.80)
    shop.add_service(new_service)

    new_employee = Employee(len(shop.employees) +1, "Jane Smith", "9051234567", True)
    shop.add_employee(new_employee)

    new_employee = Employee(len(shop.employees) +1, "Dave Johnson", "9054321923", False)
    shop.add_employee(new_employee)

    new_appointment = Appointment(shop.customers[0], shop.employees[0], datetime.datetime(2025,5,30), 'Error')
    print(new_appointment.customer)
    print(new_appointment.status)

    new_appointment.status = "error2" #setter only being called here, not at object creation
    print(new_appointment.status)

    for customer in shop.customers:
        print(customer)

    for employee in shop.employees:
        if employee.active:
            print(employee)







