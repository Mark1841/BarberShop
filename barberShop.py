from appointment import Appointment
from customer import Customer
from employee import Employee
from service import Service
from dataHandler import load_customers, load_employees

class BarberShop:
    """ Class to manage the day-to-day operations at the store"""

    def __init__(self, name):
        self.name = name # Name of the barber shop
        self.customers = load_customers()
        self.services = []
        self.employees = load_employees()
        self.appointments = []

    def find_customer(self, name):
        """ Finds a customer by name"""
        for customer in self.customers:
            if customer.name == name.title():
                print(f'found customer: {customer}')
                return customer
        return None

    def find_service(self, name):
        """ Finds a customer by name"""
        for service in self.services:
            if service.name == name:
               return service
        return None

    def find_employee(self, name):
        """ Finds an employee by name"""
        for employee in self.employees:
            if employee.name == name.title():
               return employee
        return None

    def add_customer(self, name = None):
        """ Adds a customer to the shop """
        customer_id = len(self.customers) + 1
        if name is None:
            name = input('Enter customer name: ')
        telephone_number = input('Enter customer phone number: ')
        email = input('Enter customer email: ')
        new_customer = Customer(customer_id, name, telephone_number, email)
        self.customers.append(new_customer)

    def add_employee(self, name = None):
        """ Adds an employee to the shop """
        employee_id = len(self.employees) + 1
        if name is None:
            name = input('Enter employee name: ')
        telephone_number = input('Enter employee phone number: ')
        new_employee = Employee(employee_id, name, telephone_number, True)
        self.employees.append(new_employee)

    def add_service(self, name = None):
        """ Adds a service to the shop """
        service_id = len(self.services) + 1
        if name is None:
            name = input('Enter service name: ')
        description = input('Enter service description: ')
        price = input('Enter service price: ')
        duration = input('Enter service duration: ')
        new_service = Service(service_id, name, description, price, duration)
        self.services.append(new_service)

    def add_appointment(self):
        """ Adds an appointment to the shop """
        customer_name = input('Enter customers name: ')
        customer = self.find_customer(customer_name)
        if customer is None:
            print('Customer not found, they will need to be added to database!')
            self.add_customer(customer_name)
            customer = self.find_customer(customer_name)
        service_name = input('Enter the service the customer wants: ')
        service = self.find_service(service_name)
        if service is None:
            print('Service not found, it will need to be added to database!')
            self.add_service(service_name)
            service = self.find_service(service_name)
        employee_name = input('Enter the name of the employee completing the service: ')
        employee = self.find_employee(employee_name)
        if employee is None:
            print('Employee not found, they will need to be added to database!')
            self.add_employee(employee_name)
            employee = self.find_employee(employee_name)
        date = input('Enter the appointment date: ')
        status = "Booked"
        new_appointment = Appointment(customer, service, employee, date, status)
        (self.appointments.append(new_appointment))