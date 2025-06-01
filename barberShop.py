from customer import Customer
from employee import Employee


class BarberShop:
    """ Class to manage the day-to-day operations at the store"""

    def __init__(self, name):
        self.name = name # Name of the barber shop
        self.customers = []
        self.services = []
        self.employees = []
        self.appointments = []



    def add_customer(self):
        """ Adds a customer to the shop """

        customer_id = len(self.customers) + 1
        name = input('Enter customer name: ')
        telephone_number = input('Enter customer phone number: ')
        email = input('Enter customer email: ')
        new_customer = Customer(customer_id, name, telephone_number, email)
        self.customers.append(new_customer)

    def add_employee(self):
        """ Adds an employee to the shop """

        employee_id = len(self.employees) + 1
        name = input('Enter employee name: ')
        telephone_number = input('Enter employee phone number: ')
        new_employee = Employee(employee_id, name, telephone_number, True)
        self.employees.append(new_employee)

    def add_service(self, service):
        self.services.append(service)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)