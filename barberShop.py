class BarberShop:
    """ Class to manage the day to day operations at the store"""

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.services = []
        self.employees = []


    def add_customer(self, customer):
        self.customers.append(customer)

    def add_service(self, service):
        self.services.append(service)

    def add_employee(self, employee):
        self.employees.append(employee)