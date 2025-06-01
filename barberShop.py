from appointment import Appointment
from customer import Customer
from employee import Employee
from service import Service


class BarberShop:
    """ Class to manage the day-to-day operations at the store"""

    def __init__(self, name):
        self.name = name # Name of the barber shop
        self.customers = []
        self.services = []
        self.employees = []
        self.appointments = []

    def find_customer(self, name):
        """ Finds a customer by name"""
        for customer in self.customers:
            if customer.name == name:
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
            if employee.name == name:
               return employee
        return None

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
        """ Adds a service to the shop """
        service_id = len(self.services) + 1
        name = input('Enter service name: ')
        description = input('Enter service description: ')
        price = input('Enter service price: ')
        duration = input('Enter service duration: ')
        new_service = Service(service_id, name, description, price, duration)
        self.services.append(new_service)

    def add_appointment(self, appointment):
        """ Adds an appointment to the shop """
        customer = self.find_customer(input('Enter customers name: '))
        service = self.find_service(input('Enter the service the customer wants: '))
        employee = self.find_employee(input('Enter the name of the employee competing the service: '))
        date = input('Enter the appointment date: ')
        status = "Booked"
        new_appointment = Appointment(customer, service, employee, date, status)
        self.appointments.append(new_appointment)

